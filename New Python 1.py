import numpy as np

x = np.random.random((64, 3, 32, 10))
n = np.array(
    [[[1, 2], [5, 6], [7, 8]],
     [[5, 2], [5, 6], [7, 8]]]

)
f = np.array([[2, 3],
              [1, 2]])
z = np.array([4, 5])
b = np.dot(f, z)
print(b)
import keras
import pandas

print(pandas.__version__)
import dask

print(dask.__version__)
print(keras.datasets)
