import os

import customtkinter as ctk
from PIL import Image

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
ctk.set_default_color_theme(f"{CURRENT_PATH}\\blue.json")

ICONS = {
    "info": ctk.CTkImage(light_image=Image.open(f"{CURRENT_PATH}\\ICONS\\info.png"),
                         dark_image=Image.open(f"{CURRENT_PATH}\\ICONS\\info.png"),
                         size=(24, 24)),
    "warning": ctk.CTkImage(light_image=Image.open(f"{CURRENT_PATH}\\ICONS\\warning.png"),
                            dark_image=Image.open(f"{CURRENT_PATH}\\ICONS\\warning.png"),
                            size=(24, 24)),
    "error": ctk.CTkImage(light_image=Image.open(f"{CURRENT_PATH}\\ICONS\\error.png"),
                          dark_image=Image.open(f"{CURRENT_PATH}\\ICONS\\error.png"),
                          size=(24, 24)),
    "close": ctk.CTkImage(light_image=Image.open(f"{CURRENT_PATH}\\ICONS\\close_black.png"),
                          dark_image=Image.open(f"{CURRENT_PATH}\\ICONS\\close_white.png"),
                          size=(20, 20))
}
LINK_BTN = {
    "width": 70,
    "height": 25,
    "fg_color": "transparent",
    "hover": False,
    "text_color": "#3574F0"
}


def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_height = int((screen_width / 2) - (width / 2))
    window_width = int((screen_height / 2) - (height / 2))
    root.geometry(f"{width}x{height}+{window_height}+{window_width}")


def place_frame(master, frame, horizontal="right", vertical="bottom"):
    master_width = master.winfo_width()
    master_height = master.winfo_height()

    frame_width = frame.winfo_reqwidth()
    frame_height = frame.winfo_reqheight()

    frame_x = 20 if horizontal == "left" else master_width - frame_width - 20
    frame_y = 20 if vertical == "top" else master_height - frame_height - 20

    frame.place(x=frame_x, y=frame_y)


class CTkBanner(ctk.CTkFrame):
    def __init__(self, master, state: str = "info", title: str = "Title", btn1: str = "Action A",
                 btn2: str = "Action B", side: str = "right_bottom"):
        self.root = master
        self.width = 400
        self.height = 100
        super().__init__(self.root, width=self.width, height=self.height, corner_radius=5, border_width=1)

        self.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1)
        self.event = None

        self.horizontal, self.vertical = side.split("_")

        if state not in ICONS or ICONS[state] is None:
            icon = ICONS["info"]
        else:
            icon = ICONS[state]

        title_label = ctk.CTkLabel(self, text=f"  {title}", font=("", 16), image=icon,
                                   compound="left")
        title_label.grid(row=0, column=0, sticky="w", padx=15, pady=10)

        close_btn = ctk.CTkButton(self, text="", image=ICONS["close"], width=20, height=20, hover=False,
                                  fg_color="transparent", command=self.button_event)
        close_btn.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        btn_1 = ctk.CTkButton(self, text=btn1, **LINK_BTN, command=lambda: self.button_event(btn1))
        btn_1.grid(row=1, column=0, padx=(40, 5), pady=10, sticky="w")

        btn_2 = ctk.CTkButton(self, text=btn2, **LINK_BTN,
                              command=lambda: self.button_event(btn2))
        btn_2.grid(row=1, column=1, padx=5, pady=10, sticky="w")

        place_frame(self.root, self, self.horizontal, self.vertical)
        self.root.bind("<Configure>", self.update_position, add="+")

    def update_position(self, event):
        place_frame(self.root, self, self.horizontal, self.vertical)
        self.update_idletasks()
        self.root.update_idletasks()

    def get(self):
        if self.winfo_exists():
            self.master.wait_window(self)
        return self.event

    def button_event(self, event=None):
        self.root.unbind("<Configure>")
        self.grab_release()
        self.destroy()
        self.event = event


if __name__ == "__main__":
    app = ctk.CTk()
    center_window(app, 800, 500)
    # Usage
    banner = CTkBanner(master=app, state="error", title="title", btn1="Action 1", btn2="Action 2", side="right_bottom")
    answer = banner.get() # get answer:
    app.mainloop()
