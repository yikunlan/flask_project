from flask_script import Manager

from flask_script_demo import app

from db_script import DBManger

manager = Manager(app)

@manager.command
def runserver():
    print("服务器跑起来了")

manager.add_command('db',DBManger)

if __name__ == '__main__':
    manager.run()