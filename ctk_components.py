"""
ctk_components Module
--------------------

This module contains the implementation of various customtkinter components.
These components are designed to provide additional functionality and a modern look to your customtkinter applications.

Classes:
--------
- CTkAlert
- CTkBanner
- CTkNotification
- CTkCard
- CTkCarousel
- CTkInput
- CTkLoader
- CTkPopupMenu
- CTkProgressPopup
- CTkTreeview

Each class corresponds to a unique widget that can be used in your customtkinter application.

Author: rudymohammadbali (https://github.com/rudymohammadbali)
Date: 2024/02/26
Version: 20240226
"""

import io
import os
import sys
from tkinter import ttk

import customtkinter as ctk
from PIL import Image, ImageDraw, ImageTk

from src.util.CTkGif import CTkGif
from src.util.py_win_style import set_opacity
from src.util.window_position import center_window, place_frame

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
ICON_DIR = os.path.join(CURRENT_PATH, "src", "icons")

ICON_PATH = {
    "close": (os.path.join(ICON_DIR, "close_black.png"), os.path.join(ICON_DIR, "close_white.png")),
    "images": list(os.path.join(ICON_DIR, f"image{i}.jpg") for i in range(1, 4)),
    "eye1": (os.path.join(ICON_DIR, "eye1_black.png"), os.path.join(ICON_DIR, "eye1_white.png")),
    "eye2": (os.path.join(ICON_DIR, "eye2_black.png"), os.path.join(ICON_DIR, "eye2_white.png")),
    "info": os.path.join(ICON_DIR, "info.png"),
    "warning": os.path.join(ICON_DIR, "warning.png"),
    "error": os.path.join(ICON_DIR, "error.png"),
    "left": os.path.join(ICON_DIR, "left.png"),
    "right": os.path.join(ICON_DIR, "right.png"),
    "warning2": os.path.join(ICON_DIR, "warning2.png"),
    "loader": os.path.join(ICON_DIR, "loader.gif"),
    "icon": os.path.join(ICON_DIR, "icon.png"),
    "arrow": os.path.join(ICON_DIR, "arrow.png"),
    "image": os.path.join(ICON_DIR, "image.png"),
}

DEFAULT_BTN = {
    "fg_color": "transparent",
    "hover": False,
    "compound": "left",
    "anchor": "w",
}

LINK_BTN = {**DEFAULT_BTN, "width": 70, "height": 25, "text_color": "#3574F0"}
BTN_LINK = {**DEFAULT_BTN, "width": 20, "height": 20, "text_color": "#3574F0", "font": ("", 13, "underline")}
ICON_BTN = {**DEFAULT_BTN, "width": 30, "height": 30}
BTN_OPTION = {**DEFAULT_BTN, "text_color": ("black", "white"), "corner_radius": 5, "hover_color": ("gray90", "gray25")}
btn = {**DEFAULT_BTN, "width": 230, "height": 50, "text_color": ("#000000", "#FFFFFF"), "font": ("", 13)}
btn_active = {**btn, "fg_color": (ctk.ThemeManager.theme["CTkButton"]["fg_color"]), "hover": True}
btn_footer = {**btn, "fg_color": ("#EBECF0", "#393B40"), "hover_color": ("#DFE1E5", "#43454A"), "corner_radius": 0}

DEFAULT_ICON_ONLY_BTN = {**DEFAULT_BTN, "height": 50, "text_color": ("#000000", "#FFFFFF"), "anchor": "center"}
btn_icon_only = {**DEFAULT_ICON_ONLY_BTN, "width": 70}
btn_icon_only_active = {**btn_icon_only, "fg_color": (ctk.ThemeManager.theme["CTkButton"]["fg_color"]), "hover": True}
btn_icon_only_footer = {**DEFAULT_ICON_ONLY_BTN, "width": 80, "fg_color": ("#EBECF0", "#393B40"),
                        "hover_color": ("#DFE1E5", "#43454A"), "corner_radius": 0}

