from email.message import EmailMessage
from threading import Thread
from modulos import auxiliar as auxiliar
from modulos import hbl as hbl
import time
import smtplib
from datetime import datetime
import imghdr
from modulos import variablesGlobales as VG
import os
from modulos import log as log


TIEMPO_ENTRE_CAPTURAS_SEG = 3

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
        
        self.lastMail = datetime.now()
        
        self.count = 0
        if hbl.Mail_activado == 1:
            self.t = Thread(target = self.__run, daemon= False, name = "Mails")
            self.t.start()

<<<<<<< HEAD
    def sendIntrusoMail(self):
            self.count += 1
        
        
    def sendDoorMail(self):
        self.door = True   
        
    def add_intruso(self, date):
        myFile = open(hbl.Contador_IntrusosPendientesPath, 'a')

        with myFile:
            myFile.write(date + "\n")
            myFile.close() 
        self.pendientes = True 
        
    def __LogReport(self, texto):
        log.escribeSeparador(hbl.LOGS_hblMail)
        log.escribeLineaLog(hbl.LOGS_hblMail, texto)      
=======
    def send(self,asunto="",msg="",path=None):
        #self.count += 1   
        now = datetime.now()        
        if ((now - self.lastMail).total_seconds() > TIEMPO_ENTRE_CAPTURAS_SEG) and path != "Error":
            self.asunto = asunto
            self.msg = msg
            self.state = True
            self.path_file = path 
        else:
            log.escribeSeparador(hbl.LOGS_hblMail)
            log.escribeLineaLog(hbl.LOGS_hblMail,"Error tiempo entre mails")
            
                 
>>>>>>> 1bc0f66ad3e87c37389319b87841ad86ddfeacdc
    
    def __run(self):
        if hbl.Mail_activado == 1:
            while True:
<<<<<<< HEAD
                
                    if self.count > 0:

                            self.email = EmailMessage()
                            
                            self.email["From"] = hbl.Mail_remitente
                            self.email["To"] = hbl.Mail_destinatarios
                            self.email["Subject"] = hbl.Contador_ID+ "  " + hbl.Mail_subject
                            

                            date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                            try:
                                mensaje = "<html><body><h1> Se ha detectado un intruso en "+hbl.Contador_ID+"\
                                             a las : " + date + "</h1></body></html>"
                                self.email.set_content(mensaje)
                                smtp = smtplib.SMTP_SSL("smtp-relay.sendinblue.com")
                                
                                smtp.login(self.user, self.key)
                                smtp.sendmail(self.remitente, self.destinatario, self.email.as_string())
                                smtp.quit()
                                self.__LogReport(f"mail intruso enviado, quedan : {self.count} pendientes")
                                self.count -= 1
                                print("Intruso Enviado")
                            except Exception as e:
                                
                                self.__LogReport("No se pudo enviar el mail de intruso: %s\n" % e)
                                print("Pendiente agregado")
                                self.add_intruso(date)
                                self.pendientes = True
                                self.count -= 1
                            
                    elif self.pendientes :
                        if auxiliar.CheckInternet():
                            self.email = EmailMessage()
                            self.email["From"] = hbl.Mail_remitente
                            self.email["To"] = hbl.Mail_destinatarios
                            self.email["Subject"] = hbl.Contador_ID+ " " + "Intruso Pendiente"
                    
                            try:

                                with open(hbl.Contador_IntrusosPendientesPath) as file:
                                    lines = [line.strip() for line in file]
                                    file.close()
                                
                                with open(hbl.Contador_IntrusosPendientesPath,"w") as file:
                                    file.write("")
                                    file.close()
                                dates = ""
                                for date in lines:
                                    dates = dates + date.strip() + "\n"
                                if dates != "":
                                    mensaje = "<html><body><h1> Se ha detectado un intruso en "+hbl.Contador_ID+"\
                                            a las :  \n" + dates + "</h1></body></html>"
                                    
                                    self.email.set_content(mensaje)
                                    smtp = smtplib.SMTP_SSL("smtp-relay.sendinblue.com")
                                    smtp.login(self.user, self.key)
                                    smtp.sendmail(self.remitente, self.destinatario, self.email.as_string())
                                    smtp.quit()
                                    self.__LogReport(f"mail intruso pendiente enviado, fecha: {date}")
                                    time.sleep(0.5)
                                    self.pendientes = False
                                    print("pendientes enviados")
                                
                            except Exception as e:
                                
                                self.__LogReport("No se pudo enviar el mail de intruso pendiente : %s\n" % e)
                        else:
                            time.sleep(5)
                            
                    elif self.door:
                        if auxiliar.CheckInternet():
                            self.email = EmailMessage()
                            
                            self.email["From"] = hbl.Mail_remitente
                            self.email["To"] = hbl.Mail_destinatarios
                            self.email["Subject"] = hbl.Contador_ID + " "+ " Puerta abierta"
                            
                            date = str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
                            try:
                                mensaje = "<html><body><h1> Se ha detectado que la puerta "+hbl.Contador_ID+\
                                          " esta abierta a las : " + date + "</h1></body></html>"
                                self.email.set_content(mensaje)
                                smtp = smtplib.SMTP_SSL("smtp-relay.sendinblue.com")
                                
                                smtp.login(self.user, self.key)
                                smtp.sendmail(self.remitente, self.destinatario, self.email.as_string())
                                smtp.quit()
                                self.__LogReport(f"mail por puerta abierta enviado")
                                
                            except Exception as e:
                                self.__LogReport("No se pudo enviar el mail por puerta abierta : %s\n" % e)
                                
                            self.door = False
                        else:
                            time.sleep(5)
                    else:
                        self.HayIntrusosPendientes()
                        time.sleep(0.5)
                        
    def HayIntrusosPendientes(self):
        myFile = open(hbl.Contador_IntrusosPendientesPath, 'r')

        with myFile:
            if myFile.readline():
                self.pendientes = True 
            else:
                self.pendientes = False
            myFile.close() 
        
=======
                if True:
                    if self.state:
                        self.state = False
                        self.email = EmailMessage()
                        
                        self.email["From"] = hbl.Mail_remitente
                        self.email["To"] = hbl.Mail_destinatarios
                        self.email["Subject"] = self.asunto

        
                        
                        date = str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
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
                            
                            now = datetime.now()
                            self.lastMail = now  
                            
                            
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
>>>>>>> 1bc0f66ad3e87c37389319b87841ad86ddfeacdc
