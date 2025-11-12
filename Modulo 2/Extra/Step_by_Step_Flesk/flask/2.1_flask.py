# EX 2.1
#
#
#
#

from flask import Flask, render_template
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template('ex_2-1.html')

@app.route('/sobre')
def sobre():
    return "Fabrica de Programadores"

@app.route('/Oruam')  
def Oruam():
    return 'Achou a Rota Pae'

if __name__ == '__main__':
    app.run(debug=True)