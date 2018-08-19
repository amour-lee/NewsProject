from flask import Flask
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

# 加载app的配置
app.config.from_object(Config)

# 配置MySQL
db = SQLAlchemy(app)

# 配置redis
redis_store = StrictRedis(host = Config.REDIS_HOST,port = Config.REDIS_PORT)

# 配置和开启CSRF保护
# 什么情况下才代表保护成功:如果用户发送 POST，DELETE, PUT, ...时，没有携带csrf_token或者错误，服务器返回状态码400/403
CSRFProtect(app)
@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
