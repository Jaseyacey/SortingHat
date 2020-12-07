# Using Tkinter to visualise

import tkinter
import random

# List of houses
houses = ["Slytherin", "Gryffindor", "Hufflepuff", "Ravenclaw"]

# Function to pick a random house


def pickHouse():
    hatLabel.configure(text=(random.choice(houses)))


# Configure the tkinter GUI
root = tkinter.Tk()
# Set the tkinter window title
root.title("Python Soting Hat")
# Set the tkinter window size
root.geometry("600x100")

# Set the font style for tkinter
hatLabel = tkinter.Label(root, text="", font=("Helvetica", 32))
hatLabel.pack()

# Create a button with the label 'Choose a house'
insultButton = tkinter.Button(text="Choose a house", command=pickHouse)
insultButton.pack()

root.mainloop
