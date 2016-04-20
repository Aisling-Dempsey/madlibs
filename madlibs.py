from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']
MADLIBS = ["madlib1.html", "madlib2.html", "madlib3.html", "madlib4.html", "madlib5.html"]

@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)
@app.route('/game')
def show_game_form():

    response = request.args.get("game")

    if response == 'no':
        return render_template('goodbye.html')
    else:
        return render_template('game.html')

@app.route('/madlib')
def show_madlib():
    name = request.args.get("person")
    shade = request.args.get("color")
    thing = request.args.get("noun")
    dudes = request.args.getlist("animal")
    descriptor = request.args.get("adjective")
    if len(dudes) > 1:
        if len(dudes) > 2:
            for i in range(len(dudes)-1):
                dudes[i] = dudes[i] + ", "
        dudes[-1] = "and " + dudes[-1]
    return render_template(choice(MADLIBS),
                            person=name,
                            color=shade,
                            noun=thing,
                            adjective=descriptor,
                            animals=dudes)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
