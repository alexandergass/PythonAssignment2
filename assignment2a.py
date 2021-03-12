# try:
#     #!/usr/local/bin/python3
# except:
#     #!C:\Users\Alex\AppData\Local\Programs\Python\Python38-32\python.exe

#https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take
#i think this is a universal shebang that works
#for mac and windows
#!/usr/bin/env python3

from tkinter import *;
window = Tk();
window.geometry('400x400');
window.title('Grade checker');

label1 = Label(window, text='Please enter your grade:');
label2 = Label(window, text='Your grade is:');
label3 = Label(window, text='', font="Ariel 12 bold");
label4 = Label(window, text='', fg='red');

text1 = Entry(window, width=5);
text1.focus();

def assign_letter_grade(mark): 
    mark = int(text1.get());
    if mark >= 85: return "A"
    elif mark >= 75: return "B"
    elif mark >= 60: return "C"
    else: return "F"

def assign_number_grade(mark):
    mark = mark.upper();
    if mark == 'A': return "Mark range: 85-100"
    elif mark == 'B': return "Mark range: 75-84.99"
    elif mark == 'C': return "Mark range: 60-74.99"
    elif mark == 'F': return "Mark range: 0-59.99"

def hasClicked():
    mark = text1.get();
    if mark.isnumeric():
        label3.configure( text=assign_letter_grade(mark) );
        label4.configure( text='');
    elif assign_number_grade(mark) :
        label3.configure( text=assign_number_grade(mark) );
        label4.configure( text='');
    else: 
        label3.configure( text='');
        label4.configure( text="Invalid input");
        
button1 = Button(window, text='Submit', highlightbackground='#3E4149', bg='#3E4149', command=hasClicked);

label1.grid(column=0, row=1);
text1.grid(sticky=W, column=1, row=1);
button1.grid(sticky=W, column=0, row=2);
label2.grid(sticky=W, column=0, row=3);
label3.grid(sticky=W, column=1, row=3);
label4.grid(sticky=W, column=0, row=4);

window.mainloop();
