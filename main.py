from flask import Flask,render_template,redirect,url_for,flash,request
import Allotment as almnt
import Parking as pk
app = Flask(__name__)
app.secret_key = "mysecretkey"

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
@app.route('/delete/Small/<int:parking_no>', methods = ['POST','GET'])
def delete_small(parking_no):
    obj = almnt.alloted_small[parking_no]
    price = obj.get_totalbill()
    print(price)
    flash('Rs. {}/-'.format(price))
    almnt.alloted_small.pop(parking_no)
    return redirect(url_for('index'))
@app.route('/delete/Big/<int:parking_no>', methods = ['POST','GET'])
def delete_big(parking_no):
    print(almnt.alloted_big)
    obj = almnt.alloted_big[parking_no]
    price = obj.get_totalbill()
    almnt.alloted_big.pop(parking_no)
    print(price)
    flash('Rs. {}/-'.format(price))
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)