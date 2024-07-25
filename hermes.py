import tkinter as tk
from tkinter import messagebox

# Create the main application window
class FoodOrderingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hermes' Food Deliveries")
        
        # Initialize cart
        self.cart_items = []
        self.cart_total = 0
        
        # Main Menu
        self.main_frame = tk.Frame(self.root, bg='lightgray')
        self.main_frame.pack(padx=10, pady=10)
        
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_frame()
        
        tk.Label(self.main_frame, text="Welcome to Hermes' Food Deliveries", font=("Arial", 16), bg='lightblue').pack(pady=10)
        
        tk.Button(self.main_frame, text="Oye Papaji Punjabi Restaurant", command=self.show_oye_papaji_menu, bg='lightgreen').pack(fill='x')
        tk.Button(self.main_frame, text="Wok ON!!! Chinese", command=self.show_wok_on_menu, bg='lightgreen').pack(fill='x')
        tk.Button(self.main_frame, text="Napolean's Pizza", command=self.show_napolean_menu, bg='lightgreen').pack(fill='x')
        tk.Button(self.main_frame, text="Om Sai Pav Bhaji", command=self.show_om_sai_menu, bg='lightgreen').pack(fill='x')
        tk.Button(self.main_frame, text="Southern Corridor", command=self.show_southern_corridor_menu, bg='lightgreen').pack(fill='x')
        
        tk.Button(self.main_frame, text="View Cart", command=self.show_cart, bg='lightcoral').pack(fill='x')
        tk.Button(self.main_frame, text="Clear Cart", command=self.clear_cart, bg='lightcoral').pack(fill='x')
        tk.Button(self.main_frame, text="Exit", command=self.root.quit, bg='lightcoral').pack(fill='x')

    def show_oye_papaji_menu(self):
        self.clear_frame()
        # Create menu items
        tk.Label(self.main_frame, text="Oye Papaji Menu", font=("Arial", 14), bg='lightyellow').pack(pady=10)
        tk.Button(self.main_frame, text="Indian Breads", command=self.show_indian_breads_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Sabzi", command=self.show_sabzi_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Rice", command=self.show_rice_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Dal", command=self.show_dal_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Starters", command=self.show_starters_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Beverages", command=self.show_beverages_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, bg='lightcoral').pack(fill='x')

    def show_napolean_menu(self):
        self.clear_frame()
        # Create menu items
        tk.Label(self.main_frame, text="Napolean's Pizza Menu", font=("Arial", 14), bg='lightyellow').pack(pady=10)
        tk.Button(self.main_frame, text="Pizza", command=self.show_pizza_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Pasta", command=self.show_pasta_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Garlic Breads", command=self.show_garlic_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Beverages", command=self.show_beverages_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, bg='lightcoral').pack(fill='x')

    def show_southern_corridor_menu(self):
        self.clear_frame()
        # Create menu items
        tk.Label(self.main_frame, text="Southern Corridor Menu", font=("Arial", 14), bg='lightyellow').pack(pady=10)
        tk.Button(self.main_frame, text="Dosa", command=self.show_dosa_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Uttapa", command=self.show_uttapa_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Beverages", command=self.show_beverages_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, bg='lightcoral').pack(fill='x')

    def show_om_sai_menu(self):
        self.clear_frame()
        # Create menu items
        tk.Label(self.main_frame, text="Om Sai Pav Bhaji Menu", font=("Arial", 14), bg='lightyellow').pack(pady=10)
        tk.Button(self.main_frame, text="Pav Bhaji", command=self.show_pav_bhaji_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Pulav", command=self.show_pulav_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Beverages", command=self.show_beverages_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, bg='lightcoral').pack(fill='x')

    def show_wok_on_menu(self):
        self.clear_frame()
        # Create menu items
        tk.Label(self.main_frame, text="Wok ON!!! Chinese Menu", font=("Arial", 14), bg='lightyellow').pack(pady=10)
        tk.Button(self.main_frame, text="Manchurian", command=self.show_manchurian_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Noodles", command=self.show_noodles_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Beverages", command=self.show_beverages_menu, bg='lightblue').pack(fill='x')
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, bg='lightcoral').pack(fill='x')

    def show_indian_breads_menu(self):
        self.create_menu_frame("Indian Breads", {
            "Naan": 40,
            "Butter Roti": 30,
            "Chapati": 25
        })

    def show_sabzi_menu(self):
        self.create_menu_frame("Sabzi", {
            "Paneer Butter Masala": 150,
            "Paneer Lababdar": 160,
            "Paneer Angara": 170
        })

    def show_rice_menu(self):
        self.create_menu_frame("Rice", {
            "Steam Rice": 50,
            "Jeera Rice": 60,
            "Biryani": 120
        })

    def show_dal_menu(self):
        self.create_menu_frame("Dal", {
            "Dal Tadka": 100,
            "Dal Fry": 110
        })

    def show_starters_menu(self):
        self.create_menu_frame("Starters", {
            "Masala Papad": 30,
            "Paneer Tikka": 100,
            "Paneer Crispy": 120,
            "Hara Bhara Kabab": 80
        })

    def show_pizza_menu(self):
        self.create_menu_frame("Pizza", {
            "Mozarella": 120,
            "Farmhouse": 150,
            "Meat Lovers": 180
        })

    def show_pasta_menu(self):
        self.create_menu_frame("Pasta", {
            "Alfredo": 130,
            "Carbonara": 140,
            "Arrabbiata": 150
        })

    def show_garlic_menu(self):
        self.create_menu_frame("Garlic Breads", {
            "Classic Garlic Bread": 80,
            "Cheese Garlic Bread": 100,
            "Garlic Breadsticks": 120
        })

    def show_dosa_menu(self):
        self.create_menu_frame("Dosa", {
            "Sada Dosa": 70,
            "Masala Dosa": 90,
            "Mysore Dosa": 100
        })

    def show_uttapa_menu(self):
        self.create_menu_frame("Uttapa", {
            "Sada Uttapa": 80,
            "Tomato Uttapa": 90,
            "Onion Uttapa": 100
        })

    def show_pav_bhaji_menu(self):
        self.create_menu_frame("Pav Bhaji", {
            "Pav Bhaji (Oil)": 100,
            "Pav Bhaji (Butter)": 120
        })

    def show_pulav_menu(self):
        self.create_menu_frame("Pulav", {
            "Half Pulav": 80,
            "Full Pulav": 120
        })

    def show_manchurian_menu(self):
        self.create_menu_frame("Manchurian", {
            "Manchurian": 100,
            "Paneer Chilli": 120,
            "Paneer Crispy": 130,
            "Veg Lollipop": 110
        })

    def show_noodles_menu(self):
        self.create_menu_frame("Noodles", {
            "Noodles": 100,
            "Chinese Bhel": 120,
            "Fried Rice": 130
        })

    def show_beverages_menu(self):
        self.create_menu_frame("Beverages", {
            "Coke": 40,
            "Pepsi": 40,
            "Sprite": 40,
            "Lemonade": 10,
            "Water": 20
        })

    def create_menu_frame(self, menu_name, menu_items):
        self.clear_frame()
        tk.Label(self.main_frame, text=menu_name, font=("Arial", 14), bg='lightyellow').pack(pady=10)
        
        for item, price in menu_items.items():
            tk.Button(self.main_frame, text=f"{item} - Rs. {price}", command=lambda i=item, p=price: self.add_to_cart(i, p), bg='lightblue').pack(fill='x')
        
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, bg='lightcoral').pack(fill='x')

    def add_to_cart(self, item, price):
        self.cart_items.append(item)
        self.cart_total += price
        messagebox.showinfo("Added to Cart", f"{item} has been added to your cart.")

    def show_cart(self):
        self.clear_frame()
        if not self.cart_items:
            tk.Label(self.main_frame, text="Your cart is empty", font=("Arial", 14), bg='lightyellow').pack(pady=10)
        else:
            tk.Label(self.main_frame, text="Your Cart", font=("Arial", 14), bg='lightyellow').pack(pady=10)
            for item in self.cart_items:
                tk.Label(self.main_frame, text=item, bg='lightyellow').pack()
            tk.Label(self.main_frame, text=f"Total: Rs. {self.cart_total}", font=("Arial", 14), bg='lightyellow').pack()
        
        tk.Button(self.main_frame, text="Checkout", command=self.checkout, bg='lightgreen').pack(pady=5, fill='x')
        tk.Button(self.main_frame, text="Back", command=self.create_main_menu, bg='lightcoral').pack(fill='x')

    def checkout(self):
        if not self.cart_items:
            messagebox.showinfo("Checkout", "Your cart is empty!")
        else:
            messagebox.showinfo("Checkout", f"Thank you for your order!\nTotal Price: Rs. {self.cart_total}")
            self.cart_items = []
            self.cart_total = 0

    def clear_cart(self):
        self.cart_items = []
        self.cart_total = 0
        messagebox.showinfo("Cart Cleared", "Your cart has been cleared.")

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodOrderingApp(root)
    root.mainloop()
