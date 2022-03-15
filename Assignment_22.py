#!/usr/bin/env python
# coding: utf-8
1. What is the result of the code, and explain?

>>> X = 'iNeuron'

>>> def func():

print(X)


>>> func()
# The output of the code is 'ineuron'.
# 
# The string X is defined at the global level and its value can be accessed inside the function func(), so the value of x is printed

# In[ ]:





2. What is the result of the code, and explain?


>>> X = 'iNeuron'
>>> def func():
X = 'NI!'


>>> func()
>>> print(X)

# The output of the code is 'ineuron'.
# 
# X='iNeuron' is defined at the global level and inside the function func() there is a local variable with the same name X and is assgned to 'NI!' and the scope of this local variable is within the function. So when func() is called before print statement,
# the local variable X is assigned with 'NI! and when the function execution is done, local variable does not exist. 
# 
# When print(X) is executed, it prints the string 'iNeuron'

# In[ ]:




3. What does this code print, and why?


>>> X = 'iNeuron'
>>> def func():
X = 'NI'
print(X)


>>> func()
>>> print(X)
# The result is:
# NI
# iNeuron
# 
# when func() is called, it prints NI which is the value assigned to the local variable X of the function func().
# 
# When print(X) is executed, it prints iNeuron which is the value assigned to the global variable X

# In[ ]:





4. What output does this code produce? Why?


>>> X = 'iNeuron'
>>> def func():
global X
X = 'NI'


>>> func()
>>> print(X)
# The ouput is NI
# 
# The value of the global variable can be modified inside the function by using the global keyword.
# 
# So, when func() is called, the global variable X is changed from 'iNeuron' to 'NI'. When print(X) is executed, it prints the value of X which is NI

# In[ ]:




5. What about this code—what’s the output, and why?


>>> X = 'iNeuron'
>>> def func():
X = 'NI'
def nested():
print(X)
nested()


>>> func()
>>> X
# The ouput is:
#     
# NI
# 
# iNeuron
# 
# Local variable X defined inside the func() function can be accessed inside the nested function nested() of function func(). So, when 
# func() is called, X is assgned with 'NI' and nested function is called inside the function func and nested function prints 'NI'.
# When the last statement X is executed, it prints the value of global varibale X which is 'iNeuron'.

# In[ ]:




6. How about this code: what is its output in Python 3, and explain?


>>> def func():
X = 'NI'
def nested():
nonlocal X
X = 'Spam'
nested()
print(X)


>>> func()
# The output is:
# 
# Spam
# 
# The nonlocal keyword is used to work with the variables inside the nested function and it tells that the variable is not local for the nested function. 
# 
# When func() is called, it assigns the value 'NI' to its local variable X and then it calls nested function which access local variable of the function func() using nonlocal keyword and modifies the value to the 'Spam'. So when print(x) is executed, it prints 'Spam'. 
# 

# In[ ]:




