from modulos import log as log
from modulos import hbl as hbl

import time
from picamera import PiCamera
from datetime import datetime
from threading import Thread



class CamaraRPI(object):
    def __init__(self):
        if hbl.Camara_RPI_activado:
            try:
                self.flag = False
                self.tiempo_captura = 0
                self.path = hbl.Camara_RPI_Path_Realativo
                if hbl.Camara_RPI_activado:
                    self.t = Thread(target = self.start, daemon= False)
                    self.t.start()
            except Exception as e:
                print("Error al inicializar la camara")
    
    def Capturar(self, time):
        self.flag = True
        self.tiempo_captura = time
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        self.path = hbl.Camara_RPI_Path_Realativo + dt_string
        if self.tiempo_captura > 0:
            self.path += ".h264"
        else:
            self.path += ".png"
        
        return self.path
        
    def Capturar_Video(self):
        self.camera.start_recording(self.path)
        time.sleep(self.tiempo_captura)
        self.camera.stop_recording()
        
    def Capturar_Foto(self):
        self.camera.capture(self.path)
        
        
        
    def start(self):
        if hbl.Camara_RPI_activado:
            if self.flag:
                self.camera = PiCamera()
                self.camera.resolution = (hbl.Camara_RPI_Resolucion[0],hbl.Camara_RPI_Resolucion[1])
                try:
                    self.camera.start_preview()
                    time.sleep(2)
                    
                    if self.tiempo_captura > 0:
                        self.Capturar_Video()
                    else:
                        self.Capturar_Foto()
                    self.camera.close()
                    self.flag = False
                except Exception as e:
                    log.escribeSeparador(hbl.LOGS_hblEntradas) 
                    log.escribeLineaLog(hbl.LOGS_hblEntradas, e) 
                    self.flag = False