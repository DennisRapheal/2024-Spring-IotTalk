from flask import Flask, request, abort
from flask import render_template
from flask import make_response

import csmapi
csmapi.ENDPOINT = 'https://1.iottalk.tw'
app = Flask(__name__)

@app.route('/RC/<device_id>', methods=['GET'])
def switch_generator(device_id):
    def register_remote_control(device_id):
        profile = {
            'd_name': device_id,
            'dm_name': 'Remote_control',
            'u_name': 'yb',
            'is_sim': False,
            'df_list': [],
        }
        for i in range(1,26):
            profile['df_list'].append("Keypad%d"  % i)
            profile['df_list'].append("Button%d"  % i)
            profile['df_list'].append("Switch%d"  % i)
            profile['df_list'].append("Knob%d"    % i)
            profile['df_list'].append("Color-I%d" % i)
            profile['df_list'].append("Toggle%d"  % i)
            profile['df_list'].append("Slider%d"  % i)
        try:
            result = csmapi.register(device_id, profile)
            if result: print('Remote control generator: Remote Control successfully registered.')
            return result
        except Exception as e:
            print('Remote control generator: ', e)

    profile = None
    df_dict = {"Keyp": 0, "Butt": 0, "Swit": 0, "Knob": 0, "Colo": 0, "Togg": 0, "Slid": 0}
    try:
        profile = csmapi.pull(device_id, 'profile')
        print('df_list = ', profile['df_list'])
        df_list = profile['df_list']
		
		# check if a feature is enabled
        Ctl_O = csmapi.pull(device_id, '__Ctl_O__')

        if	Ctl_O != []:
            print('Ctl_O =', Ctl_O[0][1][1]['cmd_params'][0])
            selected_DF_index = Ctl_O[0][1][1]['cmd_params'][0]
        else:
            return 'Remote control "{}" successfully registered. <br> Please bind it in the IoTtalk GUI.'.format(device_id), 200
		
        for index in range(len(df_list)):
            if selected_DF_index[index] == '1': 
				# i.e., the df is enabled/selected in the project

                print('Selected IDF:', df_list[index])
                df_name_prefix = df_list[index][:4]
                df_dict[df_name_prefix] += 1
			
    except Exception as e:
        print('Remote control generator: ', e)
        if str(e).find('mac_addr not found:') != -1:
            print('Remote control generator: Register Remote Control...')
            result = register_remote_control(device_id)
            return 'Remote control "{}" successfully registered. <br> Please bind it in the IoTtalk GUI.'.format(device_id), 200
        else:
            print('Error: ()'.format(e))
            abort(404)
		  
    return make_response(render_template('index.html', device_id=device_id, df_dict=df_dict))	

if __name__ == '__main__':
    app.run('0.0.0.0', port=32767, threaded=True, use_reloader=False)