import tkinter
window = tkinter.Tk()

#to rename the title of window
window.title("resumeShortlistingSoftwareGUI")

#pack is used to show the object in the window
label = tkinter.Label(window, text ="Welcome to Resume Shortlisting Software", font =("Arial Bold",50)).pack()
window.geometry('350x200')
#|1.grid(column=0,row=0)

window.mainloop()