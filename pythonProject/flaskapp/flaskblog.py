'''
This is a demo project of flask implementation.
Flask is a micro web framework.
The templating engine that flask uses is called jinja2
'''

from flask import Flask, render_template, url_for, flash, redirect #from flask module import Flask class
from forms import RegistrationForm, LoginForm


app = Flask(__name__) #create an object of flask class
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

data=[
        {
            'title': 'First post',
            'content': 'First post content line 1',
            'date_posted': '24-08-2024',
            'author': 'Chandreyee Purkayastha'
        },
        {
            'title': 'Second post',
            'content': 'Second post content line 1',
            'date_posted': '25-08-2024',
            'author': 'Dummy User 2'
        }
]
@app.route("/")  #root dir
@app.route("/home") #home
def home():
    return render_template('home.html',post=data)

@app.route("/about") #adding an about route
def about():
    return render_template('about.html',title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__': #if it is run directly and not if imported onto other py file
    app.run(debug=True) #debug=True because to not restart the web server each time we make a change