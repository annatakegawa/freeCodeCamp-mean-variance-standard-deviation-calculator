import numpy as np


def calculate(list):

  if len(list) == 9:
    matrix = np.array(list).reshape(3, 3)

    calculations = {
      'mean': np.mean,
      'variance': np.var,
      'standard deviation': np.std,
      'max': np.max,
      'min': np.min,
      'sum': np.sum
    }

    for key, value in calculations.items():
      op = value
      calculations[key] = [
        op(matrix, axis=0).tolist(),
        op(matrix, axis=1).tolist(),
        op(matrix)
      ]

    return calculations

  else:
    raise ValueError('List must contain nine numbers.')
