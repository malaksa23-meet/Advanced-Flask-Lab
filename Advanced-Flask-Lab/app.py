from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://www.youthdynamics.org/wp-content/uploads/2017/11/teen-engage.png"

user_bio = "Hello Hello , it's Lour , 19YO, I'm a photographer:) "

posts = {
   
    "https://media-cdn.tripadvisor.com/media/vr-splice-j/06/cf/76/54.jpg": "<33333",
    "https://www.allaboutbirds.org/news/wp-content/uploads/2020/07/STanager-Shapiro-ML.jpg": "woooooow ",
    "https://upload.wikimedia.org/wikipedia/commons/5/58/Sunset_2007-1.jpg": "Such an amzing view <33"}


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html',image_link=image_link,user_bio=user_bio,posts=posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
