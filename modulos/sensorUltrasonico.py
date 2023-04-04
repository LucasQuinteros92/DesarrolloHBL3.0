import datetime 
from threading import Thread

from modulos import variablesGlobales as variablesGlobales
from modulos import log as log
from modulos import hbl as hbl
from modulos import auxiliar as auxiliar
import RPi.GPIO as GPIO
import time


Flanco_Inicializado = 0
Primer_Flanco = datetime.datetime.now() 

#Hacer todo como un thread que toma x muestras, las promedia y devuelve resultado

DISTANCE_KEY = 150 #cm
TIMEOUT = 8 #segundos

def shift(l, n):
    n = n % len(l)
    return l[n:] + l[:n]


class sensorUltrasonico(object):
    def __init__(self,pinECHO,pinTRIG,nMuestras):
        if hbl.sensorUltrasonico_activado:
            try:
                self.distancia_prom = 0
                self.pinECHO = pinECHO
                self.pinTRIG = pinTRIG
                self.nMuestras = nMuestras
                #Lista de n elementos con valores 2 veces mas grandes que el valor de trigger para asegurar que no se dispare hasta 
                # que las muestras sean reales.  n es self.nMuestras
                self.muestras = [DISTANCE_KEY*2] * self.nMuestras 
                self.state_obstaculo = False
                self.Flanco_SENPROX = False
                self.Distance_Prev = False
                self.before_FlancoOFF = datetime.datetime.now()
                
                self.t = Thread(target = self.start, daemon= False)
                self.t.start()
            except Exception as e:
                print("Error al inicializar la camara")

    def ReadDistance(self):
            #Contenemos el código principal en un aestructura try para limpiar los GPIO al terminar o presentarse un error
        try:
            GPIO.setmode(GPIO.BCM)     #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi            
            GPIO.setup(self.pinTRIG, GPIO.OUT) #Configuramos el pin self.pinTRIG como una salida 
            GPIO.setup(self.pinECHO, GPIO.IN)  #Configuramos el pin self.pinECHO como una salida
            # Ponemos en bajo el pin self.pinTRIG y después esperamos 0.5 seg para que el transductor se estabilice
            GPIO.output(self.pinTRIG, GPIO.LOW)
            time.sleep(0.5)

            #Ponemos en alto el pin self.pinTRIG esperamos 10 uS antes de ponerlo en bajo
            GPIO.output(self.pinTRIG, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(self.pinTRIG, GPIO.LOW)

            # En este momento el sensor envía 8 pulsos ultrasónicos de 40kHz y coloca su pin self.pinECHO en alto
            # Debemos detectar dicho evento para iniciar la medición del tiempo

            a = datetime.datetime.now()
            while True:
                pulso_inicio = time.time()
                if GPIO.input(self.pinECHO) == GPIO.HIGH:
                    break
                b = datetime.datetime.now()
                c = b-a
                if c.total_seconds() >= TIMEOUT:
                    return False
            
            # El pin self.pinECHO se mantendrá en HIGH hasta recibir el eco rebotado por el obstáculo. 
            # En ese momento el sensor pondrá el pin self.pinECHO en bajo.
        # Prodedemos a detectar dicho evento para terminar la medición del tiempo
            a = datetime.datetime.now()
            while True:
                pulso_fin = time.time()
                if GPIO.input(self.pinECHO) == GPIO.LOW:
                    break
                b = datetime.datetime.now()
                c = b-a
                if c.total_seconds() >= TIMEOUT:
                    return False
            
            # Tiempo medido en segundos
            duracion = pulso_fin - pulso_inicio

            #Obtenemos la distancia considerando que la señal recorre dos veces la distancia a medir y que la velocidad del sonido es 343m/s
            distancia = (34300 * duracion) / 2
            
            #shift(self.muestras,1)
            #La siguiente linea borra el primer elemento de la lista y lo agrega al final para luego ser pisado en la siguiente linea
            self.muestras.append(self.muestras.pop(0)) 
            self.muestras[self.nMuestras-1] = distancia
            
            self.distancia_prom = sum(self.muestras)/self.nMuestras
            
            # Imprimimos resultado
            log.escribeSeparador(hbl.LOGS_hblSensorUltrasonico)
            log.escribeLineaLog(hbl.LOGS_hblSensorUltrasonico, f"Vector de muestras: {str(self.muestras)}\nDistancia medida: {str(distancia)} cm\nDistancia promedio: {str(self.distancia_prom)} cm")

            if self.distancia_prom > DISTANCE_KEY:
                if self.Flanco_SENPROX == True:
                    self.before_FlancoOFF = datetime.datetime.now() 
                    self.Flanco_SENPROX = False
                else:
                    after_FlancoOFF = datetime.datetime.now()
                    time_OFF = after_FlancoOFF - self.before_FlancoOFF
                    if time_OFF.total_seconds() >= 6:                      
                        return False

            else:
                self.Flanco_SENPROX = 1
                return True


        finally:
            # Reiniciamos todos los canales de GPIO.
            GPIO.cleanup()
            #return False
            
    
    def ReadState(self):
        return self.state_obstaculo

    def start(self):
        while True:
            distancia = self.ReadDistance()
            try:
                if distancia == True and self.Distance_Prev==False:
                    self.Distance_Prev = True
                    log.escribeSeparador(hbl.LOGS_hblEntradas) 
                    log.escribeLineaLog(hbl.LOGS_hblEntradas, "Sensor Prox: ON") 
                    self.state_obstaculo = True

                if distancia == False and self.Distance_Prev==True:
                    self.Distance_Prev = False
                    log.escribeSeparador(hbl.LOGS_hblEntradas) 
                    log.escribeLineaLog(hbl.LOGS_hblEntradas, "Sensor Prox: OFF")
                    self.state_obstaculo = False

            except Exception as inst:  
                log.escribeLineaLog(hbl.LOGS_hblEntradas, "ERROR SENSOR: " + str(inst) + "\n") 
                self.state_obstaculo = False

            
            time.sleep(0.5)