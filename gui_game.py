import random
import os 
import tkinter as tk
from tkinter import messagebox

# Set up global game variables
secret_number=random.randint(1,100)
attempts=0

# Helper function to play built in Mac sound alerts
def play_sound(sound_type):
    # trigger's native Mac system alerts in the background so the game doesn't freeze
    os.system(f"afplay /system/Library/Sounds/{sound_type}.aiff &")

def check_guess():
    global attempts, secret_number
    try:
        # Get the number from text box
        user_guess=int(entry.get())
        attempts+=1

        if user_guess<secret_number:
           result_label.config(text="Too low! Try again.⬇️",fg="white")
           window.config(bg="#1E3A8A") # change background to a cool deep blue
           update_bg_for_labels("#1E3A8A")
           play_sound("Basso") #Play a low thump sound

        elif user_guess>secret_number:
            result_label.config(text="Too high! Try again.⬆️",fg="white")
            window.config(bg="#991B1B") # change background to a cool Warning Red
            update_bg_for_labels("#991B1B")
            play_sound("Basso") #Play a low thump sound

        else:
            window.config(bg="#065F46") # change background to a cool success green
            update_bg_for_labels("#065F46")
            play_sound("Glass") #Play a celebratory chime sound
            # Show a pop-up alert box for winning
            messagebox.showinfo("Winner!",f"🎉 Correct!\nYou found the number in {attempts} attempts!")

            #automatically reset the game for another round
            secret_number=random.randint(1,100)
            attempts=0
            window.config(bg="#1F2937") # change background to a standard dark grey
            update_bg_for_labels("#1F2937")
            result_label.config(text="New number generated! Guess again.",fg="white")

        entry.delete(0,tk.END) #Clear the input field
    except ValueError:
        result_label.config(text="❌ Please enter a valid number.",fg="orange")
        play_sound("Sosumi") #System alert beep for invalid typing

#Helper function to ensure all text labels match the current window background color
def update_bg_for_labels(color):
    title.config(bg=color)
    instruction.config(bg=color)
    result_label.config(bg=color)

# Create the main window window
window=tk.Tk()
window.title("Guessing Game")
window.geometry("350x250") #set window size (Width x Height)
window.config(bg="#1F2937") # set initial background color to a standard dark grey

# Add visual elements (Widgets)
title=tk.Label(window, text="Guess the Number (1-100)",font=("Arial",16,"bold"),bg="#1F2937",fg="white")
title.pack(pady=10)

instruction=tk.Label(window, text="Enter your guess below:",font=("Arial",12),bg="#1F2937",fg="white")
instruction.pack(pady=5)

entry=tk.Entry(window, font=("Arial",14),width=10, justify="center",bg="white",fg="black")
entry.pack(pady=5)

# This ties the button directly to the check_guess function above
guess_button=tk.Button(window, text="Submit Guess",command=check_guess,font=("Arial",12))
guess_button.pack(pady=5)

result_label=tk.Label(window, text="",font=("Arial", 12,"italic"), bg="#1F2937",fg="white")
result_label.pack(pady=5)

# Keep the standalone window open
window.mainloop()

        