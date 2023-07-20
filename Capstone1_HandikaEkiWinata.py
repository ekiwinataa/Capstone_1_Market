# Main Menu
def main_menu():
    print("""
    ----- Main Menu -----
    1. Read Data
    2. Create Data
    3. Update Data
    4. Delete Data
    5. Back to Login Page
    """)


## READ FEATURE ##
def read_feature(stock):
    while True:
        choice = input("""
    ------ Read Data ------
    1. Show All Stocks
    2. Search Stocks by:
       Barcode
       Category
    3. Back to Main Menu
    Enter your choice: """)

        # Show stock list
        if choice == "1":
            # If there's stock in stock list
            if len(stock) == 0:
                print("No products available!")
            else:
                print("------------------------ All Stocks ------------------------")
                print_table(stock)

        # Seach product stock list 
        elif choice == "2":
            if len(stock) == 0:
                print("No products available!")
            else:
                while True:
                    sub_choice = input("Enter your preference search (barcode/category): ")
                    # Seach product by its barcode
                    if sub_choice.title() == "Barcode":
                        while True:
                            barcode = input("Enter the barcode: ")
                            # Barcode should be in numeric and 4 digits
                            if not barcode.isnumeric() or len(barcode) != 4 :
                                print("Invalid barcode! Should be in number and four digits.")
                                continue

                            barcode = int(barcode)
                            product = get_product_by_barcode(stock, barcode)
                            # Check if the input barcode matches the stock list
                            if product:
                                print("---------------------- Stock Details ----------------------")
                                print_table([product])
                                break
                            else:
                                print("Product's not found! Please enter a valid barcode.")
                                break
                        break
                    # Search product by its category
                    elif sub_choice.title() == "Category":
                        while True:
                            category = input("Enter the category: ")
                            # Category should be in alphabet
                            if not category.isalpha():
                                print("Invalid category! Should be in alphabet")
                                continue

                            products = get_product_by_category(stock, category.title())
                            # Check if the input category matches the stock list
                            if products:
                                print("---------------------- Stock Details ----------------------")
                                print_table(products)
                                break
                            else:
                                print("Category does not exist")
                                break
                        break
                    else:
                        print("Wrong preference search!")
        # Back to main menu
        elif choice == "3":
            print('Returning to Main Menu..')
            break

        else:
            print("Invalid choice. Please try again!")


## CREATE FEATURE ##
def create_feature(stock):
    while True:
        choice = input("""
    ------ Create Data ------
    1. Add new product
    2. Back to main menu
    Enter your choice: """)

        if choice == "1":
            while True:
                barcode = input("Enter the new barcode of the product: ")
                # Barcode should be in number and 4 digits
                if not barcode.isnumeric() or len(barcode) != 4:
                    print("Invalid barcode! Should be in number and four digits.")
                    continue

                barcode = int(barcode)
                # Barcode cannot be duplicate
                if get_product_by_barcode(stock, barcode):
                    print("Barcode already exists! Please try again with a distinct barcode.")
                    break

                # Continue adding product details
                while True:
                    name = input("Enter the name of the product: ").title()
                    if get_product_by_name(stock, name):
                        print("Product name's already exists. Please try a different name.")
                        continue
                    break

                while True:
                    category = input("Enter the category of the product: ").title()
                    if not category.isalpha():
                        print("Invalid category! Should be in alphabet")
                        continue
                    break

                while True:
                    quantity = input("Enter the quantity of the product: ")
                    if not quantity.isnumeric():
                        print("Invalid quantity! Should be in number.")
                        continue
                    quantity = int(quantity)
                    break

                while True:
                    price = input("Enter the price of the product: ")
                    if not price.isnumeric():
                        print("Invalid price! Should be in number")
                        continue
                    price = int(price)
                    break
                
                # Show the new product details
                new_product = [barcode, name, category, quantity, price]
                print("------------------- New product Details -------------------")        
                print_table([new_product])

                # User confirmation
                while True:
                    confirm = input("Are you sure to add this new product? (Y/N): ")
                    if confirm.lower() == "y":
                        stock.append(new_product)
                        print("New product's successfully added to stock list.")
                        print_table(stock)
                        break
                    elif confirm.lower() == "n":
                        print("Adding new product has been canceled")
                        break
                    else:
                        print("Invalid choice. Please enter 'Y' or 'N'.")
                break
        # Return to main menu
        elif choice == "2":
            print('Returning to Main Menu..')
            break

        else:
            print("Invalid choice. Please try again.")


