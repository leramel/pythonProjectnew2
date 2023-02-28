from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return f'''<h1>Жди нас, Марс!<h1></br><img width=700pt src="{url_for('static', filename='img/ri.jpeg')}" 
               alt="здесь должна была быть картинка, но не нашлась"><title>Привет, Марс!</title>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
