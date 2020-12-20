from flask import Flask, request
import random
app = Flask(__name__)


@app.route('/')
def index():
    return "hello world"

@app.route('/json/object')
def get_json_object():
    response={"id":1}
    return response

@app.route('/json/list')
def get_json_list():
    list =[]
    for i in range(100):
        list.append(i)
    random.shuffle(list)
    response={"list":list}
    return response

@app.route('/sensor/data/list')
def get_sensor_data_list():
    data1 = {"device_id": "LED01", "data": "on", "datetime": "20190731 00:12:47"}
    data2 = {"device_id": "LED02", "data": "off", "datetime": "20190731 00:58:01"}
    list = [data1, data2]
    response = {"data_list": list}
    return response

if __name__ == '__main__':
    app.run(debug=True)