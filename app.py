from flask import Flask,render_template
app=Flask("app")


@app.route("/")
def index():
    return render_template("index.html",product={"name1":"انواع ست قندساب","name2":"انواع ست بله برون","name3":"انواع دفتر قباله و قران"})

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

app.run()