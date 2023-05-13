from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello 中国'


@app.route('/profile')
def profile():
    return '我是个人中心'


# 携带参数/blog/<blog_id>
@app.route('/blog/<blog_id>')
def blog_id(blog_id):
    print(blog_id)
    return '你访问的博客id是%s'%blog_id


@app.route('/book/list')
def book_list():
    # 参数 类字典类型
    # 查询字符串的方式传参
    # default传递默认值
    page = request.args.get('page',default=1,type=int)
    return f'你获取的是第{page}页'

if __name__ == '__main__':
    app.run(port=5000)