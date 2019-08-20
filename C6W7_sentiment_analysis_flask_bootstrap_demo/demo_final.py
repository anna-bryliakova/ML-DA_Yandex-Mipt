# -*- coding: utf-8 -*- 
__author__ = 'xead'
from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, validators
from wtforms.validators import Required, Length


app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    text = TextField('Review:', validators=[Required(), Length(1, 5000)])

print "Preparing classifier"
start_time = time.time()
classifier = SentimentClassifier()
print "Classifier is ready"
print time.time() - start_time, "seconds"

@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    form = ReusableForm(request.form)
    print form.errors
    if form.validate():
        if request.method == "POST":
            text = request.form["text"]
            logfile = open("ydf_demo_logs.txt", "a", "utf-8")
        print text
        print >> logfile, "<response>"
        print >> logfile, text
        
            
        prediction_message = u'Тональность отзыва:' + classifier.get_prediction_message(text)
       
            
        
    
        print prediction_message
	print >> logfile, prediction_message
	print >> logfile, "</response>"
	logfile.close()
    
    
	
    return render_template('hello_final.html', text = text, prediction_message=prediction_message)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
