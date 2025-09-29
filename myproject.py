import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-2*np.pi, 2*np.pi, 1000)

def generate_sine(f, A):
    return A*np.sin(2*np.pi*f*t)

# def generate_square():

# def triangular

# def sawtooth
def generate_unit_step(t0, A):
    return np.where(t>=t0, A, 0)

def generate_unit_impulse(t0):
    return np.where(t==t0, 1, 0)


# TESTING OUT THE FUNCTIONS

plt.plot(t, generate_sine(1/(2*np.pi), -1))
plt.title("Sine Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

plt.plot(t, generate_unit_step(1, 1))
plt.title("Unit Step Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
        
plt.plot(t, generate_unit_impulse(0))
plt.title("Unit Impulse Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# OPERATIONS ON FUNCTIONS

# perform operationson signald and plot them (time shifcting, tie scafling, addition, multiplication)
# (optional) Compute and plot the Fourier series and Fourier transform of signals