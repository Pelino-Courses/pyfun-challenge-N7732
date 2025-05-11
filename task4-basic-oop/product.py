inventory={}
class product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def add_inventory(self):
        """"Preform addition of new product in the inventory dictionary 
        by making it's id through the key=len(inventory)+1 as shown in code bellow then we add key
          and value in inventory dictionary then return inventory"""
        key=len(inventory)+1
        name=str(input("Enter product name:"))
        price=int(input("Enter product price:"))
        quant=int(input("Enter product Quantity:"))
        values = {
           "name": name, 
           "price": price,
           "Quantity": quant
        }
        inventory[key] = values
        return inventory
    def remove_inventory(self):
        """Here perform to remove product from inventory by id through checking id in inventory then
        if exist it remove these id as key and it's value"""
        id=int(input("Enter product id :"))
        for id in inventory:
            inventory.pop(id)
            return f"stock:{inventory}"
    def calculation_value(self):
        """Here function perform calculation of price value"""
        id=int(input("Enter product id :"))
        for values in inventory.values():
            total = values['price'] * values['Quantity']
            return f"The total amount of {values['name']} is {total}"
        # return f"Total value of product is:{total_value}"
    def display(self):
        """ This display product information by respect to product id"""
        id=int(input("Enter product id :"))
        if id in inventory:
            return inventory[id]
        else:
            print("Not Found")
count=0
while(True):
    def main():
        """Here we make objectives of all classes in order to print our data by following main menu:
         as shown in printf bellow """
        print("Menu:\n1.Add product\n2.Remove product\n3.Calculation_value\n4.display")
        chose=int(input("Enter your choice:"))
        if chose==1:
            obje=product("",0,0)
            print(obje.add_inventory())
        elif chose==2:
            objec=product("",0,0)
            print(objec.remove_inventory())
        elif chose==3:
             object=product("",0,0)
             print(object.calculation_value())
        elif chose==4:
            objecti=product("",0,0)
            print(objecti.display())
        
    if __name__ == "__main__":
        main()
    count +1