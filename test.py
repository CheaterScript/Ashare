import easyquotation
import time
import tkinter as tk
from threading import Thread

quotation = easyquotation.use("sina")
# code = "300147"
code = "301279"
# code = "301388"
# code = "300043"
def update_price(label):
    while True:
        try:
            data = quotation.real([code])
            label.config(text=f"FPS: {data[code]['now']}")
        except Exception as e:
            label.config(text='Error')
        time.sleep(1)

def on_mouse_down(event):
    global drag_data
    drag_data = {"x": event.x, "y": event.y}

def on_mouse_drag(event):
    x = root.winfo_x() - drag_data["x"] + event.x
    y = root.winfo_y() - drag_data["y"] + event.y
    root.geometry(f"+{x}+{y}")

def on_right_click_close(event):
    root.quit()  # Close the application

def create_app():
    global root, drag_data
    root = tk.Tk()
    root.title("Stock Price")
    root.geometry("200x100")
    root.attributes('-topmost', True)  # Always on top
    root.wm_attributes('-transparentcolor', 'black')  # Set the transparent color
    root.config(bg='black')  # Set window background color
    root.overrideredirect(True)  # Hide the title bar and menu

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the position to the top-right corner
    x_position = screen_width - 200  # Adjust for window width
    y_position = 0  # Top position

    root.geometry(f"200x100+{x_position}+{y_position}")

    label = tk.Label(root, font=("Arial", 18), bg='black', fg='white')  # Background black, text white
    label.pack(expand=True)

    # Bind mouse events for dragging and closing
    label.bind("<ButtonPress-1>", on_mouse_down)  # Left mouse button press
    label.bind("<B1-Motion>", on_mouse_drag)  # Dragging with left button
    label.bind("<Double-Button-3>", on_right_click_close)  # Right mouse double-click to close

    # Start the price update in a separate thread
    Thread(target=update_price, args=(label,), daemon=True).start()

    root.mainloop()

create_app()  