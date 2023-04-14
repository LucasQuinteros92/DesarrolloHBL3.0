import json
import os
import sys


""" --------------------------------------------------------------------------------------------


   Cargar parametros del JSON en memoria


-------------------------------------------------------------------------------------------- """
class cargarParametros(object):
    def __init__(self ,  archivo):
        # ******************************************************************************************************************************************
        
        
        # variable para guardar que pantalla esta activa
        self.pantallaOled = 1
    

        # ******************************************************************************************************************************************
        #   Inicio de la carga de datos en las variables
        # ******************************************************************************************************************************************

        # path del archivo
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) 
    

        # Leo los parametros de configuracion en el JSON
        with open(os.path.join(__location__ , archivo), "r") as f:
            data = json.load(f)


        
        
        self.ID_HBL = data["IDHBL"]
        self.IDHBL  = data["IDHBL"]
        
        # reporte
        self.REPORTE_idNitro4=data["reporte"]["idNitro4"]       
        self.REPORTE_lastUpdate=data["reporte"]["lastUpdate"]  
        self.REPORTE_tiempoUpdate=data["reporte"]["tiempoUpdate"]
        self.REPORTE_activado=data["reporte"]["activado"]   
        self.REPORTE_timeOutRequest=data["reporte"]["timeOutRequest"]  
        self.REPORTE_encodeAutorization=data["reporte"]["encodeAutorization"]
        self.REPORTE_URLToken=data["reporte"]["URLToken"]
        self.REPORTE_URLChequeoConfiguracion=data["reporte"]["URLChequeoConfiguracion"] 
        self.REPORTE_URLReporteInicial=data["reporte"]["URLReporteInicial"]
        self.REPORTE_URLReporte=data["reporte"]["URLReporte"]


        

        self.TAREAS_Tarea1=data['Tareas']['Tarea1']
        self.TAREAS_Tarea2=data['Tareas']['Tarea2']
        self.TAREAS_Tarea3=data['Tareas']['Tarea3']
        self.TAREAS_Tarea4=data['Tareas']['Tarea4']
        self.TAREAS_Tarea5=data['Tareas']['Tarea5']
        self.TAREAS_Tarea6=data['Tareas']['Tarea6']
        self.TAREAS_Tarea7=data['Tareas']['Tarea7']
        self.TAREAS_Tarea8=data['Tareas']['Tarea8']
        self.TAREAS_Tarea9=data['Tareas']['Tarea9']
        self.TAREAS_Tarea10=data['Tareas']['Tarea10']

        self.TareasJSON = data['Tareas']
        self.CantidadTareas = 0

        for key in self.TareasJSON:
            if self.TareasJSON[key] != "":
                self.CantidadTareas = self.CantidadTareas + 1

        #  Seleccion de funcionamiento hbl
        #
        #   0  :  repetidor wiegand IN : W1 -> OUT : W2
        #   1  :  funcionamiento supeditado al request - IN : W1 -> OUT : W2
        #   2  :  decodificador wiegand W1 - TCP
        #   3  :  decodificador wiegand W1 - decodificador wiegand W2
        #   4  :  hidDevice Teclado - Display LCD - TCP
        #   5  :  lector DNI HID -> wiegand 34
        #   6  :  decodificador wiegand W1 -> envio ID con request a URL (test lector Tags RFID)
        #   7  :  conexion TCP con minipc para envio de datos del teclado
        #   8  :  lectura serial de lector de dni 2D -> envio wiegand 34 al reloj
        #   9  :  decodificador wiegand W1 -> envio ID a dato.json
        self.FUNC_modo=data["funcionamiento"]["modo"]  
        
        # wiegand
        self.WD_W1_activado=data["wiegand"]["W1"]["activado"]
        self.WD_W1_modo=data["wiegand"]["W1"]["modo"]
        self.WD_W1_esperaSenial=data["wiegand"]["W1"]["esperaSenial"]
        self.WD_W1_bits=data["wiegand"]["W1"]["bitsSalida"]
        self.WD_W1_delayPulso=data["wiegand"]["W1"]["delayPulso"]
        self.WD_W1_delayIntervalo=data["wiegand"]["W1"]["delayIntervalo"]
        self.WD_W1_primerBit=data["wiegand"]["W1"]["primerBit"]

        self.WD_W2_activado=data["wiegand"]["W2"]["activado"]
        self.WD_W2_modo=data["wiegand"]["W2"]["modo"]
        self.WD_W2_esperaSenial=data["wiegand"]["W2"]["esperaSenial"]
        self.WD_W2_bitsSalida=data["wiegand"]["W2"]["bitsSalida"]
        self.WD_W2_delayPulso=data["wiegand"]["W2"]["delayPulso"]
        self.WD_W2_delayIntervalo=data["wiegand"]["W2"]["delayIntervalo"]
        self.WD_W2_primerBit=data["wiegand"]["W2"]["primerBit"]


    
        # digital
        self.DIG_in_pushDelay=data["digital"]["in"]["pushDelay"] 
        self.DIG_in_in1_activado=data["digital"]["in"]["in1"]["activado"]
        self.DIG_in_in1_logica=data["digital"]["in"]["in1"]["logica"]
        self.DIG_in_in1_id=data["digital"]["in"]["in1"]["id"]    

        self.DIG_in_in2_activado=data["digital"]["in"]["in2"]["activado"]
        self.DIG_in_in2_logica=data["digital"]["in"]["in2"]["logica"]
        self.DIG_in_in2_id=data["digital"]["in"]["in2"]["id"]
        
        self.DIG_in_in3_activado=data["digital"]["in"]["in3"]["activado"]
        self.DIG_in_in3_logica=data["digital"]["in"]["in3"]["logica"]
        self.DIG_in_in3_id=data["digital"]["in"]["in3"]["id"]

        self.DIG_in_in4_activado=data["digital"]["in"]["in4"]["activado"]
        self.DIG_in_in4_logica=data["digital"]["in"]["in4"]["logica"]
        self.DIG_in_in4_id=data["digital"]["in"]["in4"]["id"]

        if self.DIG_in_in1_logica == "NA":
            self.DIG_in_in1_ON = 0
            self.DIG_in_in1_OFF = 1
        if self.DIG_in_in2_logica == "NA":
            self.DIG_in_in2_ON = 0
            self.DIG_in_in2_OFF = 1
        if self.DIG_in_in3_logica == "NA":
            self.DIG_in_in3_ON = 0
            self.DIG_in_in3_OFF = 1
        if self.DIG_in_in4_logica == "NA":
            self.DIG_in_in4_ON = 0
            self.DIG_in_in4_OFF = 1







    
        self.DIG_out_out1_activado=data["digital"]["out"]["out1"]["activado"]
        self.DIG_out_out1_id=data["digital"]["out"]["out1"]["id"]
        self.DIG_out_out1_repeticion=data["digital"]["out"]["out1"]["repeticion"]
        self.DIG_out_out1_tiempo=data["digital"]["out"]["out1"]["tiempo"]

        self.DIG_out_out2_activado=data["digital"]["out"]["out2"]["activado"]
        self.DIG_out_out2_id=data["digital"]["out"]["out2"]["id"]
        self.DIG_out_out2_repeticion=data["digital"]["out"]["out2"]["repeticion"]
        self.DIG_out_out2_tiempo=data["digital"]["out"]["out2"]["tiempo"]

        self.DIG_out_out3_activado=data["digital"]["out"]["out3"]["activado"]
        self.DIG_out_out3_id=data["digital"]["out"]["out3"]["id"]
        self.DIG_out_out3_repeticion=data["digital"]["out"]["out3"]["repeticion"]
        self.DIG_out_out3_tiempo=data["digital"]["out"]["out3"]["tiempo"]

        self.DIG_out_out4_activado=data["digital"]["out"]["out4"]["activado"]
        self.DIG_out_out4_id=data["digital"]["out"]["out4"]["id"]
        self.DIG_out_out4_repeticion=data["digital"]["out"]["out4"]["repeticion"]
        self.DIG_out_out4_tiempo=data["digital"]["out"]["out4"]["tiempo"]
        
        # define la logica si es inversa o directa

        ON = 0
        OFF = 1

        
        # serial
        self.SERIAL_COM1_activado=data["serial"]["COM1"]["activado"]
        self.SERIAL_COM1_port=data["serial"]["COM1"]["port"]
        self.SERIAL_COM1_baudrate=data["serial"]["COM1"]["baudrate"]
        self.SERIAL_COM1_bytesize=data["serial"]["COM1"]["bytesize"]
        self.SERIAL_COM1_parity=data["serial"]["COM1"]["parity"]
        self.SERIAL_COM1_stopbits=data["serial"]["COM1"]["stopbits"] 

        self.SERIAL_COM2_activado=data["serial"]["COM2"]["activado"]
        self.SERIAL_COM2_port=data["serial"]["COM2"]["port"]
        self.SERIAL_COM2_baudrate=data["serial"]["COM2"]["baudrate"]
        self.SERIAL_COM2_bytesize=data["serial"]["COM2"]["bytesize"]
        self.SERIAL_COM2_parity=data["serial"]["COM2"]["parity"]
        self.SERIAL_COM2_stopbits=data["serial"]["COM2"]["stopbits"]   

        # hidDevices   
        self.HID_device1_activado=data["hidDevices"]["device1"]["activado"]
        self.HID_device1_bufferSize=data["hidDevices"]["device1"]["bufferSize"]
        self.HID_device1_timeout=data["hidDevices"]["device1"]["timeout"]
        self.HID_device1_endpoint=data["hidDevices"]["device1"]["endpoint"]
        self.HID_device1_vendor_ID=data["hidDevices"]["device1"]["vendor_ID"]
        self.HID_device1_product_ID=data["hidDevices"]["device1"]["product_ID"]

        self.HID_device2_activado=data["hidDevices"]["device2"]["activado"]
        self.HID_device2_bufferSize=data["hidDevices"]["device2"]["bufferSize"]
        self.HID_device2_timeout=data["hidDevices"]["device2"]["timeout"]
        self.HID_device2_endpoint=data["hidDevices"]["device2"]["endpoint"]
        self.HID_device2_vendor_ID=data["hidDevices"]["device2"]["vendor_IDself."]
        self.HID_device2_product_ID=data["hidDevices"]["device2"]["product_self.ID"]

        self.HID_device3_activado=data["hidDevices"]["device3"]["activado"]
        self.HID_device3_bufferSize=data["hidDevices"]["device3"]["bufferSize"]
        self.HID_device3_timeout=data["hidDevices"]["device3"]["timeout"]
        self.HID_device3_endpoint=data["hidDevices"]["device3"]["endpoint"]
        self.HID_device3_vendor_ID=data["hidDevices"]["device3"]["vendor_ID"]
        self.HID_device3_product_ID=data["hidDevices"]["device3"]["product_ID"]

        self.HID_device4_activado=data["hidDevices"]["device4"]["activado"]
        self.HID_device4_bufferSize=data["hidDevices"]["device4"]["bufferSize"]
        self.HID_device4_timeout=data["hidDevices"]["device4"]["timeout"]
        self.HID_device4_endpoint=data["hidDevices"]["device4"]["endpoint"]
        self.HID_device4_vendor_ID=data["hidDevices"]["device4"]["vendor_ID"]
        self.HID_device4_product_ID=data["hidDevices"]["device4"]["product_ID"]

        # tcp 
        self.TCP_serverDefault_ip=data["tcp"]["serverDefault"]["ip"]
        self.TCP_serverDefault_port=data["tcp"]["serverDefault"]["port"]
        self.TCP_serverDefault_activado=data["tcp"]["serverDefault"]["activado"]
        self.TCP_serverDefault_intentosConexion=data["tcp"]["serverDefault"]["intentosConexion"] 

        # http
        self.HTTP_server_activado=data["http"]["server"]["activado"]
        self.HTTP_server_port=data["http"]["server"]["port"]
        self.HTTP_server_respuesta=data["http"]["server"]["respuesta"] 

    
        # request
        self.REQ_activado=data["request"]["activado"]
        self.REQ_seleccionURL=data["request"]["seleccionURL"] 
        self.REQ_urlRequest1=data["request"]["urlRequest1"] 
        self.REQ_urlRequest2=data["request"]["urlRequest2"] 
        self.REQ_urlRequest3=data["request"]["urlRequest3"] 
        self.REQ_urlRequest4=data["request"]["urlRequest4"] 
        self.REQ_urlRequest5=data["request"]["urlRequest5"] 

        self.REQ_urlError=data["request"]["urlError"] 
        self.REQ_timeoutRequest=data["request"]["timeoutRequest"] 
        self.REQ_timerActivado=data["request"]["timerActivado"]


        self.TXT_activado=data["GenerarTXT"]["activado"]
        self.TXT_path=data["GenerarTXT"]["path"]

        # log   
        self.LOGS_pathBackup=data["logs"]["pathBackup"] 
        self.LOGS_tamanioRotator=data["logs"]["tamanioRotator"] 
        self.LOGS_hblCore=data["logs"]["hblCore"]  
        self.LOGS_hblConexiones=data["logs"]["hblConexiones"] 
        self.LOGS_hblWiegand=data["logs"]["hblWiegand"] 
        self.LOGS_hblTcp=data["logs"]["hblTcp"] 
        self.LOGS_hblEntradas=data["logs"]["hblEntradas"] 
        self.LOGS_hblHTTP=data["logs"]["hblHTTP"]  
        self.LOGS_hblReporte=data["logs"]["hblReporte"]  
        self.LOGS_hblhidDevice=data["logs"]["hblhidDevice"]  
        self.LOGS_hbli2c=data["logs"]["hbli2c"] 
        self.LOGS_FTP=data["logs"]["hblFTP"] 
        self.LOGS_hblSerial=data["logs"]["hblSerial"]   
        self.LOGS_hblCacheo=data["logs"]["hblCacheo"]    
        self.LOGS_hblKiosco=data["logs"]["hblKiosco"]    
        self.LOGS_hblTareas=data["logs"]["hblTareas"]
        self.LOGS_hblBioStar2_WebSocket=data["logs"]["hblBioStar2_WebSocket"]
        
        self.LOGS_hblEsclusa = data["logs"]["hblEsclusa"]
        self.LOGS_hblMQTT = data["logs"]["hblMQTT"]
        self.LOGS_hblTimer = data["logs"]["hblTimer"]

        self.LOGS_hblPuerta = data["logs"]["hblPuerta"]
        self.LOGS_hblMail   = data["logs"]["hblMail"]
        self.LOGS_hblCamaraRPI = data["logs"]["hblCamaraRPI"]
        self.LOGS_hblSensorUltrasonico = data["logs"]["hblSensorUltrasonico"]

        


        self.DISPLAY_activado  =  data["display"]["activado"]
        self.DISPLAY_line0     =  data["display"]["line0"]
        self.DISPLAY_line1     =  data["display"]["line1"]
        self.DISPLAY_line2     =  data["display"]["line2"]
        self.DISPLAY_line3     =  data["display"]["line3"]
        
        # network
        self.NETWORK_activado=data["network"]["activado"]

        self.NETWORK_eth0_activado=data["network"]["eth0"]["activado"]
        self.NETWORK_eth0_dhcp=data["network"]["eth0"]["dhcp"]
        self.NETWORK_eth0_static_ip_address=data["network"]["eth0"]["static_ip_address"]
        self.NETWORK_eth0_static_routers=data["network"]["eth0"]["static_routers"]
        self.NETWORK_eth0_gateway=data["network"]["eth0"]["gateway"]
        self.NETWORK_eth0_DNS=data["network"]["eth0"]["DNS"]
        self.NETWORK_eth0_netmask=data["network"]["eth0"]["netmask"]
        self.NETWORK_eth0_network=data["network"]["eth0"]["network"]
        self.NETWORK_eth0_broadcast=data["network"]["eth0"]["broadcast"]  
        self.NETWORK_eth0_metric=data["network"]["eth0"]["metric"]

        self.NETWORK_eth1_activado=data["network"]["eth1"]["activado"]
        self.NETWORK_eth1_dhcp=data["network"]["eth1"]["dhcp"]
        self.NETWORK_eth1_static_ip_address=data["network"]["eth1"]["static_ip_address"]
        self.NETWORK_eth1_static_routers=data["network"]["eth1"]["static_routers"]
        self.NETWORK_eth1_gateway=data["network"]["eth1"]["gateway"]
        self.NETWORK_eth1_DNS=data["network"]["eth1"]["DNS"]
        self.NETWORK_eth1_netmask=data["network"]["eth1"]["netmask"]
        self.NETWORK_eth1_network=data["network"]["eth1"]["network"]
        self.NETWORK_eth1_broadcast=data["network"]["eth1"]["broadcast"]  
        self.NETWORK_eth1_metric=data["network"]["eth1"]["metric"]
        self.NETWORK_eth1_vendor_ID=data["network"]["eth1"]["vendor_ID"]  
        self.NETWORK_eth1_product_ID=data["network"]["eth1"]["product_ID"] 
        self.NETWORK_eth1_timeDelay=data["network"]["eth1"]["timeDelay"] 

        self.NETWORK_wlan0_activado=data["network"]["wlan0"]["activado"]
        self.NETWORK_wlan0_dhcp=data["network"]["wlan0"]["dhcp"]
        self.NETWORK_wlan0_static_ip_address=data["network"]["wlan0"]["static_ip_address"]
        self.NETWORK_wlan0_static_routers=data["network"]["wlan0"]["static_routers"]
        self.NETWORK_wlan0_gateway=data["network"]["wlan0"]["gateway"]
        self.NETWORK_wlan0_DNS=data["network"]["wlan0"]["DNS"]
        self.NETWORK_wlan0_netmask=data["network"]["wlan0"]["netmask"]
        self.NETWORK_wlan0_network=data["network"]["wlan0"]["network"]
        self.NETWORK_wlan0_broadcast=data["network"]["wlan0"]["broadcast"] 
        self.NETWORK_wlan0_metric=data["network"]["wlan0"]["metric"]
        self.NETWORK_wlan0_ssid=data["network"]["wlan0"]["ssid"]
        self.NETWORK_wlan0_password=data["network"]["wlan0"]["password"] 

        self.NETWORK_ppp0_activado=data["network"]["ppp0"]["activado"]
        self.NETWORK_ppp0_vendor_ID=data["network"]["ppp0"]["vendor_ID"]
        self.NETWORK_ppp0_product_ID=data["network"]["ppp0"]["product_ID"]  
        self.NETWORK_ppp0_dialcommand=data["network"]["ppp0"]["dialcommand"]
        self.NETWORK_ppp0_init1=data["network"]["ppp0"]["init1"]
        self.NETWORK_ppp0_init2=data["network"]["ppp0"]["init2"]
        self.NETWORK_ppp0_init3=data["network"]["ppp0"]["init3"]
        self.NETWORK_ppp0_init4=data["network"]["ppp0"]["init4"]
        self.NETWORK_ppp0_stupidmode=data["network"]["ppp0"]["stupidmode"]
        self.NETWORK_ppp0_ISDN=data["network"]["ppp0"]["ISDN"]
        self.NETWORK_ppp0_modemType=data["network"]["ppp0"]["modemType"]
        self.NETWORK_ppp0_askPassword=data["network"]["ppp0"]["askPassword"]
        self.NETWORK_ppp0_phone=data["network"]["ppp0"]["phone"] 
        self.NETWORK_ppp0_username=data["network"]["ppp0"]["username"]
        self.NETWORK_ppp0_password=data["network"]["ppp0"]["password"]
        self.NETWORK_ppp0_baud=data["network"]["ppp0"]["baud"]
        self.NETWORK_ppp0_newPPPD=data["network"]["ppp0"]["newPPPD"]
        self.NETWORK_ppp0_carrierCheck=data["network"]["ppp0"]["carrierCheck"]
        self.NETWORK_ppp0_autoReconnect=data["network"]["ppp0"]["autoReconnect"] 
        self.NETWORK_ppp0_dialAttempts=data["network"]["ppp0"]["dialAttempts"] 
        self.NETWORK_ppp0_metric=data["network"]["ppp0"]["metric"] 
    
        self.NETWORK_testConexion_activado=data["network"]["testConexion"]["activado"] 
        self.NETWORK_testConexion_url=data["network"]["testConexion"]["url"] 
        self.NETWORK_testConexion_timeoutUrl=data["network"]["testConexion"]["timeoutUrl"] 
        self.NETWORK_testConexion_timeDelay=data["network"]["testConexion"]["timeDelay"] 
        self.NETWORK_testConexion_timeRepeat=data["network"]["testConexion"]["timeRepeat"] 
        self.NETWORK_testConexion_intentosConexion=data["network"]["testConexion"]["intentosConexion"] 
        self.NETWORK_testConexion_resetActivado=data["network"]["testConexion"]["resetActivado"]   

        self.FTP_activado=data["ftp"]["activado"] 
        self.FTP_server=data["ftp"]["server"] 
        self.FTP_user=data["ftp"]["user"] 
        self.FTP_pass=data["ftp"]["pass"]     

        self.CACHEO_activado=data["cacheo"]["activado"] 
        self.CACHEO_cantidadCacheos=data["cacheo"]["cantidadCacheos"]
        self.CACHEO_cacheosPositivos=data["cacheo"]["cacheosPositivos"]
        self.CACHEO_tiempoRelePositivo=data["cacheo"]["tiempoRelePositivo"]
        self.CACHEO_repRelePositivo=data["cacheo"]["repRelePositivo"]
        self.CACHEO_tiempoReleNegativo=data["cacheo"]["tiempoReleNegativo"]
        self.CACHEO_repReleNegativo=data["cacheo"]["repReleNegativo"]


        self.KIOSCO_activado=data["kiosco"]["activado"]
        self.KIOSCO_URL=data["kiosco"]["URL"]
        self.KIOSCO_width=data["kiosco"]["width"]
        self.KIOSCO_height=data["kiosco"]["height"]
        
        self.MQTT_activado=data["MQTT"]["activado"]
        self.MQTT_broker=data["MQTT"]["broker"]
        self.MQTT_port=data["MQTT"]["port"]
        self.MQTT_TopicSend=data["MQTT"]["TopicSend"]
        self.MQTT_TopicRecv=data["MQTT"]["TopicRecv"]


        self.Audio_activado=data["Audio"]["activado"]
        self.Audio_path_Pasa=data["Audio"]["path"]["Pasa"]
        self.Audio_path_NoPasa=data["Audio"]["path"]["NoPasa"]
        self.Audio_path_ErrorDNI=data["Audio"]["path"]["ErrorDNI"]
        
        self.BioStar2_WebSocket_activado=data["BioStar2_WebSocket"]["activado"]
        self.BioStar2_WebSocket_WebSocket_Host=data["BioStar2_WebSocket"]["WebSocket_Host"]
        self.BioStar2_WebSocket_Api_Host=data["BioStar2_WebSocket"]["Api_Host"]
        self.BioStar2_WebSocket_Tipo_Evento=data["BioStar2_WebSocket"]["Tipo_Evento"]
        self.BioStar2_WebSocket_Device_ID=data["BioStar2_WebSocket"]["Device_ID"]
        self.BioStar2_WebSocket_BioStar2_User=data["BioStar2_WebSocket"]["BioStar2_User"]
        self.BioStar2_WebSocket_BioStar2_Password=data["BioStar2_WebSocket"]["BioStar2_Password"]

        #CONTADOR DE PERSONAS
        self.Contador_activado                = data["ContadorPersonas"]["activado"]
        self.Contador_MaxTimeIN               = data["ContadorPersonas"]["MaxTimeIN"]
        self.Contador_MaxTimeAlarma           = data["ContadorPersonas"]["MaxTimeAlarma"]
        self.Contador_MaxTimeBlink            = data["ContadorPersonas"]["MaxTimeBlink"]
        self.Contador_MaxTimeLEDCicloCompleto = data["ContadorPersonas"]["MaxTimeLEDCicloCompleto"]
        self.Contador_MaxTimePuerta           = data["ContadorPersonas"]["MaxTimePuerta"]
        self.Contador_MaxTimeEnable           = data["ContadorPersonas"]["MaxTimeEnable"]
        self.Contador_MaxTimeDisable          = data["ContadorPersonas"]["MaxTimeDisable"]
        self.Contador_TiempoBlinkAlarmaPuerta = data["ContadorPersonas"]["TiempoBlinkAlarmaPuerta"]
        self.Contador_IntrusosPendientesPath  = data["ContadorPersonas"]["IntrusosPendientesPath"]
        self.Contador_ID                      = data["ContadorPersonas"]["ID"]
        self.Contador_Buzzer                  = data["ContadorPersonas"]["Buzzer"]
        self.Contador_MailPuertaAbierta       = data["ContadorPersonas"]["MailPuertaAbierta"]
        self.Contador_DebugSensores           = data["ContadorPersonas"]["DebugSensores"]
        
        #Mails
        self.Mail_activado                   = data["Mail"]["activado"]
        self.Mail_destinatarios              = data["Mail"]["destinatarios"]
        self.Mail_remitente                  = data["Mail"]["remitente"]
        self.Mail_user                       = data["Mail"]["user"]
        self.Mail_subject                    = data["Mail"]["subject"]
        self.Mail_key                        = data["Mail"]["key"]
        self.Mail_message                    = data["Mail"]["message"]
    
        #Camara RPI
        self.Camara_RPI_activado             = data["Camara_RPI"]["activado"]
        self.Camara_RPI_Resolucion           = data["Camara_RPI"]["Resolucion"]
        self.Camara_RPI_Path_Realativo       = data["Camara_RPI"]["Path_Relativo"]
        self.Camara_RPI_Duracion_Video_seg   = data["Camara_RPI"]["Duracion_Video_seg"]
        
        
        self.sensorUltrasonico_activado              = data["sensorUltrasonico"]["activado"]
        self.sensorUltrasonico_cantidadMuestras      = data["sensorUltrasonico"]["cantidadMuestras"]
        self.sensorUltrasonico_distanciaTrigger_cm   = data["sensorUltrasonico"]["distanciaTrigger_cm"]

        return self