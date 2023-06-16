""" --------------------------------------------------------------------------------------------

    _   _ ____  _     
   | | | | __ )| |    
   | |_| |  _ \| |    
   |  _  | |_) | |___ 
   |_| |_|____/|_____|
                   
   (Hardware building layers)
   v3.0

-------------------------------------------------------------------------------------------- """

import os
import sys
import pigpio
import signal
import time
import datetime
import json
from modulos import delays as delays
from modulos import hbl as hbl
from modulos import hidDevice as hidDevice
from modulos import i2cDevice as i2cDevice
from modulos import tcp as tcp
from modulos import log as log
from modulos import hblCore as hblCore
from modulos import conexiones as conexiones
from modulos import reporte as reporte
from modulos import ftp as ftp
from modulos import tcp as tcp
from modulos import httpServer as httpServer
from modulos import serial as serial
from modulos import kiosco as kiosco
from modulos import MQTT as MQTT
from modulos import Monitoreo as Monitoreo
from modulos import funcionamiento as funcionamiento
from modulos import Control_Personal as CP
from modulos import SendMail
from modulos import BioStar2_WebSocket
from modulos import CamaraRPI


from modulos.decoderWiegand import Decoder
from modulos.encoderWiegand import Encoder
from modulos.salidas import Salidas
from modulos.entradas import Entradas




dicc  = {   
            "objeto":{
                        "ob":{
                            "ob":1,
                            "ob2":"string"    
                        },
                        "ob2":"cont"
            },
            "rango":{
                "hbl" : 2,
                "ID" : "nombre"
            }
}

class HBL(object):
    def __init__(self):
        self.pi = pigpio.pi()

        # cargar parametros del archivo de configuracion
        #self = hbl.cargarParametros(self, 'hbl.json')
        
        self.Cargarparametros()
            
        
        #print(self.__dict__)
        #print(self.BioStar2_WebSocket_Tipo_Evento)
    
    def funcionamiento(self):
        pass
    
    def Cargarparametros(self):
        # path del archivo
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 
        print(__location__)
        # Leo los parametros de configuracion en el JSON
        with open(os.path.join(__location__+"/modulos" , "hbl.json"), "r") as f:
            data = json.load(f)

        self.JSONtoSELF(data,modulo='request')
        
    def JSONtoSELF(self, dic1,name = '',modulo = ''):

        for key in dic1:

            
            if type(dic1[key]) == dict and (key == modulo or modulo == 'TODO'):
                
                
                self.JSONtoSELF( dic1[key],name + key + '_',modulo='TODO')
                
                    
                
            elif modulo == '' or modulo == 'TODO':
                if dic1[key] is not None or dic1[key] != " ":
                    
                    self.__dict__[name+key] = dic1[key]
                    
                    print(name + key, ":",dic1[key])
                    
                
            
            #for item in variables[key]:
            #    print("item")
        name = ''
            
        
            
if __name__ == "__main__":
    HBL()
    
