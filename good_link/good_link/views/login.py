from flask import Flask, render_template, request, session,redirect,url_for
from flask import Blueprint
from ..sql_help import db
# 登录路由
Sign_in = Blueprint('wy',__name__)

@Sign_in.route('/login',methods=["GET","POST"],endpoint='lo')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if username != '' or password != '' or username != '' and password != '':
        if len(username) < 16 and len(password) < 16:
                user = db.fetchone('select * from user where username = %s', username)
                if user == None:
                    oser = '账号未注册请注册后再次尝试登录'
                    return render_template('register.html', oser=oser)
                elif user != None:
                    if username == user[0] and password == user[1]:
                        session["aaaaa"] = "aaaaa"
                        return redirect('/ajk')
                    else:
                        oser = '密码错误请出重新输入'
                        return render_template('login.html', oser=oser)
        else:
            oser = '账号不存在！！！'
            return render_template('login.html',oser=oser)
    else:
        oser = '"未知错误"'
        return render_template('login.html',oser=oser)