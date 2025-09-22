from signals import generate_sine_wave
import matplotlib.pyplot as plt

wave = generate_sine_wave(5, 10, 100)

t = [i / sample_rate 
     for i in range(int(duration * sample_rate))]

plt.plot(t, wave)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title(f"{frequency}Hz Sine Wave")
plt.grid(True)
plt.show()