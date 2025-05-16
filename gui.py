import tkinter as tk
from tkinter import messagebox, simpledialog
from auth import login, signup
from inventory import add_product, get_all_products, get_low_stock

def show_dashboard():
    def add_new_product():
        name = simpledialog.askstring("Input", "Product name:")
        qty = int(simpledialog.askstring("Input", "Quantity:"))
        price = float(simpledialog.askstring("Input", "Price:"))
        cat = simpledialog.askstring("Input", "Category:")
        add_product(name, qty, price, cat)
        messagebox.showinfo("Success", "Product added!")

    def show_products():
        products = get_all_products()
        text.delete("1.0", tk.END)
        for p in products:
            text.insert(tk.END, f"{p}\n")

    def show_low_stock():
        products = get_low_stock()
        text.delete("1.0", tk.END)
        text.insert(tk.END, "Low stock products:\n")
        for p in products:
            text.insert(tk.END, f"{p}\n")

    dashboard = tk.Tk()
    dashboard.title("Inventory Dashboard")
    tk.Button(dashboard, text="Add Product", command=add_new_product).pack()
    tk.Button(dashboard, text="View All Products", command=show_products).pack()
    tk.Button(dashboard, text="Low Stock Report", command=show_low_stock).pack()
    text = tk.Text(dashboard, height=20, width=80)
    text.pack()
    dashboard.mainloop()

def start_gui():
    root = tk.Tk()
    root.title("Inventory Login")

    tk.Label(root, text="Username").pack()
    user_entry = tk.Entry(root)
    user_entry.pack()

    tk.Label(root, text="Password").pack()
    pass_entry = tk.Entry(root, show="*")
    pass_entry.pack()

    def try_login():
        if login(user_entry.get(), pass_entry.get()):
            root.destroy()
            show_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def try_signup():
        if signup(user_entry.get(), pass_entry.get()):
            messagebox.showinfo("Success", "User registered! Now log in.")
        else:
            messagebox.showerror("Error", "User already exists")

    tk.Button(root, text="Login", command=try_login).pack()
    tk.Button(root, text="Sign Up", command=try_signup).pack()

    root.mainloop()
