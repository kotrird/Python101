import matplotlib.pyplot as plt

# define trapezoid parameters
base1 = 5
base2 = 8
height = 3

# plot trapezoid
x = [0, base1, base2, 0]
y = [0, height, height, 0]
plt.plot(x, y)
plt.fill_between(x, y, color='lightblue')

# calculate area of trapezoid
area = 0.5 * (base1 + base2) * height

# display area in result window
print(f"The area of the trapezoid is {area}")

# display plot
plt.show()
