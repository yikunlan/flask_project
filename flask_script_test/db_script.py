from flask_script import Manager

DBManger = Manager()

@DBManger.command
def init():
    print("数据库初始化完成")

@DBManger.command
def migrate():
    print("数据库迁移完成")