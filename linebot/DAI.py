
import time, random, requests
import DAN
import crawl

#ServerURL = 'http://yourServerIP:9999'     #with non-secure connection;
ServerURL = 'https://7.iottalk.tw'
#Reg_addr = None 
Reg_addr = "AABB3388" + str( random.randint(100,999 ) )  #None #if None, Reg_addr = MAC address
DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list'] = ['Dummy_Sensor', 'Dummy_Control']
DAN.profile['d_name']= str( random.randint(1,999))+'.TingWei'  ##  who are you? �A�O�� 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

def pushIDF(data):
    DAN.push('Dummy_Sensor',data)
    time.sleep(0.2)

def getdata(datatype):
    try:
        data = crawl.getdata()
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)  
    match datatype:
        case "觀測時間":
            pushIDF(str(data['觀測時間'][0]));
        case "溫度":
            pushIDF(data['溫度(°C)'][0]);    
        case "天氣":
            pushIDF(data['天氣'][0]);    
        case "風向":
            pushIDF(data['風向'][0]);    
        case "風力":
            pushIDF(data['風力 (m/s)'][0]);    
        case "陣風":
            pushIDF(data['陣風 (m/s)'][0]);    
        case "能見度": 
            pushIDF(data['能見度(公里)'][0]);   
        case "濕度":
            pushIDF(data['相對溼度(%)'][0]);    
        case "氣壓":
            pushIDF(data['海平面氣壓(百帕)'][0]);    
        case "累積雨量":
            pushIDF(data['當日累積雨量(毫米)'][0]);    
        case "日照時數":
            pushIDF(data['日照時數(小時)'][0]);    
            #==================================
        case _:
            pushIDF('Hi! This is you weather assistant. I can only reply relative information.')
            
    ODF_data = DAN.pull('Dummy_Control')#Pull data from an output device feature "Dummy_Control"
    if ODF_data != None:
        print (ODF_data)
        
    return ODF_data

             

