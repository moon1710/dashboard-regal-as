from flask import Flask, render_template, redirect, url_for
from collections import namedtuple

app = Flask(__name__)

# Filtro para formatear números con separador de miles
def number_format(value):
    return f"{value:,}"
app.jinja_env.filters['number_format'] = number_format

Regalia = namedtuple('Regalia', ['total', 'count'])

@app.route('/')
def dashboard():
    # Datos simulados; más tarde conecta tu BD real
    regalias = {
        'soundrecording': Regalia(total=1000, count=2),
        'publishing'    : Regalia(total=132,  count=28),
        'mlc'           : Regalia(total=343434, count=1),
        'sayco'         : Regalia(total=3434, count=1),
        'sacam'         : Regalia(total=9000, count=5)
    }
    return render_template('dashboard.html', regalias=regalias)

@app.route('/logout')
def logout():
    # tu lógica de logout
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
