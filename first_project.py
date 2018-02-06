from flask import Flask, url_for, redirect, render_template
import flask_config
#初始化一个Flask对象
app = Flask(__name__)
app.config.from_object(flask_config)
#是一个装饰器
#@开口，并且在函数上面。说明都是装饰器
#作用是作一个URL与视图函数的映射，简单来说就是方法名
@app.route('/hello_world')
def hello_world():

    #重定向
    article_url = url_for('article',id='dfdfd')
    return redirect(article_url)
    return '我靠，真的起来了啊'
#article为浏览器上面请求的方法,id 为参数
@app.route('/article/<id>')
def article(id):
    return '传入的参数为：%s' %id

@app.route('/index')
def index():
    context = {'username':'黄艺坤',
               'age':100,
               'gender':'男'}
    #注意：在context前面需要添加；**，两个星号
    return render_template('index.html',**context)

@app.route('/index2')
def index2():
    class person(object):
        name = '张三'
        age = 10;
    p = person()
    context = {'username':'黄艺坤',
               'age':100,
               'gender':'男',
               'person':p}
    #注意：在context前面需要添加；**，两个星号
    return render_template('index.html',**context)


@app.route('/login')
def login():
    return '登录界面'
@app.route('/question/<is_login>')
def question(is_login):
    if is_login == '1':
        return '发布问答界面'
    else:
        return redirect(url_for('login'))

#如果当前这个文件是作为主程序运行，那么久执行app.run*)方法
if __name__ == '__main__':
    #启动一个应用服务器来接受用户的请求
    #app.run()
    #开启debug模式，当开启debug模式的时候，1、有任何‘python’的修改文件的操作都会重新启动服务器
    #2、在页面上面可以打印出错误的信息
    app.run(debug=True)
