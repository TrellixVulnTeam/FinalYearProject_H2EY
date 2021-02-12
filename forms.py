from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField
from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, FloatField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, Regexp, NumberRange
#from app import db

class SignUpForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    email = StringField('Email')
    submit = SubmitField('Sign Up')
    
#    def __init__(self, username, password, email, submit):
#        self.username = username
#        self.password = password
#        self.email = email
#        self.submit = submit


class SignInForm(FlaskForm):
    ausername = StringField('Username')
    apassword = PasswordField('Password')
    submit = SubmitField('Sign In')

#    def __init__ (self, username, password, submit):
#        self.username = username
#        self.password = password
#        self.submit = submit

class AddCustomerForm(FlaskForm):
    customerid = HiddenField()
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    Length(max=20, message="Too long Firstname")
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    Length(max=20, message="Too long Surname")
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    submit = SubmitField ('Add Customer')

class AddStockForm(FlaskForm):
    stockid = HiddenField()
    size = StringField('Size', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Size"),
    Length(min=0,max=3, message="Too many characters for Size")
    ])
    type = StringField('Type', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Type of clothing"),
    ])
    colour = StringField('Colour', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Colour"),
    ])
    brand = StringField('Brand', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Brand"),
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    supplierid = IntegerField('Supplier ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Supplier ID")
    ])
    material = StringField('Material', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Material"),
    ])
    submit = SubmitField('Add Stock')
    

class AddSupplierForm(FlaskForm):
    supplierid = HiddenField()
    suppliername = StringField('Supplier Name', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Supplier Name"),
    ])
    submit = SubmitField('Add Supplier')

class AddListingForm(FlaskForm):
    listingid = HiddenField()
    supplierid = IntegerField('Supplier ID', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Supplier ID")
    ])
    price = FloatField('Price', [InputRequired(),
    NumberRange(min=1.00, max=4000, message= "Invalid Price Range. Please enter a price of at least £1"),
    ])
    submit = SubmitField('Add Listing')






class AddAdminForm(FlaskForm):
    id = HiddenField()
    ausername = StringField('Username', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Username"),
    ])
    apassword = StringField('Password', [InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Password"),
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    submit = SubmitField('Sign Up')
    

class CustomerSearchForm(FlaskForm):
    choices = [('customerid', 'customerid'), ('customerfirstname'), ('customersurname', 'customersurname'), ('email','email')]
    select = SelectField ('Search for a customer', choices=choices)
    search = StringField('')
# class CustomerSearchForm(FlaskForm):
#     choices = [('customersurname', 'customersurname')]
#     select = SelectField ('Search for a customer', choices=choices)
#     search = StringField('')


class EditCustomerForm(FlaskForm):
    customerfirstname = StringField('Customer Firstname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Firstname"),
    Length(max=20, message="Too long Firstname")
    ])
    customersurname = StringField('Customer Surname',[InputRequired(),
    Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Surname"),
    Length(max=20, message="Too long Surname")
    ])
    email = StringField('Email',[InputRequired(),
    #Regexp(r'^[A-Za-z\s\-\'\'\/]+$', message= "Invalid Customer Email"),
    ])
    update = SubmitField('Update')
    cancel = SubmitField('Cancel')