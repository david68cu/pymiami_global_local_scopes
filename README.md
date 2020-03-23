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

  locals() will
  


### References

1- [W3 school Pyhton](https://www.w3schools.com/python/python_scope.asp)
2- [Gloabs vs Locals](https://stackoverflow.com/questions/52310792/python3-globals-and-locals-contents)

