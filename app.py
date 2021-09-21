from flask import Flask,render_template,request
import requests

from bs4 import BeautifulSoup
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/movies' ,methods=["POST"]) 
def movies():
    numberofmovies=request.form["number"]
    r=requests.get("https://www.imdb.com/search/title/?title_type=feature&sort=num_votes,desc&count="+ numberofmovies)
    source=BeautifulSoup(r.content, 'html.parser')
    print(numberofmovies)
    return render_template("movies.html",source=source)


if __name__ == '__main__':
   app.run()

