import pickle
import os

class Animal:
    """Animal class"""
    def __init__(self, id):
        self.id = id
        self.name = "Cat"
        self.food = 30.0
        self.water = 100.0
        self.power = 100.0
        self.fun = 100.0
        self.money = 100.0
        self.action = None
        self.last_action_time = None
        self.last_action = None
    def set_la_time (self, time):
        self.last_action_time = time

        
def create_new_user(id):
    print ("Created new user")
    a = Animal(id)
    with open("saves/{0}.save".format(id), 'wb') as f:
        pickle.dump(a, f)
    return a

def load_user(id):
    print ("Loaded user")
    if (os.path.isfile("saves/{0}.save".format(id))): 
        with open("saves/{0}.save".format(id), 'rb') as f:
            a = pickle.load(f)
        return a
    else:
        return -1
        
def save_user(obj):
    print ("Saved user")
    obj.food = round(obj.food, 1)
    obj.water = round(obj.water, 1)
    obj.power = round(obj.power, 1)
    obj.money = round(obj.money, 1)
    with open("saves/{0}.save".format(obj.id), 'wb') as f:
        pickle.dump(obj, f)

def remove_user(obj):
    os.remove("saves/{0}.save".format(obj))

