from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
   # args = request.args
   # id = args.get('id')
   # date = args.get('date')
   # print("id:", id)
   # print("date: ", date)
    return "Query String"

@app.route('/body', methods=['POST'])
def request_body():
    print(request.json)
    body= request.json
    id=body['id']
    first=body['name']['first']
    last =body['name']['last']

    print(id)
    print(first, last)
    #print(request.json)
    return "request body"

#@app.route('/body', method=['POST'])
    #print(request.json)

#def request_body():
    #body= request.json
    #id=body['id']
    #name=body['name']

    ##print(id)
    #print(name)
    #return "request body"




if __name__ == '__main__':
    app.run(debug=True)
