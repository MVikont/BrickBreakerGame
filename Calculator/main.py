from tkinter import *

FONT = ("Arial", 25)
BFONT = ("Arial", 15)
expression = ""
expression_two = ""
first = ""
answer = ""
o = ""
calculation_done = False

#----------FUNCTIONALITY----------#
#ALL MATHEMATICAL OPERATORS
def operation(oper):
    global expression
    global expression_two
    global o
    global first
    global calculation_done
    global answer
    calculation_done = False
    first = expression
    expression = ""
    o = oper.cget("text")
    mid_calc()

#FACTORIAL
def factorial(a):
    global expression
    try:
        w = 1
        for n in range(1, int(a)+1):
            w *= n
    except ValueError:
        pass
    else:
        expression = str(w)
    finally:
        update_screen()

#RESULT - = BUTTON
def result():
    try:
        global expression
        global expression_two
        global o
        global first
        global calculation_done
        global answer
        calculation_done = True
        expression_two = screen.get()
        expression = eval(f"{first}{expression_two}")
        #First = first number, expression_two = operator & second number.
        answer = expression
        update_screen()
        reset_values()
    except SyntaxError:
        pass


#DIALER - Prints numbers on the screen.
def print_numbers(button):
    global calculation_done
    if calculation_done:
        clear_screen()
    calculation_done = False
    global expression
    screen.config(state="normal")
    new_num = button.cget("text")
    if (len(str(expression)) < 1 and new_num == "0") or len(str(expression)) >= 15:
        pass
    else:
        screen.insert(INSERT, new_num)
        expression = str(expression) + str(new_num)
    screen.config(state="disabled")

#DECIMAL POINT - Adds decimal point
def add_decimal(button):
    global expression
    if "." in expression: #If there is a decimal point already, do not add another one.
        pass
    elif len(expression) == 0: #If the screen shows 0, decimal point will be added and not replace 0.
        expression += "0."
    else:
        expression += "."
    update_screen()

#CLEAR ENTIRE SCREEN
def clear_screen():
    reset_values()
    update_screen()

#DELETE LAST DIGIT
def correct():
    global expression
    if len(expression) > 0:
        expression = expression[:-1] # Erases last digit. Works like a backspace
        update_screen()
    else:
        pass

#UPDATE SCREEN
def update_screen():
    screen.config(state="normal")
    screen.delete(0, END)
    screen.insert(INSERT, str(expression))
    screen.config(state="disabled")

#UPDATE SCREEN IN MID-CALCULATION
def mid_calc():
    global o
    screen.config(state="normal")
    screen.delete(0, END)
    screen.insert(INSERT, o)
    screen.config(state="disabled")

#RESETS ALL VALUES
def reset_values():
    global expression
    global expression_two
    global first
    global o
    global answer
    expression = ""
    expression_two = ""
    first = ""
    o = ""
    answer = ""

#----------WINDOW & SCREEN----------#
win = Tk()
win.title("Calculator")
win.minsize(width=350, height=300)
win.config(padx=30, pady=30)

screen = Entry(width=16, font=FONT)
screen.grid(column=0, row=2, columnspan=7)
screen.insert(INSERT, "")
screen.config(state="disabled")

#----------BUTTONS----------#
#NUMBER BUTTONS
one = Button(text="1", width=3, height=1, font=BFONT, command=lambda: print_numbers(one))
one.grid(column=0, row=4)
two = Button(text="2", width=3, height=1, font=BFONT, command=lambda: print_numbers(two))
two.grid(column=1, row=4)
three = Button(text="3", width=3, height=1, font=BFONT, command=lambda: print_numbers(three))
three.grid(column=2, row=4)

four = Button(text="4", width=3, height=1, font=BFONT, command=lambda: print_numbers(four))
four.grid(column=0, row=5)
five = Button(text="5", width=3, height=1, font=BFONT, command=lambda: print_numbers(five))
five.grid(column=1, row=5)
six = Button(text="6", width=3, height=1, font=BFONT, command=lambda: print_numbers(six))
six.grid(column=2, row=5)

seven = Button(text="7", width=3, height=1, font=BFONT, command=lambda: print_numbers(seven))
seven.grid(column=0, row=6)
eight = Button(text="8", width=3, height=1, font=BFONT, command=lambda: print_numbers(eight))
eight.grid(column=1, row=6)
nine = Button(text="9", width=3, height=1, font=BFONT, command=lambda: print_numbers(nine))
nine.grid(column=2, row=6)

zero = Button(text="0", width=3, height=1, font=BFONT, command=lambda: print_numbers(zero))
zero.grid(column=1, row=7)

#OPERATOR BUTTONS
plus = Button(text="+", width=3, height=1, font=BFONT, command=lambda: operation(plus))
plus.grid(column=5, row=4)
minus = Button(text="-", width=3, height=1, font=BFONT, command=lambda: operation(minus))
minus.grid(column=5, row=5)
ast = Button(text="*", width=3, height=1, font=BFONT, command=lambda: operation(ast))
ast.grid(column=5, row=6)
slash = Button(text="/", width=3, height=1, font=BFONT, command=lambda: operation(slash))
slash.grid(column=5, row=7)

equals = Button(text="=", width=13, height=1, font=BFONT, command=result)
equals.grid(column=0, row=8, columnspan=3)

floor = Button(text="//", width=3, height=1, font=BFONT, command=lambda: operation(floor))
floor.grid(column=6, row=4)
exclamation = Button(text="!", width=3, height=1, font=BFONT, command=lambda: factorial(expression))
exclamation.grid(column=6, row=5)
percent = Button(text="%", width=3, height=1, font=BFONT, command=lambda: operation(percent))
percent.grid(column=6, row=6)
decimal = Button(text=".", width=3, height=1, font=BFONT, command=lambda: add_decimal(decimal))
decimal.grid(column=6, row=7)
backspace = Button(text="<<", width=3, height=1, font=BFONT, command=correct)
backspace.grid(column=6, row=8)
ce = Button(text="CE", width=3, height=1, font=BFONT, command=clear_screen)
ce.grid(column=5, row=8)






win.mainloop()