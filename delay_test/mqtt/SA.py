import random
import DAI
import DAN
import time 

ServerURL = "https://class.iottalk.tw" #For example: 'https://DomainName'
MQTT_broker = None #"class.iottalk.tw"#"localhost" # MQTT Broker address, for example: 'DomainName' or None = no MQTT support
MQTT_port = 1883
MQTT_encryption = False
MQTT_User = 'iottalk'
MQTT_PW = 'iottalk2023'

device_model = 'Dummy_Device'
IDF_list = ['Dummy_Sensor']
ODF_list = ['Dummy_Control']
device_id = None #if None, device_id = MAC address
device_name = 'Dennis_device'
exec_interval = 1  # IDF/ODF interval

def Dummy_Sensor():
    return random.randint(0, 100) 

def Dummy_Control(data:list):
    return data[0]

def on_register(r):
    print(f'Device name: {r["d_name"]}')  
          
    '''
    #You can write some SA routine code here, for example: 
    import time, DAI
    while True:
        DAI.push('Dummy_Sensor', [100, 200])  
        time.sleep(exec_interval)    
    '''
    

'''
pip install requests paho-mqtt

'''