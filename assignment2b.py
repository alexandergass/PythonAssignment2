#!/usr/bin/env python3

from tkinter import *;
window = Tk();
window.geometry('500x400');
window.title('Pizzaria');

label1 = Label(window, text='Choose pizza size:');
label2 = Label(window, text='Choose toppings:');

from tkinter import ttk;
numbers = ("Small", "Medium", "Large", "Extra-Large");
select1 = ttk.Combobox(window, value=numbers, width=20);
select1.current(0);

checkVar1 = StringVar();
check1 = Checkbutton(window, anchor="w", width="10", text="Pepperoni", highlightbackground='#3E4149', bg='#3E4149', variable=checkVar1);

checkVar2 = StringVar();
check2 = Checkbutton(window, anchor="w", width="10", text="Cheese", highlightbackground='#3E4149', bg='#3E4149', variable=checkVar2);

checkVar3 = StringVar();
check3 = Checkbutton(window, anchor="w", width="10", text="Olive", highlightbackground='#3E4149', bg='#3E4149', variable=checkVar3);

checkVar4 = StringVar();
check4 = Checkbutton(window, anchor="w", width="10", text="Pineapple", highlightbackground='#3E4149', bg='#3E4149', variable=checkVar4);

checkVar5 = StringVar();
check5 = Checkbutton(window, anchor="w", width="10", text="Ham", highlightbackground='#3E4149', bg='#3E4149', variable=checkVar5);

checkVar1.set(0);
checkVar2.set(0);
checkVar3.set(0);
checkVar4.set(0);
checkVar5.set(0);
total = 0;

def pizzaSize():
    global total;
    total = 0;

    if select1.get() == "Small":
        total = 9;
    if select1.get() == "Medium":
        total = 12.50;
    if select1.get() == "Large":
        total = 15.00;
    if select1.get() == "Extra-Large":
        total = 17.50;

    return total;

def pizzaToppings():
    toppings = [];
    global total;

    if int(checkVar1.get()) == 1:
        toppings.append("Pepperoni");
        total += 1;
    if int(checkVar2.get()) == 1:
        toppings.append("Cheese");
    if int(checkVar3.get()) == 1:
        toppings.append("Olive");
        total += 1;
    if int(checkVar4.get()) == 1:
        toppings.append("Pineapple");
        total += 1;
    if int(checkVar5.get()) == 1:
        toppings.append("Ham");
        total += 1;
    
    return toppings;

def hasClicked():
    size = select1.get();
    pizzaSize();
    displaytoppings = "";
    for topping in pizzaToppings():
        displaytoppings += topping +"\n";

    msg = "Size: \n" + size + "\n\nToppings Selected:\n" + displaytoppings + "\nTotal: $" + str(total) ;
    from tkinter import messagebox;
    messagebox.showinfo("Your Order", msg);
        
button1 = Button(window, text='Submit', highlightbackground='#3E4149', bg='#3E4149', command=hasClicked);

label1.grid(sticky=W, column=0, row=0);
label2.grid(sticky=W, column=1, row=0);
select1.grid(column=0, row=1);
check1.grid(column=1, row=1);
check2.grid(column=1, row=2);
check3.grid(column=1, row=3);
check4.grid(column=1, row=4);
check5.grid(column=1, row=5);
button1.grid(column=3, row=1);

window.mainloop();
