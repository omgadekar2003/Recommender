# import joblib
# import pandas as pd
# import streamlit as st

# # Load the trained model
# model = joblib.load("predict_.pkl")

# # Feature names extracted during model training
# # Replace this list with the actual feature names from your model
# feature_names = [
#     'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
#     'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
#     'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain',
#     'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
#     'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever',
#     'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache',
#     'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
#     'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
#     'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
#     'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm',
#     'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion',
#     'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements',
#     'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness',
#     'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes',
#     'enlarged_thyroid', 'brittle_nails', 'swollen_extremities', 'excessive_hunger',
#     'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain',
#     'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness',
#     'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side',
#     'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine',
#     'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression',
#     'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain',
#     'abnormal_menstruation', 'watering_from_eyes', 'increased_appetite', 'polyuria',
#     'family_history', 'lack_of_concentration', 'visual_disturbances'
# ]

# # Streamlit app UI
# st.title("Disease Prediction System")
# st.write("Enter your symptoms to predict the likely disease.")

# # Multi-select dropdown for symptom input
# user_symptoms = st.multiselect(
#     "Select your symptoms from the list:",
#     feature_names,
#     help="Select one or more symptoms you are experiencing."
# )

# if st.button("Predict Disease"):
#     if not user_symptoms:
#         st.warning("Please select at least one symptom to proceed.")
#     else:
#         # Create a feature vector with 1 for selected symptoms and 0 otherwise
#         input_vector = [1 if symptom in user_symptoms else 0 for symptom in feature_names]
        
#         # Create a DataFrame for the model
#         input_df = pd.DataFrame([input_vector], columns=feature_names)

#         try:
#             # Make predictions
#             prediction = model.predict(input_df)[0]
#             st.success(f"The predicted disease is: {prediction}")
#         except Exception as e:
#             st.error(f"An error occurred during prediction: {str(e)}")




###
##
#
import joblib
import pandas as pd
import streamlit as st
import numpy as np

# Load the trained model
model = joblib.load("predict_.pkl")

# Symptom dictionary and diseases list
symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of_urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}

diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}

# Custom helper function
def helper(dis):
    # Assuming you have your dataframes like 'description', 'precautions', 'medications', etc. available
    # These would need to be defined or loaded with real data in your project
    desc = description[description['Disease'] == dis]['Description']
    desc = " ".join([w for w in desc])

    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']]
    pre = [col for col in pre.values]

    med = medications[medications['Disease'] == dis]['Medication']
    med = [med for med in med.values]

    die = diets[diets['Disease'] == dis]['Diet']
    die = [die for die in die.values]

    wrkout = workout[workout['disease'] == dis] ['workout']

    return desc, pre, med, die, wrkout

# Model Prediction function
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in patient_symptoms:
        input_vector[symptoms_dict[item]] = 1
    disease_index = model.predict([input_vector])[0]
    disease_name = diseases_list[disease_index]
    return disease_name

# Streamlit app UI
st.title("Disease Prediction System")
st.write("Enter your symptoms to predict the likely disease.")

# Multi-select dropdown for symptom input
user_symptoms = st.multiselect(
    "Select your symptoms from the list:",
    symptoms_dict.keys(),
    help="Select one or more symptoms you are experiencing."
)

if st.button("Predict Disease"):
    if not user_symptoms:
        st.warning("Please select at least one symptom to proceed.")
    else:
        # Get prediction
        predicted_disease = get_predicted_value(user_symptoms)
        
        # Display predicted disease
        st.success(f"The predicted disease is: {predicted_disease}")
        
        # Display additional info
        description, precautions, medications, diet, workout = helper(predicted_disease)
        
        st.subheader("Description")
        st.write(description)
        
        st.subheader("Precautions")
        st.write(precautions)
        
        st.subheader("Medications")
        st.write(medications)
        
        st.subheader("Diet")
        st.write(diet)
        
        st.subheader("Recommended Workouts")
        st.write(workout)
