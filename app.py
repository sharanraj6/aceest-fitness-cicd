from flask import Flask, request, jsonify

app = Flask(__name__)

# Business logic extracted from Aceestver scripts
PROGRAMS = {
    "Fat Loss (FL)": {"factor": 22},
    "Muscle Gain (MG)": {"factor": 35},
    "Beginner (BG)": {"factor": 26}
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to ACEest Fitness & Gym API"})

@app.route('/calculate_calories', methods=['POST'])
def calculate_calories():
    data = request.get_json()
    
    if not data or 'weight' not in data or 'program' not in data:
        return jsonify({"error": "Missing weight or program data"}), 400

    weight = data['weight']
    program = data['program']

    if program not in PROGRAMS:
        return jsonify({"error": "Invalid program selected"}), 400

    # Calculate calories based on the logic from the provided scripts
    calories = int(weight * PROGRAMS[program]["factor"])
    
    return jsonify({
        "program": program, 
        "weight_kg": weight,
        "target_calories": calories
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)