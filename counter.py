from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key= "is it safe?"

@app.route('/')
def index():
    if "count" not in session:
        session['count'] = 1
    else:
            session['count'] = session['count'] + 1
    return render_template('index.html', count= session.get('count'))
    

@app.route('/count' , methods= ['POST'])
def count():
    return redirect('/')

@app.route('/destroy')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)