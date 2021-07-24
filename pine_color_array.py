#/usr/bin/python3
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def interpolate_colors(c1, c2, weight=0):
    c1=np.array(mpl.colors.to_rgb(c1))
    c2=np.array(mpl.colors.to_rgb(c2))
    return mpl.colors.to_hex((1-weight)*c1 + weight*c2)

def create_gradient(color1, color2, steps):
    gradient = []
    for n in range(steps):
        gradient.append(interpolate_colors(color1, color2, n/steps))
    return gradient

def preview_gradient(gradient):
    ig, ax = plt.subplots(figsize=(8, 5))
    n = len(gradient)
    for x in range(n):
        ax.axvline(x, color=gradient[x], linewidth = 5 * (200 / n))
    plt.show()

def generate_pine_color_array(name, gradient):
    array_declaration = "var color[] " + name + " = array.new_color()\n\n"
    array_colors = ["if barstate.isfirst\n"]
    for color in gradient:
        push_str = "\tarray.push(" + name + ", " + color + ")\n"
        array_colors.append(push_str)
    array_function = "\nf_" + name + "(_idx) => array.get(id=" + name + ", index=_idx)"
    return ''.join([array_declaration, ''.join(array_colors), array_function])

# Usage:
#c1='white'
#c2='green'
#n=100
#gradient = create_gradient(c1, c2, n)
#pine_code = generate_pine_color_array("grayscale", gradient)
#print(pine_code)
