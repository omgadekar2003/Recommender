# import joblib
# import pandas as pd
# import streamlit as st

# # Load the trained model (joblib file)
# model = joblib.load("predict.pkl")

# # Load additional data files (CSV or other formats)
# symptoms_data = pd.read_csv("symtoms_df.csv")
# descriptions_data = pd.read_csv("description.csv")
# precautions_data = pd.read_csv("precautions_df.csv")
# diets_data = pd.read_csv("diets.csv") 

# # Helper function to get recommendations
# def get_recommendations(predicted_disease):
#     try:
#         description = descriptions_data.loc[descriptions_data['Disease'] == predicted_disease, 'Description'].values[0]
#         precautions = precautions_data.loc[precautions_data['Disease'] == predicted_disease, 'Precautions'].values.tolist()
#         diet = diets_data.loc[diets_data['Disease'] == predicted_disease, 'Diet'].values[0]
#         return description, precautions, diet
#     except IndexError:
#         return "No description available", ["No precautions available"], "No diet information available"

# # Streamlit app
# def main():
#     st.title("Disease Prediction and Recommendations")

#     st.write(
#         "Enter your symptoms below to predict the disease and get personalized recommendations."
#     )

#     # Input fields for symptoms
#     symptoms = []
#     for i in range(1, 6):
#         symptom = st.text_input(f"Symptom {i}:")
#         symptoms.append(symptom.strip().lower())

#     if st.button("Predict"):
#         if all(not symptom for symptom in symptoms):
#             st.warning("Please enter at least one symptom.")
#         else:
#             try:
#                 # Convert input to a dataframe (ensure compatibility with the model)
#                 input_data = pd.DataFrame([symptoms], columns=symptoms_data.columns[:-1])

#                 # Predict the disease
#                 prediction = model.predict(input_data)[0]

#                 # Get recommendations based on the prediction
#                 description, precautions, diet = get_recommendations(prediction)

#                 # Display the results
#                 st.subheader(f"Predicted Disease: {prediction}")
#                 st.write(f"**Description**: {description}")
                
#                 st.subheader("Precautions:")
#                 st.write("\n".join([f"- {precaution}" for precaution in precautions]))

#                 st.subheader("Diet Recommendations:")
#                 st.write(diet)

#             except Exception as e:
#                 st.error(f"An error occurred during prediction: {e}")

# if __name__ == "__main__":
#     main()



#####
###
##
#
# import joblib
# import pandas as pd
# import streamlit as st

# # Load the trained model (joblib file)
# model = joblib.load("predict.pkl")

# # Load additional data files (CSV or other formats)
# symptoms_data = pd.read_csv("symtoms_df.csv")
# descriptions_data = pd.read_csv("description.csv")
# precautions_data = pd.read_csv("precautions_df.csv")
# diets_data = pd.read_csv("diets.csv")

# # Helper function to get recommendations
# def get_recommendations(predicted_disease):
#     try:
#         description = descriptions_data.loc[descriptions_data['Disease'] == predicted_disease, 'Description'].values[0]
#         precautions = precautions_data.loc[precautions_data['Disease'] == predicted_disease, 'Precautions'].values.tolist()
#         diet = diets_data.loc[diets_data['Disease'] == predicted_disease, 'Diet'].values[0]
#         return description, precautions, diet
#     except IndexError:
#         return "No description available", ["No precautions available"], "No diet information available"

# # Streamlit app
# def main():
#     st.title("Disease Prediction and Recommendations")

#     st.write(
#         "Enter your symptoms below to predict the disease and get personalized recommendations."
#     )

#     # Dropdown options based on symptoms data
#     symptom_options = symptoms_data.columns[:-1].tolist()

#     # Input fields for symptoms
#     symptoms = []
#     for i in range(1, 6):
#         symptom = st.selectbox(f"Symptom {i}:", [""] + symptom_options, key=f"symptom_{i}")
#         symptoms.append(symptom.strip().lower() if symptom else "")

#     if st.button("Predict"):
#         if all(not symptom for symptom in symptoms):
#             st.warning("Please select at least one symptom.")
#         else:
#             try:
#                 # Convert input to a dataframe (ensure compatibility with the model)
#                 input_data = pd.DataFrame([symptoms], columns=symptoms_data.columns[:-1])
#                 input_data.fillna(0, inplace=True)  # Fill missing values with 0 if required by the model

