import random
from datetime import datetime
import Allotment as almnt
from flask import Flask,render_template,redirect,url_for,flash,request
"""
50 slots  for cars,tempos,bus
100 slots for bikes 
""" 

class Parking(): #Parking class. Each object represents a parking slot
    
    parking_no = -1
    def __init__(self,vehicle_type,vehicle_number):
        # self.parking_no = int(random.randint(0,50))
        self.type_vehicle = vehicle_type
        self.vehicle_number = vehicle_number
        self.entry = datetime.now()
        print(self.vehicle_number)
    # def get_slot(self,typev):
    #     self.parking_no = int(random.randint(0,50))
    #     while not(self.parking_no not in almnt.small and self.parking_no not in almnt.big):
    #         random.shuffle()
    #         self.parking_no = int(random.randint(0,50))
        
    #     if(typev=="small" or typev == "Small"):
    #         almnt.alloted_small[self.parking_no] = self.vehicle_number
    #         almnt.small.remove(self.parking_no)
    #     elif(typev=="big" or typev == "Big"):
    #         almnt.alloted_big[self.parking_no] = self.vehicle_number
    #         almnt.big.remove(self.parking_no)
            
       

    def get_exit_time(self):
        return datetime.now()
    def get_difference_time(self,entry):
        try:
            diff = self.get_exit_time() - entry
            
            return divmod(diff.total_seconds(),60)[0]
        except:
            print("Error in get_difference_time")
    def get_totalbill(self):
        total_time = int(self.get_difference_time(self.entry))
        print(total_time)
        price = 10
        price += int(total_time/60)*20
        print(price)
        return price
    # def add_to_stack(self,type):
    #     if(self.type_vehicle == "small" or self.type_vehicle == "Small"):
    #         small.append()
    



    
def get_slot(obj):
        obj.parking_no = int(random.randint(0,50))
        while (obj.parking_no not in almnt.small and obj.parking_no not in almnt.big):

            obj.parking_no = int(random.randint(0,50))
        
        if(obj.type_vehicle=="small" or obj.type_vehicle == "Small"):
            print(obj.parking_no)
            almnt.alloted_small[obj.parking_no] = obj
            almnt.small.remove(obj.parking_no)
        elif(obj.type_vehicle=="big" or obj.type_vehicle == "Big"):
            almnt.alloted_big[obj.parking_no] = obj
            almnt.big.remove(obj.parking_no)
        else:
            flash("Please enter small or big!")

        
