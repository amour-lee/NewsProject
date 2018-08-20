from redis import StrictRedis
import logging

# 准备配置类
class Config(object):
    """app配置类"""
    # DEBUG = True

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

class DevelopmentConfig(Config):
    """开发环境配置类
        如果开发环境的配置和父类一致，可以直接pass
        """
    DEBUG = True

    # 开发环境的日志等级为调试模式
    LOGGING_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    """生产环境配置类
        实际开发中，需要额外配置生产环境下的数据库和其他的信息
        """
    DEBUG = False

    # 生产环境的日志等级为调试模式
    LOGGING_LEVEL = logging.WARNING

# 工厂方法需要的原材料
configs = {
    'dev':DevelopmentConfig,
    'prod':ProductionConfig
}