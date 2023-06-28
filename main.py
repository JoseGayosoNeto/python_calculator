from tkinter import *

# Entry Box font
entry_font = "Verdana 15 bold"

# Buttons font
button_font = "Verdana 10"

# Activate Numbers Buttons


def btNumbers(number):
    getNumber = entry_box.get()
    entry_box.delete(0, END)
    entry_box.insert(0, str(getNumber) + str(number))


# Clear button
def clear():
    entry_box.delete(0, END)


# Addition
def addition():
    getNumber = entry_box.get()
    global first_number
    global operation
    operation = "addition"
    first_number = int(getNumber)
    entry_box.delete(0, END)

# Substraction


def substraction():
    getNumber = entry_box.get()
    global first_number
    global operation
    operation = "substraction"
    first_number = int(getNumber)
    entry_box.delete(0, END)

# Multiplication


def multiplication():
    getNumber = entry_box.get()
    global first_number
    global operation
    operation = "multiplication"
    first_number = int(getNumber)
    entry_box.delete(0, END)

# Division


def division():
    getNumber = entry_box.get()
    global first_number
    global operation
    operation = "division"
    first_number = float(getNumber)
    entry_box.delete(0, END)

# Percent


def percent():
    getNumber = entry_box.get()
    global first_number
    global operation
    operation = "percent"
    first_number = int(getNumber)
    entry_box.delete(0, END)

# Power


def power():
    getNumber = entry_box.get()
    global first_number
    global operation
    operation = "power"
    first_number = int(getNumber)
    entry_box.delete(0, END)

# Square root


def squareroot():
    getNumber = entry_box.get()
    entry_box.delete(0, END)
    newNumber = int(getNumber) ** (1/2)
    entry_box.insert(0, newNumber)
    global first_number
    first_number = newNumber

# Add


def add():
    getNumber = entry_box.get()
    entry_box.delete(0, END)
    newNumber = int(getNumber) * (-1)
    entry_box.insert(0, newNumber)
    global first_number
    first_number = newNumber


# Equal
def equal():
    getNumber = entry_box.get()
    entry_box.delete(0, END)
    if operation == "addition":
        entry_box.insert(0, first_number + int(getNumber))
    elif operation == "substraction":
        entry_box.insert(0, first_number - int(getNumber))
    elif operation == "multiplication":
        entry_box.insert(0, first_number * int(getNumber))
    elif operation == "division":
        if getNumber == "0":
            entry_box.insert(0, "Error")
            raise ZeroDivisionError("Division by zero! Rerun the code.")
            exit
        entry_box.insert(0, first_number / int(getNumber))
    elif operation == "percent":
        entry_box.insert(0, (first_number * int(getNumber)) / 100)
    elif operation == "power":
        entry_box.insert(0, first_number ** int(getNumber))


if __name__ == "__main__":
    # Configurations
    app = Tk()
    app.title("Calculadora Python")
    app.geometry = (500, 500)
    app.resizable(width=False, height=False)
    app.config(bg="black")
    calc_icon = PhotoImage(file="logo_icon.png")
    app.iconphoto(False, calc_icon)

 # Frames definitions
    # App frame
    frame = Frame(app, width=500, height=400, bg="black")
    frame.grid(row=1, column=0)
    # Entry box frame
    top_frame = Frame(app, width=500, height=100, bg="black")
    top_frame.grid(row=0, column=0)

 # Entry
    entry_box = Entry(top_frame, bg="#0C0C0C",
                      font=entry_font, width=30, fg="white")
    entry_box.grid(row=0, column=0, ipady=15)

 # Buttons
    bt_1 = Button(frame, text="1", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(1))
    bt_1.grid(row=3, column=0, padx=5)

    bt_2 = Button(frame, text="2", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(2))
    bt_2.grid(row=3, column=1, padx=5)

    bt_3 = Button(frame, text="3", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(3))
    bt_3.grid(row=3, column=2, padx=5)

    bt_4 = Button(frame, text="4", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(4))
    bt_4.grid(row=2, column=0, padx=5)

    bt_5 = Button(frame, text="5", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(5))
    bt_5.grid(row=2, column=1, padx=5)

    bt_6 = Button(frame, text="6", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(6))
    bt_6.grid(row=2, column=2, padx=5)

    bt_7 = Button(frame, text="7", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(7))
    bt_7.grid(row=1, column=0, padx=5)

    bt_8 = Button(frame, text="8", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(8))
    bt_8.grid(row=1, column=1, padx=5)

    bt_9 = Button(frame, text="9", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(9))
    bt_9.grid(row=1, column=2, padx=5)

    bt_0 = Button(frame, text="0", width=10, height=3, bg="#36688D",
                  activebackground="#36688D", font=button_font, command=lambda: btNumbers(0))
    bt_0.grid(row=4, column=1, padx=5)

    bt_clear = Button(frame, text="C", width=10, height=3, bg="#36688D",
                      activebackground="#36688D", font=button_font, command=clear)
    bt_clear.grid(row=0, column=2, padx=5)

    bt_add = Button(frame, text="+/-", width=10, height=3, bg="#36688D",
                    activebackground="#36688D", font=button_font, command=add)
    bt_add.grid(row=4, column=0, padx=5)

    bt_percentage = Button(frame, text="%", width=10, height=3, bg="#36688D",
                           activebackground="#36688D", font=button_font, command=percent)
    bt_percentage.grid(row=4, column=2, padx=5)

    bt_division = Button(frame, text="÷", width=10, height=3, bg="#F18904",
                         activebackground="#F18904", font=button_font, command=division)
    bt_division.grid(row=0, column=3, padx=5)

    bt_mult = Button(frame, text="x", width=10, height=3, bg="#F18904",
                     activebackground="#F18904", font=button_font, command=multiplication)
    bt_mult.grid(row=1, column=3, padx=5)

    bt_addition = Button(frame, text="+", width=10, height=3, bg="#F18904",
                         activebackground="#F18904", font=button_font, command=addition)
    bt_addition.grid(row=3, column=3, padx=5)

    bt_substraction = Button(frame, text="-", width=10, height=3, bg="#F18904",
                             activebackground="#F18904", font=button_font, command=substraction)
    bt_substraction.grid(row=2, column=3, padx=5)

    bt_equal = Button(frame, text="=", width=10, height=3, bg="#F18904",
                      activebackground="#F18904", font=button_font, command=equal)
    bt_equal.grid(row=4, column=3, padx=5)

    bt_power = Button(frame, text="xⁿ", width=10, height=3, bg="#36688D",
                      activebackground="#36688D", font=button_font, command=power)
    bt_power.grid(row=0, column=1, padx=5)

    bt_sqrt = Button(frame, text="√", width=10, height=3, bg="#36688D",
                     activebackground="#36688D", font=button_font, command=squareroot)
    bt_sqrt.grid(row=0, column=0, padx=5)

    app.mainloop()
