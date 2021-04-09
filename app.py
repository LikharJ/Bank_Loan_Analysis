# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:13:03 2021

@author: vaishali.gunjal
"""

from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
#import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route("/", methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
     
      
    if request.method == 'POST':
        
        Credit_History = float(request.form['Credit_History'])
        
        ApplicantIncome = float(request.form['ApplicantIncome'])
        CoapplicantIncome = float(request.form['CoapplicantIncome'])
        Total_Income=ApplicantIncome + CoapplicantIncome
        #TotalIncomeLog=np.log(TotalIncome)
        
        LoanAmount = float(request.form['LoanAmount'])
        Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
        EMI=LoanAmount/Loan_Amount_Term
       # EMI=np.log(EMI)
       
        BalanceIncome = Total_Income - EMI
         
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender_Male=1
            Gender_Female=0
                 
        else:
            Gender_Male=0
            Gender_Female=1
        
        Married=request.form['Married']
        if(Married=='Yes'):
            Married_Yes=1
            Married_No=0
                 
        else:
            Married_Yes=0
            Married_No=1
            
        Dependents = int(request.form['Dependents'])
        if(Dependents==0):
            Dependents_0=1
            Dependents_1=0
            Dependents_2=0
            Dependents_3=0
            
        elif(Dependents==1):
            Dependents_0=0
            Dependents_1=1
            Dependents_2=0
            Dependents_3=0
            
        elif(Dependents==2):
            Dependents_0=0
            Dependents_1=0
            Dependents_2=1
            Dependents_3=0
            
        else:
            Dependents_0=0
            Dependents_1=0
            Dependents_2=0
            Dependents_3=1
        
        Education=request.form['Education']
        if(Education=='Graduate'):
            Education_Graduate = 1
            Education_NotGraduate = 0
                 
        else:
            Education_Graduate = 0
            Education_NotGraduate = 1
        
        Self_Employed=request.form['Self_Employed']
        if(Self_Employed=='Yes'):
            Self_Employed_Yes=1
            Self_Employed_No=0
                 
        else:
            Self_Employed_Yes=0
            Self_Employed_No=1
        
       
    
        Property_Area = (request.form['Property_Area'])
        if(Property_Area=='Semiurban'):
            Property_Area_Semiurban=1
            Property_Area_Urban=0
            Property_Area_Rural=0
        elif(Property_Area=='Urban'):
            Property_Area_Semiurban=0
            Property_Area_Urban=1
            Property_Area_Rural=0
        else:
            Property_Area_Semiurban=0
            Property_Area_Urban=0
            Property_Area_Rural=1


        #prediction=rf_model.predict([[Dependents, Credit_History, TotalIncomeLog, EMI, Gender_Male,Married_Yes, Education_Not , Self_Employed_Yes, Property_Area_Semiurban, Property_Area_Urban]])
        prediction=model.predict([[Credit_History, Total_Income, EMI, BalanceIncome, Gender_Female, Gender_Male, Married_No, Married_Yes, Dependents_3, Dependents_0, Dependents_1, Dependents_2,Education_Graduate, Education_NotGraduate, Self_Employed_No, Self_Employed_Yes, Property_Area_Rural, Property_Area_Semiurban, Property_Area_Urban]])
        output=prediction[0]
        if output==0:
            return render_template('index.html',prediction_text="Sorry Loan cannot be given!")
        else:
            return render_template('index.html',prediction_text="Applicable for Loan:)")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)