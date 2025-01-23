import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")

        # GUI Elements
        self.image_label = tk.Label(root, text="No image loaded", width=50, height=20, relief="solid")
        self.image_label.pack(pady=10)

        self.load_button = tk.Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack(pady=5)

        self.options_label = tk.Label(root, text="Select Conversion Option:")
        self.options_label.pack(pady=5)

        self.options = ["Convert to Grayscale", "Resize (100x100)", "Rotate 90°"]
        self.selected_option = tk.StringVar(value=self.options[0])
        self.options_menu = tk.OptionMenu(root, self.selected_option, *self.options)
        self.options_menu.pack(pady=5)

        self.convert_button = tk.Button(root, text="Convert Image", command=self.convert_image)
        self.convert_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Save Image", command=self.save_image, state=tk.DISABLED)
        self.save_button.pack(pady=10)

        self.image = None
        self.processed_image = None

    def load_image(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
        )
        if filepath:
            self.image = Image.open(filepath)
            self.display_image(self.image)
            self.save_button.config(state=tk.DISABLED)

    def display_image(self, img):
        img.thumbnail((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk, text="")
        self.image_label.image = img_tk

    def convert_image(self):
        if self.image is None:
            messagebox.showerror("Error", "No image loaded!")
            return

        option = self.selected_option.get()
        if option == "Convert to Grayscale":
            self.processed_image = self.image.convert("L")
        elif option == "Resize (100x100)":
            self.processed_image = self.image.resize((100, 100))
        elif option == "Rotate 90°":
            self.processed_image = self.image.rotate(90)
        else:
            messagebox.showerror("Error", "Invalid conversion option!")
            return

        self.display_image(self.processed_image)
        self.save_button.config(state=tk.NORMAL)

    def save_image(self):
        if self.processed_image is None:
            messagebox.showerror("Error", "No processed image to save!")
            return

        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All Files", "*.*")]
        )
        if filepath:
            self.processed_image.save(filepath)
            messagebox.showinfo("Success", "Image saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
