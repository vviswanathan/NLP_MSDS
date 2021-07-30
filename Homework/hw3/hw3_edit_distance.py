# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:38:35 2019

@author: anant
"""


# To find the edit distance between my name and nickname; My legal first name is Anantharam and nickname is Anthu
import Levenshtein as lv

Str1 = "trial"

Str2 = "trail"

Distance = lv.distance(Str1.lower(), Str2.lower())

print("The edit distance between trial and trail is :", Distance)

Ratio = lv.ratio(Str1.lower(), Str2.lower())

print("The ratio between the names is:", Ratio)
