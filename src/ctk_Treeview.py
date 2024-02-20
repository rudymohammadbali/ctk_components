import os
from tkinter import ttk

import customtkinter as ctk
from PIL import Image, ImageTk

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
ctk.set_default_color_theme(f"{CURRENT_PATH}\\blue.json")


class CTkTreeView(ctk.CTkFrame):
    def __init__(self, master: any, items):
        self.root = master
        self.items = items
        super().__init__(self.root)

        self.grid_columnconfigure(0, weight=1)

        label = ctk.CTkLabel(master=self, text="Treeview", font=("", 16))
        label.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        bg_color = self.root._apply_appearance_mode(ctk.ThemeManager.theme["CTkFrame"]["fg_color"])
        text_color = self.root._apply_appearance_mode(ctk.ThemeManager.theme["CTkLabel"]["text_color"])
        selected_color = self.root._apply_appearance_mode(ctk.ThemeManager.theme["CTkButton"]["fg_color"])

        tree_style = ttk.Style(self)
        tree_style.theme_use('default')

        im_open = Image.open(f"{CURRENT_PATH}\\icons\\arrow.png")
        im_close = im_open.rotate(90)
        im_empty = Image.new('RGBA', (15, 15), '#00000000')

        self.img_open = ImageTk.PhotoImage(im_open, name='img_open', size=(15, 15))
        self.img_close = ImageTk.PhotoImage(im_close, name='img_close', size=(15, 15))
        self.img_empty = ImageTk.PhotoImage(im_empty, name='img_empty', size=(15, 15))

        tree_style.element_create('Treeitem.myindicator',
                                  'image', 'img_close', ('user1', '!user2', 'img_open'), ('user2', 'img_empty'),
                                  sticky='w', width=15, height=15)

        tree_style.layout('Treeview.Item',
                          [('Treeitem.padding',
                            {'sticky': 'nsew',
                             'children': [('Treeitem.myindicator', {'side': 'left', 'sticky': 'nsew'}),
                                          ('Treeitem.image', {'side': 'left', 'sticky': 'nsew'}),
                                          ('Treeitem.focus',
                                           {'side': 'left',
                                            'sticky': 'nsew',
                                            'children': [('Treeitem.text', {'side': 'left', 'sticky': 'nsew'})]})]})]
                          )

        tree_style.configure("Treeview", background=bg_color, foreground=text_color, fieldbackground=bg_color,
                             borderwidth=0, font=("", 10))
        tree_style.map('Treeview', background=[('selected', bg_color)], foreground=[('selected', selected_color)])
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


if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("500x500")
    # Usage
    data = [
        {
            'name': 'Item 1',
            'children': ['Subitem 1', 'Subitem 2', {"name": "Subitem 3", "children": ["Sub-subitem 1", "Sub-subitem 2"]}]
        },
        'Item 2',
        {
            'name': 'Item 3',
            'children': ['Subitem 3']
        }
    ]
    tree_view = CTkTreeView(master=app, items=data)
    tree_view.pack(pady=20, padx=20, fill="both", expand=True)
    app.mainloop()
