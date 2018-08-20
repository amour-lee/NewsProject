from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import create_app,db
from flask import current_app


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

    # 测试日志等级
    import logging
    logging.debug('测试debug')
    logging.info('测试info')
    logging.error('测试error')
    logging.warning('测试warning')
    logging.fatal('测试fatal')

    # 注意点：默认等级DEBUG，我们配置的等级是影响logging模块的。所以最好使用logging模块输出日志
    current_app.logger.debug('测试 current_app debug')

    return 'index'

# 准备程序的启动入口
if __name__ == '__main__':
    # app.run()

    # 启动程序
    manager.run()