import pickle

import streamlit as st
import numpy as np

def main():
    model=pickle.load(open("vc.pickle", "rb"))

# create Streamlit app

    st.write("Enter the following features to check if the transaction is legitimate or fraudulent:")

    col1,col2=st.columns(2)

#time
    with col1:
        inp_t=st.number_input('Enter Time taken',key='col1')

#Amount
    with col2:
        inp_a=st.number_input('Enter Amount credited',key='col2')

# create input fields for user to enter feature values
    input_df = st.text_input('Input All features')
    input_df_lst = input_df.split(',')
# create a button to submit input and get prediction
    submit = st.button("Submit")

    if submit:
    # get input feature values
        features = np.array(input_df_lst, dtype=np.float64)
        features=np.hstack([inp_t,features,inp_a])
    # make prediction
        prediction = model.predict(features.reshape(1,-1))
    # display result
        if prediction[0] == 0:
            st.write("Legitimate transaction")
        else:
            st.write("Fraudulent transaction")