TEXT = "Some quick example text to build on the card title and make up the bulk of the card's content."


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

        if state not in ICON_PATH or ICON_PATH[state] is None:
            self.icon = ctk.CTkImage(Image.open(ICON_PATH["info"]), Image.open(ICON_PATH["info"]), (30, 30))
        else:
            self.icon = ctk.CTkImage(Image.open(ICON_PATH[state]), Image.open(ICON_PATH[state]), (30, 30))

        self.close_icon = ctk.CTkImage(Image.open(ICON_PATH["close"][0]), Image.open(ICON_PATH["close"][1]), (20, 20))

        self.title_label = ctk.CTkLabel(self.frame_top, text=f"  {title}", font=("", 18), image=self.icon,
                                        compound="left")
        self.title_label.grid(row=0, column=0, sticky="w", padx=15, pady=20)
        self.title_label.bind("<B1-Motion>", self.move_window)
        self.title_label.bind("<ButtonPress-1>", self.old_xy_set)

        self.close_btn = ctk.CTkButton(self.frame_top, text="", image=self.close_icon, width=20, height=20, hover=False,
                                       fg_color="transparent", command=self.button_event)
        self.close_btn.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        self.message = ctk.CTkLabel(self.frame_top,
                                    text=body_text,
                                    justify="left", anchor="w", wraplength=self.width - 30)
        self.message.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="nsew", columnspan=2)

        self.btn_1 = ctk.CTkButton(self.frame_top, text=btn1, width=120, command=lambda: self.button_event(btn1),
                                   text_color="white")
        self.btn_1.grid(row=2, column=0, padx=(10, 5), pady=20, sticky="e")

        self.btn_2 = ctk.CTkButton(self.frame_top, text=btn2, width=120, fg_color="transparent", border_width=1,
                                   command=lambda: self.button_event(btn2), text_color=("black", "white"))
        self.btn_2.grid(row=2, column=1, padx=(5, 10), pady=20, sticky="e")

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

        if state not in ICON_PATH or ICON_PATH[state] is None:
            self.icon = ctk.CTkImage(Image.open(ICON_PATH["info"]), Image.open(ICON_PATH["info"]), (24, 24))
        else:
            self.icon = ctk.CTkImage(Image.open(ICON_PATH[state]), Image.open(ICON_PATH[state]), (24, 24))

        self.close_icon = ctk.CTkImage(Image.open(ICON_PATH["close"][0]), Image.open(ICON_PATH["close"][1]), (20, 20))

        self.title_label = ctk.CTkLabel(self, text=f"  {title}", font=("", 16), image=self.icon,
                                        compound="left")
        self.title_label.grid(row=0, column=0, sticky="w", padx=15, pady=10)

        self.close_btn = ctk.CTkButton(self, text="", image=self.close_icon, width=20, height=20, hover=False,
                                       fg_color="transparent", command=self.button_event)
        self.close_btn.grid(row=0, column=1, sticky="ne", padx=10, pady=10)

        self.btn_1 = ctk.CTkButton(self, text=btn1, **LINK_BTN, command=lambda: self.button_event(btn1))
        self.btn_1.grid(row=1, column=0, padx=(40, 5), pady=10, sticky="w")

        self.btn_2 = ctk.CTkButton(self, text=btn2, **LINK_BTN,
                                   command=lambda: self.button_event(btn2))
        self.btn_2.grid(row=1, column=1, padx=5, pady=10, sticky="w")

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

        if state not in ICON_PATH or ICON_PATH[state] is None:
            self.icon = ctk.CTkImage(Image.open(ICON_PATH["info"]), Image.open(ICON_PATH["info"]), (24, 24))
        else:
            self.icon = ctk.CTkImage(Image.open(ICON_PATH[state]), Image.open(ICON_PATH[state]), (24, 24))

        self.close_icon = ctk.CTkImage(Image.open(ICON_PATH["close"][0]), Image.open(ICON_PATH["close"][1]), (20, 20))

        self.message_label = ctk.CTkLabel(self, text=f"  {message}", font=("", 13), image=self.icon, compound="left")
        self.message_label.grid(row=0, column=0, sticky="nsw", padx=15, pady=10)

        self.close_btn = ctk.CTkButton(self, text="", image=self.close_icon, width=20, height=20, hover=False,
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


class CTkCard(ctk.CTkFrame):
    def __init__(self, master: any, border_width=1, corner_radius=5, **kwargs):
        super().__init__(master, border_width=border_width, corner_radius=corner_radius, **kwargs)
        self.grid_propagate(False)

    def card_1(self, image_path=None, width=300, height=380, title="Card title", text=TEXT, button_text="Go somewhere",
               command=None):
        self.configure(width=width, height=height)
        self.grid_rowconfigure(2, weight=1)

        image_width = width - 10
        image_height = height - 180
        wrap_length = width - 20

        if image_path:
            load_image = ctk.CTkImage(Image.open(image_path), Image.open(image_path),
                                      (image_width, image_height))
        else:
            new_image = self.create_image(image_width, image_height)
            load_image = ctk.CTkImage(Image.open(new_image), Image.open(new_image),
                                      (image_width, image_height))

        card_image = ctk.CTkLabel(self, text="", image=load_image)
        card_image.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        card_title = ctk.CTkLabel(self, text=title, font=("", 18))
        card_title.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

        card_text = ctk.CTkLabel(self, text=text, font=("", 13), wraplength=wrap_length, justify="left")
        card_text.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

        card_button = ctk.CTkButton(self, text=button_text, height=35, command=command if command else None)
        card_button.grid(row=3, column=0, padx=10, pady=20, sticky="sw")

    def card_2(self, width=380, height=170, title="Card title", subtitle="Subtitle", text=TEXT, link1_text="Card link1",
               link2_text="Card link2", command1=None, command2=None):
        self.configure(width=width, height=height)

        wrap_length = width - 20

        card_title = ctk.CTkLabel(self, text=title, font=("", 18))
        card_title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="sw")

        card_subtitle = ctk.CTkLabel(self, text=subtitle, font=("", 15))
        card_subtitle.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="nw")

        card_text = ctk.CTkLabel(self, text=text, font=("", 13), wraplength=wrap_length, justify="left")
        card_text.grid(row=2, column=0, padx=10, pady=5, sticky="nw", columnspan=100)

        card_link1 = ctk.CTkButton(self, text=link1_text, **BTN_LINK, command=command1 if command1 else None)
        card_link1.grid(row=3, column=0, padx=5, pady=10, sticky="w")
        card_link2 = ctk.CTkButton(self, text=link2_text, **BTN_LINK, command=command2 if command2 else None)
        card_link2.grid(row=3, column=1, padx=5, pady=10, sticky="w")

    def card_3(self, width=600, height=180, header="Header", title="Card title", text=TEXT, button_text="Go somewhere",
               command=None):
        self.configure(width=width, height=height)
        self.grid_columnconfigure(0, weight=1)

        wrap_length = width - 20

        card_header = ctk.CTkLabel(self, text=header, font=("", 15))
        card_header.grid(row=0, column=0, padx=10, pady=5, sticky="nw")

        ctk.CTkFrame(self, height=2, fg_color=("#C9CCD6", "#5A5D63")).grid(row=1, column=0, padx=0, pady=2, sticky="ew")

        card_title = ctk.CTkLabel(self, text=title, font=("", 18))
        card_title.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="sw")

        card_text = ctk.CTkLabel(self, text=text, font=("", 13), wraplength=wrap_length, justify="left")
        card_text.grid(row=3, column=0, padx=10, pady=5, sticky="nw")

        card_button = ctk.CTkButton(self, text=button_text, height=35, command=command if command else None)
        card_button.grid(row=4, column=0, padx=10, pady=10, sticky="sw")

    @staticmethod
    def create_image(width, height):
        create_image = Image.new('RGB', (width, height), 'gray')
        image_data = io.BytesIO()
        create_image.save(image_data, format='PNG')
        image_data.seek(0)
        return image_data


