import tkinter as tk
import RPi.GPIO as GPIO

# LED PIN NUMBER
LED_PINS = {
    "Red": 17,    
    "Green": 18,
    "Blue": 27,
}

# GPIO INITIALIZED 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

for pin in LED_PINS.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# LED COLOR SETUP
def set_led_color(color):
    for pin in LED_PINS.values():
        GPIO.output(pin, GPIO.LOW)  
    GPIO.output(LED_PINS[color], GPIO.HIGH)  

#CREATING WINDOW
root = tk.Tk()
root.title("LED Controller")
root.geometry("300x200")  

# CREATING LABEL
label = tk.Label(root, text="Select the color of LED: ", font=("Arial", 20))
label.pack(pady=20)
 
def button_click(color):
    set_led_color(color)

# LOOP FOR  DIFFERENT LED LIGHT 
for color in LED_PINS.keys():
    button = tk.Button(root, text=color, command=lambda c=color: button_click(c))
    button.pack(pady=15)

#EXITING 
exit_button = tk.Button(root, text="Exiting", command=root.quit)
exit_button.pack(pady=10)

root.mainloop()

# CLEAN THE GPIO
GPIO.cleanup()