from functions import *
import matplotlib.pyplot as plt


# testing sine generating function and time shifting function
t1, y1 = generate_sine(1, 1)
t2, y2 = sine_time_shifting(1, 1, shift=1.4)
t3, y3 = sine_time_scaling(1, 1, scale=0.2)

plt.plot(t1, y1, label="original graph")
plt.plot(t2, y2, label="time shifted by 1.4")
plt.plot(t3, y3, label="time scaled by 0.2")
plt.title("Sinusoidal Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()


# testing unit step generating function and time scaling function
t1, y1 = generate_unit_step(1, 1)
t2, y2 = unit_step_time_shifting(1, 1, shift=1.4)

plt.plot(t1, y1, label="original graph")
plt.plot(t2, y2, label="time shifted by 1.4")
plt.title("Unit Step Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()


# TDD 

# Normal case
t, y = generate_sine(f=1, A=1)
assert len(t) == 1000
assert len(y) == 1000

# Edge case - zero frequency
t, y = generate_sine(f=0, A=1)
assert max(y) == 0

# Edge case - zero amplitude  
t, y = generate_sine(f=1, A=0)
assert max(y) == 0