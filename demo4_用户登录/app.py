import datetime

from flask import Flask,render_template,request,redirect,url_for,session
import functools

app = Flask(__name__)
app.secret_key = 'aaaa'
app.permanent_session_lifetime = datetime.timedelta(seconds=10)
# 定义一个字典
DATA_DICT = {
    1: {'name': '小明','age': 71},
    2: {'name': '小红','age': 84},
    3: {'name': '小明', 'age': 71},
    4: {'name': '小红', 'age': 84},
    5: {'name': '小明', 'age': 71},
    6: {'name': '小红', 'age': 84},
}
# image_path_list = ["./static/1.jpg","./static/2.jpg","./static/3.jpg"]
# methods ==可接受请求方式
# 登录路由

# 装饰器判断是否登录
def auth(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        user_name = session.get('xxx')
        if not user_name:
            return redirect(url_for('login'))
        return func(*args,**kwargs)
    return inner



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    #request.form.get从前端拿数据
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == '123' and pwd == '123':
        session['xxx'] = '456'
        return redirect('/index')
    errno = '用户名或密码错误'
    #输入错误时errno前端返回数据
    return render_template('login.html',errno=errno)

# 主页路由 修改小名endpoint
@app.route('/index',endpoint='idx')
@auth
def index():
    data_dict = DATA_DICT
    # 传递参数
    return render_template('index.html',data_dict=data_dict)


# 修改路由
@app.route('/edit',methods=['GET','POST'])
@auth
def edit():
    # 通过前端获取nid为int类型
    nid = request.args.get('nid')
    nid = int(nid)
    if request.method == 'GET':
        info = DATA_DICT[nid]
        return render_template('edit.html',info=info)
    user = request.form.get('user')
    age = request.form.get('age')
    DATA_DICT[nid]['name'] = user
    DATA_DICT[nid]['age'] = age
    print(user, age)
    return redirect(url_for('idx'))

# 删除路由
@app.route('/delete/<int:nid>')
@auth
def delete(nid):
    del DATA_DICT[nid]
    return redirect(url_for('idx'))


if __name__ == '__main__':
    app.run()