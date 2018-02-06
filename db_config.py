
#dialect_driver://username:password@host:port/databese：

#dialect是数据库的实现，比如mysql、postgreSQL,SQLite,并且转换成小写。driver是python对应的驱动，如果不指定，会选择
#默认的驱动，比如mysql的默认驱动是：mysqldb。username是链接数据库的用户名，password是密码，host是链接数据库的域名。port是数据库
#的端口号，database是链接的数据库的库的名字


#dialect_driver://username:password@host:port/databese：
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'db_demo1'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,
                          DRIVER,USERNAME,PASSWORD,HOST,PORT,DATABASE)