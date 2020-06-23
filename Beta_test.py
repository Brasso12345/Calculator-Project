from tkinter import*

def btnClick(numbers):
    global operator
    operator = str(operator)
    operator += str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")

def btnEqualsInput():
    global operator
    operator = eval(operator)
    text_input.set(operator)


cal = Tk()
cal.title("Calculator Project")
operator = ""
text_input = StringVar()
button_color_1 = "light gray"
button_color_text_1 = "gray24"
button_num_size_x = 16
button_num_size_y = 2

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                   bg="azure4", justify='right').grid(columnspan=10)
btn9 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="9",
              bg=button_color_1, command=lambda:btnClick(9)).grid(row=1, column=2)
btn8 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="8",
              bg=button_color_1, command=lambda:btnClick(8)).grid(row=1, column=1)
btn7 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="7",
              bg=button_color_1, command=lambda:btnClick(7)).grid(row=1, column=0)
clear = Button(cal, padx=16, pady=2, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="C",
              bg=button_color_1, command=btnClearDisplay).grid(row=1, column=3)
#====================================================================
btn6 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="6",
              bg=button_color_1, command=lambda:btnClick(6)).grid(row=2, column=2)
btn5 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="5",
              bg=button_color_1, command=lambda:btnClick(5)).grid(row=2, column=1)
btn4 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="4",
              bg=button_color_1, command=lambda:btnClick(4)).grid(row=2, column=0)
multiplication = Button(cal, padx=18, pady=2, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="x",
                bg=button_color_1, command=lambda:btnClick("*")).grid(row=2, column=3)
division = Button(cal, padx=16, pady=2, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="/",
                bg=button_color_1, command=lambda:btnClick("/")).grid(row=2, column=4)
#=====================================================================
btn3 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="3",
              bg=button_color_1, command=lambda :btnClick(3)).grid(row=3, column=2)
btn2 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="2",
              bg=button_color_1, command=lambda:btnClick(2)).grid(row=3, column=1)
btn1 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="1",
              bg=button_color_1, command=lambda:btnClick(1)).grid(row=3, column=0)
Addition = Button(cal, padx=16, pady=2, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="+",
                bg=button_color_1, command=lambda:btnClick("+")).grid(row=3, column=3)
Subtraction = Button(cal, padx=16, pady=2, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="-",
                bg=button_color_1, command=lambda:btnClick("-")).grid(row=3, column=4)
#=====================================================================
btn0 = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="0",
              bg=button_color_1, command=lambda:btnClick(0)).grid(row=4, column=0)
equals = Button(cal, padx=16, pady=2, bd=8, fg=button_color_text_1, font=('arial', 20, 'bold'), text="=",
              bg=button_color_1, command=btnEqualsInput).grid(row=4, column=2)
decimal_point = Button(cal, padx=button_num_size_x, pady=button_num_size_y, bd=8,)
cal.mainloop()