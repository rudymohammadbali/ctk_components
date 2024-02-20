import os
import sys

import customtkinter as ctk

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
ctk.set_default_color_theme(f"{CURRENT_PATH}\\blue.json")
BTN_OPTION = {
    "compound": "left",
    "anchor": "w",
    "fg_color": "transparent",
    "text_color": ("black", "white"),
    "corner_radius": 5,
    "hover_color": ("gray90", "gray25")
}


class PopupMenu(ctk.CTkToplevel):
    def __init__(self,
                 master=None,
                 width=250,
                 height=270,
                 title="Title",
                 corner_radius=8,
                 border_width=0,
                 **kwargs):

        super().__init__(takefocus=1)

        self.y = None
        self.x = None
        self.width = width
        self.height = height
        self.focus()
        self.master_window = master
        self.corner = corner_radius
        self.border = border_width
        self.hidden = True

        if sys.platform.startswith("win"):
            self.after(100, lambda: self.overrideredirect(True))
            self.transparent_color = self._apply_appearance_mode(self._fg_color)
            self.attributes("-transparentcolor", self.transparent_color)
        elif sys.platform.startswith("darwin"):
            self.overrideredirect(True)
            self.transparent_color = 'systemTransparent'
            self.attributes("-transparent", True)
        else:
            self.attributes("-type", "splash")
            self.transparent_color = '#000001'
            self.corner = 0
            self.withdraw()

        self.frame = ctk.CTkFrame(self, bg_color=self.transparent_color, corner_radius=self.corner,
                                  border_width=self.border, **kwargs)
        self.frame.pack(expand=True, fill="both")

        self.title = ctk.CTkLabel(self.frame, text=title, font=("", 16))
        self.title.pack(expand=True, fill="x", padx=10, pady=5)

        self.master.bind("<ButtonPress>", lambda event: self._withdraw_off(), add="+")
        self.bind("<Button-1>", lambda event: self._withdraw(), add="+")
        self.master.bind("<Configure>", lambda event: self._withdraw(), add="+")

        self.resizable(width=False, height=False)
        self.transient(self.master_window)

        self.update_idletasks()

        self.withdraw()

    def _withdraw(self):
        self.withdraw()
        self.hidden = True

    def _withdraw_off(self):
        if self.hidden:
            self.withdraw()
        self.hidden = True

    def popup(self, x=None, y=None):
        self.x = x
        self.y = y
        self.deiconify()
        self.focus()
        self.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        self.hidden = False


def do_popup(event, frame):
    try:
        frame.popup(event.x_root, event.y_root)
    finally:
        frame.grab_release()


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("500x500")
    # Usage
    popup_menu = PopupMenu(master=app, width=250, height=270, title="Title", corner_radius=8, border_width=0)
    app.bind("<Button-3>", lambda event: do_popup(event, popup_menu), add="+")

    btn1 = ctk.CTkButton(popup_menu.frame, text="Option 1", command=lambda: print("Hello"), **BTN_OPTION)
    btn1.pack(expand=True, fill="x", padx=10, pady=0)

    btn2 = ctk.CTkButton(popup_menu.frame, text="Option 2", command=lambda: print("Hello"), **BTN_OPTION)
    btn2.pack(expand=True, fill="x", padx=10, pady=(1, 0))

    btn3 = ctk.CTkButton(popup_menu.frame, text="Option 3", command=lambda: print("Hello"), **BTN_OPTION)
    btn3.pack(expand=True, fill="x", padx=10, pady=(1, 0))

    btn4 = ctk.CTkButton(popup_menu.frame, text="Option 4", command=lambda: print("Hello"), **BTN_OPTION)
    btn4.pack(expand=True, fill="x", padx=10, pady=(1, 0))

    btn5 = ctk.CTkButton(popup_menu.frame, text="Option 5", command=lambda: print("Hello"), **BTN_OPTION)
    btn5.pack(expand=True, fill="x", padx=10, pady=(1, 10))

    app.mainloop()
