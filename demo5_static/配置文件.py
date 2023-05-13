from flask import Flask,render_template

app = Flask(__name__)

# 加载配置文件
app.config.from_object('config.settings')

print(app.config['DB_GOST'])

@app.route('/index')
def index():
    return 'index'