## UPDATE FEATURE ##
def update_feature(stock):
    while True:
        choice = input("""
    ------ Update Data ------
    1. Update existing product
    2. Back to main menu
    Enter your choice: """)

        if choice == "1":
            # If there's stock in stock list
            if len(stock) == 0:
                print("No products available!")
            else:

                while True:
                    barcode = input("Enter the barcode of the product to update: ")
                    # Barcode should be in numeric and 4 digits
                    if not barcode.isnumeric() or len(barcode) != 4:
                        print("Invalid barcode! Should be in number and four digits.")
                        continue

                    barcode = int(barcode)
                    # Check if the input barcode matches the stock list
                    product = get_product_by_barcode(stock, barcode)
                    if not product:
                        print("Product's not found. Please enter a valid barcode.")
                        break

                    # Show currect product details
                    print("---------------------- Stock Details ----------------------")
                    print_table([product])

                    # Proceed to updating data
                    while True:
                        confirm = input("Do you want to proceed updating product details? (Y/N): ")

                        if confirm.lower() == "y":
                            while True:
                                update_choice = input("""
    "Name"
    "Category"
    "Quantity"
    "Price"
    "Back"
                                                    
Enter the desired product detail to be updated: """)

                                # New name of product
                                if update_choice.title() == "Name":
                                    while True:
                                        new_name = input("Enter the new name: ").title()
                                        # Name cannot be duplicate
                                        if get_product_by_name(stock, new_name):
                                            print("Product name already exists. Please enter a different name.")
                                            continue

                                        break

                                    while True:
                                        # User confirmation
                                        confirm = input("Are you sure to update this product? (Y/N): ")
                                        if confirm.lower() == "y":
                                            product[1] = new_name.title()
                                            print("Product name has been updated.")
                                            break
                                        elif confirm.lower() == "n":
                                            print("Updating has been canceled.")
                                            break
                                        else:
                                            print("Invalid choice. Please enter 'Y' or 'N'.")

                                elif update_choice.title() == "Category":
                                    while True:
                                        new_category = input("Enter the new category: ").lower()
                                        # Category should be in alphabet
                                        if not new_category.isalpha():
                                            print("Invalid category! Should be in alphabet")
                                            continue

                                        break

                                    while True:
                                        # User confirmation
                                        confirm = input("Are you sure to update this product? (Y/N): ")
                                        if confirm.lower() == "y":
                                            product[2] = new_category.title()
                                            print("Product category has been updated.")
                                            break
                                        elif confirm.lower() == "n":
                                            print("Updating has been canceled.")
                                            break
                                        else:
                                            print("Invalid choice. Please enter 'Y' or 'N'.")

                                elif update_choice.title() == "Quantity":
                                    while True:
                                        new_quantity = input("Enter the new quantity: ")
                                        # Quantity should be in number
                                        if not new_quantity.isnumeric():
                                            print("Invalid quantity! Should be in number.")
                                            continue

                                        new_quantity = int(new_quantity)

                                        break
                                    
                                    while True:
                                        # User confirmation
                                        confirm = input("Are you sure to update this product? (Y/N): ")
                                        if confirm.lower() == "y":
                                            product[3] = new_quantity
                                            print("Product quantity has been updated.")
                                            break
                                        elif confirm.lower() == "n":
                                            print("Updating has been canceled.")
                                            break
                                        else:
                                            print("Invalid choice. Please enter 'Y' or 'N'.")

                                elif update_choice.title() == "Price":
                                    while True:
                                        new_price = input("Enter the new price: ")
                                        # Price should be in number
                                        if not new_price.isnumeric():
                                            print("Invalid price. Should be in number")
                                            continue

                                        new_price = int(new_price)

                                        break
                                    
                                    while True:
                                        # User confirmation
                                        confirm = input("Are you sure to update this product? (Y/N): ")
                                        if confirm.lower() == "y":
                                            product[4] = new_price
                                            print("Product price has been updated.")
                                            break
                                        elif confirm.lower() == "n":
                                            print("Updating has been canceled.")
                                            break
                                        else:
                                            print("Invalid choice. Please enter 'Y' or 'N'.")

                                elif update_choice.title() == "Back":
                                    break

                                else:
                                    print("Invalid input. Please try again.")

                            # Display the stock details after updated
                            print("------------------- Updated Stock Details -------------------")                
                            print_table(stock)

                            break

                        elif confirm.lower() == "n":
                            print("Updating has been canceled.")
                            break
                        else:
                            print("Invalid choice. Please enter 'Y' or 'N'.")
                    break

        elif choice == "2":
            print("Returning to main menu")
            break

        else:
            print("Invalid choice. Please try again.")


