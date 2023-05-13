from flask import Flask, render_template, request, session
from flask import Blueprint
from ..sql_help import db
import re
# 注册路由
Register = Blueprint('register',__name__)

# 注册路由
@Register.route('/register',methods=["GET","POST"])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        new_password = request.form.get('new_password')
        phone = request.form.get('phone')
        if username != '' and password != '' and new_password != '' and phone != '':
            if new_password != password:
                prompt = '两次输入密码不一致'
                return render_template('register.html',prompt=prompt)
            else:
                pattern = re.compile(r'^(13[0-9]|14[0|5|6|7|9]|15[0|1|2|3|5|6|7|8|9]|'
                                     r'16[2|5|6|7]|17[0|1|2|3|5|6|7|8]|18[0-9]|'
                                     r'19[1|3|5|6|7|8|9])\d{8}$')
                if pattern.search(phone):
                    if db.fetchone('select * from user where username = %s', username) == None:
                        db.insert_one( f'insert into user(username,password,phone) values({username},{password},{phone});')
                        return render_template('login.html')
                    else:
                        prompt = '该账号已被注册尝试找回密码'
                        return render_template('register.html', prompt=prompt)
                else:
                    prompt = '请正确填写手机号'
                    return render_template('register.html', prompt=prompt)
        else:
            prompt = '注册失败所有字段都不能为空'
            return render_template('register.html',prompt=prompt)
    return render_template('register.html')
