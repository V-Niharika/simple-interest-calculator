from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    principal = float(request.form['principal'])
    rate = float(request.form['rate'])
    time = float(request.form['time'])
    interest = (principal * rate * time) / 100
    return render_template('result.html', interest=interest)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
