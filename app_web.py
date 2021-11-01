#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 07:07:36 2021

@author: pierrelouis
"""


import xgboost as xgb
from scipy.sparse import hstack
import joblib
vectorizer_keyword=joblib.load('pickle_files/vectorizer_keyword.pkl')
vectorizer_location=joblib.load('pickle_files/vectorizer_location.pkl')
tfidf_vectorizer=joblib.load('pickle_files/tfidf_vectorizer.pkl')
clf=joblib.load('pickle_files/logistic_regression.pkl')
#bst=joblib.load('pickle_files/model_xgb_boost.pkl')

#bst = xgb.Booster()
#bst.load_model("pickle_files/model_xgb_boost.json")


from flask import Flask,render_template,request,url_for
app = Flask(__name__)


#
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def form_input():
    return render_template('index.html')

@app.route('/predict',methods=['post'])
def predict():
    location=request.form['location']
    keyword=request.form['keyword']
    message=request.form['message']

    location_transform=vectorizer_location.transform([location])
    keyword_transform=vectorizer_keyword.transform([keyword])
    message_transform=tfidf_vectorizer.transform([message])

    X_query=hstack([location_transform,keyword_transform,message_transform])
    pred=clf.predict(X_query)
    #X_query = xgb.DMatrix(X_query)
    #pred=bst.predict(X_query)
    if(pred>0.5):
        return 'It is a Disaster tweet'
    else:
        return 'The tweet is not related to diaster category'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)