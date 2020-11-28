from flask import Flask, request, render_template, redirect, flash, jsonify, session
from boggle import Boggle

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool"

boggle_game = Boggle()

@app.route('/')
def create_board():
    """
    Root Route that creates game board 
    and stores it in session
    """
    board = boggle_game.make_board()
    session["board"] = board

    return render_template('index.html', board=board)

@app.route('/check-answer')
def check_answer():
    """
    Checks if the submitted word is on
    gameboard
    """
    word = request.args["word"]
    board = session["board"]
    
    return jsonify(
        {'result':boggle_game.check_valid_word(board, word)}
    )

@app.route('/num-plays', methods=['POST'])
def calculate_plays():
    """
    Stores highest score and
    number of times user has played to
    session
    """ 

    score = request.json["score"]

    session["count"] = session.get("count", 0) + 1
    highest_score = session.get("highest_score", 0)

    if score > highest_score:
        highest_score = score
    
    session["highest_score"] = highest_score
    
    return jsonify(highest_score)
