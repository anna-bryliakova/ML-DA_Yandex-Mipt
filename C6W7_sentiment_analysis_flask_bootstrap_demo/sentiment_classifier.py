# -*- coding: utf-8 -*- 
__author__ = 'xead'
from sklearn.externals import joblib


class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("./LogisticRegression_mini.pkl")
        self.vectorizer = joblib.load("./BigramTfidfVectorizer_mini.pkl")
        self.classes_dict = {0: u"отрицательная", 1: u"положительная", -1: u"ошибка предсказания"}

    @staticmethod
    def get_probability_words(probability):
        if probability < 0.55:
            return u"нейтральная/возможно,"
        if probability < 0.7:
            return u"вероятно,"
        if probability > 0.95:
            return u"определенно"
        else:
            return ""

    def predict_text(self, text):
        

            
        try:
            vectorized = self.vectorizer.transform([text])
            return self.model.predict(vectorized)[0],\
                   self.model.predict_proba(vectorized)[0].max()
        except:
            print u"ошибка предсказания"
            return -1, 0.8
       

   

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        class_prediction = prediction[0]
        prediction_probability = prediction[1]
       

        return self.get_probability_words(prediction_probability) + " " + self.classes_dict[class_prediction]
    
