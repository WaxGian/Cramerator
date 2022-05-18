#Cramerator Code


#DA = float((Cx1*Cy2*Cz3)+(Cy1*Cz3*Cx3)+(Cz1*Cx2*Cy3)-(Cz1*Cy2*Cx3)-(Cy1*Cx2*Cz3)-(Cx1*Cz2*Cy3))
#DX = float((r1*Cy2*Cz3)+(Cy1*Cz2*r3)+(Cz1*Cx2*r3)-(Cx1*Cz2*r3)-(r1*Cx2*Cz3)-(Cz1*r2*Cx3))
#DY = float((Cx1*r2*Cz3)+(r1*Cz2*Cx3)+(Cz1*Cx2*r3)-(Cx1*r2*Cy3)-(Cx)-())
#DZ = float(())





#Systems of equations solver with cramer method
#By WaxGian "2P2L"


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Window Settings
window = Tk()
window.title('Cramerator')
window.geometry("486x918")
window.configure(bg = "#152D35")


#Window Structur Gui
canvas = Canvas(
    window,
    bg = "#152D35",
    height = 918,
    width = 486,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    295.5,
    485.9999694824219,
    296.0,
    fill="#C4C4C4",
    outline="")

canvas.create_rectangle(
    0.0,
    484.1188049316406,
    486.0,
    487.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    131.0,
    322.0,
    anchor="nw",
    text="Result X :",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 36 * -1)
)

canvas.create_text(
    131.0,
    411.0,
    anchor="nw",
    text="Result Y :",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 36 * -1)
)






button_image_C = PhotoImage(
    file=relative_to_assets("button_C.png"))
button_C = Button(
    image=button_image_C,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_C clicked"),
    relief="flat"
)
button_C.place(
    x=16.0,
    y=507.0,
    width=80.0,
    height=80.0
)

button_image_SOLVE = PhotoImage(
    file=relative_to_assets("button_SOLVE.png"))
button_SOLVE = Button(
    image=button_image_SOLVE,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_SOLVE clicked"),
    relief="flat"
)
button_SOLVE.place(
    x=142.0,
    y=506.0,
    width=201.0,
    height=80.0
)

button_image_BS = PhotoImage(
    file=relative_to_assets("button_BS.png"))
button_BS = Button(
    image=button_image_BS,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_BS clicked"),
    relief="flat"
)
button_BS.place(
    x=391.0,
    y=507.0,
    width=80.0,
    height=80.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=16.0,
    y=612.0,
    width=80.0,
    height=80.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=142.0,
    y=612.0,
    width=80.0,
    height=80.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=265.0,
    y=613.0,
    width=80.0,
    height=80.0
)

button_image_MINUS = PhotoImage(
    file=relative_to_assets("button_MINUS.png"))
button_MINUS = Button(
    image=button_image_MINUS,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_MINUS clicked"),
    relief="flat"
)
button_MINUS.place(
    x=391.0,
    y=612.0,
    width=80.0,
    height=80.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=17.0,
    y=718.0,
    width=80.0,
    height=80.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=142.0,
    y=717.0,
    width=80.0,
    height=80.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=267.0,
    y=718.0,
    width=80.0,
    height=80.0
)

button_image_COMMA = PhotoImage(
    file=relative_to_assets("button_COMMA.png"))
button_COMMA = Button(
    image=button_image_COMMA,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_COMMA clicked"),
    relief="flat"
)
button_COMMA.place(
    x=391.0,
    y=718.0,
    width=80.0,
    height=80.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=16.0,
    y=822.0,
    width=80.0,
    height=80.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=142.0,
    y=822.0,
    width=80.0,
    height=80.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=265.0,
    y=824.0,
    width=80.0,
    height=80.0
)

button_image_0 = PhotoImage(

    file=relative_to_assets("button_0.png"))
button_0 = Button(
    image=button_image_0,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_0 clicked"),
    relief="flat"
)
button_0.place(
    x=391.0,
    y=822.0,
    width=80.0,
    height=80.0
)





#Gui Input

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    67.0,
    54.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_1.place(
    x=39.5,
    y=43.0,
    width=55.0,
    height=23.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    175.0,
    54.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_2.place(
    x=147.5,
    y=43.0,
    width=55.0,
    height=23.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    175.0,
    144.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_3.place(
    x=147.5,
    y=133.0,
    width=55.0,
    height=23.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    283.0,
    234.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_4.place(
    x=255.5,
    y=223.0,
    width=55.0,
    height=23.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    283.0,
    144.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_5.place(
    x=255.5,
    y=133.0,
    width=55.0,
    height=23.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    283.0,
    54.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_6.place(
    x=255.5,
    y=43.0,
    width=55.0,
    height=23.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    417.0,
    54.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_7.place(
    x=389.5,
    y=43.0,
    width=55.0,
    height=23.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    417.0,
    144.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_8.place(
    x=389.5,
    y=133.0,
    width=55.0,
    height=23.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    417.0,
    234.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_9.place(
    x=389.5,
    y=223.0,
    width=55.0,
    height=23.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    175.0,
    234.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_10.place(
    x=147.0,
    y=223.0,
    width=55.0,
    height=23.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    67.0,
    144.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_11.place(
    x=39.5,
    y=133.0,
    width=55.0,
    height=23.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    67.0,
    234.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#355B63",
    highlightthickness=0,
    font=("Arial", 22)
)
entry_12.place(
    x=39.5,
    y=223.0,
    width=55.0,
    height=23.0
)



canvas.create_oval(
    320.0,
    305.0,
    411.0,
    375.0,
    fill="#355B63",
    outline="")

canvas.create_oval(
    320.0,
    395.0,
    411.0,
    466.0,
    fill="#355B63",
    outline="")

canvas.create_text(
    111.0,
    34.0,
    anchor="nw",
    text="x",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    219.0,
    34.0,
    anchor="nw",
    text="y",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    219.0,
    124.0,
    anchor="nw",
    text="y",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    327.0,
    124.0,
    anchor="nw",
    text="z",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    327.0,
    34.0,
    anchor="nw",
    text="z",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    353.0,
    34.0,
    anchor="nw",
    text="=",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    353.0,
    124.0,
    anchor="nw",
    text="=",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    353.0,
    214.0,
    anchor="nw",
    text="=",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    327.0,
    214.0,
    anchor="nw",
    text="z",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    219.0,
    214.0,
    anchor="nw",
    text="y",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    111.0,
    124.0,
    anchor="nw",
    text="x",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)

canvas.create_text(
    111.0,
    214.0,
    anchor="nw",
    text="x",
    fill="#FFA800",
    font=("RedHatDisplay Bold", 32 * -1)
)
window.resizable(False, False)
window.mainloop()
