#ToDo set actions for buttons
# finish update and close button functions



from tkinter import*
import sqlite3
import book_backend	

def view_command():
	list_view.delete(0,END) # clearing the list upon call to avoid replicas in view
	for i in book_backend.view():
		list_view.insert(END,i)

def search_command():
	list_view.delete(0,END)
	for i in book_backend.search(tEntry.get(),aEntry.get(),yEntry.get(),isbnEntry.get()):
		list_view.insert(END,i)

def add_command():
	list_view.delete(0,END)
	book_backend.insert(tEntry.get(),aEntry.get(),yEntry.get(),isbnEntry.get())#we add to our db first
	list_view.insert(END,(tEntry.get(),aEntry.get(),yEntry.get(),isbnEntry.get()))#manually adding to our view as a success feedback mechanism

def get_selected_row(event):
	global selected_turple
	index = list_view.curselection()[0]
	# return(index)
	selected_turple = list_view.get(index)
	



def update_command():
	pass

def delete_command():
	book_backend.delete(selected_turple[0])

def close_command():
	sys.exit()

window = Tk()

#functions

# def add_book(title, author, year, isbn_no ):
# 	isbn_no = str(isbnEntry
# 	insert(tEntry, aEntry, yEntry, isbn_no)
#
# def display():
# 	returnList =view()
# 	for i in range (0,len(returnList)):
# 		i = returnList[i]
# 		book_view.insert(END, i)

#Title start--------------------------------
tLabel= 'Title'
title_txt= Label(window,text = tLabel)
title_txt.grid(row=0,column=0)

tEntry= StringVar()
title_entry= Entry(window, textvariable = tEntry)
title_entry.grid(row = 0, column =1)

#Title end--------------------------------

#Year start--------------------------------
yLabel= 'Year'
title_txt= Label(window,text = yLabel)
title_txt.grid(row=1,column=0)

yEntry= StringVar()
title_entry= Entry(window, textvariable = yEntry)
title_entry.grid(row = 1, column =1)

#Year end--------------------------------


#Author start--------------------------------
aLabel= 'Author'
title_txt= Label(window,text = aLabel)
title_txt.grid(row=0,column=2)

aEntry= StringVar()
title_entry= Entry(window, textvariable = aEntry)
title_entry.grid(row = 0, column =3)

#Author end--------------------------------



#ISBN end--------------------------------

isbnLabel= 'ISBN'
title_txt= Label(window,text = isbnLabel)
title_txt.grid(row=1,column=2)

isbnEntry= StringVar()
title_entry= Entry(window, textvariable = isbnEntry)
title_entry.grid(row = 1, column =3)


#ISBN end--------------------------------

#Buttons---------------------------------

view_btn_txt = 'View All'
view_btn = Button(window, text=view_btn_txt, width = 12, command =view_command)
view_btn.grid(row = 2, column = 3)

#used a wrapper function in here (searc_command), since we cannot pass args in the button
ser_btn_txt = 'Search Entry'
view_btn = Button(window, text=ser_btn_txt, width = 12, command=search_command)
view_btn.grid(row = 3, column = 3)

add_btn_txt = 'Add Entry'
view_btn = Button(window, text=add_btn_txt, width = 12, command =add_command)
view_btn.grid(row = 4, column = 3)

upd_btn_txt = 'Update Selected'
view_btn = Button(window, text=upd_btn_txt, width = 12 ,command=update_command)
view_btn.grid(row = 5, column = 3)



close_btn_txt = 'Close'
view_btn = Button(window, text=close_btn_txt , width = 12)
view_btn.grid(row = 7, column = 3)



list_view= Listbox(window, height = 6, width = 35)
list_view.grid(row = 3, column = 0, rowspan = 6, columnspan =2)

scrollbar = Scrollbar(window)
scrollbar.grid(row = 2, column =2, rowspan=6)

list_view.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command= list_view.yview)

#using the bind method
list_view.bind('<<ListboxSelect>>',get_selected_row)

del_btn_txt = 'Delete Selected'
view_btn = Button(window, text=del_btn_txt, width = 12, command = delete_command)
view_btn.grid(row = 6, column = 3)

window.mainloop()


