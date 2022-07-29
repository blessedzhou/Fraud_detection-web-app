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

    st.title ("Detecting Fraudulent Transactions")
    

    ### input data

    step(1-744 unit of time) = st.text_input("step of transaction")
    type(1-4 CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER)= st.text_input("Form Of The Transaction")
    amount(transaction amount) = st.text_input("Amount Per Transaction")
    oldbalanceOrg(Initial balance of sender) = st.text_input("Account Balance Of Sender")
    newbalanceOrig(balance of sender after transaction) = st.text_input("New Balance Of Sender")
    oldbalanceDest(initial balance of destination account) = st.text_input("Old Balance For Destination Account")
    newbalanceDest(balance after transaction of destination) = st.text_input("New Account Balance For Destination")
    isFlaggedFraud(0-1 either no or yes, transaction flagged as fraudulent by the bank) = st.text_input("Is Really Fraud")

    ## detecting
    detection = ''

    #creating a button 
    if st.button('Detect Fraud'):
        detection = fraud_detection([step, type, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest,  isFlaggedFraud])


    st.success(detection)




if __name__=='__main__':
    main()
