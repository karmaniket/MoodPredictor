import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import joblib
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.pkl')
vectorizer_path = os.path.join(current_dir, 'vectorizer.pkl')

model = joblib.load(model_path)
vectorizer = joblib.load(vectorizer_path)

def predict_mood():
    text = entry.get()
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)
    mood_label.config(text=f'Mood: {prediction[0]}')

root = tk.Tk()
root.title('Mood Predictor')
label = Label(root, text='Enter text:')
label.pack(pady=10)
entry = Entry(root, width=50)
entry.pack(pady=10)
predict_button = Button(root, text='Predict Mood', command=predict_mood)
predict_button.pack(pady=10)
mood_label = Label(root, text='')
mood_label.pack(pady=10)

root.mainloop()
