
import time, random, requests
import DAN
import crawl

#ServerURL = 'http://yourServerIP:9999'     #with non-secure connection;
ServerURL = 'https://3.iottalk.tw'
#Reg_addr = None 
Reg_addr = "AABB3388" + str( random.randint(100,999 ) )  #None #if None, Reg_addr = MAC address
##  �W�C�쪩 Reg_addr =  None # �h�b DAN.py ���|�� UUID, �o�ˤ@���q���u��]�@���o�{��
# DAN.profile['dm_name']='dashboard'
# DAN.profile['df_list']=['溫度idf',
#                         '風力idf',
#                         '濕度idf',
#                         '氣壓idf',
                        
#                         '溫度odf',
#                         '風力odf',
#                         '濕度odf',
#                         '氣壓odf',]  
DAN.profile['dm_name']='Tingweather'
DAN.profile['df_list']=['AtPressure',
                        'Humidity1',
                        'Temperature1',
                        'Wind1']  
DAN.profile['d_name']= str( random.randint(1,999))+'.TingWei'  ##  who are you? �A�O�� 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

while True:
    try:
        data = crawl.getdata()
        for idx, row in data.iterrows():
            # print(row)
            DAN.push ('AtPressure',row['海平面氣壓(百帕)'])
            time.sleep(0.2)
            # DAN.push ('天氣idf', data['天氣'][0])
            # time.sleep(0.1)
            DAN.push ('Humidity1', row['相對溼度(%)'])
            time.sleep(0.2)
            DAN.push ('Temperature1', row['溫度(°C)'])
            time.sleep(0.2)
            DAN.push ('Wind1', row['風力 (m/s)'])
            time.sleep(0.2)
        print('finish idf')
        #==================================

        # ODF_data = DAN.pull('TingweatherODF')#Pull data from an output device feature "Dummy_Control"
        # if ODF_data != None:
        #     print (ODF_data[0])
        

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(100)
