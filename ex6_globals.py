"""
 If you use the global keyword, the variable belongs to the global scope
"""

def myfunc():
    print("at the start locals =", locals())  # locals is empty {}
    global x
    print("at the start globals =", globals())
    x = 300
    print("at the end locals =", locals())  # locals is still empty {}
    print("at the end globals =", globals())  # globals contains 'x': 300


myfunc()
print(x)  # as globals contains # globals contains 'x': 300 we can print it from here


"""
To change the value of a global variable inside a function, refer to the variable by using the global keyword
"""


y = 788


def myfunc():
    global y  # From now on we are refering to the global y
    y = 199  # Set the global y to 199


myfunc()
print(y)
