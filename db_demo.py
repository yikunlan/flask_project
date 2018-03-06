from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import db_config

app = Flask(__name__)
db = SQLAlchemy(app)
#把数据库的配置添加进来
app.config.from_object(db_config)

class Article(db.Model):
    __tablename__='mode_article'
    id = db.Column(db.Integer,primary_key=True,autoincrement = True)
    title = db.Column(db.String(500),nullable = False)
    content = db.Column(db.Text,nullable = False)

db.create_all()

@app.route('/')
def index():
    
    #增
    article = Article(title='第一条数据',content='插入第一条数据')
    db.session.add(article)
    db.session.commit()#事物提交
    # 查
    #article = Article.query.filter(Article.title=='第一条数据').first()
    #print(article.content)
    # 改
    #article = Article.query.filter(Article.title == '第一条数据').first()
    #article.title = '标题1'
    #db.session.commit()
    #删
    #article = Article.query.filter(Article.title == '标题1').first()
    #db.session.delete(article)
    #db.session.commit()
    
    
    return 'index'

if __name__ == '__main__':
    app.run(debug=True)