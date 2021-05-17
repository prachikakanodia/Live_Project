from flask import Flask, render_template, request
import pandas as pd

app = Flask("Excel_Web-App")

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST" and "z" in request.form:
        x = request.form.get('z')
        x = int(x)
        dataset = pd.read_excel("data/Employee_salary.xlsx")
        Employee_Name = dataset["Employee_Name"]
        dataset['Salary'] = dataset['Salary'] + dataset['Salary'] * (x/100)
        filename="Updated_file.xlsx"
        dataset.to_excel(filename)
        return "Data has been Updated Successfully in Updated_file.xlsx!! Check it out!!"

    return render_template("form.html")

