import os
from flask import Flask, session

app = Flask(__name__)

# app.config['SECRET_KEY'] = os.urandom(24)
app.config['SECRET_KEY'] = 'qwertyuiopasdfghjklzxcvb'
@app.route('/')
def helloWorld():
    # 使用session需要设置secret key
    session['username'] = 'chenduxiu'
    session['password'] ='123456'
    return '添加session成功'

@app.route('/getSession')
def getSession():
    # return session['username']
    return session.get('password')
@app.route('/deleteSession')
def deletSession():
    session.pop('username')
    return '删除成功'

@app.route("/clear")
def clear():
    session.clear()
    return 'clear success'

if __name__ == '__main__':
    app.run(debug=True)