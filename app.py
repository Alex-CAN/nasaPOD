from flask import Flask, render_template
import requests
from datetime import date

app = Flask(__name__)

@app.route("/")
def index():
    return "Hey yall"

@app.route("/about")
def about():
    return "<h1>about stuff here</h1>"

@app.route('/nasa')
def nasa():
    
    today = str(date.today())    
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=GdHGB6sVubfXxXmS8Gsp5N8f9INB4hDuQqdTafOl&date="+today)
 
    data= response.json()
    
    return render_template('nasa.html' , data=data)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

