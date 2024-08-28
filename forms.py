# import pandas as pd
# from flask_wtf import FlaskForm
# from wtforms import (
#     SelectField,
#     IntegerField,
#     SubmitField, 
#     FloatField
# )
# from wtforms.validators import DataRequired

# # Getting the data
# df = pd.read_csv("credit_risk_dataset.csv")
# X_data = df.drop('loan_status', axis=1)

# class InputForm(FlaskForm):
#     PersonAge = IntegerField("person_age", validators=[DataRequired()])
#     person_income = IntegerField("person_income", validators=[DataRequired()])  # Corrected typo
#     person_home_ownership = SelectField(
#         "person_home_ownership", 
#         choices=[('RENT', 'RENT'), ('OWN', 'OWN'), ('MORTGAGE', 'MORTGAGE'), ('OTHER', 'OTHER')], 
#         validators=[DataRequired()]
#     )
#     person_emp_length = IntegerField("person_emp_length", validators=[DataRequired()])
#     loan_intent = SelectField(
#         "loan_intent", 
#         choices=[('EDUCATION', 'EDUCATION'), ('DEBTCONSOLIDATION', 'DEBTCONSOLIDATION'), ('VENTURE', 'VENTURE'), 
#                  ('PERSONAL', 'PERSONAL'), ('MEDICAL', 'MEDICAL'), ('HOMEIMPROVEMENT', 'HOMEIMPROVEMENT')],
#         validators=[DataRequired()]
#     )
#     loan_grade = SelectField(
#         "loan_grade", 
#         choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], 
#         validators=[DataRequired()]
#     )
#     loan_amnt = IntegerField("loan_amnt", validators=[DataRequired()])
#     loan_int_rate = FloatField("loan_int_rate", validators=[DataRequired()])
#     loan_percent_income = FloatField("loan_percent_income", validators=[DataRequired()])
#     cb_person_default_on_file = SelectField(
#         "cb_person_default_on_file", 
#         choices=[('Y', 'Y'), ('N', 'N')], 
#         validators=[DataRequired()]
#     )
#     cb_person_cred_hist_length = IntegerField("cb_person_cred_hist_length", validators=[DataRequired()])

#     submit = SubmitField("Submit")  # Corrected indentation




import pandas as pd
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, SubmitField, FloatField
from wtforms.validators import DataRequired

class InputForm(FlaskForm):
    person_age = IntegerField("person_age", validators=[DataRequired()])
    person_income = IntegerField("person_income", validators=[DataRequired()])
    person_home_ownership = SelectField(
        "person_home_ownership",
        choices=[('RENT', 'RENT'), ('OWN', 'OWN'), ('MORTGAGE', 'MORTGAGE'), ('OTHER', 'OTHER')],
        validators=[DataRequired()]
    )
    person_emp_length = IntegerField("person_emp_length", validators=[DataRequired()])
    loan_intent = SelectField(
        "loan_intent",
        choices=[('EDUCATION', 'EDUCATION'), ('DEBTCONSOLIDATION', 'DEBTCONSOLIDATION'), ('VENTURE', 'VENTURE'),
                 ('PERSONAL', 'PERSONAL'), ('MEDICAL', 'MEDICAL'), ('HOMEIMPROVEMENT', 'HOMEIMPROVEMENT')],
        validators=[DataRequired()]
    )
    loan_grade = SelectField(
        "loan_grade",
        choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')],
        validators=[DataRequired()]
    )
    loan_amnt = IntegerField("loan_amnt", validators=[DataRequired()])
    loan_int_rate = FloatField("loan_int_rate", validators=[DataRequired()])
    loan_percent_income = FloatField("loan_percent_income", validators=[DataRequired()])
    cb_person_default_on_file = SelectField(
        "cb_person_default_on_file",
        choices=[('Y', 'Y'), ('N', 'N')],
        validators=[DataRequired()]
    )
    cb_person_cred_hist_length = IntegerField("cb_person_cred_hist_length", validators=[DataRequired()])

    submit = SubmitField("Submit")
    
