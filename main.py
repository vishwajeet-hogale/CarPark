from flask import Flask,render_template,redirect,url_for,flash,request
import Allotment as almnt
import Parking as pk
app = Flask(__name__)


def get_all_parking_details():
    list1 = list(almnt.alloted_big.values())
    
    list2 = list(almnt.alloted_small.values())
    print(list2)
    data = [(i.parking_no,i.vehicle_number,i.type_vehicle,i.entry) for i in list1+ list2]
    return data 

@app.route("/")
def index():
    data = get_all_parking_details()
    
    return render_template("index.html",pet = data)

@app.route("/add",methods = ["POST","GET"])
def add():
    if request.method == "POST":
        v_no = request.form['vehicle_number']
        v_type = request.form["Type"]
        obj = pk.Parking(v_type,v_no)
        pk.get_slot(obj)
        print(almnt.alloted_small)
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)