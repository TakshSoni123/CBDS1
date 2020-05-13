from django.shortcuts import render
from .apps import WebsiteConfig
from tensorflow.keras.preprocessing import sequence
from twitter_extractor import twitter_main

# Create your views here.

def login(request):
    return render(request, 'login.html', {})

def home(request):
    return render(request, 'home.html', {})

def dashboard(request):
    tweets = []
    tweets_df = twitter_main.run()
    for i in range(tweets_df.shape[0]):
        # tweets.append((tweets_df.loc[i].tweet, prediction(tweets_df.loc[i].tweet)))
        tweets.append((tweets_df.loc[i].username,tweets_df.loc[i].tweet,tweets_df.loc[i].date, prediction(tweets_df.loc[i].tweet)))

    return render(request, 'dashboard.html', {'tweets':tweets})

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