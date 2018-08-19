from flask import Flask


app = Flask(__name__)

# 准备配置类
class Config(object):
    """app配置类"""
    DEBUG = True
# 加载app的配置
app.config.from_object(Config)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)
