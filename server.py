from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key="random"

@app.route('/')
def index():
    session['randNum'] = random.randint(1,100)
    print(session['randNum'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    try:
        session['guess'] = int(request.form['guess'])
        print(session['guess'])
        return redirect('/guessed')
    except:
        return redirect('/guessed')

@app.route('/guessed')
def guessed():
    response = 0
    if session['guess'] == session['randNum']:
        response = 0
        session.pop('guess')
    elif session['guess'] > session['randNum']:
        response = 1
    elif session['guess'] < session['randNum']:
        response = 2
    return render_template('index.html', response = response, randNum = session['randNum'])



if __name__ == '__main__':
    app.run(debug=True)