from tkinter import * 
import calendar
 

def showCal() :
    new_gui = Tk()   
    new_gui.config(background = "#00154f")    
    new_gui.title("CALENDER") 
      
    fetch_year = int(year_field.get()) 
    l1=Label(new_gui,text=fetch_year,bg = "#f4af1b",fg="#00154f",font = ("times", 30, 'bold'),width=20) 
    l1.grid(row = 1, column = 1) 
    cal_content = calendar.calendar(fetch_year)    
    cal_year = Label(new_gui, text = cal_content, font =("times",10, 'bold'),bg = "#eedc82",fg="#00154f")   
    cal_year.grid(row = 5, column = 1,pady=20,padx=20)    
    new_gui.mainloop()
 
     
gui = Tk()  
gui.config(background = "white")    
gui.title("CALENDER")     
   
cal = Label(gui, text = "CALENDAR", bg = "#f4af1b",fg="#00154f",font = ("times", 30, 'bold'))
cal.grid(row = 1, column = 1,columnspan=2)   

year = Label(gui, text = "Enter Year :",fg="#00154f",bg="white",font = ("times",30))     
year.grid(row = 2, column = 1)

year_field = Entry(gui,bg = "#eedc82",fg="#00154f",width=10,font = ("times",20)) 
year_field.grid(row = 2, column = 2,padx=5,pady=5)

Show = Button(gui, text = "Show Calendar", fg = "#00154f",bg = "#f4af1b",width=12,font = ("times",15), command = showCal,activebackground="#00154f",activeforeground="#f4af1b") 
Show.grid(row = 4, column = 1)

Exit = Button(gui, text = "Exit", fg = "White", bg = "red", width=12,font = ("times",15,"bold"),command = exit)     
Exit.grid(row = 4, column = 2,padx=5,pady=5)   
 
gui.mainloop()