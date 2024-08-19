import tkinter as tk
from tkinter import font

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.configure(bg="#282c34")

        # Custom font
        self.custom_font = font.Font(family="Helvetica", size=24, weight="bold")

        # Display
        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Display Entry
        self.display = tk.Entry(self, textvariable=self.result_var, font=self.custom_font, bd=0, bg="#1e1e1e", fg="#ffffff", justify='right')
        self.display.pack(pady=20, padx=20, fill=tk.BOTH)

        # Buttons Frame
        button_frame = tk.Frame(self, bg="#282c34")
        button_frame.pack()

        # Buttons Configuration
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]

        # Create Buttons
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                button = tk.Button(button_frame, text=text, font=self.custom_font, bg="#444b53", fg="#ffffff", relief=tk.RAISED, bd=0, width=5, height=2, command=lambda t=text: self.on_button_click(t))
                button.grid(row=i, column=j, padx=5, pady=5)

        # Additional Styling
        for widget in button_frame.winfo_children():
            widget.config(bg="#444b53", fg="#ffffff", activebackground="#555e67", activeforeground="#ffffff")

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char == '=':
            try:
                # Evaluate the expression
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            self.result_var.set(current_text + char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
