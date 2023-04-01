#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def checkIfNotNumeric(*args):    
    return all((isinstance(x,(int,float))) for x in args)


def addAllNumerics(*args):
    return sum(args)

myName = "Python Course"



