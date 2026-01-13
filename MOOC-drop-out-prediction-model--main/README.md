# MOOC-drop-out-prediction-model-
Project Overview

This project predicts the dropout risk of students in MOOC (Massive Open Online Courses) using Machine Learning (Random Forest Classifier).
A complete Flask-based web application is built that allows users to:

Enter student activity data

Predict dropout probability

visualize the data in charts

View dashboard summaries

This project combines Machine Learning + Data Processing + Web Development into one integrated system.

🧠 Features
🔍 1. ML-Based Prediction

Random Forest Model

Predicts At Risk or Active

Provides probability score

Handles non-linear data patterns

🖥️ 2. Web Interface (Flask)

User-friendly prediction form

Input validation (highlight out-of-range values)

Probability bar

Home, About, Contact pages

📊 3. Dashboard & Analytics

Total activity statistics

Feature averages

Risk distribution

Chart.js visualizations

📁 4. Data Handling

CSV Dataset 

Cleaned and processed using Pandas

Derived features:

Total Activity

Early + Mid + Late Events

Active Days

Activity Duration

🛠 Tech Stack
Backend

Python

Flask

Pickle (Model Saving)

Pandas

Frontend

HTML

CSS

Bootstrap

JavaScript

Chart.js

Jinja2 Templating

Machine Learning

Random Forest Classifier

Scikit-Learn

📂 Project Structure
MOOC-Prediction/
│
├── app.py                      # Flask backend
├── pbl.py                      # Model training
├── predict_risk.py             # ML prediction logic
├── mooc.csv                    # Dataset
├── templates/                  # HTML UI
│   ├── index.html
│   ├── predict.html
│   ├── dashboard.html
│   ├── about.html
│   └── contact.html
                   

🔮 How It Works

User enters student activity input

Data is validated

Flask sends data to ML model

Random Forest predicts dropout probability

Web UI displays:

Risk result

Percentage bar

Chart

📦 Installation
pip install flask pandas scikit-learn pickle-mixin


Run the project:

python app.py

