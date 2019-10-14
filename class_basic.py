# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:52:57 2019

@author: abvil
"""

class Employee:
    raise_ammount=1.04
    no+of_emp=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first.lower()+"."+last.lower()+"@gmail.com"
        Employee.no_of_emp+=1
        
    def fullname(a):
        return "the full name of employee is {} {}".format(a.first,a.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_ammount)
        
    @classmethod
    def set_raise_amt(cls,ammount):
        cls.raise_ammount=ammount
    
emp_1=Employee("Aman","Sharma",5000)
emp_2=Employee("Yogendra","Singh",6000)
print(Employee.raise_ammount)
Employee.set_raise_ammount(1.05)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.fullname())
print(emp_2.fullname())