from flask import Flask,send_from_directory
app = Flask(__name__)
app.secret_key = 'test'

@app.route('/')
def home():
   return "Proxy is up!"

@app.route('/proxy/', methods=['GET'])
def result():
    return send_from_directory('','proxy.json')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000,use_reloader=True)