#                 # Predict the disease
#                 prediction = model.predict(input_data)[0]

#                 # Get recommendations based on the prediction
#                 description, precautions, diet = get_recommendations(prediction)

#                 # Display the results
#                 st.subheader(f"Predicted Disease: {prediction}")
#                 st.write(f"**Description**: {description}")
                
#                 st.subheader("Precautions:")
#                 for precaution in precautions:
#                     st.write(f"- {precaution}")

#                 st.subheader("Diet Recommendations:")
#                 st.write(diet)

#             except Exception as e:
#                 st.error(f"An error occurred during prediction: {e}")

# if __name__ == "__main__":
#     main()



# import joblib
# import pandas as pd
# import streamlit as st

# # Load the trained model (joblib file)
# model = joblib.load("predict.pkl")

# # List of all symptoms (leave blank for now)
# all_symptoms = [
#   ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 'prognosis']
# ]

# # Streamlit app
# st.title("Disease Prediction and Recommendations")
# st.write("Enter your symptoms below to predict the disease and get personalized recommendations.")

# # Dynamically add symptom inputs based on the number of symptoms
# num_symptoms = st.number_input("How many symptoms do you want to input?", min_value=1, max_value=10, value=3)
# symptom_inputs = []

# for i in range(num_symptoms):
#     symptom = st.text_input(f"Symptom {i + 1}:")
#     symptom_inputs.append(symptom)

# # Process inputs
# if st.button("Predict Disease"):
#     # Check if all inputs are in the symptom list
#     if not all_symptoms:
#         st.error("The symptom list is empty. Please populate `all_symptoms`.")
#     else:
#         # Create a feature vector based on all_symptoms
#         input_vector = [1 if symptom in symptom_inputs else 0 for symptom in all_symptoms]

#         # Create a DataFrame for the model
#         input_df = pd.DataFrame([input_vector], columns=all_symptoms)

#         try:
#             # Make predictions
#             prediction = model.predict(input_df)[0]
#             st.success(f"Predicted Disease: {prediction}")

#             # Placeholder for recommendations
#             st.info(f"Recommendations for {prediction} will be added here.")
#         except Exception as e:
#             st.error(f"An error occurred during prediction: {str(e)}")





import joblib
import pandas as pd
import streamlit as st

# Load the trained model (joblib file)
model = joblib.load("predict.pkl")

# Load the list of all symptoms from a file
# (e.g., symptoms.txt where each symptom is on a new line)
try:
    with open("symptoms.txt", "r") as f:
        all_symptoms = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    st.error("The symptoms file is missing. Please provide a 'symptoms.txt' file with symptoms listed line by line.")
    # List of all symptoms
    all_symptoms = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 
    'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 
    'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain', 
    'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 
    'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 
    'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 
    'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 
    'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 
    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 
    'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 
    'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 
    'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 
    'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 
    'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 
    'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 
    'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 
    'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 
    'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 
    'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of_urine', 
    'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 
    'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 
    'belly_pain', 'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 
    'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 
    'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 
    'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 
    'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 
    'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 
    'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 
    'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze', 'prognosis'
     ]


# Streamlit app
st.title("Disease Prediction and Recommendations")
st.write("Enter your symptoms below to predict the disease and get personalized recommendations.")

# Dynamically add symptom inputs based on the number of symptoms
num_symptoms = st.number_input("How many symptoms do you want to input?", min_value=1, max_value=10, value=3)
symptom_inputs = []

for i in range(num_symptoms):
    symptom = st.text_input(f"Symptom {i + 1}:")
    symptom_inputs.append(symptom)

# Process inputs
if st.button("Predict Disease"):
    if not all_symptoms:
        st.error("The symptom list is empty. Please ensure the 'symptoms.txt' file is loaded correctly.")
    else:
        # Create a feature vector based on all_symptoms
        input_vector = [1 if symptom in symptom_inputs else 0 for symptom in all_symptoms]

        try:
            # Create a DataFrame for the model
            input_df = pd.DataFrame([input_vector], columns=all_symptoms)

            # Make predictions
            prediction = model.predict(input_df)[0]
            st.success(f"Predicted Disease: {prediction}")

            # Placeholder for recommendations
            st.info(f"Recommendations for {prediction} will be added here.")
        except Exception as e:
            st.error(f"An error occurred during prediction: {str(e)}")
