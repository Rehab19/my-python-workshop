from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world from Rehab'
print(' the name of this app ....: ', __name__)


if __name__=='__main__':
    #app.run('localhost',port=5000, debug=True)
    #app.run(debug=True)    
    app.run('0.0.0.0', port=80) 