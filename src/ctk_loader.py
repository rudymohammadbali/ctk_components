import os

import customtkinter as ctk

from CTkGif import CTkGif
from py_win_style import set_opacity

path = os.path.dirname(os.path.realpath(__file__))


class CTkLoader(ctk.CTkFrame):
    def __init__(self, master: any, opacity: float = 0.8, width: int = 40, height: int = 40):
        self.master = master
        self.master.update()
        master_width = self.master.winfo_width()
        master_height = self.master.winfo_height()
        super().__init__(master, width=master_width, height=master_height, corner_radius=0)

        set_opacity(self, value=opacity)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.loader = CTkGif(self, f'{path}/icons/loader.gif', width=width, height=height)
        self.loader.grid(row=0, column=0, sticky="nsew")
        self.loader.start()

        self.place(relwidth=1.0, relheight=1.0)

    def stop_loader(self):
        self.loader.stop()
        self.destroy()


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("1280x720")
    ctk.CTkButton(app, command=lambda: print("Hello")).pack(expand=True, fill="x")
    # Usage
    loader = CTkLoader(master=app, opacity=0.8, width=40, height=40)
    # app.after(5000, loader.stop_loader) # Stop Loader after 5sec
    app.mainloop()
