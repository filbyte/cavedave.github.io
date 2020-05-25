from flask import Flask, render_template, flash, request,redirect, url_for
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import csv

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextAreaField('Name:', validators=[validators.required()])
    text = TextAreaField('exampleFormControlTextarea1', validators=[validators.required()])
    text1 = TextAreaField('exampleFormControlTextarea2', validators=[validators.required()])
    text2 = TextAreaField('exampleFormControlTextarea3', validators=[validators.required()])
    text3 = TextAreaField('exampleFormControlTextarea4', validators=[validators.required()])
    text4 = TextAreaField('exampleFormControlTextarea5', validators=[validators.required()]) 


    @app.route('/success/')
    def success():
     # replace this with a query from whatever database you're using
     #result = get_result_from_database(result_id)
     # access the result in the tempalte, for example {{ result.name }}

     return render_template('success.html')
   
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        form = ReusableForm(request.form)
        
        print(form.errors)
        if request.method == 'POST':
            name=request.form['name']
            text=request.form['exampleFormControlTextarea1']
            text1=request.form['exampleFormControlTextarea2']
            text2=request.form['exampleFormControlTextarea3']
            text3=request.form['exampleFormControlTextarea4']
            text4=request.form['exampleFormControlTextarea5']            
            print(text)
            print(name)

 # This array is the fields your csv file has and in the following code
        # you'll see how it will be used. Change it to your actual csv's fields.
            fieldnames = ['name', 'question','question1','question2','question3','question4']

        # We repeat the same step as the reading, but with "w" to indicate
        # the file is going to be written.
            with open('nameList.csv','a+') as inFile:
            # DictWriter will help you write the file easily by treating the
            # csv as a python's class and will allow you to work with
            # dictionaries instead of having to add the csv manually.
                writer = csv.DictWriter(inFile, fieldnames=fieldnames)

            # writerow() will write a row in your csv file
                writer.writerow({'name': name, 'question': text, 'question1': text1, 'question2': text2, 'question3': text3, 'question4': text4})




        
        if form.validate():
        # Save the comment here.
            flash('Your questions were' + name)
            flash('text was ' + text)
        else:
            flash('Error: All the form fields are required. ')
        #return redirect(url_for('success'))
        return render_template('hello.html', form=form)

if __name__ == "__main__":
    app.run()
