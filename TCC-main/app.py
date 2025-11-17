from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
