import datetime
from write import update_product_file
from read import load_products

new_cost_price= None
products = load_products("Available_Products.txt")
def get_suppliers_details():
           print("For invoice generation enter your details first: ")
           print("\n")
           supplier_name= input("Please enter supplier's name: ")
           print("\n")
           phone_number = input("Please enter phone number: ")
           print("\n")
           return supplier_name,phone_number
    

def get_valid_product_id():
           while True:
            #taking valid product id 
            try:
               product_id=int(input("Please provide the ID of the product : "))
               print("\n")
               if product_id>0:
                   return product_id
               else:
                    print("Please provide the valid product ID")
                    print("\n")
                    product_id = int(input("Please provide the ID of the product : "))
                    print("\n")
            except ValueError: 
                      print("Please provide the valid product ID")
                      print("\n")
                      
                    
def get_product_quantity():
     while True:
                   try:
                        new_product_quantity = int(input("Please enter number of quantity you purchased: "))
                        print("\n")
                        if new_product_quantity>0:
                           return new_product_quantity
                        else:
                            print("Quantity should be positive")
                   except ValueError: 
                      print("Please provide the valid product quantity")
                      print("\n")
                      new_product_quantity = int(input("Please enter number of quantity you purchased: "))
                      print("\n")
                  

def add_new_product(products,product_id):
                      product_id=int(product_id)
                      new_product_name = input("Enter name of new product: ")
                      new_product_brand= input("Enter name of the brand: ")
                      new_product_quantity=get_product_quantity()
                      new_product_price = input("Enter price of new product: ")
                      new_product_origin=input("Enter the origin of new product:")
                      products[product_id] = [new_product_name, new_product_brand, new_product_quantity,new_product_price,new_product_origin]
                      print("Product is added")
                      return new_product_quantity
                        
           
            
def update_existing_product(products,product_id,new_quantity,new_cost_price):
            #updating available stock
             name, brand, qty, cost_price, origin = products[product_id]
             current_quantity=int(qty)
             products[product_id][2]=str(current_quantity + new_quantity)
             print("\n")
             if new_cost_price.strip():
               products[product_id][3]= new_cost_price
             return name,brand

             
def display_updated_inventory(products):
           #displaying the updated dictionary(inventory)
            "print(products)"
            print("\nUPDATED INVENTORY:")
            print("*" * 80)
            print("ID\tNAME\t\tBRAND\t\tQTY\tCOST\tORIGIN") 
            print("*" * 80)

            for product_id, product_data in products.items():
               # Extract product details
               name, brand, quantity, cost, origin = product_data
               
    
               # Print with tab separation
               print(product_id, end="\t")
               print(name, end="\t")  
               print(brand, end="\t")  
               print(quantity, end="\t")
               print(cost, end="\t")
               print(origin)

            print("*" * 80)

def generate_invoice_content(supplier_name,phone_number,user_buy_items,grand_total):
            total_vat=0
            final_total=0
             # date and time for invoice
            Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


             # invoice content
            invoice_content = ""
            invoice_content += "*" * 77 + "\n"
            invoice_content += "\t\t\t\t  INVOICE RECEIPT\n"
            invoice_content += "=" * 77 + "\n"
            invoice_content += "Supplier's Name: " + supplier_name + "\n"
            invoice_content += "Phone Number: " + phone_number + "\n"
            invoice_content += "Date and Time: " + Time + "\n"
            invoice_content += "=" * 77 + "\n"
            invoice_content += "ITEMS PURCHASED:\n"
            invoice_content += "-" * 17 

            # Add items to invoice_content
            for item in user_buy_items:
              invoice_content += "\n"
              invoice_content += "Product ID: " + str(item['Product ID']) + "\n"+"Product Name: " + item['Product Name'] + "\n"
              invoice_content += "Price: " + str(float(item['Price'])) + " x " + str(item['Quantity']) + " = " + str(float(item['Total'])) + "\n"
              total =float(item['Total'])
              vat = total* 0.13
              final_price=total + vat
              total_vat += vat
              final_total +=final_price

            # Add total to invoice_content
            invoice_content += "=" * 77 + "\n"
            invoice_content += "VAT: " + str(float(vat))+ "\n"
            invoice_content += "SUB TOTAL: " + str(float(grand_total))+ "\n"
            invoice_content += "GRAND TOTAL: " + str(float(final_price))+ "\n"
            invoice_content += "=" * 77 + "\n"
            invoice_content += "\t\t\t Thank you for shopping with us!\n"
            invoice_content += "*" * 77
            return invoice_content

