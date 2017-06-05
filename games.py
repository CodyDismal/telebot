from user_operations import *
from random import randrange

class Casino:
    def __init__(self, bot):
        pass

class Math_game:
    actions_list = ["+", "-", "*"]
    def __init__(self, a):
        self._type = "math_game"
        self._a = randrange(0,100)
        self._b = randrange(0,100)
        self._action = self.actions_list[randrange(0,2)]
        self._string = "{0} {1} {2}".format (self._a, self._action, self._b)
        self._ans = eval(self._string)
        a.action = "Game"
        save_user(a)

    def get_req_string(self):
        return ("{0} = ?".format(self._string))

    def is_correct(self, numb):
        if (int(numb) == int(self._ans)):
            return True
        else:
            return False