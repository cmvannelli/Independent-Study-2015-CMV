# -*- coding: utf-8 -*-
"""
Claire Vannelli
Python Coding Challenge #1
Feb 23, 2015

"""
class Athlete:
    def __init__(self, kind = "rower"):
        self.kind = kind
        
    def whatKind(self):
        return self.kind

def main():
    Rower = Athlete()
    Triathlete = Athlete('Triathlete')
    Soccer_Player = Athlete('Soccer Player')
    Swimmer = Athlete('Swimmer')
    Runner = Athlete('Runner')
    Ballet_Dancer = Athlete('Ballet Dancer')
    print("Which Athlete will you be?")
    print(Triathlete.whatKind())
    print(Soccer_Player.whatKind())
    print(Swimmer.whatKind())
    print(Runner.whatKind())
    print(Ballet_Dancer.whatKind())
    print("Let's do some numerical comparisons!")
    numbers()
    
def numbers():
    a, b, c = 0, 1, 5
    print('a = {}, b = {} and c = {}'.format(a, b, c))
    s = "a less than b" if a < b else "a not less than b" 
    print(s)
    t = "b less than c" if b < c else "b not less than c"
    print(t)
    w = "c less than a" if c < a else "c not less than a"
    print(w)
    
    
if __name__ == "__main__": main()
    
