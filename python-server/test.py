import json
from flask import Flask
from flask_cors import *
from cisco import devices_data
from cisco import host_data

app = Flask(__name__)
CORS(app, supports_credentials=True)  # 设置跨域

# GET, 根据用户ID查询特定用户

@app.route('/devices', methods=['GET'])
def get_devices():
    return json.dumps(devices_data)
# # 也可以自定义其他的方法


@app.route('/host', methods=['GET'])
def get_host():
    return json.dumps(host_data)
# # 也可以自定义其他的方法

# 设定监听端口为3000
if __name__ == '__main__':
    app.run(host='localhost', port=3000)
