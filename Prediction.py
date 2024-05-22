import streamlit as st
import numpy as np
import nltk
import re
import os
import pickle
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Embedding, SpatialDropout1D, LSTM, Dense
from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
from keras._tf_keras.keras.preprocessing.text import Tokenizer
from nltk.tokenize import word_tokenize

st.set_page_config(page_title='Sarcasm Detector', layout='wide')
st.header('Sarcasm Detector', divider='rainbow')

#tokenizer_path = 'tokenizer.pickle'
#if os.path.exists(tokenizer_path):
#    with open(tokenizer_path, 'rb') as handle:
#        tokenizer = pickle.load(handle)
#else:
#    st.error("Tokenizer file not found. Please check the file path.")
       
max_features = 2000
max_len = 29
model = Sequential()
model.add(Embedding(max_features, 128))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(196, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(2, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

def preprocess_input(sentence, tokenizer):
    sentence = sentence.lower()
    sentence = re.sub('[^a-zA-z0-9\s]', '', sentence)
    X = tokenizer.texts_to_sequences([sentence])
    X = pad_sequences(X, maxlen=max_len)
    return X
def predict_class(sentence, tokenizer):
    X = preprocess_input(sentence, tokenizer)
    predictions = model.predict(X)
    predicted_class = np.argmax(predictions)
    return predicted_class
def main():
    # Get user input
    sentence = st.text_area("Enter a sentence")

    if st.button("Predict"):
        # Load tokenizer
        tokenizer = Tokenizer(num_words=max_features, split=' ')
        tokenizer.fit_on_texts(sentence)

        # Make prediction
        predicted_class = predict_class(sentence, tokenizer)

        # Display prediction
        if predicted_class == 1:
            st.error("Sarcastic")
        else:
            st.success("Non-Sarcastic")
if __name__ == "__main__":
    main()