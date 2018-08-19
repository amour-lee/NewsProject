from flask import Flask
from flask_script import Manager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis

app = Flask(__name__)

# 准备配置类
class Config(object):
    """app配置类"""
    DEBUG = True

    # 配置MySQL:指定数据库位置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@mysql@127.0.0.1:3306/information_new'
    # 禁用追踪mysql:因为mysql的性能差，如果再去追踪mysql的所有的修改，会再次浪费性能
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # 准备秘钥
    SECRET_KEY = 'ajkhdflhslfjlfh'

    # 配置Session:将flask的session数据引导到redis
    SESSION_TYPE = 'redis'  # 存储到redis
    # 配置redis的位置
    SESSION_REDIS=StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    # 使用签名将session的明文转成密文
    SESSION_USE_SIGNER = True
    # 设置session有效期：一天，以秒为单位
    PERMANENT_SESSION_LIFETIME = 60*60*24


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

@app.route('/')
def index():
    return 'index'

# 准备程序的启动入口
if __name__ == '__main__':
    # app.run()

    # 启动程序
    manager.run()