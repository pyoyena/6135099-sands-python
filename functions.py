import numpy as np
import matplotlib.pyplot as plt


# define functions that generate sine wave and time shifts it

def generate_sine(f, A, T=2*np.pi):
    t = np.linspace(0, T, 1000)
    y = A*np.sin(2*np.pi*f*t)
    return t, y

def sine_time_shifting(f, A, shift,T=2*np.pi):
    t = np.linspace(0, T, 1000)
    y = A*np.sin(2*np.pi*f*(t-shift))
    return t, y

def sine_time_scaling(f, A, scale, T=2*np.pi):
    t = np.linspace(0, T, 1000)
    y = A*np.sin(2*np.pi*f*(t*scale))
    return t, y



# define functions that generate unit step wave and tie scales it

def generate_unit_step(t0, A, T=2*np.pi):
    t = np.linspace(0, T, 1000)
    y = np.where(t >= t0, A, 0)    # if t>=t0 gives A, otherwise 0
    return t, y

def unit_step_time_shifting(t0, A, shift,T=2*np.pi):
    t = np.linspace(0, T, 1000)
    y = np.where((t-shift) >= t0, A, 0)   
    return t, y

# perform operationson signald and plot them (time shifcting, tie scafling, addition, multiplication)
# (optional) Compute and plot the Fourier series and Fourier transform of signals