from django.shortcuts import render
from .apps import WebsiteConfig
from tensorflow.keras.preprocessing import sequence
from twitter_extractor import twitter_main
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Create your views here.

def login(request):
    return render(request, 'login.html', {})

def home(request):
    return render(request, 'home.html', {})

def dashboard(request):
    tweets = []
    bully_array = []
    tweets_df = twitter_main.run()
    # tweets_df = df.tail(20)
    for i in range(tweets_df.shape[0]):
        bully_array.append(prediction(tweets_df.loc[i].tweet))
        tweets.append((tweets_df.loc[i].username,tweets_df.loc[i].tweet,tweets_df.loc[i].date, bully_array[-1]))
    tweets_df['bully'] = bully_array
    pie = pie_val(tweets_df)

    return render(request, 'dashboard.html', {'tweets':tweets,'pie_bull':round(pie[0]*100/(pie[0]+pie[1]),2),'pie_nbull':round(pie[1]*100/(pie[0]+pie[1]),2)})

def prediction(sentence):
    test_sequences = WebsiteConfig.tokenizer.texts_to_sequences([sentence])
    test_sequences_matrix = sequence.pad_sequences(test_sequences, maxlen=1000)
    prediction = WebsiteConfig.model.predict(test_sequences_matrix, batch_size=None, verbose=0, steps=None)
    # response = {'Bully': str(prediction[0][0])}
    # print(response)
    # return str(prediction[0][0])
    if prediction[0][0]>0.5:
        return 'Bully'
    else:
        return 'Not Bully'

def pie_val(df):
    data = [len(df[df['bully'] == 'Bully']),len(df[df['bully'] == 'Not Bully'])]
    return data