## DELETE FEATURE ##
def delete_feature(stock):
    while True:
        choice = input("""
    ------ Delete Feature ------
    1. Delete existing product
    2. Back to main menu
    Enter your choice: """)

        if choice == "1":
            if len(stock) == 0:
                print("No products available!")
            else:
                while True:
                    barcode = input("Enter the barcode of the product to be deleted: ")
                    # Barcode should be in number and four digits
                    if not barcode.isnumeric() or len(barcode) != 4:
                        print("Invalid barcode. Should be in number and four digits")
                        continue

                    barcode = int(barcode)
                    #Check if the input barcode matches the stock list
                    product = get_product_by_barcode(stock, barcode)
                    if not product:
                        print("Product's not found. Please enter a valid barcode.")
                        break

                    # Display product before being deleted
                    print("------------------- Deleted Stock Details -------------------")
                    print_table([product])

                    while True:
                        # User confirmation
                        confirm = input("Are you sure to delete this product? (Y/N): ")
                        if confirm.lower() == "y":
                            stock.remove(product)
                            print("Product successfully deleted.")
                            print_table(stock)
                            break
                        elif confirm.lower() == "n":
                            print("Deletion canceled.")
                            break
                        else:
                            print("Invalid choice. Please enter 'Y' or 'N'.")

                    break

        elif choice == "2":
            break

        else:
            print("Invalid choice. Please try again.")


# Tabular setup used in Staff mode #
def print_table(stock):
    table_header = ["Barcode", "Name", "Category", "Quantity", "Price"]
    header_format = "{:<10} {:<15} {:<15} {:<10} {:<10}"
    row_format = "{:<10} {:<15} {:<15} {:<10d} {:<10d}"

    print(header_format.format(*table_header))
    for product in stock:
        print(row_format.format(*product))

# Tabular setup used in Customer mode #
def print_cart(cart):
    table_header = ["Barcode", "Name", "Category", "Quantity", "Price"]
    header_format = "{:<10} {:<15} {:<15} {:<10} {:<10}"
    row_format = "{:<10d} {:<15} {:<15} {:<10d} {:<10d}"

    print(header_format.format(*table_header))
    for product in cart:
        print(row_format.format(*product))


# Function for product search by its primary key #
def get_product_by_barcode(stock, barcode):
    for product in stock:
        if product[0] == barcode:
            return product
    return None

# Function for product search by its category #
def get_product_by_category(stock, category):
    products = []
    for product in stock:
        if product[2] == category:
            products.append(product)
    return products

# Function for product search by its name #
def get_product_by_name(stock, name):
    products = []
    for product in stock:
        if product[1] == name:
            products.append(product)
    return products


