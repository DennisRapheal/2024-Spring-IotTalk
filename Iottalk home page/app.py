# 注意該 import 的
import os
import os.path
from os.path import exists, join, isdir
from flask import Flask, render_template, make_response, send_from_directory, send_file
WEB_DA_DIR_PATH = join(os.path.dirname(__file__), 'da/')   # 注意這句跟你檔案放置位置有關

app = Flask(__name__)
###

from flask import send_from_directory

from flask import send_from_directory
# @app.route('/static/<file>')
# def ret_static_file(file):
#     return send_from_directory('static', file)

@app.route('/')
def show_web_da_list():
    global WEB_DA_DIR_PATH
    # 找出 da/ 目錄之下全部子目錄並做排序放 js_da_list[ ], 但須裡面有 index.html
    js_da_list = sorted(
    f
    for f in os.listdir(WEB_DA_DIR_PATH)
    if isdir(join(WEB_DA_DIR_PATH, f))
       and f not in ('vp')
       and 'index.html' in os.listdir(join(WEB_DA_DIR_PATH, f))
    )
    # 找出 /da/vp/py/ 內全部 .py 檔案名稱, 但要去掉 ".py", 放 vp_da_list[ ]
    vp_da_list = sorted(
        f.replace('.py', '')
        ## 注意下句寫法會和這 web.py 放在哪個目錄有關 !!! 
        for f in os.listdir(join(os.path.dirname(__file__), './da/vp/py'))
        if f.endswith('.py')
    )
    print("=== js_da_list -----", js_da_list)   # 印出來看看 :-)
    print("\n=== vp_da_list -----", vp_da_list, end="\n\n")
    # 用 Jinja2 render_template 對 templates 內 web_da_index.html 做排版
    #, vp_da_list=vp_da_list
    return render_template('web_da_index.html', js_da_list=js_da_list, vp_da_list=vp_da_list)

@app.route('/da/<path:path_name>')
def serve_directory(path_name):
    return send_file(f'da/{path_name}')



if __name__ == '__main__':
    app.run('0.0.0.0', port=32767, threaded=True, use_reloader=False)