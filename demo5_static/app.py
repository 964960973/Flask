from flask import Flask,render_template

app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/static')

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()