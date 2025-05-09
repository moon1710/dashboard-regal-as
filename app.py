from flask import Flask, render_template
from collections import namedtuple

app = Flask(__name__)

# Aquí defines el filtro, antes de levantar el servidor
@app.template_filter('number_format')
def number_format(value):
    return f"{value:,}"

# Resto de tus rutas…
Regalia = namedtuple('Regalia', ['total', 'count'])

@app.route('/')
def dashboard():
    regalias = {
        'soundrecording': Regalia(total=1000, count=2),
        'publishing'    : Regalia(total=132, count=28),
        'mlc'           : Regalia(total=343434, count=1),
        'sayco'         : Regalia(total=3434, count=1),
        'sacam'         : Regalia(total=9000, count=5)
    }
    return render_template('dashboard.html', regalias=regalias)

if __name__ == '__main__':
    app.run(debug=True)
