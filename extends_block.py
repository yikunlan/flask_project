#继承事例使用的python
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('extends_index.html')

@app.route('/login')
def login():
    return render_template('extends_login.html')

if __name__ == '__main__':
    app.run(debug=True)
