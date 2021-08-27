import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods = ['POST', 'GET'])
def predict():
    input = float(request.form.get('getLevels'))
    
    model=pickle.load(open('clf1.pkl','rb'))

    if input > 1800 or input <0 :
        return render_template('index.html', pred = "Unrealistic value of tree cover loss")

    input = input * (10**6)

    tcl = model.predict([[input]])

    tcl = tcl / (10**3)

    return render_template('index.html', pred = format(tcl[0], '.2f') + ' Thousand hectare of Tree Cover loss')

if __name__ == '__main__':
    app.run(debug = True)