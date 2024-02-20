import os
import sys

import customtkinter as ctk
from PIL import Image

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
ctk.set_default_color_theme(f"{CURRENT_PATH}\\blue.json")

ICONS = {
    "info": ctk.CTkImage(light_image=Image.open(f"{CURRENT_PATH}\\ICONS\\info.png"),
                         dark_image=Image.open(f"{CURRENT_PATH}\\ICONS\\info.png"),
                         size=(30, 30)),
    "warning": ctk.CTkImage(light_image=Image.open(f"{CURRENT_PATH}\\ICONS\\warning.png"),
                            dark_image=Image.open(f"{CURRENT_PATH}\\ICONS\\warning.png"),
                            size=(30, 30)),
    "error": ctk.CTkImage(light_image=Image.open(f"{CURRENT_PATH}\\ICONS\\error.png"),
                          dark_image=Image.open(f"{CURRENT_PATH}\\ICONS\\error.png"),
                          size=(30, 30)),
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


class CTkAlert(ctk.CTkToplevel):
    def __init__(self, state: str = "info", title: str = "Title",
                 body_text: str = "Body text", btn1: str = "OK", btn2: str = "Cancel"):
        super().__init__()
        self.old_y = None
        self.old_x = None
        self.width = 420
        self.height = 200
        center_window(self, self.width, self.height)
        self.resizable(False, False)
        self.overrideredirect(True)
        self.lift()

        self.x = self.winfo_x()
        self.y = self.winfo_y()
        self.event = None

        if sys.platform.startswith("win"):
            self.transparent_color = self._apply_appearance_mode(self.cget("fg_color"))
            self.attributes("-transparentcolor", self.transparent_color)

        self.bg_color = self._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.frame_top = ctk.CTkFrame(self, corner_radius=5, width=self.width,
                                      border_width=1,
                                      bg_color=self.transparent_color, fg_color=self.bg_color)
        self.frame_top.grid(sticky="nsew")
        self.frame_top.bind("<B1-Motion>", self.move_window)
        self.frame_top.bind("<ButtonPress-1>", self.old_xy_set)
        self.frame_top.grid_columnconfigure(0, weight=1)
        self.frame_top.grid_rowconfigure(1, weight=1)

        if state not in ICONS or ICONS[state] is None:
            icon = ICONS["info"]
        else:
            icon = ICONS[state]

        title_label = ctk.CTkLabel(self.frame_top, text=f"  {title}", font=("", 18), image=icon,
                                   compound="left")
        title_label.grid(row=0, column=0, sticky="w", padx=15, pady=20)
        title_label.bind("<B1-Motion>", self.move_window)
        title_label.bind("<ButtonPress-1>", self.old_xy_set)

        close_btn = ctk.CTkButton(self.frame_top, text="", image=ICONS["close"], width=20, height=20, hover=False,
                                  fg_color="transparent", command=self.button_event)
        close_btn.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        message = ctk.CTkLabel(self.frame_top,
                               text=body_text,
                               justify="left", anchor="w", wraplength=self.width - 30)
        message.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="nsew", columnspan=2)

        btn_1 = ctk.CTkButton(self.frame_top, text=btn1, width=120, command=lambda: self.button_event(btn1),
                              text_color="white")
        btn_1.grid(row=2, column=0, padx=(10, 5), pady=20, sticky="e")

        btn_2 = ctk.CTkButton(self.frame_top, text=btn2, width=120, fg_color="transparent", border_width=1,
                              command=lambda: self.button_event(btn2), text_color=("black", "white"))
        btn_2.grid(row=2, column=1, padx=(5, 10), pady=20, sticky="e")

        self.bind("<Escape>", lambda e: self.button_event())

    def get(self):
        if self.winfo_exists():
            self.master.wait_window(self)
        return self.event

    def old_xy_set(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def move_window(self, event):
        self.y = event.y_root - self.old_y
        self.x = event.x_root - self.old_x
        self.geometry(f'+{self.x}+{self.y}')

    def button_event(self, event=None):
        self.grab_release()
        self.destroy()
        self.event = event


if __name__ == "__main__":
    # Usage
    alert = CTkAlert(state="error", title="title", body_text="body text", btn1="Ok", btn2="Cancel")
    answer = alert.get() # get answer:
    alert.mainloop()
