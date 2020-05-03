from flask import Flask, render_template
from data import *

app = Flask(__name__)


@app.template_filter('beautiful_price')
def beautiful_price(price):
    return str(f'{price:,}').replace(',', ' ')


@app.route('/')
def render_index():
    return render_template('index.html',
                           tours=tours,
                           title=title,
                           subtitle=subtitle,
                           description=description,
                           departures=departures)


@app.route('/departures/<departure>/')
def render_departure(departure):
    return render_template('departure.html',
                           tours=[i for i in tours if i['departure'] == departure],
                           departures=departures,
                           title=title,
                           dep_city=departures[departure][3:],
                           price_tours=[i['price'] for i in tours if i['departure'] == departure],
                           nights_tours=[i['nights'] for i in tours if i['departure'] == departure])


@app.route('/tours/<int:id>/')
def render_tours(id):
    if [i for i in tours if i['id'] == id]:
        return render_template('tour.html',
                               tours=[i for i in tours if i['id'] == id],
                               title=title,
                               departures=departures)
    else:
        return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(404)
def render_not_found(error): return "Ничего не нашлось! Вот неудача, отправляйтесь на главную!"


@app.errorhandler(500)
def render_not_found(error): return "Все сломалось"


if __name__ == '__main__':
    app.run()
