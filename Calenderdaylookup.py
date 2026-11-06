from datetime import date
import tkinter as tk

class Calendardaylookup:
    def __init__(self, root):
        self.root = root
        self.root.title("Calendar day lookup")
        self.root_label = tk.Label(self.root, text="Enter a date (DD-MM-YYYY):", font=("Helvetica", 14), fg="white", bg="#111111")
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.root.configure(bg="#111111")
        self.root_entry = tk.Entry(self.root, font=("Helvetica", 14), width=20)
        self.root_button = tk.Button(self.root, text="Lookup", command=self.lookup_day, font=("Helvetica", 14), bg="#1E90FF", fg="white")
        self.root_label.pack()
        self.root_entry.pack()
        self.root_button.pack()
        self.root_button2 = tk.Button(self.root, text="Reset", command=self.reset_entry, font=("Helvetica", 14), bg="#1E90FF", fg="white")
        self.root_button2.pack()

    def lookup_day(self):
        try:
            day, month, year = map(int, self.root_entry.get().strip().split("-"))
            result = date(year, month, day).strftime("%A")
            self.root_button.config(text=result)
        except (ValueError, TypeError):
            self.root_button.config(text="Invalid date. Please enter a valid date in DD-MM-YYYY format.", font=("Helvetica", 10), fg="#ff6666")

    def reset_entry(self):
        self.root_entry.delete(0, tk.END)
        self.root_button.config(text="Lookup")

if __name__ == "__main__":
    root = tk.Tk()
    app = Calendardaylookup(root)
    root.mainloop()