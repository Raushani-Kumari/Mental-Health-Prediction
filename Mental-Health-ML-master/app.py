from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('stacking_model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    print(final)
    prediction=model.predict_proba(final)
    output='{0:.{1}f}'.format(prediction[0][1], 2)

    if output>str(0.5):
        return render_template('index.html',pred='Probability of taking treatment is  {} .\n The probability seems higher but please do not stress. There is nothing that cannot be done. You can either opt for focusing on your health by doing some exercise or you can go for your checkup. There is nothing wrong to have an appointment for a checkup. \n Do not stress. It will be alright!!'.format(output),bhai="feel free to have a treatment")
    else:
        return render_template('index.html',pred='Probability of taking treatment is {}.\nThe probability result seems good and you have a good mental health state. And, Yes please do not forget to maintain it.\n Have a good day!! '.format(output),bhai="good mental state")


if __name__ == '__main__':
    app.run(debug=True)