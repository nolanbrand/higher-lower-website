from flask import Flask
import random

random_num = random.randint(0, 9)

app = Flask(__name__)


@app.route("/")
def header():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<iframe src="https://giphy.com/embed/13RcbHeXlLNysE" width="480" height="302" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/i-love-lucy-lucille-ball-13RcbHeXlLNysE">via GIPHY</a></p>'


@app.route("/<int:number>")
def check_number(number):
    if number < random_num:
        return "<h1 style= 'color: blue'>Too low, try again!</h1>"\
               '<iframe src="https://giphy.com/embed/QKTJJPsNjdwCaKQ23I" width="480" height="269" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/tacomafd-trutv-tacoma-fd-ta101-QKTJJPsNjdwCaKQ23I">via GIPHY</a></p>'
    if number > random_num:
        return "<h1 style= 'color: red'>Too high, try again!</h1>"\
               '<iframe src="https://giphy.com/embed/3orif1PeKFMluWmxkQ" width="480" height="362" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/season-7-the-simpsons-7x12-3orif1PeKFMluWmxkQ">via GIPHY</a></p>'
    if number == random_num:
        return "<h1 style= 'color: green'>You found me!</h1>"\
               '<iframe src="https://giphy.com/embed/l0HUnQR733uhm48UM" width="480" height="319" style="" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/ptm-l0HUnQR733uhm48UM">via GIPHY</a></p>'


if __name__ == "__main__":
    app.run(debug=True)
