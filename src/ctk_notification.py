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


class CTkNotification(ctk.CTkFrame):
    def __init__(self, master, state: str = "info", message: str = "message", side: str = "right_bottom"):
        self.root = master
        self.width = 400
        self.height = 60
        super().__init__(self.root, width=self.width, height=self.height, corner_radius=5, border_width=1)
        self.grid_propagate(False)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.horizontal, self.vertical = side.split("_")

        if state not in ICONS or ICONS[state] is None:
            icon = ICONS["info"]
        else:
            icon = ICONS[state]

        self.message_label = ctk.CTkLabel(self, text=f"  {message}", font=("", 13), image=icon, compound="left")
        self.message_label.grid(row=0, column=0, sticky="nsw", padx=15, pady=10)

        self.close_btn = ctk.CTkButton(self, text="", image=ICONS["close"], width=20, height=20, hover=False,
                                       fg_color="transparent", command=self.close_notification)
        self.close_btn.grid(row=0, column=1, sticky="nse", padx=10, pady=10)

        place_frame(self.root, self, self.horizontal, self.vertical)
        self.root.bind("<Configure>", self.update_position, add="+")

    def update_position(self, event):
        place_frame(self.root, self, self.horizontal, self.vertical)
        self.update_idletasks()
        self.root.update_idletasks()

    def close_notification(self):
        self.root.unbind("<Configure>")
        self.destroy()


if __name__ == "__main__":
    app = ctk.CTk()
    center_window(app, 800, 500)
    # Usage
    CTkNotification(master=app, state="info", message="message", side="right_bottom")
    app.mainloop()
