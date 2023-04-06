import tkinter as tk

class Calculator:
    
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(width=False, height=False)
        
        # Entry widget to display the numbers and results
        self.display = tk.Entry(self.master, width=30, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Buttons for numbers and operators
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("C", 4, 2)
        self.create_button("+", 4, 3)
        
        self.create_button("=", 5, 0, 1, 4)
    
    # Function to create a button and attach a command to it
    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, width=7, height=2, font=('Arial', 14), command=lambda:self.click_button(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)
    
    # Function to handle button clicks
    def click_button(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)
            
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
