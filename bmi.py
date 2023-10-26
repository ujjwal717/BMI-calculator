import tkinter as tk

def bmi_calculation():
    try:
        weight = float(weight_input.get())
        height = float(height_input.get())
        bmi = weight/height ** 2
        result_label.config(text="Your BMI: " + str(round(bmi, 2)))
    except ValueError:
        result_label.config(text="Invalid input")


window = tk.Tk()
window.title("BMI CALCULATOR ")

label = tk.Label(window, text='''BMI Ranges explained :- 

Underweight Range ----> When BMI is less than 18.5

Healthy Weight Range ----> When BMI is between 18.5 to 24.9

Overweight Range ----> When BMI  is between 25.0 to 29.9

Obese Range ----> When BMI is more than 30.0


''')

label.pack()

instruction_label1 = tk.Label(window, text="Enter your weight in Kgs :")
instruction_label1.pack()

weight_input = tk.Entry(window)
weight_input.pack()

instruction_label2 = tk.Label(window, text="Enter your height in metres:")
instruction_label2.pack()

height_input = tk.Entry(window)
height_input.pack()

add_button = tk.Button(window, text=" CALCULATE ", command=bmi_calculation)
add_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