# Function to calculate the total price of items in the cart #
def calculate_total_price(cart):
    total_price = 0
    for item in cart:
        total_price += item[3] * item[4]  # Quantity * Price
    return total_price


# Function to get the amount of payment from the customer input #
def get_amount_pay(amount_pay):
    while True:
        amount_pay = input("Enter the amount of payment: ")
        if not amount_pay.isnumeric():
            print("Invalid input. Please enter a numeric value for the amount of payment.")
            continue

        amount_pay = int(amount_pay)
        return amount_pay

## CUSTOMER MODE ##
def customer_mode(stock):
    cart = []

    while True:
        customer_choice = input("""
    -------- Customer Menu --------
    1. View All Products
    2. Search Products by Category
    3. Add Product to Cart
    4. Delete product in cart
    5. View Cart
    6. Checkout
    7. Back to main menu
    Enter your choice: """)

        # View all products
        if customer_choice == "1":
            # Check if there's product in stock list
            if len(stock) == 0:
                print("No products available!")
            else:
                print("------------------------ All Stocks ------------------------")
                print_table(stock)

        # Searching specific product
        elif customer_choice == "2":
            # Check if there's product in stock list
            if len(stock) == 0:
                print("No products available!")
            else:
                while True:
                    category = input("Enter the category: ").lower()
                    # Category should be in alphabet
                    if not category.isalpha():
                        print("Invalid category! Should be in alphabet")
                        continue

                    products = get_product_by_category(stock, category.title())
                    # Check if the category input matches the stock list
                    if products:
                        print("---------------------- Product Details ---------------------")
                        print_table(products)
                        break
                    else:
                        print("Category does not exist! Try again with a valid category")
                        break
        
        # Add item to cart
        elif customer_choice == "3":
            #Check if there's product in stock list
            if len(stock) == 0:
                print("No products available!")
            else:
                while True:
                    barcode = input("Enter the barcode of the product to add to cart: ")
                    # Barcode should be in number and four digits
                    if not barcode.isnumeric() or len(barcode) != 4:
                        print("Invalid barcode! Should be in number and four digits")
                        continue

                    barcode = int(barcode)

                    # Check if input barcode matches the stock list
                    product = get_product_by_barcode(stock, barcode)
                    if product:
                        print("--------------------- Product Details ---------------------")
                        print_table([product])

                        while True:
                            quantity = input("Enter the quantity to add to cart: ")
                            # Quantity should be in number
                            if not quantity.isnumeric():
                                print("Invalid quantity! Should be in number.")
                                continue

                            quantity = int(quantity)

                            # Check if the input quantity not exceed the stock details
                            if quantity > product[3]:
                                print("Quantity exceeds the available stock. Please enter a valid quantity.")
                                continue

                            while True:
                                # User confirmation
                                confirm = input("Are you sure to add this product into cart? (Y/N): ")
                                if confirm.lower() == "y":
                                    cart.append([product[0], product[1], product[2], quantity, product[4]])
                                    print("Product has been added to cart.")
                                    break
                                elif confirm.lower() == "n":
                                    print("Adding to cart has been cancelled")
                                    break
                                else:
                                    print("Invalid choice. Please enter 'Y' or 'N'.")
                            break

                    else:
                        print("Product not found. Please enter a valid barcode.")
                    break

        # Delete item in cart
        elif customer_choice == "4":
            # Check if cart is empty
            if len(cart) == 0:
                print("Cart is empty.")
            else:
                while True:
                    barcode = input("Enter the barcode of the product to be deleted from cart: ")
                    # Barcode should be in number and four digits
                    if not barcode.isnumeric() or len(barcode) != 4:
                        print("Invalid barcode! Should be in number and four digits")
                        continue

                    barcode = int(barcode)

                    # Check if the input barcode matches item in cart
                    product = get_product_by_barcode(cart, barcode)
                    if not product:
                        print("Product's not found! Please enter a valid barcode") 
                        break

                    # Display item before deletion
                    print("------------------ Deleted Product Details -----------------")
                    print_cart([product])

                    while True:
                        # User confirmation
                        confirm = input("Are you sure to remove this product from the cart? (Y/N): ")
                        if confirm.lower() == "y":
                            cart.remove(product)
                            print("Product has been removed from cart.")
                            break
                        elif confirm.lower() == "n":
                            print("Removing has been canceled")
                            break
                        else:
                            print("Invalid choice. Please enter 'Y' or 'N'.")
                    break
                
        # View item in cart
        elif customer_choice == "5":
            # Check if cart is empty
            if len(cart) == 0:
                print("Cart is empty.")
            else:
                print("---------------------------- Cart --------------------------")
                print_cart(cart)

        # Checkout item in cart
        elif customer_choice == "6":
            # Check if cart is empty
            if len(cart) == 0:
                print("Cart is empty. Please add products to cart first.")
            else:
                print("-------------------------- Cart ----------------------------")
                print_cart(cart)

                while True:
                    # User confirmation to checkout the cart
                    confirm = input("Are you sure that would be all for today's shopping? (Y/N): ")
                    if confirm.lower() == "y":
                        while True:
                            total_price = calculate_total_price(cart)
                            print("Total Price: Rp.", total_price)

                            amount_pay = get_amount_pay(total_price)

                            # If amount entered from user is less than the required amount to pay
                            if amount_pay < total_price:
                                amount_needed = total_price - amount_pay
                                print(f"Insufficient payment. Please add Rp.{amount_needed} more.")
                                continue
                            # If amount entered from user is exactly equal to the required amount to pay
                            elif amount_pay == total_price:
                                print("Thank you for shopping with us!")
                                break
                            # If amount entered from user is less than the required amount to pay
                            else:
                                change = amount_pay - total_price
                                print(f"Thank you for shopping with us! Your change: Rp.{change}")
                                break
                        
                        # Reduce the quantity of bought products in the stock
                        for item in cart:
                            barcode = item[0]
                            for product in stock:
                                if product[0] == barcode:
                                    product[3] -= item[3]
                                    break

                        # Empty the cart after checkout
                        cart = []  
                        break
                    
                    elif confirm.lower() == "n":
                        break
                    else:
                        print("Invalid choice. Please enter 'Y' or 'N'.")

        elif customer_choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")
    


