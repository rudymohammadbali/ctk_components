<h1 align="center">CTk Widgets</h1>
CTk Widgets is a collection of widgets and utilities designed as extensions or add-ons for `customtkinter (ctk)`. 


## Widgets

There are 7 widgets included in this pack:

1. `CTkAlert`
2. `CTkBanner`
3. `CTkNotification`
4. `CTkLoader`
5. `CTkPopup`
6. `CTkProgressPopup`
7. `CTkTreeVew`

## Utilities

The pack also includes 4 utilities:

- `window_position.py`
- `ctkgif.py`
- `py_win_style.py`
- `blue.json`

## Preview

You can check the `preview` folder for images of the widgets!

![alert](https://github.com/rudymohammadbali/ctk_widgets/assets/63475761/8f003a83-8200-4852-b3bb-91baaba8b432)
![banner](https://github.com/rudymohammadbali/ctk_widgets/assets/63475761/749eb31c-95dd-4322-a252-a98cf2a28760)
![notification](https://github.com/rudymohammadbali/ctk_widgets/assets/63475761/6c70fc2b-98cf-4ec7-b4b0-2ad0e2fc605b)
![loader](https://github.com/rudymohammadbali/ctk_widgets/assets/63475761/0f956574-8299-46bd-85c1-5bc9596f3f34)
![popupmenu](https://github.com/rudymohammadbali/ctk_widgets/assets/63475761/8dbc2980-af93-4c6e-9708-a1fd7a45d202)
![progresspopup](https://github.com/rudymohammadbali/ctk_widgets/assets/63475761/6ec81b4f-ff2b-43f7-9f44-e92218dc43a6)
![treeview](https://github.com/rudymohammadbali/ctk_widgets/assets/63475761/2c03e258-784d-4b01-b58b-3f53bb50344b)


## Full example
```python
# CTkAlert
alert = CTkAlert(state="error", title="title", body_text="body text", btn1="Ok", btn2="Cancel")
answer = alert.get() # get answer: This will return the user's response to the alert.

# CTkBanner
banner = CTkBanner(master=app, state="info", title="title", btn1="Action 1", btn2="Action 2", side="right_bottom")
answer = banner.get() # get answer: This will return the user's response to the banner.

# CTkNotification
CTkNotification(master=app, state="info", message="message", side="right_bottom") # This will display a notification at the right bottom of the app.

# CTkLoader
loader = CTkLoader(master=app, opacity=0.8, width=40, height=40)
# app.after(5000, loader.stop_loader) # Stop Loader after 5sec: This will stop the loader after 5 seconds.

# PopupMenu
# Custom button
BTN_OPTION = {
    "compound": "left",
    "anchor": "w",
    "fg_color": "transparent",
    "text_color": ("black", "white"),
    "corner_radius": 5,
    "hover_color": ("gray90", "gray25")
}
popup_menu = PopupMenu(master=app, width=250, height=270, title="Title", corner_radius=8, border_width=0)
app.bind("<Button-3>", lambda event: do_popup(event, popup_menu), add="+") # bind app for right click: This will show the popup menu when the user right clicks on the app.

# Add buttons to the popup menu
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

# CTkProgressPopup
# Usage
progress_popup = CTkProgressPopup(master=app, title="Background Tasks", label="Label...", message="Do something...", side="right_bottom")
progress_popup.update_label("New Label...") # This will update the label of the progress popup.
progress_popup.update_message("New Message...") # This will update the message of the progress popup.
progress_popup.update_progress(54) # This will update the progress bar of the progress popup (0-100).
progress_popup.cancel_task() # This will cancel the task and close the progress popup.

# CTkTreeView
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
tree_view = CTkTreeView(master=app, items=data) # This will create a tree view with the specified data.
tree_view.pack(pady=20, padx=20, fill="both", expand=True) # This will pack the tree view into the app.
```

## Arguments

### CTkAlert
| Parameter | Description |
| --- | --- |
| `state` | The icon of alert (info: default, warning and error) |
| `title` | Title of alert |
| `body_text` | Message or body text of alert |
| `btn1` | The text on the first button (Ok: default)|
| `btn2` | The text on the second button (Cancel: default)|

### CTkBanner
| Parameter | Description |
| --- | --- |
| `master` | Set parent window, the widget will spawn at right bottom of the parent window |
| `state` | The icon of alert (info: default, warning and error) |
| `title` | Title of alert |
| `btn1` | The text on the first button (Ok: default)|
| `btn2` | The text on the second button (Cancel: default)|
| `side` | The position where the widget should be displayed (right_bottom: default)|

### CTkNotification
| Parameter | Description |
| --- | --- |
| `master` | Set parent window, the widget will spawn at right bottom of the parent window |
| `state` | The icon of alert (info: default, warning and error) |
| `message` | Message or body text of notification |
| `side` | The position where the widget should be displayed (right_bottom: default)|

### CTkLoader
| Parameter | Description |
| --- | --- |
| `master` | Set parent window, the widget will spawn at center with full screen of the parent window |
| `opacity` | The opacity of frame background (0.8: default) |
| `width` | Loader icon width (40: default) |
| `height` | Loader icon height (40: default) |

### PopupMenu
| Parameter | Description |
| --- | --- |
| `master` | Set parent window, the widget will spawn at where the the mouse is clicked of the parent window |
| `width` | Popup width (250: default) |
| `height` | Popup height (270: default) |
| `title` | Popup title (Title: default) |
| `corner_radius` | Popup frame corner_radius (8: default) |
| `border_width` | Popup frame border (0: default) |

### CTkProgressPopup
| Parameter | Description |
| --- | --- |
| `master` | Set parent window, the widget will spawn at right bottom of the parent window |
| `title` | Title of progressbar (Background Tasks: default) |
| `label` | Label text of progressbar (Label...: default)|
| `message` | Message or body text of progressbar (Do something...: default)|
| `side` | The position where the widget should be displayed (right_bottom: default)|

### CTkTreeView
| Parameter | Description |
| --- | --- |
| `master` | Set parent window |
| `items` | The data or items should be inserted to treeview, takes lists and dict |

## Support

<p align="left">If you'd like to support my ongoing efforts in sharing fantastic open-source projects, you can contribute by making a donation via PayPal.</p>

<div align="center">
  <a href="https://www.paypal.com/paypalme/iamironman0" target="_blank">
    <img src="https://img.shields.io/static/v1?message=PayPal&logo=paypal&label=&color=00457C&logoColor=white&labelColor=&style=flat" height="40" alt="paypal logo"  />
  </a>
</div>
