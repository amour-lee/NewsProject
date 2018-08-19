from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import Config

app = Flask(__name__)

# 加载app的配置
app.config.from_object(Config)

# 配置MySQL
db = SQLAlchemy(app)

# 配置redis
redis_store = StrictRedis(host = Config.REDIS_HOST,port = Config.REDIS_PORT)

# 配置和开启CSRF保护
# 什么情况下才代表保护成功:如果用户发送 POST，DELETE, PUT, ...时，没有携带csrf_token或者错误，服务器返回状态码400/403
CSRFProtect(app)

# 配置Session:将flask中session的数据引导到redis
Session(app)

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