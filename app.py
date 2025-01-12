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
import joblib
import pandas as pd
import streamlit as st

# Load the trained model (joblib file)
model = joblib.load("predict.pkl")

# Load additional data files (CSV or other formats)
symptoms_data = pd.read_csv("symtoms_df.csv")
descriptions_data = pd.read_csv("description.csv")
precautions_data = pd.read_csv("precautions_df.csv")
diets_data = pd.read_csv("diets.csv")

# Helper function to get recommendations
def get_recommendations(predicted_disease):
    try:
        description = descriptions_data.loc[descriptions_data['Disease'] == predicted_disease, 'Description'].values[0]
        precautions = precautions_data.loc[precautions_data['Disease'] == predicted_disease, 'Precautions'].values.tolist()
        diet = diets_data.loc[diets_data['Disease'] == predicted_disease, 'Diet'].values[0]
        return description, precautions, diet
    except IndexError:
        return "No description available", ["No precautions available"], "No diet information available"

# Streamlit app
def main():
    st.title("Disease Prediction and Recommendations")

    st.write(
        "Enter your symptoms below to predict the disease and get personalized recommendations."
    )

    # Dropdown options based on symptoms data
    symptom_options = symptoms_data.columns[:-1].tolist()

    # Input fields for symptoms
    symptoms = []
    for i in range(1, 6):
        symptom = st.selectbox(f"Symptom {i}:", [""] + symptom_options, key=f"symptom_{i}")
        symptoms.append(symptom.strip().lower() if symptom else "")

    if st.button("Predict"):
        if all(not symptom for symptom in symptoms):
            st.warning("Please select at least one symptom.")
        else:
            try:
                # Convert input to a dataframe (ensure compatibility with the model)
                input_data = pd.DataFrame([symptoms], columns=symptoms_data.columns[:-1])
                input_data.fillna(0, inplace=True)  # Fill missing values with 0 if required by the model

                # Predict the disease
                prediction = model.predict(input_data)[0]

                # Get recommendations based on the prediction
                description, precautions, diet = get_recommendations(prediction)

                # Display the results
                st.subheader(f"Predicted Disease: {prediction}")
                st.write(f"**Description**: {description}")
                
                st.subheader("Precautions:")
                for precaution in precautions:
                    st.write(f"- {precaution}")

                st.subheader("Diet Recommendations:")
                st.write(diet)

            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")

if __name__ == "__main__":
    main()
