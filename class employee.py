class employee():
    def __init__(self):
       print("Employee is called..")
    def __delete__(self):
        print("Destructor called")

def make_ob():
    print("program object to...")
    obj = make_ob()
    print("Function make_ob ends.")
    return obj

print("calling make_ob func....")
obj = make_ob()
print("program done.")
