from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

@app.route('/robobert/')
def robobert():
    return render_template('bot.html')

if __name__ == '__main__':
    app.run(debug=True)