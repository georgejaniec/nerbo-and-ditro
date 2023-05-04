from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  return render_template('index.html')


@app.route("/register")
def register():
  return render_template('register.html')


@app.route("/login")
def login():
  return render_template('login.html')


@app.route("/criteria")
def criteria():
  return render_template('criteria.html')


@app.route("/gallery")
def gallery():
  return render_template('gallery.html')


@app.route("/grasps")
def grasps():
  return render_template('grasps.html')


@app.route("/samples")
def samples():
  return render_template('samples.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
