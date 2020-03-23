# Undesrating Python scope

## local vs global

 - globals() refers to the current modules' attribute dictionary. 
 - locals() refers to the current local variables in your function/code-snippet.

 - Setting a variable will only ever change locals(). (Unless you tell python otherwise using the global or nonlocal keyword.)

At the begining of a script without any declaration of variable  

ex1_local.py


## Local Scopes

- ex1_local.py , ex2_local.py

  A variable created inside a function is available inside that function:
  However the values of gloabls() and locals() will depend on what point will you call both functions
  See ex1_local.py  and ex2_local.py


- ex3_local.py 

  The content of locals and globals will depend on where you call them.
  ex3_local.py  example will show that the content of globals() will be the same to locals() in some points 
  Also locals() will autoupdate each time we created new local() scope variables in function or classes
  
-ex5_locals_vs_globals.py

  Variabes created outside  a functions are globals
  Variables created inside a functions are locals
   A variable created outside of a function is global and can be used by anyone
  
- ex6_globals

   If you use the global keyword, the variable belongs to the global scope



### References

1- [W3 school Pyhton](https://www.w3schools.com/python/python_scope.asp)
2- [Gloabs vs Locals](https://stackoverflow.com/questions/52310792/python3-globals-and-locals-contents)

