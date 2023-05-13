from flask import Flask, render_template

app = Flask(__name__)

class User:
    def __int__(self,username,email):
        self.username = username
        self.email = email


@app.route('/')
def heelo():
     user = User(username='知了',email='964960973@qq.com')
     person = {
         'username':'zhangsan',
         'emael':'0636'
     }
     return render_template('index.html',user=user)

@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    # 传递参数
    return render_template('blog_id.html',blog_id=blog_id,user_name='关忆北')

if __name__ == '__main__':
    app.run(debug=True)