# Rick Mur - Maverick Solutions - (c) 2016
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/generate', methods=['POST'])
def generate():
    fname = request.form['name']
    frole = request.form['role']
    femail = request.form['email']
    fphone = request.form['phone']
    ffont = "Calibri, Arial"
    try:
        if request.form['macbook'] == 'on':
            ffont = 'Arial'
    except:
        pass
    ffiphone = False
    try:
        if request.form['iphone'] == 'on':
            ffiphone = True
    except:
        pass

    return render_template('generate.html', name = fname, role = frole, email = femail,
                            phone = fphone, font = ffont, iphone = ffiphone)

if __name__ == '__main__':
    try:
        app.run()
    except Exception as e:
        print e
