from read import load_products
from operations import restock_products
from operations import sell_products
from operations import exit_statement
from operations import display

print("*"*77)
print("\t\t\t\t WeCare Store")
print("\t\t\t\t Pulchowk,Patan ")
print("*"*77)

    

#Main loop for admin options
main_loop = True
products = load_products("Available_Products.txt")
while main_loop:
    print("Please enter 1 to purchase from manufacturer.")
    print("Please enter 2 to sell the product to customer.")
    print("Please enter 3 to exit from the system.")
    print("Please enter 4 to display products.")
    print("\n")
    try:
      choice = int(input(" Enter your choice: "))
    except ValueError:
        print("Invalid input.Please Enter a number")
        continue
    if choice==1:
        restock_products(products)
    elif choice==2:
        sell_products(products)
    elif choice==3:
        main_loop=False
        exit_statement()
    elif choice==4:
        display(products)
    else:
            print("Your option",choice,"does not seem to match our requirement.Please try again.")
            print("\n")





        
        
        

    
