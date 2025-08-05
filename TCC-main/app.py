from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/dados')
def dados():
    return render_template('dados.html')

if __name__ == '__main__':
    app.run(debug=True)