## MAIN FUNCTION ##
def jaya_mart():
    # Dummy data
    stock = [
        [1001, "Coffee Can", "Beverage", 15, 7000],
        [1002, "Coffee Sachet", "Beverage", 9, 1000],
        [1003, "Milk", "Beverage", 10, 15000],
        [1004, "Milk Powder", "Beverage", 12, 30000],
        [1005, "White Bread", "Food", 5, 10000],
        [1006, "Croissant", "Food", 4, 8000],
        [1007, "Chip", "Food", 14, 9000],
        [1008, "Cake", "Food", 8, 25000]
    ]

    # Choosing the desired mode to enter the program
    while True:
        print("""
    ===============================
    | WELCOME TO THE JAYA JAYA MART |
    ===============================
        """)
        user_type = input("""
    LOGIN AS:
    1. Staff
    2. Customer
    3. Exit
    Enter your choice: """)

        # Staff Mode
        if user_type == "1":
            access_code = input("Enter the Access Code: ")
            if access_code == "1212":
                print("Access Granted!")
                while True:
                    main_menu()
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        read_feature(stock)
                    elif choice == "2":
                        create_feature(stock)
                    elif choice == "3":
                        update_feature(stock)
                    elif choice == "4":
                        delete_feature(stock)
                    elif choice == "5":
                        print("Returning to Login Page..")
                        break
                    else:
                        print("Wrong Menu Input!")
            else:
                print("Access Denied! Re enter the program")
                break

        # Customer Mode
        elif user_type == "2":
            customer_mode(stock)
        elif user_type == "3":
            print("Exiting the program..")
            break
        else:
            print("Invalid choice!")





# Run the program
jaya_mart()
