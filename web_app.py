from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/intro1")
def intro1():
    return render_template("intro1.html")

@app.route("/intro2")
def intro2():
    return render_template("intro2.html")

@app.route("/intro3")
def intro3():
    return render_template("intro3.html")

@app.route("/intro4")
def intro4():
    return render_template("intro4.html")

@app.route("/intro5")
def intro5():
    return render_template("intro5.html")

@app.route("/world_select.html")
def world_select():
    return render_template("world_select.html")

@app.route("/demo")
def demo():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(debug=True)
