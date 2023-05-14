import matplotlib.pyplot as plt
import numpy as np

# Load the training history data
history = np.loadtxt('./logs/test_training_history.csv', delimiter=',', skiprows=1)

# Extract the relevant columns
epochs = history[:, 0]
loss = history[:, 1]
yval = history[:, 2]


# Create the figure and axes
fig, ax = plt.subplots(1, 2, figsize=(15, 6))

# Plot the loss
color = 'tab:blue'
ax[0].semilogy(epochs, loss, color=color)
ax[0].set_xlabel('$n_{epoch}$')
ax[0].set_ylabel('Loss')
ax[0].set_title('Loss')

# Plot the value y=u(0,x)
ax[1].plot(epochs, yval, color=color)
ax[1].set_xlabel('$n_{epoch}$')
ax[1].set_ylabel('$y=u(0,x)$')
ax[1].set_title('Value $u(0,x)$')

plt.savefig('logs/stats_plot( Burgers_Type_Equation ).png')

# Show the plot
plt.show()

