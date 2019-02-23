from flask import Flask
from movies_tools import *
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>{} movies recorded</h1>".format(str(len(row_lst)))

@app.route("/movies/ratings")
def random_five_movies():
    movie_var_1 = Movie(row_lst[random.randint(1,len(row_lst))])
    movie_var_2 = Movie(row_lst[random.randint(1,len(row_lst))])
    movie_var_3 = Movie(row_lst[random.randint(1,len(row_lst))])
    movie_var_4 = Movie(row_lst[random.randint(1,len(row_lst))])
    movie_var_5 = Movie(row_lst[random.randint(1,len(row_lst))])
    return movie_var_1.get_name_rating() + movie_var_2.get_name_rating() + movie_var_3.get_name_rating() + movie_var_4.get_name_rating() + movie_var_5.get_name_rating()


@app.route("/movies/ratings/<score>")
def score_mov(score):
    mov_filter = MovieFilter(row_lst,score)
    return mov_filter.filter()
