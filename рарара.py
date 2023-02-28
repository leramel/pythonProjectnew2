from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса, <a href=http://127.0.0.1:8080/index>index</a>"

@app.route('/index')
def index2():
    return 'И на Марсе будут яблони цвести!, <a href=http://127.0.0.1:8080/promotion>promotion</a>'

@app.route('/promotion')
def promotion():
    data = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.', 'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return f'''{'</br>'.join(data)}, <a href=http://127.0.0.1:8080/image_mars>image_mars</a>'''

@app.route('/image_mars')
def image_mars():
    return f'''<h1>Жди нас, Марс!<h1></br><img width=700pt src="{url_for('static', filename='img/ri.jpg')}" 
               alt="здесь должна была быть картинка, но не нашлась"><title>Привет, Марс!</title>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
