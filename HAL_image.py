from PIL import Image, ImageTk
import tkinter as tk
import sys

# Global variable to store the Tkinter window object
image_window = None

def import_and_display_image(image_path, width, height):
    image_window = tk.Tk()
    image_window.title("HAL Image")

    # Open and resize the image using PIL
    image = Image.open(image_path)
    image = image.resize((width, height))

    # Convert the image to a format that Tkinter can display
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = tk.Label(image_window, image=photo)
    label.image = photo  # Keep a reference to avoid garbage collection
    label.pack()

    image_window.mainloop()

def image_window_exists():
    global image_window
    return image_window is not None and tk._default_root is not None

def close_image_window():
    global image_window

    if image_window_exists():
        image_window.after(10, image_window.destroy)
        image_window.quit()
        image_window = None
    with open('bot_response.txt', 'w') as file:
                    file.close()

    # Close the Tkinter window forcibly
    close_image_window()
    sys.exit()