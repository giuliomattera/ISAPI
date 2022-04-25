import numpy as np

def my_first_function(A, THR):
    c = 0
    for i in range(0, 10, 1):
        c = A + i
        if c > THR:
            print('Il risultato della somma e ', c)
            break
        else:
            print('Il risultato non è corretto, siamo all iterazione ', i)
    
    return c

def altro():
    print('Posso fare altre cose')
    

def random_matrix(size):
    A = np.ones(size, dtype = np.float32)
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            A[i,j] = np.random.rand(1)
            
    return A
