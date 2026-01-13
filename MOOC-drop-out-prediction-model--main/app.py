from flask import Flask, render_template, request
import pickle, pandas as pd
from predict_risk import predict_student_risk

app = Flask(__name__)

# Load CSV for Dashboard Stats
df = pd.read_csv("mooc.csv").fillna(0)
df['total_activity'] = df[['navigate','access','page_close','problem','video','discussion','wiki','server','browser']].sum(axis=1)
df['early_mid_late'] = df['early events'] + df['mid events'] + df['late events']
df['active_days'] = df['study days']
df['activity_duration'] = df['lastlog-firstlog']

# Compute Risk for Dashboard
def compute_risk(row):
    risk_count = 0
    if row['total_activity'] < 50: risk_count += 1
    if row['active_days'] < 5: risk_count += 1
    if row['video'] < 3: risk_count += 1
    if row['problem'] < 3: risk_count += 1
    return 1 if risk_count >= 2 else 0

df['at_risk'] = df.apply(compute_risk, axis=1)
risk_map = {0:"Active",1:"At Risk"}
df['risk_label'] = df['at_risk'].map(risk_map)

team_members = ["Shivanshi Rawat","Suhani Bora","Prateek Bisht","Ansh Karki"]

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    prediction = None
    error = None
    if request.method == 'POST':
        try:
            student_data = {
                'total_activity': float(request.form['total_activity']),
                'early_mid_late': float(request.form.get('early_mid_late',0)),
                'active_days': float(request.form['active_days']),
                'activity_duration': float(request.form.get('activity_duration',0)),
                'video': float(request.form['video']),
                'discussion': float(request.form.get('discussion',0)),
                'problem': float(request.form['problem'])
            }
            prediction, probability = predict_student_risk(student_data)
            prediction = f"{prediction} ({probability:.2f}%)"
        except ValueError as e:
            error = str(e)

    return render_template('predict.html', prediction=prediction, error=error)


@app.route('/dashboard')
def dashboard():
    risk_counts = df['risk_label'].value_counts().to_dict()
    avg_features = df[['total_activity','early_mid_late','active_days','activity_duration','video','discussion','problem']].mean().round(2).to_dict()
    return render_template('dashboard.html', risk_counts=risk_counts, avg_features=avg_features, team_members=team_members)

if __name__ == '__main__':
    app.run(debug=True)  