def save_invoice(supplier_name,invoice_content):
            # Save to file 
            filename =supplier_name+".txt"
            with open(filename, 'w') as file:
                  file.write(invoice_content)
     
            print("Invoice saved as " + filename)
            print(invoice_content)

def restock_products(products):
    supplier_name,phone_number = get_suppliers_details()
    user_buy_items=[]
    grand_total=0

    buy_loop= True
    while buy_loop==True:
        product_id=get_valid_product_id()
        new_cost_price=None

        if product_id in products:
            new_quantity = get_product_quantity()
            new_cost_price = input("Enter new cost price (press enter if the cost price is same as before): ")
            name, brand = update_existing_product(products, product_id, new_quantity, new_cost_price)
        else:
            if input("Do you want to add new product? (y/n): ").lower()=='y':
                                new_quantity = add_new_product(products, product_id)
                                name, brand = products[product_id][0], products[product_id][1]
            else:
                print("Task Cancelled")
                continue
        display_updated_inventory(products)
        #calculate total
        Cost_price_per_item=float(products[product_id][3])
        total = Cost_price_per_item *new_quantity
        grand_total += total
        
 #adding item to invoice
        user_buy_items.append({
                'Product ID': product_id,
                'Product Name': products[product_id][0],
                'Product Brand':brand,
                'Price': Cost_price_per_item,
                'Quantity': new_quantity,
                'Total': total,
            })
            

        Continue = input("Do you wish to continue(yes/no) :")
        if Continue =="no":
                break
    invoice_content=generate_invoice_content(supplier_name,phone_number,user_buy_items,grand_total)
    save_invoice(supplier_name,invoice_content)
    update_product_file(products)
    








def inform_free_items():
    print("We are having Buy 3 , get 1 free, offer. So, Enjoy Shopping!!!!")



def display_products(products):
        print("*" * 80)
        print("ID\tNAME\t\tBRAND\t\tQTY\tPRICE\tORIGIN")
        print("*" * 80)
        for key, value in products.items():
           
            name, brand, qty, cost_price, origin = value
    
            # Calculate selling price with 200% markup 
            selling_price = float(cost_price) * 3
    
            # Print 
            print(key, end="\t")
            print(name, end="\t")
            print(brand, end="\t")
            print(qty, end="\t")
            print(format(selling_price), end="\t")  
            print(origin)

        print("*" * 80)
def get_customer_details():
        print("For bill generation enter your details first: ")
        print("\n")
        customer_name= input("Please enter customer's name: ")
        print("\n")
        phone_number = input("Please enter phone number: ")
        print("\n")
        return customer_name,phone_number

def get_valid_product_ids(products):
    while True:
        try:
                 product_id=int(input("Please provide the ID of the product : "))
                 print("\n")

              #validating entered product ID
                 if product_id in products:
                       return product_id
                 else:
                    print("Please provide the valid product ID")
                    print("\n")
                    product_id = int(input("Please provide the ID of the product : "))
                    print("\n")
        except ValueError: 
                    print("Please provide the valid product ID")
                    print("\n")
                    product_id = int(input("Please provide the ID of the product : "))
                    print("\n")

        
        
def calculate_free_items(products,product_id,requested_quantity):
            get_quantity_of_selected_product = int(products[product_id][2])
            free_items = requested_quantity // 3
            total_deducted = requested_quantity + free_items
            
             #validating available stock
            if total_deducted > int(get_quantity_of_selected_product):
                print("The quantity you are seeking is not available in our shop. Please look again in the table and enter the quantity.")
                print("\n")
                return None,None
            else:
              return total_deducted,free_items
def update_inventory(products, product_id, total_deducted):
    products[product_id][2]=str(int(products[product_id][2])-total_deducted)
