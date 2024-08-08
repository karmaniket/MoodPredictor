import streamlit as st
import joblib
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')
vectorizer_path = os.path.join(current_dir, 'vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

st.markdown("""
    <style>
            
    .result {
        font-size: 20px;
        color: #ccc;
        position : absolute;
        top: -52px;
        left: 580px;
    }
            .footer{
            position : absolute;
            top: 250px;
            left: 190px;
            color : white;
            }

            .footer a{
            color : white;
            }

            @media only screen and (max-width: 620px) {
        .result {
            left: 160px;
        }   
            
            .footer{
            top: 432px;
            left: 0;
            font-size: 15px;
            text-align : center;
            }
}
    </style>
    """, unsafe_allow_html=True)

st.title('Mood Predictor')

text = st.text_input('', key='text-input', placeholder='Type your text here...')

if st.button('Predict Mood'):
    if text:
        text_vec = vectorizer.transform([text])
        prediction = model.predict(text_vec)
        st.markdown(f'<div class="result">Mood: {prediction[0]}</div>', unsafe_allow_html=True)
    else:
        st.write('Please enter some text to predict the mood.')

st.markdown("""
    <div class="footer">
        Copyright © 2024 <a href="https://karmaniket.pages.dev/" target="_blank">karmaniket</a>. All rights reserved.
    </div>
    """, unsafe_allow_html=True)
