import time
from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

# ----- Settings -----
duration = 60         # seconds to run
interval = 1          # seconds between samples

# ----- Storage for Plotting -----
timestamps = []
soil_humidity = []
air_temperature = []

# ----- Setup Plot -----
plt.ion()
fig, ax = plt.subplots()
line_temp, = ax.plot([], [], 'o-', label='Air Temperature (°C)', color='blue')
line_hum, = ax.plot([], [], 'o-', label='Soil Humidity (%)', color='green')
ax.set_xlabel('Time')
ax.set_ylabel('Sensor Readings')
ax.legend()
ax.grid(True)

print("Real-Time Plant Environment Monitor")

# ----- Real-Time Simulation -----
start_time = time.time()

while time.time() - start_time < duration:
    now = datetime.now()
    time_label = now.strftime('%H:%M:%S')

    # --- Simulate sensor readings ---
    # Soil humidity in %, fluctuating around 35–50%
    humidity = 35 + 10 * np.sin(time.time() / 5) + np.random.normal(0, 1)

    # Air temperature in °C, around 26–32°C
    temperature = 28 + 2 * np.cos(time.time() / 10) + np.random.normal(0, 0.5)

    # --- Save data ---
    timestamps.append(time_label)
    soil_humidity.append(humidity)
    air_temperature.append(temperature)

    # --- Print to console ---
    print(f"[{time_label}] Soil Humidity: {humidity:.2f}%  |  Air Temp: {temperature:.2f}°C")

    # --- Update plot ---
    ax.clear()
    ax.plot(timestamps, air_temperature, 'o-', label='Air Temperature (°C)', color='orangered')
    ax.plot(timestamps, soil_humidity, 'o-', label='Soil Humidity (%)', color='green')
    ax.set_xlabel('Time')
    ax.set_ylabel('Sensor Readings')
    ax.set_title("Real-Time Soil & Air Monitoring")
    ax.legend()
    ax.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.pause(0.1)

    # Wait for the next sample
    time.sleep(interval)

plt.ioff()
plt.show()
