import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import os


def create_main_window(num_values):
    # Create the main window
    window = tk.Tk()
    window.title('Kalkulator otpora')
    
    entry_frame = tk.Frame(window)
    entry_frame.pack()

    space_label = tk.Label(window)
    space_label.pack()
    space_label = tk.Label(window)
    space_label.pack()

    # Create a list to hold the entry widgets
    entries = []

    # Create a dropdown menu and label for each band
    for i in range(num_values):
        label = tk.Label(entry_frame, text=f'Prsten {i+1}:')
        label.grid(row=i, column=0)
        entry = tk.OptionMenu(entry_frame, tk.StringVar(), 'Crna', 'Smeđa', 'Crvena', 'Narančasta', 'Žuta', 'Zelena', 'Plava', 'Ljubičasta', 'Siva', 'Bijela', 'Zlatna', 'Srebrna')
        entry.grid(row=i, column=1)
        entries.append(entry)

    # Create a function to calculate the resistance
    def calculate_resistance():
        values = [entry.cget("text") for entry in entries]
        # Define a dictionary that maps the colors of the values to their corresponding values
        color_values = {
            'Crna': 0,
            'Smeđa': 1,
            'Crvena': 2,
            'Narančasta': 3,
            'Žuta': 4,
            'Zelena': 5,
            'Plava': 6,
            'Ljubičasta': 7,
            'Siva': 8,
            'Bijela': 9,
            'Zlatna': -1,
            'Srebrna': -2
        }

        # Define a dictionary that maps the tolerance values to their corresponding percentages
        tolerance_values = {
            'None': 20,
            'Srebrna': 10,
            'Zlatna': 5,
            'Crvena': 2,
            'Smeđa': 1,
            'Zelena': 0.5,
            'Plava': 0.25,
            'Ljubičasta': 0.1,
            'Siva': 0.05
        }

        # Define a dictionary that maps the temperature coefficient values to their corresponding parts per million per degree Celsius
        temperature_coefficient_values = {
            'none': 0,
            'Smeđa': 100,
            'Crvena': 50,
            'Narančasta': 15,
            'Žuta': 25,
            'Plava': 10,
            'Ljubičasta': 5,
            'Siva': 1,
            'Zelena': 0.5,
            'Bijela': 0.25
        }
        # Calculate the resistance
        if len(values) == 4:
            # 4-band resistor
            # The first two values represent the first two digits, and the third band represents the number of zeros
            resistance = int(str(color_values[values[0]]) + str(color_values[values[1]])) * 10 ** color_values[values[2]]
            # The fourth band represents the tolerance
            tolerance = tolerance_values[values[3]]
            temperature_coefficient = temperature_coefficient_values['none']
        elif len(values) == 5:
            # 5-band resistor
            # The first three values represent the first three digits, and the fourth band represents the number of zeros
            resistance = int(
                str(color_values[values[0]]) + str(color_values[values[1]]) + str(color_values[values[2]])) * 10 ** \
                         color_values[values[3]]
            # The fifth band represents the tolerance
            tolerance = tolerance_values[values[4]]
            temperature_coefficient = temperature_coefficient_values['none']
        elif len(values) == 6:
            # 6-band resistor
            # The first three values represent the first three digits, and the fourth band represents the number of zeros
            resistance = int(
                str(color_values[values[0]]) + str(color_values[values[1]]) + str(color_values[values[2]])) * 10 ** color_values[values[3]]
            # The fifth band represents the tolerance
            tolerance = tolerance_values[values[4]]
            # The sixth band represents the temperature coefficient
            temperature_coefficient = temperature_coefficient_values[values[5]]
        else:
            raise ValueError('Invalid number of values')

        # Calculate the tolerance
        tolerable = resistance * tolerance / 100
        
        # Convert the result to ohms, kilo-ohms or mega-ohms depending on the value
        if resistance > 1000:
            resistance = resistance / 1000
            tolerable = tolerable / 1000
            if resistance > 1000:
                resistance = resistance / 1000
                tolerable = tolerable / 1000
                resistance = str(round(resistance, 2)) + "M"
                tolerable = str(round(tolerable, 2)) + "M"
            else:
                resistance = str(round(resistance, 2)) + "k"
                tolerable = str(round(tolerable, 2)) + "k"
            
        # Set the result label to the resistance and tolerance
        result_label.config(text=f'Otpor je {resistance}Ω ± {tolerable}Ω (± {tolerance}%)')
        if temperature_coefficient != 0:
            temp_label.config(text=f'Temperaturni koeficijent: {temperature_coefficient}ppm/°C')

    # Open the image using the Image module
    image_path = os.path.join(os.path.dirname(__file__), f"{num_values}_band_resistor.png")
    image = Image.open(image_path)

    # Resize the image
    image = image.resize((125, 50))

    photo_image = ImageTk.PhotoImage(image)

    label = tk.Label(window, image=photo_image)

    label.pack()

    # Place the image between selector buttons and calculate button
    label.place(x=80, y=5+30*num_values)

    # Add a label to display the result
    result_label = tk.Label(window)
    result_label.pack()

    # Add a label to display the temperature coefficient
    temp_label = tk.Label(window)
    temp_label.pack()

    # Create a button to trigger the calculation
    calculate_button = tk.Button(window, text='Izračunaj', command=calculate_resistance)
    calculate_button.pack()

    # Create a function to return to the start menu
    def return_to_start_menu():
        window.destroy()
        create_start_menu()

    # Add a space between the return button and the calculate button
    space_label = tk.Label(window)
    space_label.pack()

    # Create a button to return to the start menu
    return_button = tk.Button(window, text='Natrag', command=return_to_start_menu)
    return_button.pack()

    # Resize the window
    size = 170 + num_values * 30
    window.geometry(f"280x{size}+330+320")

    # Run the main loop
    window.mainloop()

