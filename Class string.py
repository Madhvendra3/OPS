class IOString():
    def __init__(self):
        self.str = ""
    def get_string(self):
        self.str = input("enter string: ") 
    def print_string(self):
        print("Result is: ",self.str.upper())      
str = IOString()
str.get_string()
str.print_string()        