import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import tensorflow as tf
from sklearn.metrics import confusion_matrix
import seaborn as sn
import pandas as pd
import time

def xslx_2_numpy(PATH, VAL_SIZE=0.2, TEST_SIZE=0.3):
    '''
    Dati organizzati in modo tale che nell'ultima colonna ci sono
    le etichette
    
    '''
    
    df = pd.read_excel(PATH, header = None)
    data = df.to_numpy()
    data = data[1:,0:13]
    labels = data[:,12]
    data = data[:,0:13]
    print('[INFO] Splitting training, validation and test data.......')
    X_train, X_val, y_train, y_val = train_test_split(data, labels, \
                                                    test_size=VAL_SIZE, 
                                                    random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(data, labels, \
                                                    test_size=TEST_SIZE, 
                                                    random_state=42)
        
    Data_struct ={'Train data':X_train,'Train labels':y_train, 
                  'Validation data':X_val, 'Validation labels':y_val,
                  'Test data':X_test, 'Test labels':y_test}
    
    print('[INFO] Casting and reshaping....')
    #Estrazione dal dizionario e casting
    x = Data_struct['Train data'].astype(np.float32)
    y = Data_struct['Train labels'].astype(np.int32)

    x_val = Data_struct['Validation data'].astype(np.float32)
    y_val = Data_struct['Validation labels'].astype(np.int32)

    x_t = Data_struct['Test data'].astype(np.float32)
    y_te = Data_struct['Test labels'].astype(np.int32)

    y = y.reshape(y.shape[0], 1)
    y_val = y_val.reshape(y_val.shape[0], 1)
    y_te = y_te.reshape(y_te.shape[0], 1)
     
    #del Data_struct, X_train, X_val, y_train, X_test, y_test

    return x,y, x_val, y_val, x_t, y_te

def module_error(x):
    e_1 = (x[:,10]-x[:,11])/x[:,10] #dv
    e_2 = (x[:,0]-x[:,4])/x[:,0] #dI min
    e_3 = (x[:,1] - x[:,6])/x[:,1] #dI max
    e_4 = (x[:,7]-x[:,7])/x[:,8] # dV
    
    error = np.array([e_1, e_2, e_3, e_4]).T
    #error = error.reshape(error.shape[0], error.shape[1], 1)
    return error

def check_NaN(dati):
    idx = []
    for i in range(dati.shape[0]):
        a = np.isnan(dati[i,:])
        for j in range(a.shape[0]):
            if a[j]:
                idx.append([i,j])
    if len(idx) == 0:
        print('No NaN found')
        del idx
    else:
        print('Nan found, see idx tuple for index')

    del i, j, a

def error_values(x, x_val):

    #Valutazione degli errori rispetto alle WPS
    print('[INFO] Error computing for training samples....')
    error_t = module_error(x).astype(np.float32)
    print('[INFO] Cheking presence of Nan in training set...')
    check_NaN(error_t)
    print('[INFO] Error computing for validation samples....')
    error_v = module_error(x_val).astype(np.float32)
    check_NaN(error_v)
    print('[INFO] Cheking presence of Nan in validation set...')

    return error_t, error_v

def testing(model, x_t, y_t):
    print('[INFO] Running predictions....')
    start = time.time()
    error_te = module_error(x_t).astype(np.float32)
    y_te = model.predict(error_te)
    for i in range(y_t.shape[0]):
        if y_te[i] >= 0.5:
            y_te[i] = 1
        else:
            y_te[i] = 0 

    print('Computational time is ', (time.time()-start)*1000, ' milliseconds')
    del start, error_te
    #  Risultato finale
    print('[INFO] Plotting confusion matrix and testing accuracy.....')
    A = confusion_matrix(y_te, y_t)
    df_cm = pd.DataFrame(A)
    sn.set(font_scale = 1.4)
    sn.heatmap(df_cm, annot=True)
    accuracy = 0; i =0
    for i in range(A.shape[0]):
        accuracy = accuracy + A[i,i]
    del i
    accuracy = accuracy/y_te.shape[0]*100

    print('[INFO] The accuracy of model is  ', accuracy)