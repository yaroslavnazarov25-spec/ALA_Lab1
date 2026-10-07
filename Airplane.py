import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot_off (vertices, faces) :
    fig = plt. figure(figsize= (8, 8))
    ax = fig. add_subplot (111, projection='3d')
    mesh = Poly3DCollection([vertices[face] for face in faces],
    alpha=0.3, edgecolor='k')
    ax.add_collection3d(mesh)
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], s=2, c='r')
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.auto_scale_xyz(vertices[:, 0], vertices[:, 1], vertices[:, 2])
    plt.show()

def read_off (filename: str):
    with open(filename, "r") as f:
        if 'OFF' != f.readline().strip():
            raise ValueError('Not a valid OFF header')
        n_verts, n_faces, _ = map(int, f.readline(). strip(). split())
        verts = [list(map(float, f.readline().strip().split())) for _ in range (n_verts) ]
        faces = [list(map(int, f.readline().strip().split()[1:])) for _ in range (n_faces) ]
    return np.array(verts), faces

vertices, faces = read_off("/Users/yaroslav/Desktop/archive/ModelNet40/airplane/test/airplane_0725.off")

def rotate_xy(x, c):
    x = x.copy()

    matrix = np.array([
        [np.cos(c), -np.sin(c), 0],
        [np.sin(c),  np.cos(c), 0],
        [0,          0,         1]
    ])
    print("Transformation matrix:")
    print(matrix)

    points = x.T
    transformed = matrix @ points

    return transformed.T


def rotate_yz(x, c):
    x = x.copy()

    matrix = np.array([
        [1, 0,          0],
        [0, np.cos(c), -np.sin(c)],
        [0, np.sin(c),  np.cos(c)]
    ])
    print("Transformation matrix:")
    print(matrix)

    points = x.T
    transformed = matrix @ points

    return transformed.T


def rotate_xz(x, c):
    x = x.copy()

    matrix = np.array([
        [ np.cos(c), 0, np.sin(c)],
        [ 0,         1, 0        ],
        [-np.sin(c), 0, np.cos(c)]
    ])
    print("Transformation matrix:")
    print(matrix)

    points = x.T
    transformed = matrix @ points

    return transformed.T

angle_45_deg = np.pi / 4

X_xy = rotate_xy(vertices, angle_45_deg)
X_yz = rotate_yz(vertices, angle_45_deg)
X_xz = rotate_xz(vertices, angle_45_deg)

plot_off(X_xy, faces)
plot_off(X_yz, faces)
plot_off(X_xz, faces)

X1 = rotate_xy(vertices, angle_45_deg)
X2 = rotate_yz(X1, angle_45_deg)
X3 = rotate_xz(X2, angle_45_deg)

plot_off(X3, faces)

R_xy = np.array([
    [np.cos(angle_45_deg), -np.sin(angle_45_deg), 0],
    [np.sin(angle_45_deg),  np.cos(angle_45_deg), 0],
    [0, 0, 1]
])
R_yz = np.array([
    [1, 0, 0],
    [0, np.cos(angle_45_deg), -np.sin(angle_45_deg)],
    [0, np.sin(angle_45_deg),  np.cos(angle_45_deg)]
])
R_xz = np.array([
    [np.cos(angle_45_deg), 0, np.sin(angle_45_deg)],
    [0, 1, 0],
    [-np.sin(angle_45_deg), 0, np.cos(angle_45_deg)]
])

matrix = R_xz @ R_yz @ R_xy
print("Overall transformation matrix:")
print(matrix)