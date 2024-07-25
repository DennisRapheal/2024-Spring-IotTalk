import time, random, requests
import DAN
import statistics
from time import process_time

ServerURL = "https://class.iottalk.tw"      #with non-secure connection
#ServerURL = 'https://DomainName' #with SSL connection
Reg_addr = None #if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['Dummy_Sensor', 'Dummy_Control',]
#DAN.profile['d_name']= 'Assign a Device Name' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#DAN.deregister()  #if you want to deregister this device, uncomment this line
#exit()            #if you want to deregister this device, uncomment this line

delay_times = []

while True:
    try:
        start = process_time()
        IDF_data = random.uniform(1, 10)
        DAN.push ('Dummy_Sensor', IDF_data) #Push data to an input device feature "Dummy_Sensor"

        #==================================

        ODF_data = DAN.pull('Dummy_Control')#Pull data from an output device feature "Dummy_Control"
        # if ODF_data != None:
        #     print (ODF_data[0])
        end = process_time()
        if len(delay_times) < 101 and ODF_data != None:
            print('Delay time: ', end - start)
            delay_times.append(end - start)
        if len(delay_times) == 100:
            print('Mean:                     ', statistics.mean(delay_times))
            print('Coefficient of Variation: ', statistics.stdev(delay_times) / statistics.mean(delay_times))
        
    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerURL, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            time.sleep(1)    

    time.sleep(0.2)

