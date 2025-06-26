def load_products(Available_Products):
    products={}
    with open("Available_Products.txt",'r') as file:
        product_id=1
        for line in file:
            line=line.replace("\n","").split(",")
            products[product_id]=line   
            product_id=product_id+1
    return products
