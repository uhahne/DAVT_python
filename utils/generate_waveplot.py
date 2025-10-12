import numpy as np
import matplotlib.pyplot as plt

# Create random data for a typical waveform
np.random.seed(42)  # For reproducibility
t = np.linspace(0, 2 * np.pi, 500)  # Time axis
waveform = np.sin(2 * np.pi * 3 * t) + np.random.normal(scale=0.3, size=t.shape)  # Sine with random noise

# Plot
plt.figure(figsize=(10, 5))
# Plot with visible axes, but without ticks
plt.figure(figsize=(10, 5))
plt.plot(t, waveform, color="blue")
plt.title("$f(t)$", fontsize=16)
plt.gca().set_xticks([])  # Removes ticks on the x-axis
plt.gca().set_yticks([])  # Removes ticks on the y-axis
# Show axis lines
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
# Axis labels

plt.xlabel("Time (t)", fontsize=12)
plt.ylabel("Amplitude", fontsize=12)
plt.tight_layout()

# Save the image
file_path = "./data/jingle_waveform_with_axes.png"
plt.savefig(file_path)
plt.close()