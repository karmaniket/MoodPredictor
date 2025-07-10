<h1 align="center">Mood Predictor</h1>

**Mood Predictor** is a Flask-based web application that allows users to input text and get a prediction of their mood. The app uses a machine learning model trained on a dataset of text and corresponding mood labels. It is designed to be simple, responsive, and easy to deploy on platforms like Render.

## Demo

You can try the app [here](https://moodpredictor-86ek.onrender.com/).

## Features

- Predicts mood based on user input
- Uses a machine learning model trained with scikit-learn
- Easy to deploy on Render
- Supports adding more data for larger scale training
- Responsive user-friendly interface for mobile and desktop

## Project Structure

```bash
.
├── notebooks                       # Jupyter notebooks for data exploration and model training
│   ├── dataframe.ipynb
│   ├── model_trainer.ipynb
│   └── mood_dataset.csv            # dataset for training the model
├── app
│   ├── __init__.py                 # Flask app initialization
│   ├── model.pkl                   # Trained ml model
│   ├── vectorizer.pkl              # Vectorizer for text preprocessing
│   ├── server.py                   # Flask server
│   └── Procfile                    # deployment configuration
├── static                          # scripts and styles
│   ├── scripts.js  
│   └── styles.css
├── templates                       # HTML for rendering the web page
│   └── index.html
├── render.py                       # Entry point for the Flask app
├── requirements.txt                # Python dependencies
```

## Setup

### 1. Clone the repository

```bash
    git clone https://github.com/karmaniket/MoodPredictor.git
    cd MoodPredictor
```

### 2. Create and activate virtual environment

```bash
    python -m venv .venv
    .venv\Scripts\activate.bat   #on Windows
    source .venv/bin/activate    #on Mac
```

### 3. Install dependencies

```bash
    pip install -r requirements.txt
```

### 4. Run locally

```bash
    python render.py
```

## Deploy on Render

- Push your code to a GitHub repository
- Create a new web service on Render
- Connect your repository

- Build Command:

```bash
      pip install -r requirements.txt
```

- Start Command:

```bash
      gunicorn render:app
```

- Set the Runtime:

```bash
      Python 3
```

## License

This project is licensed under the MIT License. Feel free to use, modify and distribute with attribution.