def display_updated_products(products):
            print("\nUPDATED INVENTORY:")
            print("*" * 80)
            print("ID\tNAME\t\tBRAND\t\tQTY\tCOST\tORIGIN") 
            print("*" * 80)

            for product_id, product_data in products.items():
               # Extract product details
               name, brand, quantity, cost, origin = product_data
    
               # Print with tab separation
               print({product_id}, end="\t")
               print(name, end="\t")  
               print(brand, end="\t")  
               print(quantity, end="\t")
               print(cost, end="\t")
               print(origin)

            print("*" * 80)
def calculate_total_price(products,product_id,quantity):
    Cost_price_per_item=float(products[product_id][3])
    return Cost_price_per_item*quantity,Cost_price_per_item
def generate_bill_content(customer_name,phone_number,user_sell_items,grand_total):
            total_vat=0
            final_price=0
      # bill content
        #time for bill
            Time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            bill_content=""
            bill_content += "*" * 77 + "\n"
            bill_content += "\t\t\t\t  INVOICE RECEIPT\n"
            bill_content += "=" * 77 + "\n"
            bill_content += "Customer Name: " + customer_name + "\n"
            bill_content += "Phone Number: " + phone_number + "\n"
            bill_content += "Date and Time: " + Time + "\n"
            bill_content += "=" * 77 + "\n"
            bill_content += "ITEMS PURCHASED:\n"
            bill_content += "-" * 17 

            
            # Add items to bill_content
            for item in user_sell_items:
             bill_content += "\n"
             bill_content += "Product ID: " + str(item['Product ID']) + "\n"+"Product Name: " + item['Product Name'] + "\n"
             bill_content += "Price: " + str(float(item['Price'])) + " x " + str(item['Quantity']) + " = " + str(float(item['Total'])) + "\n"
             total =float(item['Total'])
             vat = float(item['Price'])* 0.13
             total_vat += vat
             bill_content += "(Free items: " + str(item['Free Items']) + ")\n"

            # Add total to bill_content
            bill_content += "=" * 77 + "\n"
            bill_content += "VAT: " + str(float(total_vat))+ "\n"
            bill_content += "SUB TOTAL: " + str(float(final_price))+ "\n"
            bill_content += "GRAND TOTAL: " + str(float(final_price+total_vat))+ "\n"
            bill_content += "=" * 77 + "\n"
            bill_content += "\t\t\t Thank you for shopping with us!\n"
            bill_content += "*" * 77+"\n"
            return bill_content


def save_bill(phone_number,bill_content):
     filename =phone_number+".txt"
     with open(filename, 'w') as file:
               file.write(bill_content)
    
     print("Bill saved as "+filename)
     print(bill_content)
def sell_products(products):
    inform_free_items()
    display_products(products)
    customer_name,phone_number=get_customer_details()
    user_sell_items=[]
    grand_total=0

    while True:
        product_id = get_valid_product_ids(products)
        product_quantity = get_product_quantity()

        total_deducted, free_items = calculate_free_items(products, product_id, product_quantity)
        if total_deducted is None:
            continue

        

        update_inventory(products, product_id, total_deducted)
        display_updated_inventory(products)

        total, Cost_price_per_item = calculate_total_price(products, product_id, product_quantity)
        grand_total += total

        user_sell_items.append({
                'Product ID': product_id,
                'Product Name': products[product_id][0],
                'Product Brand':products[product_id][1],
                'Price': Cost_price_per_item,
                'Quantity': product_quantity,
                'Total': total,
                'Free Items': free_items
            
        })

        cont = input("Do you wish to continue (yes/no): ").strip().lower()
        if cont == "no":
            break

    bill_content = generate_bill_content(customer_name, phone_number, user_sell_items, grand_total)
    save_bill(phone_number+".txt", bill_content)
    update_product_file(products)
       






def exit_statement():
             print("Thank you for using our system")
             print("\n")

def display(products):
        print("*" * 80)
        print("ID\tNAME\t\tBRAND\t\tQTY\tPRICE\tORIGIN")
        print("*" * 80)
        for key, value in products.items():
           
            name, brand, qty, cost_price, origin = value
    
            # Calculate selling price with 200% markup 
            selling_price = float(cost_price) * 3
    
            # Print 
            print(key, end="\t")
            print(name, end="\t")
            print(brand, end="\t")
            print(qty, end="\t")
            print(format(selling_price), end="\t")  
            print(origin)

        print("*" * 80)
            








             
             
            
    
