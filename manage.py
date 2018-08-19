from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from info import create_app,db


# 调用工厂方法，创建app
app = create_app('dev')

# 创建脚本管理器对象
manager = Manager(app)

# 迁移时让app和db建立关联
Migrate(app,db)
# 把迁移脚本命令添加到脚本管理器
# 参数1：别名,参数2：迁移命令
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    return 'index'

# 准备程序的启动入口
if __name__ == '__main__':
    # app.run()

    # 启动程序
    manager.run()