class CTkCarousel(ctk.CTkFrame):
    def __init__(self, master: any, img_list=None, width=None, height=None, img_radius=25, **kwargs):
        if img_list is None:
            img_list = ICON_PATH["images"]

        self.img_list = img_list
        self.image_index = 0
        self.img_radius = img_radius

        if width and height:
            self.width = width
            self.height = height
            for path in self.img_list.copy():
                try:
                    Image.open(path)
                except Exception as e:
                    self.remove_path(path)
        else:
            self.width, self.height = self.get_dimensions()
        super().__init__(master, width=self.width, height=self.height, fg_color="transparent", **kwargs)

        self.prev_icon = ctk.CTkImage(Image.open(ICON_PATH["left"]), Image.open(ICON_PATH["left"]), (30, 30))
        self.next_icon = ctk.CTkImage(Image.open(ICON_PATH["right"]), Image.open(ICON_PATH["right"]), (30, 30))

        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(expand=True, fill="both")

        self.button_bg = ctk.ThemeManager.theme["CTkButton"]["fg_color"]

        self.previous_button = ctk.CTkButton(self.image_label, text="", image=self.prev_icon, **ICON_BTN,
                                             command=self.previous_callback, bg_color=self.button_bg)
        self.previous_button.place(relx=0.0, rely=0.5, anchor='w')
        set_opacity(self.previous_button.winfo_id(), color=self.button_bg[0])

        self.next_button = ctk.CTkButton(self.image_label, text="", image=self.next_icon, **ICON_BTN,
                                         command=self.next_callback, bg_color=self.button_bg)
        self.next_button.place(relx=1.0, rely=0.5, anchor='e')
        set_opacity(self.next_button.winfo_id(), color=self.button_bg[0])

        self.next_callback()

    def get_dimensions(self):
        max_width, max_height = 0, 0

        for path in self.img_list.copy():
            try:
                with Image.open(path) as img:
                    width, height = img.size

                    if width > max_width and height > max_height:
                        max_width, max_height = width, height
            except Exception as e:
                self.remove_path(path)

        return max_width, max_height

    def remove_path(self, path):
        self.img_list.remove(path)

    @staticmethod
    def add_corners(image, radius):
        circle = Image.new('L', (radius * 2, radius * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, radius * 2 - 1, radius * 2 - 1), fill=255)
        alpha = Image.new('L', image.size, 255)
        w, h = image.size
        alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
        alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
        alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
        alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
        image.putalpha(alpha)
        return image

    def next_callback(self):
        self.image_index += 1

        if self.image_index > len(self.img_list) - 1:
            self.image_index = 0

        create_rounded = Image.open(self.img_list[self.image_index])
        create_rounded = self.add_corners(create_rounded, self.img_radius)

        next_image = ctk.CTkImage(create_rounded, create_rounded, (self.width, self.height))

        self.image_label.configure(image=next_image)

    def previous_callback(self):
        self.image_index -= 1

        if self.image_index < 0:
            self.image_index = len(self.img_list) - 1

        create_rounded = Image.open(self.img_list[self.image_index])
        create_rounded = self.add_corners(create_rounded, self.img_radius)

        next_image = ctk.CTkImage(create_rounded, create_rounded, (self.width, self.height))

        self.image_label.configure(image=next_image)


