    
def update_product_file(products, filename="Available_Products.txt"):
    with open(filename, 'w') as file:
        for product_id, product_data in products.items():
            name = product_data[0]
            brand = product_data[1]
            quantity = product_data[2]
            price = product_data[3]
            origin = product_data[4]
            line = name + "," + brand + "," + str(quantity) + "," + str(price) + "," + origin + "\n"
            file.write(line)



     
