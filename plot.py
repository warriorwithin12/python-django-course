import matplotlib.pyplot as plt
import numpy as np

# An issue detected with numpy v1.19.4 with AMD processors, so downgrade to version 1.19.3
# > python -m pip install matplotlib

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
plt.show()                   # Display the plot