# defining a blueprint for objects 
class student:
    # lets overwrite the construtor function init
    #its a duner?Magic method always start with __
    def __init__(self):
        print("Hey I am a constructor")


obj1 = student() #when the object is created it gets memory and construtor is also get called.




