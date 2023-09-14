from flask import Flask

app=Flask(__name__)

@app.route('/hello')
def helloIndex():
    return 'hello world'

app.run(host='0.0.0.0',port=9001)
