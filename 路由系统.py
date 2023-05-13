from flask import Flask, request,render_template


app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

#另外一种路由系统
# app.add_url_rule('/index','index',index)


'''路由加载流程
    将url和函数打包成rule对象
    将url对象添加到map对象中
    app.url_map = map
'''


'''动态路由
    @app.route('/login/<name>')
    @app.route('/login/<int:name>')
'''

@app.route('/login')
def index():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()