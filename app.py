from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def captura():
    return render_template('indicador.html')

if __name__ == "__main__":
    app.run(debug = True)
