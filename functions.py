import numpy as np
import matplotlib.pyplot as plt


# define functions that generate sine wave and time shifts it

def generate_sine(f, A, T=2*np.pi):
    """
    Generate a sine wave signal.
    
    Parameters
    ----------
    f : float
        Frequency of the sine wave in Hz
    A : float
        Amplitude of the sine wave
    T : float, optional
        Time duration of the signal, default is 2π
    
    Returns
    -------
    t : ndarray
        Time array from 0 to T with 1000 points
    y : ndarray
        Sine wave values: y = A*sin(2πf*t)
    """
    t = np.linspace(0, T, 1000)
    y = A*np.sin(2*np.pi*f*t)
    return t, y

def sine_time_shifting(f, A, shift, T=2*np.pi):
    """
    Generate a time-shifted sine wave signal.
    
    Parameters
    ----------
    f : float
        Frequency of the sine wave in Hz
    A : float
        Amplitude of the sine wave
    shift : float
        Time shift amount (positive shift delays the signal)
    T : float, optional
        Time duration of the signal, default is 2π
    
    Returns
    -------
    t : ndarray
        Time array from 0 to T with 1000 points
    y : ndarray
        Time-shifted sine wave: y = A*sin(2πf*(t-shift))
    """
    t = np.linspace(0, T, 1000)
    y = A*np.sin(2*np.pi*f*(t-shift))
    return t, y

def sine_time_scaling(f, A, scale, T=2*np.pi):
    """
    Generate a time-scaled sine wave signal.
    
    Parameters
    ----------
    f : float
        Frequency of the sine wave in Hz
    A : float
        Amplitude of the sine wave
    scale : float
        Time scaling factor (scale > 1 compresses, scale < 1 expands)
    T : float, optional
        Time duration of the signal, default is 2π
    
    Returns
    -------
    t : ndarray
        Time array from 0 to T with 1000 points
    y : ndarray
        Time-scaled sine wave: y = A*sin(2πf*(t*scale))
    """    
    t = np.linspace(0, T, 1000)
    y = A*np.sin(2*np.pi*f*(t*scale))
    return t, y



# define functions that generate unit step wave and tie scales it

def generate_unit_step(t0, A, T=2*np.pi):
    """
    Generate a unit step signal.
    
    Parameters
    ----------
    t0 : float
        Step time location where the signal transitions from 0 to A
    A : float
        Amplitude after the step
    T : float, optional
        Time duration of the signal, default is 2π
    
    Returns
    -------
    t : ndarray
        Time array from 0 to T with 1000 points
    y : ndarray
        Unit step signal: y = A for t >= t0, 0 otherwise
    """
    t = np.linspace(0, T, 1000)
    y = np.where(t >= t0, A, 0)    # if t>=t0 gives A, otherwise 0
    return t, y

def unit_step_time_shifting(t0, A, shift, T=2*np.pi):
    """
    Generate a time-shifted unit step signal.
    
    Parameters
    ----------
    t0 : float
        Step time location where the signal transitions from 0 to A
    A : float
        Amplitude after the step
    shift : float
        Time shift amount (positive shift delays the signal)
    T : float, optional
        Time duration of the signal, default is 2π
    
    Returns
    -------
    t : ndarray
        Time array from 0 to T with 1000 points
    y : ndarray
        Time-shifted unit step: y = A for (t-shift) >= t0, 0 otherwise
    """    
    t = np.linspace(0, T, 1000)
    y = np.where((t-shift) >= t0, A, 0)   
    return t, y

# perform operationson signald and plot them (time shifcting, tie scafling, addition, multiplication)
# (optional) Compute and plot the Fourier series and Fourier transform of signals



def test_generate_sine():
    t, y = generate_sine(f=1, A=2)
    assert len(t) == 1000
    assert len(y) == 1000
    assert np.isclose(y[0], 0, atol=1e-6)

    t, y = generate_sine(f=1, A=3)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = generate_sine(f=1, A=0)
    assert np.allclose(y, 0)

    t, y = generate_sine(f=10, A=1)
    assert len(y) == 1000