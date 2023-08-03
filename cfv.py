import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors

# Complex Functions
def f1(z):
    return z**2

def f2(z):
    return z**3 - z

def f3(z):
    return np.sin(z)

def f4(z):
    return (1/z)

def f5(z):
    return np.log(z)


# Visualizes complex function 
# f: C -> C
# with W = f(Z)
def visualize(f, x_lower, x_upper, y_lower, y_upper):
    
    x = np.linspace(x_lower, x_upper, 100)
    y = np.linspace(y_lower, y_upper, 100)
    X, Y = np.meshgrid(x, y)
    
    Z = X + (Y*1j)  #domain
    W = f(Z) #image

    re_image = np.real(W)
    im_image = np.imag(W)

    # Create a 3D surface plot
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(projection='3d')
    
    im_image_normalizer = im_image - im_image.min()
    im_image_normalizer /= im_image.max()
    # Heat map
    ax.plot_surface(np.real(Z), np.imag(Z), re_image, facecolors=plt.cm.plasma(im_image_normalizer), cmap='plasma')
    
    # Color bar key
    m = cm.ScalarMappable(cmap=plt.cm.plasma)
    m.set_array([])
    plt.colorbar(m, label="Color Scale (Im image)", orientation = "horizontal")
    
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.set_zlabel('Re (image)')
    
    ax.set_title(f)
    plt.show()

    
print("Select Function for Visualization:")
print("0: z^2")
print("1: z^3-z")
print("2: sin(z)")
print("3: 1/z")
print("4: ln(z)")

while (True):   
    inp = int(input())
    
    if (inp==0):
        visualize(f1, -10, 10, -10, 10)
    elif (inp==1):
        visualize(f2, -10, 10, -10, 10)
    elif (inp==2):
        visualize(f3, -10, 10, -10, 10)
    elif (inp==3):
        visualize(f4, -10, 10, -10, 10)
    elif (inp==4):
        visualize(f5, -10, 10, -10, 10)
