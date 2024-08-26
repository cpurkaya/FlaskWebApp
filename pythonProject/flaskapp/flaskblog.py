from flask import Flask,render_template #from flask module import Flask class

app = Flask(__name__) #create an object of flask class

@app.route("/")  #root dir
@app.route("/home") #home
def home():
    return render_template('home.html')

@app.route("/about") #adding an about route
def about():
    return render_template('about.html')

if __name__ == '__main__': #if it is run directly and not if imported onto other py file
    app.run(debug=True) #debug=True because to not restart the web server each time we make a change