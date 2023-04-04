from email.message import EmailMessage
from threading import Thread
import modulos.auxiliar as auxiliar
import modulos.hbl as hbl
import time
import smtplib
import datetime
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import imghdr
from modulos import variablesGlobales as VG
import os
from modulos import log as log

class SendMail(object):

    def __init__(self):
        self.pendientes = False
        self.remitente = hbl.Mail_remitente
        self.destinatario = hbl.Mail_destinatarios
        self.state = False


        self.user = hbl.Mail_user
        self.key = hbl.Mail_key
        self.path_file = ""
        
        self.msg = ""
        self.asunto = ""
        
        self.count = 0
        if hbl.Mail_activado == 1:
            self.t = Thread(target = self.__run, daemon= False)
            self.t.start()

    def send(self,asunto="",msg="",path=None):
        
        self.asunto = asunto
        self.msg = msg
        #self.count += 1   
        self.state = True
        self.path_file = path      
    
    def __run(self):
        if hbl.Mail_activado == 1:
            while True:
                if True:
                    if self.state:
                        self.state = False
                        self.email = EmailMessage()
                        
                        self.email["From"] = hbl.Mail_remitente
                        self.email["To"] = hbl.Mail_destinatarios
                        self.email["Subject"] = self.asunto

        
                        
                        date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                        self.msg += self.msg + date
                        self.email.set_content(self.msg) 
                        sent_message = f"Asunto: {self.asunto} \nMensaje: {self.msg}"
                        try:
                            if self.path_file != None:
                                try:
                                    time.sleep(hbl.Camara_RPI_Duracion_Video_seg + 2)
                                    ImgFileName = "/usr/programas/" + VG.path_last_capture
                                    with open(ImgFileName, 'rb') as f:
                                        image_data = f.read()
                                        image_type = imghdr.what(f.name)
                                        image_name = f.name
                                    self.email.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
                                    sent_message += f"\nAdjunto: {VG.path_last_capture}"
                                except Exception as e:
                                    print("No se pudo adjuntar el archivo")
                            
                            smtp = smtplib.SMTP_SSL("smtp-relay.sendinblue.com")
                            smtp.login(self.user, self.key)
                            smtp.sendmail(self.remitente, self.destinatario, self.email.as_string())
                            smtp.quit()
                            
                            
                            log.escribeSeparador(hbl.LOGS_hblMail)
                            log.escribeLineaLog(hbl.LOGS_hblMail,sent_message)
                            
                            
                        except Exception as e:
                            print("No se pudo enviar el mail : %s\n" % e)
                            
                elif self.pendientes :
                    self.email = EmailMessage()
                    self.email["From"] = hbl.Mail_remitente
                    self.email["To"] = hbl.Mail_destinatarios
                    self.email["Subject"] = "Intruso Pendiente"
            
                    try:

                        with open(hbl.Contador_IntrusosPendientesPath) as file:
                            lines = [line.strip() for line in file]
                            file.close()
                            
                        with open(hbl.Contador_IntrusosPendientesPath,"w") as file:
                            file.write("")
                            file.close()
                        
                        for date in lines:
                            mensaje = "<html><body><h1> Se ha detectado un intrusoa a las : " + date + "</h1></body></html>"
                            self.email.set_content(mensaje)
                            smtp = smtplib.SMTP_SSL("smtp-relay.sendinblue.com")
                            smtp.login(self.user, self.key)
                            smtp.sendmail(self.remitente, self.destinatario, self.email.as_string())
                            smtp.quit()
                            print(f"mail enviado, fecha: {date}")
                            time.sleep(0.5)
                        self.pendientes = False
                        
                        
                    except Exception as e:
                        print("No se pudo enviar el mail : %s\n" % e)
                                        
                else:
                    print("No se hay conexion a internet")
                    time.sleep(0.5)