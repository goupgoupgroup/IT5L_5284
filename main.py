#Import 'Database' Class from database.py to borrow functions
from database import Database

#Connect to 'supre_db' Database using 'Database' Class
db = Database('localhost', 'SupreAdmin', 'supr34dmIN', 'supre_db')

#Import tkinter, tkinter.ttk, functools.partial for Class Supre
import tkinter as tk
from tkinter import ttk
#from PIL import ImageTk, Image
import tkinter.messagebox
from functools import partial

#Create Supre Class
class Supre:
    __role_user = None
    __role_pass = None

    def __init__(self):
        #Create 'Supre' Class Main Window
        self.window = tk.Tk()
        self.window.title('Final Project - Supre')

        self.width = self.window.winfo_screenwidth()
        self.height = self.window.winfo_screenheight()

        print(f'{self.width}, {self.height}')

        self.window.geometry(f'{self.width}x{self.height}')
        self.window.resizable(width='false', height='false')

        #self.img = ImageTk.PhotoImage(Image.open('supre_clothes.png'))
        
        
        #Add Style to Frames
        self.style = ttk.Style()
        self.style.theme_use('default')

        self.style.configure('bg.TFrame', background= 'burlywood3')
        self.bg_frame = ttk.Frame(self.window, style='bg.TFrame')
        self.bg_frame.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        #self.bg_label= tk.Label(self.window, image = self.img, border=False)
        #self.bg_label.place(relx=0.17, rely=0.36)
        
        #Entry Styles
        self.style.configure('TEntry', foreground='tan4')
        
        #Labels for 'Supre' Main Window
        self.style.configure('supre.TLabel', foreground='tan4', background='burlywood3', font= ('Times New Roman Bold Italic', 130))
        self.style.configure('TLabel', foreground='cornsilk2', background='burlywood3', font= ('Times New Roman Bold', 15))
        ttk.Label(self.window, text='Supre', style='supre.TLabel').place(relx=0.18, rely=0.28, relwidth= 0.3, relheight= 0.2)
        ttk.Label(self.window, text='Where Style Meets Confidence').place(relx = 0.31, rely=0.45)

        #LabelFrame for Roles
        self.frame = tk.LabelFrame(self.window, text='Welcome', fg='cornsilk2', bg='burlywood3', font= ('Times New Roman Bold Italic', 30))
        for row in range(3):
            self.frame.grid_rowconfigure(row, weight=1)
        for col in range(1):
            self.frame.grid_columnconfigure(col, weight=1)

        #Button Styles
        self.style.configure('TButton', foreground= 'cornsilk2', background='tan4', font= ('Times', 25))
        self.style.map('TButton', foreground = [('pressed', 'tan4')], background=[('pressed', 'burlywood3')])
        
        
        ttk.Button(self.frame, text='Manager', command=partial(self.login_new_window, self.window, 'MANAGER')).grid(row=0, column=0, sticky='s', ipady=10)
        ttk.Button(self.frame, text='Cashier', command=partial(self.login_new_window, self.window, 'CASHIER')).grid(row=1, column=0, ipady=10)

        self.frame.pack(fill='y', expand= 'yes', anchor = 'e', padx=300, pady=300, ipadx=100)

        #Execute Window when 'Supre' Class is called
        self.window.mainloop()
    
    #Login Window
    def login_new_window(self, window, role):
        self.role = role
        
        self.login_window = tk.Toplevel(window)
        self.bgframe = ttk.Frame(self.login_window, style='bg.TFrame')
        self.bgframe.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        self.login_window.geometry('500x400')

        self.login_frame = tk.LabelFrame(self.login_window, text=f'You are logging in as {role}', fg='cornsilk2', bg='burlywood', font= ('Times New Roman Bold Italic', 15))

        self.entry_user= tk.StringVar()
        self.entry_pass= tk.StringVar()
         
        for row in range(3):
            self.login_frame.grid_rowconfigure(row, weight=1)
        for col in range(2):
            self.login_frame.grid_columnconfigure(col, weight=1)

        ttk.Label(self.login_frame, text='Username:').grid(row=0, column=0, sticky='e')
        ttk.Entry(self.login_frame, textvariable= self.entry_user).grid(row=0, column=1, padx=20, ipady=7, ipadx=50, sticky='w')
        ttk.Label(self.login_frame, text='Password:').grid(row=1, column=0, sticky='ne')
        ttk.Entry(self.login_frame, textvariable= self.entry_pass, show='*').grid(row=1, column=1, padx=20, ipady=7, ipadx=50, sticky='nw')
        self.log_btn = ttk.Button(self.login_frame, text='Login', command=partial(self.login, self.login_window, self.role, self.entry_user, self.entry_pass))
        self.log_btn.grid(row=2, column=0, columnspan=2, sticky='n')

        if self.role == 'CASHIER':
            self.__role_user = 'cash'
            self.__role_pass = 'cash'
            self.entry_user.set(self.__role_user)
            self.entry_pass.set(self.__role_pass)

        self.login_frame.pack(fill='both', expand='yes', padx=10, pady= 10)
    
    #Check Login
    def login(self, login_window, role, username, password):
        
        if role == 'MANAGER':
            self.__role_user = 'admin'
            self.__role_pass = 'admin'
            
        if self.__role_user == username.get() and self.__role_pass == password.get():
            if self.__role_user == 'admin':
                self.product()
                login_window.destroy()
            elif self.__role_user == 'cash':    
                self.cart()
                login_window.destroy()
        else:
            tkinter.messagebox.showerror(title='Login Error', message= 'Incorrect Username or Password')
  
    #Product Window
    def product(self):
        self.product_window = tk.Toplevel(self.window)
        self.bgframe = ttk.Frame(self.product_window, style='bg.TFrame')
        self.bgframe.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        self.product_window.geometry('500x400')
        self.product_window.resizable(width = 'false', height= 'false')
        
        for row in range(4):
            self.product_window.grid_rowconfigure(row, weight=1)
        for col in range(1):
            self.product_window.grid_columnconfigure(col, weight=1)

        #Button for Adding Products
        self.add_btn = ttk.Button(self.product_window, text='Add Products', command=self.add)
        self.add_btn.grid(row=0, column=0, sticky='nsew')
        #Button for Viewing Products
        self.view_btn = ttk.Button(self.product_window, text='View Products', command=self.view)
        self.view_btn.grid(row=1, column=0, sticky='nsew')
        #Button for Updating Products
        self.upd_btn = ttk.Button(self.product_window, text='Update Products', command=self.update)
        self.upd_btn.grid(row=2, column=0, sticky='nsew')
        #Button for Removing Products
        self.del_btn = ttk.Button(self.product_window, text='Remove Products', command=self.remove)
        self.del_btn.grid(row=3, column=0, sticky='nsew')
    
    #Window for Adding Products
    def add(self):
        self.add_window = tk.Toplevel(self.window)
        self.bgframe = ttk.Frame(self.add_window, style='bg.TFrame')
        self.bgframe.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        
        self.add_window.geometry('500x400')
        self.add_window.resizable(width = 'false', height= 'false')

        self.product_name = tk.StringVar()
        self.product_stocks = tk.StringVar()
        self.product_price = tk.StringVar()

        for row in range(4):
            self.add_window.grid_rowconfigure(row, weight=1)
        for col in range(2):
            self.add_window.grid_columnconfigure(col, weight=1)
        
        ttk.Label(self.add_window, text='Enter Product Name:').grid(row=0, column=0)
        ttk.Entry(self.add_window, textvariable=self.product_name).grid(row=0, column=1, padx=20, ipady=7)

        ttk.Label(self.add_window, text='Enter No. of Stocks Available:').grid(row=1, column=0)
        ttk.Entry(self.add_window, textvariable=self.product_stocks).grid(row=1, column=1, padx=20, ipady=7)

        ttk.Label(self.add_window, text='Enter Price of Product:').grid(row=2, column=0)
        ttk.Entry(self.add_window, textvariable=self.product_price).grid(row=2, column=1, padx=20, ipady=7)
        

        self.confirm_btn = ttk.Button(self.add_window, text='Confirm', command=partial(self.add_products, self.add_window, self.product_name, self.product_stocks, self.product_price))
        self.confirm_btn.grid(row=3, column=0, columnspan=2)
    
    #Add Product to Database
    def add_products(self, window, name, stocks, price):
        window.destroy()
        
        if not name.get() or not stocks.get() or not price.get():
            tkinter.messagebox.showwarning(title='Added New Product', message=f'An Empty field has been found. Please Try Again.')    
        else: 
            db.add_product(name.get(), stocks.get(), price.get())
            tkinter.messagebox.showinfo(title='Added New Product', message=f'{name.get().upper()} has been added successfully.')

    #Window for Viewing Products    
    def view(self):
        self.view_window = tk.Toplevel(self.window)
        self.bgframe = ttk.Frame(self.view_window, style='bg.TFrame')
        self.bgframe.place(x=0, y=0, relwidth=1.0, relheight=1.0)
        
        self.view_window.geometry('800x500')
        self.view_window.resizable(width = 'false', height= 'false')

        self.table = ttk.Treeview(self.view_window, columns= ('id', 'name', 'stock', 'price'), show= 'headings')
        self.table.heading('id', text = 'Product ID')
        self.table.heading('name', text = 'Name')
        self.table.heading('stock', text = 'Stocks')
        self.table.heading('price', text = 'Price')
        
        #View Product Data from 'products' Table
        db.cursor.execute('SELECT * FROM products')
        self.product_table = db.cursor.fetchall()

        for product in self.product_table:
            self.table.insert(parent = '', index='end', values=list(product))

        self.table.pack(fill='both', expand='yes')
    
    #Window for Updating Products
    def update(self):
        self.update_window = tk.Toplevel(self.window)
        self.bgframe = ttk.Frame(self.update_window, style='bg.TFrame')
        self.bgframe.place(x=0, y=0, relwidth=1.0, relheight=1.0)
     
        self.update_window.geometry('500x400')
        self.update_window.resizable(width = 'false', height= 'false')

        self.entry_id = tk.StringVar()
        self.entry_name = tk.StringVar()
        self.entry_stocks = tk.StringVar()
        self.entry_price = tk.StringVar()

        ttk.Label(self.update_window, text='Enter ID of product to Update:').pack()
        ttk.Entry(self.update_window, textvariable=self.entry_id).pack(pady=7)
        ttk.Label(self.update_window, text='Enter Product Name:').pack()
        ttk.Entry(self.update_window, textvariable=self.entry_name).pack(pady=7)
        ttk.Label(self.update_window, text='Enter No. of Stocks:').pack()
        ttk.Entry(self.update_window, textvariable=self.entry_stocks).pack(pady=7)
        ttk.Label(self.update_window, text='Enter Price:').pack()
        ttk.Entry(self.update_window, textvariable=self.entry_price).pack(pady=7)
        ttk.Button(self.update_window, text='Update', command=partial(self.update_products, self.update_window, self.entry_id, self.entry_name, self.entry_stocks, self.entry_price)).pack()
    
    #Update Products from Database
    def update_products(self, window, id, name, stocks, price):
        window.destroy()
        
        if not id.get() or not name.get() or not stocks.get() or not price.get():
            tkinter.messagebox.showwarning(title='Added New Product', message=f'An Empty field has been found. Please Try Again.')    
        else: 
            db.update_product(id.get(), name.get(), stocks.get(), price.get())
            tkinter.messagebox.showinfo(title='Updated New Product', message=f'{name.get().upper()} has been updated successfully.')

    #Window for Removing Products
    def remove(self):
        self.remove_window = tk.Toplevel(self.window)
        self.bgframe = ttk.Frame(self.remove_window, style='bg.TFrame')
        self.bgframe.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        self.remove_window.geometry('300x200')
        self.remove_window.resizable(width = 'false', height= 'false')
        
        self.entry_id = tk.StringVar()

        ttk.Label(self.remove_window, text='Enter ID of product to remove:').pack()
        ttk.Entry(self.remove_window, textvariable=self.entry_id).pack(pady=7)
        ttk.Button(self.remove_window, text='Remove', command=partial(self.remove_products, self.remove_window, self.entry_id)).pack()
    
    #Remove Products from Database
    def remove_products(self, window, id):
        window.destroy()
        
        if not id.get():
            tkinter.messagebox.showwarning(title='Removed New Product', message=f'An Empty field has been found. Please Try Again.')    
        else: 
            db.remove_product(id.get())
            tkinter.messagebox.showinfo(title='Removed New Product', message=f'Product with ID No.{id.get()} has been removed successfully.')
    
    #Cart Window for Cashier
    def cart(self):
        self.cart_window = tk.Toplevel(self.window)
        self.bgframe = ttk.Frame(self.cart_window, style='bg.TFrame')
        self.bgframe.place(x=0, y=0, relwidth=1.0, relheight=1.0)

        self.cart_window.geometry('1200x700')
        self.cart_window.resizable(width = 'false', height= 'false')
        
        for row in range(5):
            self.cart_window.grid_rowconfigure(row, weight=1)
        for col in range(3):
            self.cart_window.grid_columnconfigure(col, weight=1)

        self.search_id = tk.StringVar()
        self.add_id = tk.StringVar()
        
        #Search and Show All Buttons for Product Table
        ttk.Label(self.cart_window, text='Search ID:').grid(row=0, column=0, padx=25, pady=5, sticky='se')
        ttk.Entry(self.cart_window, textvariable=self.search_id).grid(row=0, column=1, pady=5, ipadx=15, ipady=5, sticky='sew')
        self.showall_btn = ttk.Button(self.cart_window, text='Show All', command=partial(self.all))
        self.showall_btn.grid(row=1, column=0, sticky='ne')
        self.search_btn = ttk.Button(self.cart_window, text='Search', command=partial(self.search, self.search_id))
        self.search_btn.grid(row=1, column=1, sticky='new')
        
        #Clear, Add to Cart and Purchase Button for Cart Table
        ttk.Label(self.cart_window, text='Product ID:').grid(row=2, column=0, padx=25, pady=5, sticky='se')
        ttk.Entry(self.cart_window, textvariable=self.add_id).grid(row=2, column=1, pady=5, ipadx=15, ipady=5, sticky='sew')
        self.clear_btn = ttk.Button(self.cart_window, text='Clear', command=self.clear_cart)
        self.clear_btn.grid(row=3, column=0, sticky='ne')
        self.adcrt_btn = ttk.Button(self.cart_window, text='Add to Cart', command=partial(self.add_cart, self.add_id))
        self.adcrt_btn.grid(row=3, column=1, sticky='new')
        self.purchase_btn = ttk.Button(self.cart_window, text='Purchase', command=self.purchase)
        self.purchase_btn.grid(row=4, column=1, columnspan=2, padx=20, sticky='ne')

        
        self.table = ttk.Treeview(self.cart_window, columns= ('id', 'name', 'stock', 'price'), show= 'headings')
        self.table.heading('id', text = 'Product ID')
        self.table.heading('name', text = 'Name')
        self.table.heading('stock', text = 'Stocks')
        self.table.heading('price', text = 'Price')

        self.table.grid(row=0, rowspan=2, column=2, padx=20, pady=20, sticky='nsew')
        
        #Cart Treeview
        self.cart_table = ttk.Treeview(self.cart_window, columns= ('id', 'name', 'stock', 'price'), show= 'headings')
        self.cart_table.heading('id', text = 'Product ID')
        self.cart_table.heading('name', text = 'Name')
        self.cart_table.heading('stock', text = 'Stocks')
        self.cart_table.heading('price', text = 'Price')

        self.cart_table.grid(row=2, rowspan=2, column=2, padx=20, pady=20, sticky='nsew')
    
    #Show All Products
    def all(self):
        for product in self.table.get_children():
            self.table.delete(product)
        
        #Show Product Data from 'products' Table
        db.cursor.execute('SELECT * FROM products')
        self.product_table = db.cursor.fetchall()

        for product in self.product_table:
            self.table.insert(parent = '', index='end', values=list(product))

    #Search ID for Cart
    def search(self, id):
        for product in self.table.get_children():
            self.table.delete(product)

        db.cursor.execute(f"SELECT * FROM products WHERE id = {id.get()}")
        self.product_table = db.cursor.fetchall()

        for product in self.product_table:
            self.table.insert(parent = '', index='end', values=list(product))
    
    #Add Products to Cart
    __total = float(0)
    __quantity = int(0)
    __product_id_list = []
    def add_cart(self, id):
        db.cursor.execute(f"SELECT * FROM products WHERE id = {id.get()}")
        self.product_table = db.cursor.fetchall()
        
        for product in self.product_table:
            if product[2] == 0:
                tkinter.messagebox.showerror(title='Out of Stock', message=f'Product with ID No.{product[0]} has {product[2]} stocks.')
            else:
                self.cart_table.insert(parent = '', index='end', values=list(product))
                self.__total += float(product[3])
                self.__quantity += int(1)
                self.__product_id_list.append(product[0])
    
    #Clear Products in Cart
    def clear_cart(self):
        for product in self.table.get_children():
            self.cart_table.delete(product)

        self.__total = float(0)
        self.__quantity = int(0)
        self.__product_id_list = []
    
    #Confirm Purchase from Cart
    def purchase(self):
        for product in self.__product_id_list:
            db.purchase(product)

        tkinter.messagebox.showinfo(title='Purchased Product', message=f'Successfully purchased {self.__quantity} items. Total Payment: ${self.__total:.2f}')
        
        self.__total = float(0)
        self.__quantity = int(0)

#Run 'Supre' Class
Supre()
