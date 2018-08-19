from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import configs


def create_app(config_name):
    """创建app的工厂方法"""

    # 读取配置类
    config_class = configs[config_name]
    # 创建app实例
    app = Flask(__name__)

    # 加载app的配置
    app.config.from_object(config_class)

    # 配置MySQL
    db = SQLAlchemy(app)

    # 配置redis
    redis_store = StrictRedis(host = config_class.REDIS_HOST,port = config_class.REDIS_PORT)

    # 配置和开启CSRF保护
    # 什么情况下才代表保护成功:如果用户发送 POST，DELETE, PUT, ...时，没有携带csrf_token或者错误，服务器返回状态码400/403
    CSRFProtect(app)

    # 配置Session:将flask中session的数据引导到redis
    Session(app)

    return app