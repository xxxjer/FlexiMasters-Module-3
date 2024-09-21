from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
# GET = We are now in backend. Get information from frontend 
# POST = Retrieve information from backend to frontend
# Direction will change depending on whether we are in backend or frontend
# @ is like a decorator. With @, the code app.route will run first before render template
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run()
