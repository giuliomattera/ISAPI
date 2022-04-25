#!/usr/bin/env python3
"""
Codice sviluppato da:
Il giorno :
    
proprietà intellettuale di:
    
Questo codice fa bla,bla

"""

import MyLibrary as nik
import numpy as np

M = nik.random_matrix((3,3))
mean = M.mean()
if mean > 1:
    print('TO DO')
else:
    print('exit')

Z = np.zeros((3,1))

R = np.dot(M, Z)

print(np.linalg.inv(M))

import pandas as pd

df = pd.read_csv("./datastets/Automobile_data.csv")

A = df["wheel-base"]
B = df["length"]
A = A.to_numpy()
B = B.to_numpy()

C = np.array([A, B]).T