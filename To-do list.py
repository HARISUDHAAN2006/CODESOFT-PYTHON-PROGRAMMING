from tkinter import Entry, Frame, Button, Tk, Label, END, Listbox
from tkinter import messagebox


def addTask():
    task = taskentry.get()
    if task.strip():
        task_listbox.insert(END, task)
        taskentry.delete(0, END)
    else:
        messagebox.showwarning("No input error", "Please enter a task to continue!")

def removetask():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("No selection error", "No task is selected to remove!")


w = Tk()
w.title("To-Do List")
w.geometry("400x500+500+150")
w.config(bg="hotpink")


titlelabel = Label(w, text="My To-Do List", font=("Verdana", 18, "bold"), bg="lightblue")
titlelabel.pack(pady=10)


taskentry = Entry(w, font=("Arial", 14), width=30)
taskentry.pack(pady=10)


buttonframe = Frame(w)
buttonframe.pack(pady=5)

add_button = Button(buttonframe, text="Add Task", font=("Verdana", 14), width=13, command=addTask)
add_button.grid(row=0, column=0, padx=10)

remove_button = Button(buttonframe, text="Remove Task", font=("Verdana", 14), width=13, command=removetask)
remove_button.grid(row=0, column=1, padx=10)


task_listbox = Listbox(w, font=("Verdana", 14), width=38, height=17, selectbackground="skyblue")
task_listbox.pack(pady=20)


w.mainloop()
