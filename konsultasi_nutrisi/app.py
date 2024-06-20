from flask import Flask, request, render_template, jsonify
import pandas as pd

app = Flask(__name__)

# Load CSV data
df = pd.read_csv('kekurangan_nutrisi_padi_bersih.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    symptom = request.form['symptom'].lower()
    growth_phase = request.form['growth_phase'].lower()
    
    # Filter data based on partial match for symptom and growth_phase
    filtered_df = df[df['Gejala Kekurangan'].str.lower().str.contains(symptom) & 
                     df['Fase Pertumbuhan Padi'].str.lower().str.contains(growth_phase)]
    
    results = filtered_df.to_dict(orient='records')
    
    # If no exact match is found, try to find partial matches for growth_phase
    if not results:
        filtered_df_partial = df[df['Gejala Kekurangan'].str.lower().str.contains(symptom) |
                                 df['Fase Pertumbuhan Padi'].apply(lambda x: growth_phase in x.lower())]
        print(filtered_df)
        results = filtered_df_partial.to_dict(orient='records')
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
