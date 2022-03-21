from flask import Flask , jsonify , request
import csv 

all_movies = []
with open('movies.csv' , encoding='utf-8') as f:
    r = csv.reader(f)
    data = list(r)
    all_movies = data[1:]

like_movies = []
not_liked_movies = []
did_not_watch_movies = []

app = Flask(__name__) 
@app.route("/")

def homepage():
    return "Welcome"

@app.route('/get-movies') 
def getmovie():
    return jsonify({
        "data" : all_movies[0],
        "status" : "success!"
    })   
@app.route('/liked-movies',methods = ["POST"])

def likedmovie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:] 
    like_movies.append(movie)
    return jsonify({
        "status" : "success!"
    }),200

@app.route('/unliked-movies',methods = ["POST"])

def unlikedmovie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:] 
    not_liked_movies.append(movie)
    return jsonify({
        "status" : "success!"
    }),200

@app.route('/did-not-watch-movies',methods = ["POST"])

def didnotwatchmovie():
    global all_movies
    movie = all_movies[0]
    all_movies = all_movies[1:] 
    did_not_watch_movies.append(movie)
    return jsonify({
        "status" : "success!"
    }),200

if __name__ == "__main__":
    app.run(debug = True)    



         