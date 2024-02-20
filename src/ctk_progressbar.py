import os

import customtkinter as ctk
from PIL import Image

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
ctk.set_default_color_theme(f"{CURRENT_PATH}\\blue.json")


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


class CTkProgressPopup(ctk.CTkFrame):
    def __init__(self, master, title: str = "Background Tasks", label: str = "Label...",
                 message: str = "Do something...", side: str = "right_bottom"):
        self.root = master
        self.width = 420
        self.height = 120
        super().__init__(self.root, width=self.width, height=self.height, corner_radius=5, border_width=1)
        self.grid_propagate(False)
        self.grid_columnconfigure(0, weight=1)

        self.cancelled = False

        self.title = ctk.CTkLabel(self, text=title, font=("", 16))
        self.title.grid(row=0, column=0, sticky="ew", padx=20, pady=10, columnspan=2)

        self.label = ctk.CTkLabel(self, text=label, height=0)
        self.label.grid(row=1, column=0, sticky="sw", padx=20, pady=0)

        self.progressbar = ctk.CTkProgressBar(self)
        self.progressbar.set(0)
        self.progressbar.grid(row=2, column=0, sticky="ew", padx=20, pady=0)

        self.close_icon = ctk.CTkImage(light_image=Image.open(f"{CURRENT_PATH}\\ICONS\\close_black.png"),
                                       dark_image=Image.open(f"{CURRENT_PATH}\\ICONS\\close_white.png"),
                                       size=(16, 16))

        self.cancel_btn = ctk.CTkButton(self, text="", width=16, height=16, fg_color="transparent",
                                        command=self.cancel_task, image=self.close_icon)
        self.cancel_btn.grid(row=2, column=1, sticky="e", padx=10, pady=0)

        self.message = ctk.CTkLabel(self, text=message, height=0)
        self.message.grid(row=3, column=0, sticky="nw", padx=20, pady=(0, 10))

        self.horizontal, self.vertical = side.split("_")
        place_frame(self.root, self, self.horizontal, self.vertical)
        self.root.bind("<Configure>", self.update_position, add="+")

    def update_position(self, event):
        place_frame(self.root, self, self.horizontal, self.vertical)
        self.update_idletasks()
        self.root.update_idletasks()

    def update_progress(self, progress):
        if self.cancelled:
            return "Cancelled"
        self.progressbar.set(progress)

    def update_message(self, message):
        self.message.configure(text=message)

    def update_label(self, label):
        self.label.configure(text=label)

    def cancel_task(self):
        self.cancelled = True
        self.close_progress_popup()

    def close_progress_popup(self):
        self.root.unbind("<Configure>")
        self.destroy()


if __name__ == "__main__":
    app = ctk.CTk()
    center_window(app, 800, 500)
    # Usage
    progress_popup = CTkProgressPopup(master=app, title="Background Tasks", label="Label...", message="Do something...", side="right_bottom")
    # progress_popup.update_label("New Label...") # Updates label
    # progress_popup.update_message("New Message...") # Updates message
    # progress_popup.update_progress(54) # Update progress bar (0-100)
    # progress_popup.cancel_task() # Cancel task and close progress popup
    app.mainloop()