class CTkInput(ctk.CTkEntry):
    def __init__(self, master: any, icon_width=20, icon_height=20, **kwargs):
        super().__init__(master, **kwargs)

        self.icon_width = icon_width
        self.icon_height = icon_height

        self.is_hidden = False
        self.eye_btn = None

        self.warning = ctk.CTkImage(Image.open(ICON_PATH["warning2"]), Image.open(ICON_PATH["warning2"]),
                                    (self.icon_width, self.icon_height))
        self.eye1 = ctk.CTkImage(Image.open(ICON_PATH["eye1"][0]), Image.open(ICON_PATH["eye1"][1]),
                                 (self.icon_width, self.icon_height))
        self.eye2 = ctk.CTkImage(Image.open(ICON_PATH["eye2"][0]), Image.open(ICON_PATH["eye2"][1]),
                                 (self.icon_width, self.icon_height))

        self.button_bg = ctk.ThemeManager.theme["CTkEntry"]["fg_color"]
        self.border_color = ctk.ThemeManager.theme["CTkEntry"]["border_color"]

    def custom_input(self, icon_path, text=None, compound="right"):
        icon = ctk.CTkImage(Image.open(icon_path), Image.open(icon_path), (self.icon_width, self.icon_height))

        icon_label = ctk.CTkLabel(self, text=text if text else None, image=icon, width=self.icon_width,
                                  height=self.icon_height, compound=compound)
        icon_label.grid(row=0, column=0, padx=4, pady=0, sticky="e")

    def password_input(self):
        self.is_hidden = True
        self.configure(show="*")
        self.eye_btn = ctk.CTkButton(self, text="", width=self.icon_width, height=self.icon_height,
                                     fg_color=self.button_bg, hover=False, image=self.eye1,
                                     command=self.toggle_input)
        self.eye_btn.grid(row=0, column=0, padx=2, pady=0, sticky="e")

    def show_waring(self, border_color="red"):
        self.configure(border_color=border_color)
        icon_label = ctk.CTkLabel(self, text="", image=self.warning, width=self.icon_width, height=self.icon_height)
        icon_label.grid(row=0, column=0, padx=4, pady=0, sticky="e")

    def toggle_input(self):
        if self.is_hidden:
            self.is_hidden = False
            self.configure(show="")
            self.eye_btn.configure(image=self.eye2)
        else:
            self.is_hidden = True
            self.configure(show="*")
            self.eye_btn.configure(image=self.eye1)

    def reset_default(self):
        self.configure(border_color=self.border_color)
        self.configure(show="")
        self.is_hidden = False
        for widget in self.winfo_children():
            widget_name = widget.winfo_name()
            if widget_name.startswith("!ctklabel") or widget_name.startswith("!ctkbutton"):
                widget.destroy()


