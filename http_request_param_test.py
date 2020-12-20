from flask import Flask, request
app = Flask(__name__)
@app.route('/query')
def index():
    args = request.args
    id= args.get('id')
    date=args.get('date')
    print("id:",id)
    print("date: ", date)
    return "Query String"



if __name__ == '__main__':
    app.run(debug=True)
    