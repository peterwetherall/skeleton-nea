import tkinter as tk
root = tk.Tk()
root.geometry("960x687")
root.resizable(0, 0)
root.title("Body Parts")
root.config(background="white")

skeleton = tk.PhotoImage(file="skele.gif")
tk.Label(root, image=skeleton, width=303, height=662).place(x=10, y=10)

parts = ["skull", "jaw", "shoulder", "upperarm", "spine", "rib", "lowerarmhigh", "lowerarmlow", "tailbone", "hip", "pelvic", "upperleg", "lowerleghigh", "lowerleglow", "knee"]

button = tk.PhotoImage(file="button.gif")
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(0, info)).place(x=159, y=38)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(1, info)).place(x=159, y=98)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(2, info)).place(x=196, y=135)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(3, info)).place(x=225, y=176)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(4, info)).place(x=159, y=189)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(5, info)).place(x=184, y=200)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(6, info)).place(x=75, y=270)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(7, info)).place(x=56, y=301)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(8, info)).place(x=159, y=297)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(9, info)).place(x=189, y=280)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(10, info)).place(x=159, y=326)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(11, info)).place(x=119, y=407)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(12, info)).place(x=119, y=518)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(13, info)).place(x=133, y=548)
tk.Button(root, image=button, width=5, height=5, bg="#C1D5B4", command=lambda:show(14, info)).place(x=187, y=459)

infoImage = tk.PhotoImage(file="skull.gif")
info = tk.Label(root, image=infoImage, width=620, height=620)
info.place(x=323, y=30)

def show(num, info):
    imgName = parts[num] + ".gif"
    print("Showing:", imgName)
    img = tk.PhotoImage(file=imgName)
    info.config(image=img)
    info.image = img

def leave():
    root.destroy()
root.mainloop()
