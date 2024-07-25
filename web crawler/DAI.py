
import time, random, requests
import DAN
import crawl

#ServerURL = 'http://yourServerIP:9999'     #with non-secure connection;
ServerURL = 'https://2.iottalk.tw'
#Reg_addr = None 
Reg_addr = "AABB3388" + str( random.randint(100,999 ) )  #None #if None, Reg_addr = MAC address
##  �W�C�쪩 Reg_addr =  None # �h�b DAN.py ���|�� UUID, �o�ˤ@���q���u��]�@���o�{��
DAN.profile['dm_name']='Tingweather'
DAN.profile['df_list']=['觀測時間',
                        '溫度',
                        '天氣',
                        '風向',
                        '風力',
                        '陣風',
                        '能見度',
                        '相對溼度',
                        '氣壓',
                        '累積雨量',
                        '日照時數','TingweatherODF']  
DAN.profile['d_name']= str( random.randint(1,999))+'.TingWei'  ##  who are you? �A�O�� 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

while True:
    try:
        time.sleep(20)
        data = crawl.getdata()
        print(data) 
        DAN.push ('觀測時間', str(data['觀測時間'][0]))
        time.sleep(0.5)
        DAN.push ('溫度', data['溫度(°C)'][0])
        time.sleep(0.5)
        DAN.push ('天氣', data['天氣'][0])
        time.sleep(0.5)
        DAN.push ('風向', data['風向'][0])
        time.sleep(0.5)
        DAN.push ('風力', data['風力 (m/s)'][0])
        time.sleep(0.5)
        DAN.push ('陣風', data['陣風 (m/s)'][0])
        time.sleep(0.5)
        DAN.push ('能見度', data['能見度(公里)'][0])
        time.sleep(0.5)
        DAN.push ('相對溼度', data['相對溼度(%)'][0])
        time.sleep(0.5)
        DAN.push ('氣壓', data['海平面氣壓(百帕)'][0])
        time.sleep(0.5)
        DAN.push ('累積雨量', data['當日累積雨量(毫米)'][0])
        time.sleep(0.5)
        DAN.push ('日照時數', data['日照時數(小時)'][0])
        time.sleep(0.5)
        #==================================

        ODF_data = DAN.pull('TingweatherODF')#Pull data from an output device feature "Dummy_Control"
        if ODF_data != None:
            print (ODF_data[0])

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(30)
