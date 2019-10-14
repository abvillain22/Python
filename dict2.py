# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:36:19 2019

@author: abvil
"""

st={"name":"abhay"}
temp=st.values()
st.values=st.keys()
st.keys=temp
print(st)