import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# plt.plot(x,y_sin)
# plt.plot(x,y_cos)
# plt.xlabel('x axis label')
# plt.ylabel('y axis label')
# plt.title('Since and Cosine')
# plt.legend(['Sine','Cosine'])
# plt.show()

plt.subplot(2,1,1)

# Make the first plot
plt.plot(x, y_sin)
plt.title('Sine')

# Set the second subplot as active, and make the second plot.
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')

# Show the figure.
plt.show()