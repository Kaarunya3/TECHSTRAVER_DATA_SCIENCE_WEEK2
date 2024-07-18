import tkinter as tk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit():
  try:
    celsius_value = float(celsius_entry.get())
    fahrenheit_value = (celsius_value * 9/5) + 32
    fahrenheit_result.config(text=f"{fahrenheit_value:.2f} °F")
  except ValueError:
    fahrenheit_result.config(text="Invalid Input")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius():
  try:
    fahrenheit_value = float(fahrenheit_entry.get())
    celsius_value = (fahrenheit_value - 32) * 5/9
    celsius_result.config(text=f"{celsius_value:.2f} °C")
  except ValueError:
    celsius_result.config(text="Invalid Input")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create labels for Celsius and Fahrenheit
celsius_label = tk.Label(window, text="Celsius:")
celsius_label.grid(row=0, column=0, padx=10, pady=10)
fahrenheit_label = tk.Label(window, text="Fahrenheit:")
fahrenheit_label.grid(row=1, column=0, padx=10, pady=10)

# Create entry fields for Celsius and Fahrenheit
celsius_entry = tk.Entry(window)
celsius_entry.grid(row=0, column=1, padx=10, pady=10)
fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.grid(row=1, column=1, padx=10, pady=10)

# Create buttons for conversion
celsius_to_fahrenheit_button = tk.Button(window, text="C to F", command=celsius_to_fahrenheit)
celsius_to_fahrenheit_button.grid(row=2, column=0, padx=10, pady=10)
fahrenheit_to_celsius_button = tk.Button(window, text="F to C", command=fahrenheit_to_celsius)
fahrenheit_to_celsius_button.grid(row=2, column=1, padx=10, pady=10)

# Create labels to display results
celsius_result = tk.Label(window, text="")
celsius_result.grid(row=3, column=0, padx=10, pady=10)
fahrenheit_result = tk.Label(window, text="")
fahrenheit_result.grid(row=3, column=1, padx=10, pady=10)

# Run the main event loop
window.mainloop()
