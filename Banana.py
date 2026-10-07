import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("~/Downloads/Banana_delta_1.csv", sep=";", decimal=",")

X = df.copy()
X.columns = ["x", "y"]

def show_transformation(dataframes):
    plt.figure(figsize=(8,8))
    number = 1
    for dataframe in dataframes:
        plt.scatter(dataframe["x"], dataframe["y"], s=5, label=f"Dataframe {number}")
        number+=1
    plt.axis("equal")
    plt.legend()
    plt.show()

def stretch(x, a, b):
    x = x.copy()

    matrix = np.array([
        [a, 0],
        [0, b]
    ])
    print("Transformation matrix:")
    print(matrix)

    points = x[["x", "y"]].to_numpy().T
    transformed = matrix @ points

    return pd.DataFrame(transformed.T,columns=["x", "y"])


def shear(x, a, b):
    x = x.copy()

    matrix = np.array([
        [1, a],
        [b, 1]
    ])
    print("Transformation matrix:")
    print(matrix)

    points = x[["x", "y"]].to_numpy().T
    transformed = matrix @ points

    return pd.DataFrame(transformed.T, columns=["x", "y"])

def reflection(x, a, b):
    x = x.copy()

    matrix = np.array([
        [a, b],
        [b, -a]
    ])
    print("Transformation matrix:")
    print(matrix)

    points = x[["x", "y"]].to_numpy().T
    transformed = matrix @ points

    return pd.DataFrame(transformed.T, columns=["x", "y"])

def rotation(x, c):
    x = x.copy()

    matrix = np.array([
        [np.cos(c), -np.sin(c)],
        [np.sin(c), np.cos(c)]
    ])
    print("Transformation matrix:")
    print(matrix)

    points = x[["x", "y"]].to_numpy().T
    transformed = matrix @ points

    return pd.DataFrame(transformed.T, columns=["x", "y"])


X1 = stretch(X, 2, 0.5)
X2 = shear(X1, 1, 0)
X3 = rotation(X2, np.pi / 4)

Y1 = shear(X, 1, 0)
Y2 = rotation(Y1, np.pi / 4)
Y3 = stretch(Y2, 2, 0.5)

Z1 = rotation(X, np.pi / 4)
Z2 = stretch(Z1, 2, 0.5)
Z3 = shear(Z2, 1, 0)

show_transformation([X3, Y3, Z3])
# As we can see, the final result depends on the order of transformations. This proves that AB != BA.
# So even if the same transformations are used, applying them in a different order results in a different result.
# The transformation performed first acts directly on the original data,
# while each following transformation acts on the result of the previous one.