import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# load the model
stroke_model = pickle.load(open('stroke_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Stroke Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

if (selected == 'Stroke Prediction'):

    # page title
    st.title('Stroke Prediction using ML')
    from PIL import Image

    image = Image.open('pic.jpeg')

    st.image(image)

    # getting the input data from the user



    Gender = st.text_input('Gender(0 for female,1 for male and 2 for other)')

    Age = st.text_input('Your Age')


    Hypertension = st.text_input('0 if do not have hypertension, 1 if have hypertension)')


    Heartdisease = st.text_input('0 if do not have any heart diseases, 1 if have a heart disease')


    Ever_married = st.text_input('0 for not married, 1 for married')


    Work_type = st.text_input(
            ' Work Status:0 for "Goverment job", 1 for "Never worked", 2 for "Private" , 3 for "Self-employed" or 4 for "Children"')


    Residence_type = st.text_input('0 for "Rural" or 1 for "Urban"')


    Avg_glucose_level = st.text_input('Average Glucose Level')

    BMI = st.text_input('Body Mass Index')

    Smoking_status = st.text_input(
            '0 for "Unknown", 1 for "formerly smoked", 2 for "never smoked" or 3 for "smokes"')

    # code for Prediction
    stroke_diagnosis = ''

    # creating a button for Prediction

    if st.button('Stroke Test Result'):
        stroke_prediction = stroke_model.predict([[Gender, Age, Hypertension, Heartdisease, Ever_married, Work_type,
                                                   Residence_type, Avg_glucose_level, BMI, Smoking_status]])

        if (stroke_prediction[0] == 1):
            stroke_diagnosis = 'The person has risk of getting stroke'
        else:
            stroke_diagnosis = 'The person does not has risk of getting stroke'


    st.success(stroke_diagnosis)