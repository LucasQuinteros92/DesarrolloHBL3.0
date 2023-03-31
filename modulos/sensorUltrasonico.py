

import datetime 
import requests

from modulos import variablesGlobales as variablesGlobales
from modulos import log as log
from modulos import hbl as hbl
import RPi.GPIO as GPIO
import time


Flanco_Inicializado = 0
Primer_Flanco = datetime.datetime.now() 

TRIG = 27 #Variable que contiene el GPIO al cual conectamos la señal TRIG del sensor
ECHO = 17 #Variable que contiene el GPIO al cual conectamos la señal ECHO del sensor
DISTANCE_KEY = 150 #cm
TIMEOUT = 8 #segundos


def ReadDistance():
    GPIO.setmode(GPIO.BCM)     #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi            
    GPIO.setup(TRIG, GPIO.OUT) #Configuramos el pin TRIG como una salida 
    GPIO.setup(ECHO, GPIO.IN)  #Configuramos el pin ECHO como una salida 

        #Contenemos el código principal en un aestructura try para limpiar los GPIO al terminar o presentarse un error
    try:
        # Ponemos en bajo el pin TRIG y después esperamos 0.5 seg para que el transductor se estabilice
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.5)

        #Ponemos en alto el pin TRIG esperamos 10 uS antes de ponerlo en bajo
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)

        # En este momento el sensor envía 8 pulsos ultrasónicos de 40kHz y coloca su pin ECHO en alto
        # Debemos detectar dicho evento para iniciar la medición del tiempo

        a = datetime.datetime.now()
        while True:
            pulso_inicio = time.time()
            if GPIO.input(ECHO) == GPIO.HIGH:
                break
            b = datetime.datetime.now()
            c = b-a
            if c.total_seconds() >= TIMEOUT:
                return False
        
        # El pin ECHO se mantendrá en HIGH hasta recibir el eco rebotado por el obstáculo. 
        # En ese momento el sensor pondrá el pin ECHO en bajo.
    # Prodedemos a detectar dicho evento para terminar la medición del tiempo
        a = datetime.datetime.now()
        while True:
            pulso_fin = time.time()
            if GPIO.input(ECHO) == GPIO.LOW:
                break
            b = datetime.datetime.now()
            c = b-a
            if c.total_seconds() >= TIMEOUT:
                return False
        
        # Tiempo medido en segundos
        duracion = pulso_fin - pulso_inicio

        #Obtenemos la distancia considerando que la señal recorre dos veces la distancia a medir y que la velocidad del sonido es 343m/s
        distancia = (34300 * duracion) / 2

        # Imprimimos resultado
        ##print( "Distancia: %.2f cm" % distancia)

        if distancia > DISTANCE_KEY:
            if variablesGlobales.Flanco_SENPROX == 1:
                variablesGlobales.before_FlancoOFF = datetime.datetime.now() 
                variablesGlobales.Flanco_SENPROX = 0
            else:
                after_FlancoOFF = datetime.datetime.now()
                time_OFF = after_FlancoOFF - variablesGlobales.before_FlancoOFF
                if time_OFF.total_seconds() >= 6:                      
                    return False

        else:
            variablesGlobales.Flanco_SENPROX = 1
            return True


    finally:
        # Reiniciamos todos los canales de GPIO.
        GPIO.cleanup()
        #return False


def ReadState():
    try:
        if ReadDistance() == True and variablesGlobales.Distance_Prev==0:
            variablesGlobales.Distance_Prev = 1
            log.escribeSeparador(hbl.LOGS_hblEntradas) 
            log.escribeLineaLog(hbl.LOGS_hblEntradas, "Sensor Prox: ON") 
            return True

        if ReadDistance() == False and variablesGlobales.Distance_Prev==1:
            variablesGlobales.Distance_Prev = 0
            log.escribeSeparador(hbl.LOGS_hblEntradas) 
            log.escribeLineaLog(hbl.LOGS_hblEntradas, "Sensor Prox: OFF")
            return False

    except Exception as inst:  
        log.escribeLineaLog(hbl.LOGS_hblEntradas, "ERROR SENSOR: " + str(inst) + "\n") 
        return False