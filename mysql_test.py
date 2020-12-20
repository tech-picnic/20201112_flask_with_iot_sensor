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


@app.route('/customers')
def get_customers():
    cursor = mysql.get_db().cursor()
    cursor.execute("select * from customers")
    row_headers = [x[0] for x in cursor.description]
    print(row_headers)
    results = cursor.fetchall()
    print(results)
    json_data = []
    for result in results:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)

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
    get_db = mysql.get_db() cursor = get_db.cursor()
sql = "select * from sensor_data" print(sql)
cursor.execute(sql)
row_headers = [x[0] for x in cursor.description] print(row_headers)
results = cursor.fetchall() print(results)
json_data = [] for result in results: json_data.append(dict(zip(row_headers, result)))
return jsonify(json_data)


if __name__ == '__main__':
    app.run(debug=True)