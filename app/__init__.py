# coding=utf-8

from flask import Flask
from config import config
# app = Flask(__name__)
# #: 配置项目域名, 作为Flask的ServerName
# # app.config['SERVER_NAME'] = 'xyz.com'
# # #: 指定该域名中默认的子域名
# # app.url_map.default_subdomain = 'www'
#
#
# from app.main import main_app
#
# #: 注册蓝图(BluePrint)
# app.register_blueprint(main_app)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .sub import sub as sub_blueprint
    app.register_blueprint(sub_blueprint)

    return app