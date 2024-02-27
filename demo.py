from ctk_components import *

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
THEME_DIR = os.path.join(CURRENT_PATH, "src", "util")
ctk.set_default_color_theme(os.path.join(THEME_DIR, "blue.json"))


def alert():
    my_alert = CTkAlert(state="info", title="Title", body_text="body text", btn1="Ok", btn2="Cancel")
    # answer = my_alert.get()  # get answer
    # print(answer)


def banner():
    my_banner = CTkBanner(master=preview_frame, state="info", title="Title",
                          btn1="Action 1", btn2="Action 2", side="right_bottom")
    # answer = my_banner.get()  # get answer
    # print(answer)


def notification():
    CTkNotification(master=preview_frame, state="info", message="message", side="right_bottom")


def card():
    card1 = CTkCard(preview_frame, border_width=1, corner_radius=5)
    card2 = CTkCard(preview_frame, border_width=1, corner_radius=5)
    card3 = CTkCard(preview_frame, border_width=1, corner_radius=5)

    # Create multiple cards
    card1.card_1(width=300, height=380, title="Card title", text=TEXT,
                 button_text="Go somewhere", command=lambda: print("Hello"))
    card2.card_2(width=380, height=170, title="Card title", subtitle="Subtitle", text=TEXT, link1_text="Card link1",
                 link2_text="Card link2", command1=lambda: print("Hello"), command2=lambda: print("Hello"))
    card3.card_3(width=600, height=180, header="Header", title="Card title", text=TEXT, button_text="Go somewhere",
                 command=lambda: print("Hello"))

    card1.grid(row=0, column=0, padx=5, pady=20)
    card2.grid(row=0, column=1, padx=5, pady=20)
    card3.grid(row=0, column=2, padx=5, pady=20)


def carousel():
    my_carousel = CTkCarousel(preview_frame, img_radius=25)
    my_carousel.grid(padx=20, pady=20)


def ctk_input_1():
    my_input = CTkInput(preview_frame, width=250, height=35, border_width=1)
    my_input.pack(padx=20, pady=20)
    my_input.show_waring()

    reset_btn = ctk.CTkButton(preview_frame, text="reset to default", command=my_input.reset_default)
    reset_btn.pack(padx=20, pady=20)


def ctk_input_2():
    my_input = CTkInput(preview_frame, width=250, height=35, border_width=1)
    my_input.pack(padx=20, pady=20)
    my_input.password_input()

    reset_btn = ctk.CTkButton(preview_frame, text="reset to default", command=my_input.reset_default)
    reset_btn.pack(padx=20, pady=20)


def loader():
    my_loader = CTkLoader(master=preview_frame, opacity=0.8, width=40, height=40)
    app.after(5000, my_loader.stop_loader)  # Stop Loader after 5sec


def ctk_popup():
    label1 = ctk.CTkLabel(preview_frame, text="Right click to open Popup Menu!", font=("", 18))
    # label1.grid(padx=20, pady=20, sticky="nsew")
    label1.pack()

    popup_menu = CTkPopupMenu(master=preview_frame, width=250, height=270, title="Title", corner_radius=8, border_width=0)
    preview_frame.bind("<Button-3>", lambda event: do_popup(event, popup_menu), add="+")

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


def progress_popup():
    my_progress = CTkProgressPopup(master=preview_frame, title="Background Tasks",
                                   label="Label...", message="Do something...", side="right_bottom")
    # my_progress.update_label("New Label...") # Updates label
    # my_progress.update_message("New Message...") # Updates message
    # my_progress.update_progress(54) # Update progress bar (0-100)
    # my_progress.cancel_task() # Cancel task and close progress popup


def treeview():
    data = [
        {
            'name': 'Item 1',
            'children': ['Subitem 1', 'Subitem 2',
                         {"name": "Subitem 3", "children": ["Sub-subitem 1", "Sub-subitem 2"]}]
        },
        'Item 2',
        {
            'name': 'Item 3',
            'children': ['Subitem 3']
        }
    ]       
    tree_view = CTkTreeview(master=preview_frame, items=data)
    tree_view.pack(pady=20, padx=20, fill="both", expand=True)


WIDGETS = {"CTkAlert": alert,
           "CTkBanner": banner,
           "CTkNotification": notification,
           "CTkCard": card,
           "CTkCarousel": carousel,
           "CTkInput1": ctk_input_1,
           "CTkInput2": ctk_input_2,
           "CTkLoader": loader,
           "CTkPopupMenu": ctk_popup,
           "CTkProgressPopup": progress_popup,
           "CTkTreeview": treeview}


def toggle_widgets(widget):
    for widgets in preview_frame.winfo_children():
        widgets.destroy()

    var = WIDGETS[widget]
    var()


if __name__ == "__main__":
    app = ctk.CTk()
    app.title("CTk Components - demo")
    center_window(app, 1280, 720)
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)

    options = ["CTkAlert", "CTkBanner", "CTkNotification", "CTkCard",
               "CTkCarousel", "CTkInput1", "CTkInput2", "CTkLoader",
               "CTkPopupMenu", "CTkProgressPopup", "CTkTreeview"]

    frame = ctk.CTkFrame(app, fg_color="transparent")
    frame.grid(row=0, column=0, padx=400, pady=20, sticky="ew")
    frame.grid_columnconfigure(0, weight=1)

    label = ctk.CTkLabel(frame, text="Select Widget")
    label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
    option = ctk.CTkOptionMenu(frame, values=options, width=200, command=toggle_widgets)
    option.grid(row=0, column=1, padx=20, pady=20, sticky="ew")
    option.set("None")

    preview_frame = ctk.CTkFrame(app, fg_color="transparent")
    preview_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

    app.mainloop()
