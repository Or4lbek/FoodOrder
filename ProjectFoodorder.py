from tkinter import*
from tkinter import messagebox


import tkinter as tk
import tkinter.ttk as ttk
  
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)
  
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings
  
        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)
  
        for row in rows:
            table.insert('', tk.END, values=tuple(row))
  
        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

  
import random
ID=random.randrange(1000,9999)
ID = f'Order ID:{ID}'


stars='* * * * * * * * * * * * * * * * * * * * * * *'

probel = "          "
def suggestion():
    def answer():
        def order():
            def message():
                list_t=[]
                for i in s3:
                    if i == "Borjomi":
                        a = 800
                        b = f'{i}---------------------{a}'
                        list_t.append(b)
                    elif i=="Asu":
                        a = 300
                        b = f'{i}--------------------------{a}'
                        list_t.append(b)
                    elif i == 'Espresso':
                        a = 300
                        b = f'{i}-------------------{a}'
                        list_t.append(b)
                    elif i == 'Pepsi':
                        a = 400
                        b = f'{i}------------------------{a}'
                        list_t.append(b)
                    elif i =='Americano':
                        a = 400
                        b = f'{i}--------------------{a}'
                        list_t.append(b)
                    elif i == 'Cheesecake':
                        a = 600
                        b = f'{i}-------------------{a}'
                        list_t.append(b)
                    elif i == 'Pancakes':
                        a = 600
                        b = f'{i}-------------------{a}'
                        list_t.append(b)
                    elif i == 'IceCream':
                        a = 600
                        b = f'{i}---------------------{a}'
                        list_t.append(b)
                    elif i == 'Hamburger':
                        a = 550
                        b = f'{i}-------------------{a}'
                        list_t.append(b)
                    elif i =='Cheeseburger':
                        a = 550
                        b = f'{i}-----------------{a}'
                        list_t.append(b)
                    elif i =='BigKing':
                        a = 1000
                        b = f'{i}---------------------{a}'
                        list_t.append(b)
                    elif i == 'Vopper':
                        a = 1000
                        b = f'{i}----------------------{a}'
                        list_t.append(b)
                    elif i =='Margarita':
                        a = 1150
                        b = f'{i}-------------------{a}'
                        list_t.append(b)
                    elif i == 'Bolognese':
                        a = 2200
                        b = f'{i}-------------------{a}'
                        list_t.append(b)
                    elif i =='SalamiPizza':
                        a = 1700
                        b = f'{i}-----------------{a}'
                        list_t.append(b)
                #determine data and time 
                from datetime import date
                today = date.today()
                #print("Today's date:", today)

                from datetime import datetime
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                #print("Current Time =", current_time)

                Addres =f'Address: Lorem Ipsum 85-100 \n                 CASH RECEIPT \n {stars} \n Description---------------Price \n Your order:'
                end = f'                THANK YOU \n Your order will be ready for pickup in 15 minutes. \n {ID} \n Data:{today}           Time:{current_time}'
                
                len_list_t=len(list_t)
                if len_list_t==1:
                    for i in list_t:x1=i
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {x1} \n Total:{total_amount} T  \n {stars} \n {end}' )
                elif len_list_t==2:
                    x1,x2=list_t
                    joint=f'{x1} \n {x2}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==3:
                    x1,x2,x3=list_t
                    joint=f'{x1} \n {x2} \n {x3}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==4:
                    x1,x2,x3,x4=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==5:
                    x1,x2,x3,x4,x5=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==6:
                    x1,x2,x3,x4,x6=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==7:
                    x1,x2,x3,x4,x6,x7=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==8:
                    x1,x2,x3,x4,x6,x7,x8=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==9:
                    x1,x2,x3,x4,x6,x7,x8,x9=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8} \n {x9}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==10:
                    x1,x2,x3,x4,x6,x7,x8,x9,x10=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8} \n {x9} \n {x10}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==11:
                    x1,x2,x3,x4,x6,x7,x8,x9,x10,x11=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8} \n {x9} \n {x10} \n {x11}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==12:
                    x1,x2,x3,x4,x6,x7,x8,x9,x10,x11,x12=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8} \n {x9} \n {x10} \n {x11} \n {x12}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==13:
                    x1,x2,x3,x4,x6,x7,x8,x9,x10,x11,x12,x13=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8} \n {x9} \n {x10} \n {x11} \n {x12} \n {x13}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==14:
                    x1,x2,x3,x4,x6,x7,x8,x9,x10,x11,x12,x13,x14=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8} \n {x9} \n {x10} \n {x11} \n {x12} \n {x13} \n {x14}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {stars} \n {ID} \n {joint} \n Total:{total_amount} T \n {time} \n {stars} \n THANK YOU' )
                elif len_list_t==15:
                    x1,x2,x3,x4,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8} \n {x9} \n {x10} \n {x11} \n {x12} \n {x13} \n {x14} \n {x15}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
                elif len_list_t==16:
                    x1,x2,x3,x4,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16=list_t
                    joint=f'{x1} \n {x2} \n {x3} \n {x4} \n {x5} \n {x6} \n {x7} \n {x8} \n {x9} \n {x10} \n {x11} \n {x12} \n {x13} \n {x14} \n {x15} \n {x16}'
                    messagebox.showinfo('Administration "b.for" cafe', f'{Addres} \n {joint} \n Total:{total_amount} T \n {stars} \n {end}' )
            s1 = entry_order.get()
            s2 = ' ,:@.-()/'
            for i in s2:
                s1 = s1.replace(i, ' ')
            s3=list(filter(None, s1.split()))
            total_amount = 0
            for i in s3:
                if i=="Asu" or i == 'Espresso':
                    total_amount = total_amount + 300
                elif i == 'BlackTea':
                    total_amount = total_amount + 200
                elif i == 'Pepsi' or  i =='Americano':
                    total_amount = total_amount + 400
                elif i == 'Cheesecake' or i == 'Pancakes' or i == 'IceCream':
                    total_amount = total_amount + 600
                elif i == 'Hamburger' or i == 'Cheeseburger':
                    total_amount = total_amount + 550
                elif i =='Cappuccino':
                    total_amount = total_amount + 500
                elif i =='BigKing' or i == 'Vopper':
                    total_amount = total_amount + 1000
                elif i =='Margarita':
                    total_amount = total_amount + 1150
                elif i == 'Bolognese':
                    total_amount = total_amount + 2200
                elif i =='SalamiPizza':
                    total_amount = total_amount + 1700
            message()
        answer = entry_answer.get()
        if answer == 'y':
            menu = ('Pepsi','400tg'),('Asu','300tg'),('BlackTea','200tg'),('Americano','400tg'),('Cappuccino','500tg'),('Espresso','300tg'),('Cheesecake','600tg'),('Pancakes','600tg'),('IceCream','600tg'),('Margarita','1150tg'),('Bolognese','2200tg'),('SalamiPizza','1700'),('Hamburger','550tg'),('Cheeseburger','550tg'),('BigKing','1000tg'),('Vopper','1000tg')
            table = Table(win, headings=('Description', 'price'), rows=(menu))
            table.pack(expand=tk.YES, fill=tk.BOTH)
            l3=Label(win,text=f"Are you ready to order?: ",bg='#DEB887',fg='#F5FFFA')
            l3.config(font = ('Times',18))
            l3.pack()
            entry_order = Entry(win, width = 45, bg = '#D3D3D3')
            entry_order.pack()
            entry_order.focus()
            but2 = Button(win, text = "Click",activebackground='#C0C0C0',activeforeground='#696969', command = order)
            but2.pack()
        else:
            l3=Label(win,text='Goodbye!',bg='#DEB887',fg='#F5FFFA')
            l3.config(font = ('Times',18))
            l3.pack()
           
    l2 = Label(win, text = 'Would you like to place an order?:(y/n) ',bg='#DEB887', fg ='#F5FFFA')
    l2.config(font = ('Times',18))
    l2.pack()
    entry_answer = Entry (win, width = 15, bg = '#D3D3D3')
    entry_answer.pack()
    entry_answer.focus()
    but2 = Button(win, text = "Click",activebackground='#C0C0C0',activeforeground='#696969', command = answer)
    but2.pack()

def hello():
    name = entry_name.get()
    l1.config(text = f'Hello {name},welcome to b.for food Order')
    suggestion()

    
win = Tk()
win.title("Eat & chat")
win.geometry('1124x598')
win["bg"]="#DEB887"

#l=Label
l1 = Label(win, text = 'Enter your name',bg='#DEB887', fg ='#F5FFFA')
l1.config(font = ('Times',18))
l1.pack()

entry_name = Entry (win, width = 15, bg = '#D3D3D3')
entry_name.pack()
entry_name.focus()

but = Button(win, text = "Click",activebackground='#C0C0C0',activeforeground='#696969', command = hello)
but.pack()

win.mainloop()
