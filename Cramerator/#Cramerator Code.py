#Cramerator Code


#DA = float((Cx1*Cy2*Cz3)+(Cy1*Cz3*Cx3)+(Cz1*Cx2*Cy3)-(Cz1*Cy2*Cx3)-(Cy1*Cx2*Cz3)-(Cx1*Cz2*Cy3))
#DX = float((r1*Cy2*Cz3)+(Cy1*Cz2*r3)+(Cz1*Cx2*r3)-(Cx1*Cz2*r3)-(r1*Cx2*Cz3)-(Cz1*r2*Cx3))
#DY = float((Cx1*r2*Cz3)+(r1*Cz2*Cx3)+(Cz1*Cx2*r3)-(Cx1*r2*Cy3)-(Cx)-())
#DZ = float(())





#Systems of equations solver with cramer method
#By WaxGian "2P2L"


from tkinter import Label, StringVar
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Window Settings
window = Tk()
window.title('Cramerator')
window.geometry("486x818")
window.configure(bg = "#152D35")

#Window Structur Gui

canvas = Canvas(
    window,
    bg = "#152D35",
    height = 818,
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


#Gui Input

# Define a dictionary with the common properties
entry_properties = {
    'bd': 0,
    'bg': "#355B63",
    'highlightthickness': 0,
    'font': ("Arial", 22)
}

# Define a list with the positions and image paths for each Entry widget
entries_info = [
    (67.0, 54.5, "entry_1.png", 39.5, 43.0),
    (175.0, 54.5, "entry_2.png", 147.5, 43.0),
    # Add the rest of the entries here...
]

# Create the Entry widgets in a loop
entries = []
for x, y, image_path, entry_x, entry_y in entries_info:
    entry_image = PhotoImage(file=relative_to_assets(image_path))
    entry_bg = canvas.create_image(x, y, image=entry_image)
    entry = Entry(**entry_properties)
    entry.place(x=entry_x, y=entry_y, width=55.0, height=23.0)
    entries.append(entry)

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
