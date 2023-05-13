import datetime
from flask import Flask,render_template,session,url_for,redirect
from .views.ajk import Ajk
from .views.login import Sign_in
from .views.register import Register
from .views.recruit import Recruit
from .views.wyy_music import WYY
from .views.mao_TV import MiAo

import functools
import os




def create_app():
    app = Flask(__name__)
    #随机seeion
    app.secret_key = os.urandom(16)
    # 会话保持10秒
    app.permanent_session_lifetime = datetime.timedelta(seconds=20000)
    @app.route('/')
    def index():
        return render_template('index.html')
# 注册蓝图

#   登录路由
    app.register_blueprint(Sign_in)
# 注册路由
    app.register_blueprint(Register)
# 租房信息
    app.register_blueprint(Ajk)
# 招聘信息
    app.register_blueprint(Recruit)
# 音乐信息
    app.register_blueprint(WYY)
# 电影信息
    app.register_blueprint(MiAo)
    return app


