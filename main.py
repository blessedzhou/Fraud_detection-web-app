import streamlit as st
import pandas as pd
import numpy as np
import pickle 


load_model = pickle.load(open('adaboost_model.sav', 'rb'))

###creating a function for prediction

def fraud_detection(input_data):
   
    
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    prediction =load_model.predict(input_data_reshaped)
    
    print(prediction)
    
    if(prediction[0]==0):
        return "The transaction is not fraudulent"
    else:
        return "The transaction is Fraudulent"


def main():

    st.title ("Detecting Fraudulent Transactions Using Adaboost Algorithm")
    

    ### input data

    step = st.text_input("step of transaction")
    type = st.text_input("Form Of The Transaction")
    amount = st.text_input("Amount Per Transaction")
    oldbalanceOrg = st.text_input("Account Balance Of Sender")
    newbalanceOrig= st.text_input("New Balance Of Sender")
    oldbalanceDest = st.text_input("Old Balance For Destination Account")
    newbalanceDest= st.text_input("New Account Balance For Destination")
    isFlaggedFraud = st.text_input("Is Really Fraud")

    ## detecting
    detection = ''

    #creating a button 
    if st.button('Detect Fraud'):
        detection = fraud_detection([step(1-744 time), type(1-4 CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER), amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest,  isFlaggedFraud])


    st.success(detection)




if __name__=='__main__':
    main()
