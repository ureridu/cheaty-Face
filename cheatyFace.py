# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 06:12:56 2018

@author: Ureridu
"""
import sys
import inspect
from dill.source import getsource

Locals= {}

def getFunk(callerVars):
    global Locals
    print(sys._getframe().f_code.co_name)
    print(sys._getframe(1).f_code.co_name)
    caller = sys._getframe(1).f_code.co_name
    Locals[caller] = callerVars
    
#    print(getsource(eval(caller)))
    print(inspect.getsource(eval(caller)))
#    print(inspect.getsourcelines(eval(caller)))
    print(inspect.signature(eval(caller)))
    print(inspect.signature((caller)))

#    for i in range(len(callerVars)):
#        global callerVars[i]

def a(z):
    z
    aaa=5
    x='asdf'
    getFunk(locals())
    
def b():
    bbb=4
    getFunk(locals())
    
a(1)
b()

#print(inspect.signature(a))
#caller = sys._getframe(1).f_code.co_name
#print(getsource(a))
#print(inspect.getsource(b))

#print(globals())