from flask import Flask,render_template,jsonify,request,redirect
from sql_help1 import db

app = Flask(__name__,template_folder='templates')

# 路由系统
#注册路由
@app.route('/logon',methods=['GET','POST'])
def logon():
    if request.method == 'GET':
        return render_template('logon.html')
    username = request.form.get('username')
    password = request.form.get('password')
    password_1 = request.form.get('password_1')
    phone = request.form.get('phone')
    if username != '' and password != '' and phone != '':
        if password == password_1:
            user = db.fetchone('select * from user where username = %s',username)
            if user == None:
                user = username
                db.insert_one(f'insert into user(username,password,phone) values({username},{password},{phone});')
                return render_template('login.html',user=user)
            elif user != None:
                user = '该账号存在是否找回密码 或重新创建'
                return render_template('logon.html', user=user)
        else:
            user = '两次密码不一致，检查后重新输入'
            return render_template('logon.html', user=user)

    elif username == '':
        user = '账号不能为空'
        return render_template('logon.html', user=user)
    elif password == '':
        user = '密码不能为空'
        return render_template('logon.html', user=user)

    elif phone == '':
        user = '请正确填写手机号'
        return render_template('logon.html', user=user)
    else:
        user = '请重试,未知错误'
        return render_template('logon.html',user = user)

# 登录路由
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username != '' and password != '':
        user = db.fetchone('select * from user where username = %s', username)
        if user == None:
            user = '该账号未注册，请注册'
            return render_template('logon.html', user=user)
        elif user != None:
            if username == user[0] and password == user[1]:
                return render_template('index.html', user=user[0])
            else:
                user = '账号或密码错误 请出重新输入'
                return render_template('login.html', user=user)
    elif username == '':
        user = '账号不能为空'
        return render_template('login.html', user=user)
    elif password == '':
        user = '密码不能为空'
        return render_template('login.html', user=user)
    else:
        user = '请重试,未知错误'
        return render_template('login.html', user=user)

#找回密码
@app.route('/retrieve',methods=['GET','POST'])
def retrieve():
    if request.method == 'GET':
        return render_template('retrieve.html')
    username = request.form.get('username')
    phone = request.form.get('phone')
    if username != '' and phone != '':
        user = db.fetchone('select * from user where username = %s', username)
        if user == None:
            password = '未找到该注册账号'
            return render_template('retrieve.html', passwoed=password)
        elif user != None:
            if username == user[0] and phone == user[2]:
                password = user[1]
                return render_template('retrieve.html', password=password)
            else:
                return render_template('retrieve.html', password='验证有误')
    else:
        return render_template('retrieve.html', password='输入有误')

#主页展示
@app.route('/')
def index():
    user = db.fetchall('select * from 爬虫') # 获取sql油标
    return render_template('index.html',user=user)

#编辑内容
@app.route('/edit',methods=["GET","POST"])
def edit():
    # 通过前端获取nid为int类型
    old_nid = request.args.get('nid')
    if request.method == 'GET':
        data = db.fetchone('select * from 爬虫 where 详情链接=%s',old_nid)
        return render_template('edit.html',info=data)
   # update table_1 set 列名 = 更改的数据 where 列名 = 原本的数据 update student set name = “李四” where id = 101; update student set name = "王五" where name = "李四";
    interlinkage = request.form.get('interlinkage')
    area = request.form.get('area')
    position = request.form.get('position')
    technology = request.form.get('technology')
    fringe_benefits = request.form.get('fringe_benefits')
    enterprise_information = request.form.get('enterprise_information')
    salary = request.form.get('salary')
    # data = db.update(f'update 爬虫 set 详情链接 = "{interlinkage}" ,所在地区 = "{area}" where 详情链接="{old_nid}"')
    data = db.update(f'update 爬虫 set 详情链接 = "{interlinkage}" ,所在地区 = "{area}" ,职位 = "{position}" ,所需技术 = "{technology}" ,福利待遇 = "{fringe_benefits}" ,企业信息 = "{enterprise_information}" ,工资其他信息 = "{salary}" where 详情链接="{old_nid}"')
    return redirect("/")

#删除路由
@app.route('/delete',methods=["GET","POST"])
def delete():
    # 通过前端获取nid为int类型
    old_nid = request.args.get('nid')
    if request.method == 'GET':
        db.delete(f'delete from 爬虫 WHERE 详情链接 = "{old_nid}"')
        return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)