def create_start_menu():
    # Create the start menu window
    window = tk.Tk()
    window.title('Početni Menu')

    space_label = tk.Label(window)
    space_label.pack()

    # Add a title
    label = Label(window, text="Kalkulator otpora", font=("Arial", 12, "bold"))
    label.pack()

    #Add the school info and separate the next header
    label = Label(window, text="Srednja strukovna škola Velika Gorica", font=("Arial", 9))
    label.pack()
    space_label = tk.Label(window)
    space_label.pack()
    space_label = tk.Label(window)
    space_label.pack()

    # Open the image using the Image module
    logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
    logo = Image.open(logo_path)

    # Resize the image
    logo = logo.resize((75,75))

    logo_image = ImageTk.PhotoImage(logo)

    logo = tk.Label(window, image=logo_image)

    logo.pack()

    # Place the image at 0, 0
    logo.place(x=0, y=0)

    # Create a function to open the 4-band window
    def open_4_band_window():
        window.destroy()
        create_main_window(4)

    # Create a button to open the 4-band window
    four_band_button = tk.Button(window, text='4-Prstena', command=open_4_band_window)
    four_band_button.pack()

    # Create a function to open the 5-band window
    def open_5_band_window():
        window.destroy()
        create_main_window(5)

    # Create a button to open the 5-band window
    five_band_button = tk.Button(window, text='5-Prstena', command=open_5_band_window)
    five_band_button.pack()

    # Create a function to open the 6-band window
    def open_6_band_window():
        window.destroy()
        create_main_window(6)

    # Create a button to open the 6-band window
    six_band_button = tk.Button(window, text='6-Prstena', command=open_6_band_window)
    six_band_button.pack()

    # Create a function to close the start menu window
    def close_window():
        window.destroy()

    # Add two spaces between the band selector buttons and the exit button
    space_label = tk.Label(window)
    space_label.pack()
    space_label = tk.Label(window)
    space_label.pack()
    space_label = tk.Label(window)
    space_label.pack()
    space_label = tk.Label(window)
    space_label.pack()

    # Open the image using the Image module
    image_path = os.path.join(os.path.dirname(__file__), 'resistor.png')
    image = Image.open(image_path)

    # Resize the image
    image = image.resize((176,100))

    photo_image = ImageTk.PhotoImage(image)

    label = tk.Label(window, image=photo_image)

    label.pack()

    # Place the image at 100, 190
    label.place(x=100, y=190)

    # Create a button to close the start menu window
    exit_button = tk.Button(window, text='Izlaz', command=close_window)
    exit_button.pack()

    # Make the window a certain size
    window.geometry("375x340+300+300")

    space_label = tk.Label(window)
    space_label.pack()

    # Add the made by designation
    label = Label(window, text="Napravio: Marin Mikulčić", font=("Arial", 10))
    label.pack(side=RIGHT, padx=0)

    # Run the start menu loop
    window.mainloop()

# Create the start menu
create_start_menu()