class CTkLoader(ctk.CTkFrame):
    def __init__(self, master: any, opacity: float = 0.8, width: int = 40, height: int = 40):
        self.master = master
        self.master.update()
        self.master_width = self.master.winfo_width()
        self.master_height = self.master.winfo_height()
        super().__init__(master, width=self.master_width, height=self.master_height, corner_radius=0)

        set_opacity(self.winfo_id(), value=opacity)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.loader = CTkGif(self, ICON_PATH["loader"], width=width, height=height)
        self.loader.grid(row=0, column=0, sticky="nsew")
        self.loader.start()

        self.place(relwidth=1.0, relheight=1.0)

    def stop_loader(self):
        self.loader.stop()
        self.destroy()


class CTkPopupMenu(ctk.CTkToplevel):
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

        self.close_icon = ctk.CTkImage(Image.open(ICON_PATH["close"][0]),
                                       Image.open(ICON_PATH["close"][1]),
                                       (16, 16))

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


class CTkTreeview(ctk.CTkFrame):
    def __init__(self, master: any, items):
        self.root = master
        self.items = items
        super().__init__(self.root)

        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(master=self, text="Treeview", font=("", 16))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.bg_color = self.root._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        self.text_color = self.root._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        self.selected_color = self.root._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        self.tree_style = ttk.Style(self)
        self.tree_style.theme_use('default')

        self.im_open = Image.open(ICON_PATH["arrow"])
        self.im_close = self.im_open.rotate(90)
        self.im_empty = Image.new('RGBA', (15, 15), '#00000000')

        self.img_open = ImageTk.PhotoImage(self.im_open, name='img_open', size=(15, 15))
        self.img_close = ImageTk.PhotoImage(self.im_close, name='img_close', size=(15, 15))
        self.img_empty = ImageTk.PhotoImage(self.im_empty, name='img_empty', size=(15, 15))

        self.tree_style.element_create('Treeitem.myindicator',
                                       'image', 'img_close', ('user1', '!user2', 'img_open'), ('user2', 'img_empty'),
                                       sticky='w', width=15, height=15)

        self.tree_style.layout('Treeview.Item',
                               [('Treeitem.padding',
                                 {'sticky': 'nsew',
                                  'children': [('Treeitem.myindicator', {'side': 'left', 'sticky': 'nsew'}),
                                               ('Treeitem.image', {'side': 'left', 'sticky': 'nsew'}),
                                               ('Treeitem.focus',
                                                {'side': 'left',
                                                 'sticky': 'nsew',
                                                 'children': [
                                                     ('Treeitem.text', {'side': 'left', 'sticky': 'nsew'})]})]})]
                               )

        self.tree_style.configure("Treeview", background=self.bg_color, foreground=self.text_color,
                                  fieldbackground=self.bg_color,
                                  borderwidth=0, font=("", 10))
        self.tree_style.map('Treeview', background=[('selected', self.bg_color)],
                            foreground=[('selected', self.selected_color)])
        self.root.bind("<<TreeviewSelect>>", lambda event: self.root.focus_set())

        self.treeview = ttk.Treeview(self, show="tree")
        self.treeview.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.insert_items(self.items)

    def insert_items(self, items, parent=''):
        for item in items:
            if isinstance(item, dict):
                id = self.treeview.insert(parent, 'end', text=item['name'])
                self.insert_items(item['children'], id)
            else:
                self.treeview.insert(parent, 'end', text=item)
