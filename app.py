# command for virtual environment activation:   .\venv\Scripts\activate 
# run command: python app.py
# for flask:  pip install Flask-PyMongo
# for bcrypt: pip install flask-bcrypt

from flask import Flask ,render_template,request,redirect,flash,session
from flask_pymongo import PyMongo
# from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Radiant"

mongo = PyMongo(app)
# bcrypt = Bcrypt(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/contactUs", methods=["GET"])
def contactUs():
    return render_template("contactUs.html")

@app.route("/logIn", methods=["GET"])
def logIn():
    return render_template("logIn.html")

@app.route("/product", methods=["GET"])
def product():
    return render_template("product.html")









@app.route("/orders",methods=["GET","POST"])
def orders():

    #business logic
    if request.method == "POST":
        print("it's a post call")
        
        fullName =request.form['fullName']
        email= request.form['email']
        address= request.form['address']
        city= request.form['city']
        state= request.form['state']
        zipCode= request.form['zipCode']

        # password = request.form["password"]
        
       
        cName= request.form['cName']
        cardNo= request.form['cardNo']
        expMonth= request.form['expMonth']
        expYear= request.form['expYear']

      
        mongo.db.order.insert_one(
            {
                "fullName": fullName,
                "email": email,
                "address": address,
                "city":city,
                "state":state,
                "zipCode":zipCode,
                "cName":cName,
                "cardNo":cardNo,
                "expMonth":expMonth,
                "expYear":expYear

                
                
                
                
                # "city": city,
            }
        )

     #   print(first_name,last_name, email_id, password,address,city)
    
    
        flash("User registered succesfully", "success")
        # return redirect("/login")

    return render_template("orders.html")

    # print("it's a get call")

if __name__=="__main__":
    app.secret_key = "asdkjssd"
    app.run(debug=True)