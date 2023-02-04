# import tkinter as tk

# root = tk.Tk()
# logo = tk.PhotoImage(file="cret.png")

# w1 = tk.Label(root, image=logo).pack(side="right")

# explanation = """At present, only GIF and PPM/PGM
# formats are supported, but an interface 
# exists to allow additional image file
# formats to be added easily."""

# w2 = tk.Label(root, 
#               justify=tk.LEFT,
#               padx = 10, 
#               text=explanation).pack(side="left")
# root.mainloop()

#===================================================
# import tkinter as tk

# root = tk.Tk()
# tk.Label(root, 
# 		 text="Red Text in Times Font",
# 		 fg = "red",
# 		 font = "Times").pack()
# tk.Label(root, 
# 		 text="Green Text in Helvetica Font",
# 		 fg = "light green",
# 		 bg = "dark green",
# 		 font = "Helvetica 16 bold italic").pack()
# tk.Label(root, 
# 		 text="Blue Text in Verdana bold",
# 		 fg = "blue",
# 		 bg = "yellow",
# 		 font = "Verdana 10 bold").pack()

# root.mainloop()

#===================================================

# from tkinter import *

# root = Tk()
# root.title("tk example")
# root.configure(background="yellow")
# root.minsize(200, 200)
# root.maxsize(500, 500)
# root.geometry("300x300+50+50")
# root.mainloop()
#===================================================

# from tkinter import *

# root = Tk()
# root.title("Tk Example")
# root.minsize(200, 200)  # width, height
# root.geometry("300x300+50+50")

# # Create Label in our window
# text = Label(root, text="Nothing will work unless you do.")
# text.pack()
# text2 = Label(root, text="- Maya Angelou")
# text2.pack()
# root.mainloop()
#===================================================

# from tkinter import *

# root = Tk()  # create root window
# root.title("Frame Example")
# root.config(bg="skyblue")

# # Create Frame widget
# left_frame = Frame(root, width=200, height=400)
# left_frame.grid(row=0, column=0, padx=10, pady=5)
# root.mainloop()
#===================================================

# from tkinter import *

# root = Tk()  # create root window
# root.title("Basic GUI Layout")  # title of the GUI window
# root.maxsize(900, 600)  # specify the max size the window can expand to
# root.config(bg="skyblue")  # specify background color

# # Create left and right frames
# left_frame = Frame(root, width=200, height=400, bg='grey')
# left_frame.grid(row=0, column=0, padx=10, pady=5)

# right_frame = Frame(root, width=650, height=400, bg='grey')
# right_frame.grid(row=0, column=1, padx=10, pady=5)

# # Create frames and labels in left_frame
# Label(left_frame, text="Original Image").grid(row=0, column=0, padx=5, pady=5)

# # load image to be "edited"
# image = PhotoImage(file="cret.png")
# original_image = image.subsample(3,3)  # resize image using subsample
# Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

# # Display image in right_frame
# Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)

# # Create tool bar frame
# tool_bar = Frame(left_frame, width=180, height=185)
# tool_bar.grid(row=2, column=0, padx=5, pady=5)

# # Example labels that serve as placeholders for other widgets
# Label(tool_bar, text="Tools", relief=RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget
# Label(tool_bar, text="Filters", relief=RAISED).grid(row=0, column=1, padx=5, pady=3, ipadx=10)

# # Example labels that could be displayed under the "Tool" menu
# Label(tool_bar, text="Select").grid(row=1, column=0, padx=5, pady=5)
# Label(tool_bar, text="Crop").grid(row=2, column=0, padx=5, pady=5)
# Label(tool_bar, text="Rotate & Flip").grid(row=3, column=0, padx=5, pady=5)
# Label(tool_bar, text="Resize").grid(row=4, column=0, padx=5, pady=5)
# Label(tool_bar, text="Exposure").grid(row=5, column=0, padx=5, pady=5)
# root.mainloop()
#===================================================

# from tkinter import *

# # https://www.pythonguis.com/tutorials/create-buttons-in-tkinter/

# root = Tk()  # create parent window

# #  If you are developing your own GUI 
# #  and have a few buttons that don't 
# #  yet do anything, then there is also 
# #  a way to make the button inactive. 
# #  Just add state=DISABLED as one of the 
# #  parameters and the button cannot be clicked

# # use Button and Label widgets to create a simple TV remote
# turn_on = Button(root, text="ON")
# turn_on.pack()

# turn_off = Button(root, text="OFF", command=root.quit)
# turn_off.pack()

# volume = Label(root, text="VOLUME")
# volume.pack()

# vol_up = Button(root, text="+")
# vol_up.pack()

# vol_down = Button(root, text="-")
# vol_down.pack()

# root.mainloop()

# ========================
import tkinter
tkinter._test()