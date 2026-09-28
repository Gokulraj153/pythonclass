
# Local scope

# def localScope():
#     msg = "Good evening"
#     print(msg,"Inside the function")

# localScope()
# print(msg,"Outside the function")



# Global scope

msg = "Good morning"
def globalScope():
    print(msg,"inside the function")
globalScope()
print(msg,"outside the function")

# enclosing 

def outerFun():
    department = "CSE"
    def innerFun():
        print(department,"outer fun variable")
    innerFun()

outerFun()
# print(department,"outer fun variable")