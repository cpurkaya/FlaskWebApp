'''
This is a demo project of flask implementation.
Flask is a micro web framework.
The templating engine that flask uses is called jinja2
'''

from flask import Flask,render_template #from flask module import Flask class

app = Flask(__name__) #create an object of flask class

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
    return render_template('about.html')

if __name__ == '__main__': #if it is run directly and not if imported onto other py file
    app.run(debug=True) #debug=True because to not restart the web server each time we make a change