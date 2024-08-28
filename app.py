# import numpy as np
# import pickle
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import LabelEncoder
# from sklearn import model_selection
# from sklearn.preprocessing import MinMaxScaler

# from flask import (
#     Flask,
#     url_for,
#     render_template
# )
# from forms import InputForm

# app = Flask(__name__)
# app.config["SECRET_KEY"] = "secret_key"

# # Load the model correctly using 'open' and 'with' statement

# with open("random_forest_model.pkl", "rb") as model_file:
#     model = pickle.load(model_file)


# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("home.html", title="Home")


# @app.route("/predict", methods=["GET", "POST"])
# def predict():
#     form = InputForm()
#     if form.validate_on_submit():
#         x_new = pd.DataFrame(dict(
#             person_age=[form.person_age.data],
#             person_income=[form.person_income.data],
#             person_home_ownership=[form.person_home_ownership.data],
#             person_emp_length=[form.person_emp_length.data],
#             loan_intent=[form.loan_intent.data],
#             loan_grade=[form.loan_grade.data],
#             loan_amnt=[form.loan_amnt.data],
#             loan_int_rate=[form.loan_int_rate.data],
#             loan_percent_income=[form.loan_percent_income.data],
#             cb_person_default_on_file=[form.cb_person_default_on_file.data],
#             cb_person_cred_hist_length=[form.cb_person_cred_hist_length.data],
           
#         ))
#         input_arr = []
#         def SC_LabelEncoder1(text):
#           if text == "RENT":
#             return 1
#           elif text == "MORTGAGE":
#             return 2
#           elif text == "OWN":
#            return 3
#           else:
#             return 0
        
#         x_new["person_home_ownership"] = x_new["person_home_ownership"].apply(SC_LabelEncoder1)


#         def SC_LabelEncoder1(text):
#           if text == "EDUCATION":
#             return 1
#           elif text == "DEBTCONSOLIDATION":
#            return 2
#           elif text == "VENTURE":
#            return 5
#           elif text == "PERSONAL":
#            return 4
#           elif text == "MEDICAL":
#            return 3
#           else:
#            return 0
    

#         x_new["loan_intent"] = x_new["loan_intent"].apply(SC_LabelEncoder1)

#         def SC_LabelEncoder1(text):
#           if text == "A":
#             return 0
#           elif text == "B":
#            return 1
#           elif text == "C":
#            return 2
#           elif text == "D":
#            return 3
#           elif text == "E":
#            return 4
#           elif text == "F":
#            return 5
#           elif text == "G":
#            return 6
#           else:
#            return 7
      

#         x_new["loan_grade"] = x_new["loan_grade"].apply(SC_LabelEncoder1)



#         def SC_LabelEncoder1(text):
#           if text == "Y":
#            return 1
#           else:
#            return 0
    

#         x_new["cb_person_default_on_file"] = x_new["cb_person_default_on_file"].apply(SC_LabelEncoder1)

#         scaler=MinMaxScaler()
#         x_new[x_new.columns]=scaler.fit_transform(x_new[x_new.columns])



#         input_array = np.array([input_arr])

#         prediction = model.predict(input_array)

#         if prediction[0] == 1:
#             message = " Applicant able to play risk!"
#         else:
#             message = " Applicant not able to play risk !"

#        # message = f"The predicted Attrition is {prediction[0]} "
#     else:
#         message = "Please provide valid input details!"

#     return render_template("predict.html", title="Predict", form=form, output=message)



# if __name__ == "__main__":
#     app.run(debug=True)



import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, render_template
from forms import InputForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

with open("random_forest_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    form = InputForm()
    if form.validate_on_submit():
        x_new = pd.DataFrame({
            "person_age": [form.person_age.data],
            "person_income": [form.person_income.data],
            "person_home_ownership": [form.person_home_ownership.data],
            "person_emp_length": [form.person_emp_length.data],
            "loan_intent": [form.loan_intent.data],
            "loan_grade": [form.loan_grade.data],
            "loan_amnt": [form.loan_amnt.data],
            "loan_int_rate": [form.loan_int_rate.data],
            "loan_percent_income": [form.loan_percent_income.data],
            "cb_person_default_on_file": [form.cb_person_default_on_file.data],
            "cb_person_cred_hist_length": [form.cb_person_cred_hist_length.data],
        })

        # Encoding categorical features
        def encode_home_ownership(val):
            return {"RENT": 1, "MORTGAGE": 2, "OWN": 3, "OTHER": 0}.get(val, 0)
        
        def encode_loan_intent(val):
            return {"EDUCATION": 1, "DEBTCONSOLIDATION": 2, "VENTURE": 5, "PERSONAL": 4, "MEDICAL": 3, "HOMEIMPROVEMENT": 0}.get(val, 0)
        
        def encode_loan_grade(val):
            return {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6}.get(val, 7)
        
        def encode_default_on_file(val):
            return 1 if val == "Y" else 0

        x_new["person_home_ownership"] = x_new["person_home_ownership"].apply(encode_home_ownership)
        x_new["loan_intent"] = x_new["loan_intent"].apply(encode_loan_intent)
        x_new["loan_grade"] = x_new["loan_grade"].apply(encode_loan_grade)
        x_new["cb_person_default_on_file"] = x_new["cb_person_default_on_file"].apply(encode_default_on_file)

        # Scaling features
        scaler = MinMaxScaler()
        x_new[x_new.columns] = scaler.fit_transform(x_new[x_new.columns])

        # Convert DataFrame to input array
        input_array = x_new.values

        prediction = model.predict(input_array)

        message = "Applicant able to play risk!" if prediction[0] == 0 else "Applicant not able to play risk!"
    else:
        message = "Please provide valid input details!"

    return render_template("predict.html", title="Predict", form=form, output=message)

if __name__ == "__main__":
    app.run(debug=True)
    

