"""
Python does not require you to declare variables but assumes that a varviable assigned
in the body of a function is local.

Better than Javascript that does not require varaible decalrarion, but if you forget to decalre
that variable was local, you may clover a global varaible without knowing it

IN below example at compilation time Python sees print(b) . So Python decides that b is local at compilation time
At run time, when we call f2(3) Pytons print(a) , 3, and then when looking for the local bound value of b fails

Lucioano Fluent Python Chapter 7 page 96

We can see the bycode of this function below to verify that that is what happened
Coment the call to the function f2(3) and use dis

Read Lucioano Fluent Python Chapter 7 page 96 to solve this issue and see Clousres , global , nonlocal and free vars
"""

from dis import dis

b=6
def f2(a):
    print(a)
    print(b)
    b = 9

# f2(3)

# Output
"""
3

Traceback (most recent call last):
  File "ex7_variable_scopes.py", line 16, in <module> f2(3)
  File "ex7_variable_scopes.py", line 13, in f2  print(b)
"""

dis(f2)
"""
 20           0 LOAD_GLOBAL              0 (print)
              2 LOAD_FAST                0 (a)
              4 CALL_FUNCTION            1
              6 POP_TOP

 21           8 LOAD_GLOBAL              0 (print)
             10 LOAD_FAST                1 (b)
             12 CALL_FUNCTION            1
             14 POP_TOP

 22          16 LOAD_CONST               1 (9)
             18 STORE_FAST               1 (b)
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE

"""






