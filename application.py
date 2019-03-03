from flask import Flask, flash, redirect, render_template, request, url_for
import cs50
app = Flask(__name__)
#####IT ACTUALLY WORKSS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=='POST':
        yes=0
        no=0

        forced=request.form["forced"]
        if forced=="one":
            no=no+1
        elif forced=="two":
            no=no+1
        elif forced=="three":
            no=no+1
        else :
            yes=yes+1
        if no==0:
            return redirect(url_for("pagetwo"))
            print("all are right")
        else:
            return render_template("no.html")
            print("sojme mistakes")

    else:
        return render_template("index.html")
@app.route("/pagetwo", methods=["GET", "POST"])
def pagetwo():
    if request.method=='POST':
        yes=0
        no=0
        sumforce=request.form["sumforce"]
        if sumforce=="one":
            no=no+1
        elif sumforce=="two":
            no=no+1
        elif sumforce=="three":
            no=no+1
        else :
            yes=yes+1
        if no==0:
            return redirect(url_for("pagethree"))
            print("all are right")
        else:
            return render_template("notwo.html")
            print("sojme mistakes")

    else:
        return render_template("pagetwo.html")

@app.route("/pagethree", methods=["GET", "POST"])
def pagethree():
    if request.method=='POST':
        yes=0
        no=0
        sumtorque=request.form["sumtorque"]
        if sumtorque=="one":
            no=no+1
        elif sumtorque=="two":
            no=no+1
        elif sumtorque=="three":
            no=no+1
        else :
            yes=yes+1
        if no==0:
            return redirect(url_for("pagefour"))
            print("all are right")
        else:
            return render_template("nothree.html")
            print("sojme mistakes")

    else:
        return render_template("pagethree.html")

@app.route("/pagefour", methods=["GET", "POST"])
def pagefour():
    if request.method=='POST':
        yes=0
        no=0

        combo=request.form["combo"]
        if combo=="one":
            no=no+1
        elif combo=="two":
            no=no+1
        elif combo=="three":
            no=no+1
        else :
            yes=yes+1
        if no==0:
            return redirect(url_for("pagefive"))
            print("all are right")
        else:
            return render_template("nofour.html")
            print("sojme mistakes")

    else:
        return render_template("pagefour.html")

@app.route("/pagefive", methods=["GET", "POST"])
def pagefive():
    if request.method=='POST':
        yes=0
        no=0

        accel=request.form["accel"]
        if accel=="one":
            no=no+1
        elif accel=="two":
            no=no+1
        elif accel=="three":
            no=no+1
        else :
            yes=yes+1
        if no==0:
            return redirect(url_for("pagesix"))
            print("all are right")
        else:
            return render_template("nofive.html")
            print("sojme mistakes")

    else:
        return render_template("pagefive.html")
@app.route("/pagesix", methods=["GET", "POST"])
def pagesix():
    if request.method=='POST':
        yes=0
        no=0
        alpha=request.form["alpha"]
        if alpha=="one":
            no=no+1
        elif alpha=="two":
            no=no+1
        elif alpha=="three":
            yes=yes+1
        else:
            no=no+1

        if no==0:
            return redirect(url_for("pageseven"))
            print("all are right")
        else:
            return render_template("nosix.html")
            print("sojme mistakes")

    else:
        return render_template("pagesix.html")
@app.route("/pageseven", methods=["GET", "POST"])
def pageseven():
    if request.method=='POST':
        yes=0
        no=0
        tension=request.form["tension"]
        if tension=="one":
            yes=yes+1
        elif tension=="two":
            no=no+1
        elif tension=="three":
            no=no+1
        else:
            no=no+1

        if no==0:
            return redirect(url_for("yes"))
            print("all are right")
        else:
            return render_template("noseven.html")
            print("sojme mistakes")

    else:
        return render_template("pageseven.html")


@app.route("/yes", methods=["GET", "POST"])
def yes():
    return render_template("yes.html")

@app.route("/no", methods=["GET", "POST"])
def no():
    if request.method=='POST':
        return redirect(url_for('index'))
    else:
        return render_template("no.html")
@app.route("/solution")
def solution():
    return render_template("solution.html")
