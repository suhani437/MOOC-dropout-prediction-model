# MOOC Dropout Prediction Model

## Project Overview
This project predicts the dropout risk of students in MOOCs (Massive Open Online Courses) using Machine Learning. It implements a Random Forest Classifier and integrates it into a Flask-based web application that allows users to input student activity data, receive dropout risk predictions, and visualize insights through dashboards and charts.

The project combines Machine Learning, Data Processing, and Web Development into a single end-to-end system.

---

## Features

### 1. ML-Based Prediction
- Uses a Random Forest Classifier
- Predicts student status as At Risk or Active
- Provides a dropout probability score
- Handles non-linear patterns in student activity data

### 2. Web Interface (Flask)
- User-friendly prediction form
- Input validation with highlighting for out-of-range values
- Probability bar showing prediction confidence
- Multiple pages: Home, About, and Contact

### 3. Dashboard & Analytics
- Displays total student activity statistics
- Feature-wise averages
- Risk distribution analysis
- Interactive data visualizations using Chart.js

### 4. Data Handling
- CSV-based dataset
- Data cleaning and preprocessing using Pandas
- Derived features include:
  - Total Activity
  - Early Events, Mid Events, Late Events
  - Active Days
  - Activity Duration

---

## Technology Stack

Backend:
- Python
- Flask
- Pandas
- Pickle (model serialization)

Frontend:
- HTML
- CSS
- Bootstrap
- JavaScript
- Chart.js
- Jinja2 Templating

Machine Learning:
- Random Forest Classifier
- Scikit-learn

---

## Project Structure

MOOC-Prediction/
│
├── app.py               Flask application backend  
├── pbl.py               Model training script  
├── predict_risk.py      Prediction logic  
├── mooc.csv             Dataset  
├── templates/           HTML templates  
│   ├── index.html  
│   ├── predict.html  
│   ├── dashboard.html  
│   ├── about.html  
│   └── contact.html  

---

## How It Works
1. User enters student activity data through the web interface  
2. Input data is validated  
3. Flask API sends the data to the trained ML model  
4. Random Forest model predicts dropout risk and probability  
5. Web UI displays:
   - Risk classification
   - Probability bar
   - Charts and dashboard insights

---

## Installation
Install required dependencies:
pip install flask pandas scikit-learn pickle-mixin

Run the application:
python app.py

---

## Output
- Dropout risk classification (At Risk / Active)
- Probability score
- Interactive dashboard and visual analytics

---

## Conclusion
This project demonstrates the practical application of Machine Learning in education analytics, showcasing skills in data preprocessing, model development, API integration, and full-stack web development.
