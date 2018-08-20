from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from config import configs
import logging
from logging.handlers import RotatingFileHandler


# 创建一个空的db对象
db = SQLAlchemy()

# 设置日志的记录等级
logging.basicConfig(level=logging.DEBUG)  # 调试debug级
# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
# 为刚创建的日志记录器设置日志记录格式
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象（flask app使用的）添加日志记录器
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    """创建app的工厂方法"""

    # 读取配置类
    config_class = configs[config_name]
    # 创建app实例
    app = Flask(__name__)

    # 加载app的配置
    app.config.from_object(config_class)

    # 配置MySQL
    db.init_app(app)

    # 配置redis
    redis_store = StrictRedis(host = config_class.REDIS_HOST,port = config_class.REDIS_PORT)

    # 配置和开启CSRF保护
    # 什么情况下才代表保护成功:如果用户发送 POST，DELETE, PUT, ...时，没有携带csrf_token或者错误，服务器返回状态码400/403
    CSRFProtect(app)

    # 配置Session:将flask中session的数据引导到redis
    Session(app)

    return app