from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Basic rule-based diagnosis
def get_diagnosis(symptom):
    symptom = symptom.lower()

    if "fever" in symptom and "cough" in symptom:
        return "You may have flu or COVID-19. Please consult a doctor."
    elif "headache" in symptom and "blurred vision" in symptom:
        return "You may be experiencing migraine or eye strain."
    elif "joint pain" in symptom:
        return "You may have arthritis or a minor joint injury. Please rest and consult a physician."
    elif "stomach pain" in symptom:
        return "You may be experiencing indigestion or gastritis."
    elif "vomiting" in symptom:
        return "It may be due to food poisoning or infection. Stay hydrated."
    elif "diarrhea" in symptom:
        return "You may have a stomach infection. Drink ORS and see a doctor if it continues."
    elif "skin rash" in symptom:
        return "You may have an allergic reaction or skin infection. Avoid scratching and consult a doctor."
    elif "breathing difficulty" in symptom:
        return "This could be a sign of asthma or an allergic reaction. Seek immediate medical attention."
    elif "chest pain" in symptom:
        return "This could be a sign of a heart issue. Please seek immediate medical attention."
    elif "fatigue" in symptom and "weight loss" in symptom:
        return "This could be a sign of a thyroid issue or diabetes. Please consult a healthcare provider."
    elif "nausea" in symptom and "dizziness" in symptom:
        return "You may be experiencing dehydration or low blood sugar. Drink water and eat something light."
    elif "sore throat" in symptom and "swollen glands" in symptom:
        return "You may have a throat infection or tonsillitis. Gargle with warm salt water and consult a doctor if it persists."
    elif "rash" in symptom and "itching" in symptom:
        return "You may have an allergic reaction or eczema. Avoid scratching and consider consulting a dermatologist."
    elif "pain" in symptom and "swelling" in symptom:
        return "You may have a sprain or strain. Rest the affected area and apply ice."
    elif "cough" in symptom and "sore throat" in symptom:
        return "You may have a common cold or throat infection. Rest and stay hydrated."
    elif "runny nose" in symptom and "sneezing" in symptom:
        return "You may have allergies or a common cold. Avoid allergens and consider antihistamines."
    elif "back pain" in symptom:
        return "You may have muscle strain or a herniated disc. Rest and apply heat or ice."
    elif "high blood pressure" in symptom:
        return "You may be experiencing hypertension. Monitor your blood pressure and consult a healthcare provider."
    elif "anxiety" in symptom or "stress" in symptom:
        return "You may be experiencing anxiety or stress. Consider relaxation techniques and consult a mental health professional if needed."
    elif "depression" in symptom:
        return "You may be experiencing depression. It's important to talk to someone who can help, like a mental health professional."
    elif "allergy" in symptom:
        return "You may have an allergic reaction. Identify the allergen and avoid it. Consider antihistamines."
    elif "insomnia" in symptom:
        return "You may be experiencing insomnia. Consider improving your sleep hygiene and consult a healthcare provider if it persists."
    elif "constipation" in symptom:
        return "You may be experiencing constipation. Increase your fiber intake and drink plenty of water."
    elif "urinary pain" in symptom:
        return "You may have a urinary tract infection (UTI). Drink plenty of water and consider consulting a healthcare provider."
    elif "menstrual pain" in symptom:
        return "You may be experiencing dysmenorrhea. Consider over-the-counter pain relief and consult a healthcare provider if it persists."
    elif "ear pain" in symptom:
        return "You may have an ear infection or wax buildup. Avoid inserting objects into your ear and consider consulting a healthcare provider."
    elif "swelling" in symptom and "redness" in symptom:
        return "You may have an infection or inflammation. Keep the area clean and consult a healthcare provider if it worsens."
    elif "numbness" in symptom and "tingling" in symptom:
        return "You may be experiencing nerve compression or neuropathy. Avoid positions that aggravate it and consult a healthcare provider if it persists."
    elif "cough" in symptom and "fever" in symptom:
        return "You may have a respiratory infection. Rest, stay hydrated, and consult a healthcare provider if symptoms worsen."
    elif "pain" in symptom and "numbness" in symptom:
        return "You may have a pinched nerve or sciatica. Rest and avoid activities that worsen the pain."
    elif "dizziness" in symptom and "nausea" in symptom:
        return "You may be experiencing vertigo or a vestibular issue. Rest and avoid sudden movements."
    elif "sweating" in symptom and "chest pain" in symptom:
        return "This could be a sign of a heart attack. Seek immediate medical attention."
    elif "fever" in symptom and "rash" in symptom:
        return "You may have a viral infection like measles or chickenpox. Consult a healthcare provider."
    elif "pain" in symptom and "fever" in symptom:
        return "You may have an infection or inflammation. Rest, stay hydrated, and consult a healthcare provider if symptoms worsen."
    elif "cough" in symptom and "shortness of breath" in symptom:
        return "You may have a respiratory condition like asthma or COPD. Consult a healthcare provider."
    elif "pain" in symptom and "redness" in symptom:
        return "You may have an infection or inflammation. Keep the area clean and consult a healthcare provider if it worsens."
    elif "nausea" in symptom and "vomiting" in symptom:
        return "You may have a gastrointestinal infection or food poisoning. Stay hydrated and consider consulting a healthcare provider."
    elif "fever" in symptom and "chills" in symptom:
        return "You may have an infection. Rest, stay hydrated, and consult a healthcare provider if symptoms worsen."
    elif "cough" in symptom and "fever" in symptom and "sore throat" in symptom:
        return "You may have a respiratory infection like the flu or COVID-19. Rest, stay hydrated, and consult a healthcare provider if symptoms worsen."
    elif "pain" in symptom and "swelling" in symptom and "redness" in symptom:
        return "You may have an infection or inflammation. Keep the area clean, rest, and consult a healthcare provider if it worsens."
    elif "pain" in symptom and "fever" in symptom and "swelling" in symptom:
        return "You may have an infection or inflammatory condition. Rest, stay hydrated, and consult a healthcare provider if symptoms worsen."
    elif "cough" in symptom and "fever" in symptom and "shortness of breath" in symptom:
        return "You may have a respiratory infection like pneumonia or COVID-19. Seek medical attention if symptoms worsen."
    elif "pain" in symptom and "numbness" in symptom and "tingling" in symptom:
        return "You may have a nerve issue or compression. Avoid positions that aggravate it and consult a healthcare provider if it persists."
    elif "pain" in symptom and "weakness" in symptom:
        return "You may have a muscle strain or injury. Rest the affected area and consider consulting a healthcare provider if it persists."
    elif "fever" in symptom and "headache" in symptom:
        return "You may have a viral infection like dengue or chikungunya. Rest, stay hydrated, and consult a healthcare provider if symptoms worsen."
    elif "pain" in symptom and "fever" in symptom and "rash" in symptom:
        return "You may have a viral infection like measles or chickenpox. Consult a healthcare provider."
    elif "cough" in symptom and "fever" in symptom and "chills" in symptom:
        return "You may have a respiratory infection like the flu or COVID-19. Rest, stay hydrated, and consult a healthcare provider if symptoms worsen."
    elif "pain" in symptom and "fever" in symptom and "redness" in symptom:
        return "You may have an infection or inflammatory condition. Keep the area clean, rest, and consult a healthcare provider if it worsens."
    elif "cough" in symptom and "sore throat" in symptom and "runny nose" in symptom:
        return "You may have a common cold or upper respiratory infection. Rest, stay hydrated, and consider over-the-counter medications."
    else:
        return "Sorry, I couldn't identify the condition. Please consult a nearby healthcare center."
    

@app.route('/')
def index():
    return render_template('index.html')  # Make sure your HTML is in a `templates` folder

@app.route('/get_diagnosis', methods=['POST'])
def diagnose():
    data = request.get_json()
    user_message = data.get('message', '')
    response = get_diagnosis(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
