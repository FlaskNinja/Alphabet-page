# from flask import Flask, render_template, redirect, url_for, flash, request
# from random import random
# app = Flask(__name__)
# app.config['SECRET_KEY'] = '0123456789ABC'

# users = []


# @app.route('/', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         firstname = request.form['firstname']
#         surname = request.form['surname']
#         password = request.form['password']
#         email = request.form['email']
#         if len(password) < 8:
#             flash("Password must be up to 8 character")
#             return redirect(url_for('sign_up'))
#         users.append({'name': firstname, 'surname': surname, 'password': password, 'email': email})
#         flash("Account created.")
#         return redirect(url_for('home', username=firstname))
#     return render_template('sign_up.html', users=users)

# @app.route('/user/<username>', methods=['GET', 'POST'])
# def home(username):
#     return render_template('home.html', users=users, name=username)

# @app.route('/log_in', methods=['GET', 'POST'])
# def log_in():
#     if request.method=='POST':
#         lg_name = request.form['firstname']
#         return redirect(url_for('home', username=lg_name))
#     return render_template('log_in.html')

# if __name__ == "__main__":
#     app.run(debug=True)
