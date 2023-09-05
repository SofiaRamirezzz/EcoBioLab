
```python
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate population dynamics using Lotka-Volterra equations
def lotka_volterra(t, params):
    x = params[0]
    y = params[1]
    alpha = params[2]
    beta = params[3]
    gamma = params[4]
    delta = params[5]

    dx_dt = alpha * x - beta * x * y
    dy_dt = delta * x * y - gamma * y

    return np.array([dx_dt, dy_dt])

# Run simulations for different parameters
# Parameter set 1
t = np.arange(0, 100, 0.1)
params1 = [10, 5, 1, 0.05, 1, 0.1]
populations1 = np.zeros((len(t), 2))

x0 = 10  # Initial population of predator
y0 = 10  # Initial population of prey

populations1[0] = [x0, y0]

# Solve differential equations using Euler's method
for i in range(1, len(t)):
    populations1[i] = populations1[i-1] + 0.1 * lotka_volterra(t[i-1], params1)

# Parameter set 2
params2 = [10, 5, 0.5, 0.1, 2, 0.2]
populations2 = np.zeros((len(t), 2))

populations2[0] = [x0, y0]

# Solve differential equations using Euler's method
for i in range(1, len(t)):
    populations2[i] = populations2[i-1] + 0.1 * lotka_volterra(t[i-1], params2)

# Plot population dynamics
plt.figure(figsize=(10, 5))
plt.plot(t, populations1[:, 0], label="Predator")
plt.plot(t, populations1[:, 1], label="Prey")
plt.plot(t, populations2[:, 0], label="Predator (Different Parameters)")
plt.plot(t, populations2[:, 1], label="Prey (Different Parameters)")
plt.xlabel("Time")
plt.ylabel("Population")
plt.title("Lotka-Volterra Model")
plt.legend()
plt.grid(True)
plt.show()
```
