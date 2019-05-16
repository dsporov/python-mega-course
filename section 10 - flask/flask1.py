from flask import Flask, render_template

app=Flask(__name__)

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/')
def home():
#    return "Hi there!"
    return render_template("home.html")

print __name__

if __name__=="__main__":
    app.run(debug=True)


