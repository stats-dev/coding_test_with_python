class Product:
    def __init__(self, name='', code=0):
        self.name = name
        self.code = code

    
pro1 = Product("codetree", 50)
pro2 = Product()

pro2.name, pro2.code = input().split()


print(f"product {pro1.code} is {pro1.name}")
print(f"product {pro2.code} is {pro2.name}")