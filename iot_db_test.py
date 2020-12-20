from flask import Flask, jsonify, request
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'iot'
mysql = MySQL()
mysql.init_app(app)

@app.route('/sensor', methods=['POST'])
def save_sensor_value():
    cursor = mysql.get_db().cursor()
    sql = "insert into sensor_data (type, value) values (%s, %s)"
    body = request.json
    type = body['type']
    value = body['value']
    val = (type, value)
    print(sql%val)

    cursor.execute(sql, val)
    mysql.get_db().commit()
    return {"result": "OK"}

@app.route('/sensors', methods=['GET'])
def get_sensor_values():
    get_db = mysql.get_db()
    cursor = get_db.cursor()
    #sql = "select * from sensor_data"
    sql = "select datetime, value from sensor_data where type = 'temp' order by datetime asc"
    print("sql = ",sql)
    cursor.execute(sql)
    row_headers = [x[0] for x in cursor.description]
    print("row_headers = ",row_headers)
    results = cursor.fetchall() #전부다 가져옴
    print("results = ",results)
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)

@app.route('/sensor', methods=['GET'])
def get_sensor_value():
    get_db = mysql.get_db()
    cursor = get_db.cursor()
    sql = "select * from sensor_data where id = %s"
    args = request.args
    val = args.get('id')
    print(sql % val)
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    print(row_headers)
    result = cursor.fetchone() #하나만 가져옴
    print(result)
    json_data = dict(zip(row_headers, result))
    return jsonify(json_data)

@app.route('/sensor', methods=['DELETE'])
def delete_sensor_value():
    get_db = mysql.get_db()
    cursor = get_db.cursor()
    sql = "delete from sensor_data where id = %s"
    args = request.args
    val = args.get('id')
    print(sql % val)
    cursor.execute(sql, val)
    get_db.commit()
    return {"result": "OK"}

@app.route('/sensor', methods=['PUT'])
def update_sensor_value():
    get_db = mysql.get_db()
    cursor = get_db.cursor()
    sql = "update sensor_data set value = %s where id = %s"
    body = request.json
    id = body['id']
    value = body['value']
    val = (value, id)
    print(sql % val)
    cursor.execute(sql, val)
    get_db.commit()
    return {"result": "OK"}


@app.route('/sensors/type/<sensor_type>', methods=['GET'])
def get_sensor_values_by_type(sensor_type):
    get_db = mysql.get_db()
    cursor = get_db.cursor()
    sql = "select datetime, value from sensor_data where type = %s order by datetime desc"
    val = sensor_type
    print(sql % val)
    cursor.execute(sql, val)
    row_headers = [x[0] for x in cursor.description]
    print(row_headers)
    results = cursor.fetchall() #전부다 가져옴
    print(results)
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True)