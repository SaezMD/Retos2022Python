#29 MÁQUINA EXPENDEDORA
"""
 * Simula el funcionamiento de una máquina expendedora creando una operación que reciba dinero (array de monedas) y un número que indique la selección del producto.
 * - El programa retornará el nombre del producto y un array con el dinero de vuelta (con el menor número de monedas).
 * - Si el dinero es insuficiente o el número de producto no existe, deberá indicarse con un mensaje y retornar todas las monedas.
 * - Si no hay dinero de vuelta, el array se retornará vacío.
 * - Para que resulte más simple, trabajaremos en céntimos con monedas de 5, 10, 50, 100 y 200.
 * - Debemos controlar que las monedas enviadas estén dentro de las soportadas.
"""

#List and price of items
products = {
    0:["Sandwich",250],
    1:["Water",50],
    2:["Chips",150],
    3:["Chocolate",300],
    4:["Sweets",75],
    5:["Almonds",65],
    6:["Plate",25],
    7:["Pizza",1120]
}

#List of valid coins
validCoins = [5,10,50,100,200]

#check if coins are OK
def checkCoins(coinList: list)-> bool:
    """function to check if all the items in a list are present in another list"""
    for coin in coinList:
        if coin not in validCoins:
             return False
    return True

#Create a list for the change
def listChange(amountOfChange: int)-> list:
    listOfCoins = []
    for i in validCoins[::-1]:
        while amountOfChange >= i:
            if amountOfChange - i >= 0:
                listOfCoins.append(i)
                amountOfChange -= i
    #print(listOfCoins)
    return listOfCoins

#Check if coins are enough
def checkMoneyAndPrice(coins, product) -> str:
    """function to check if the sum of a list is higher to the price in the dict"""
    if product not in products.keys():
        print(f"Returning: {coins}")
        raise Exception("Product not available.")
    else:
        price = products.get(product)[1] 
    amount = sum(coins)
    if amount < price:
        print(f"Returning: {coins}")
        raise Exception(f"Not enoght money to purchase: {products.get(product)[0]}. You need: {price-amount} cents more.")
    #We can buy:
    change = amount-price
    if change > 0:
        return listChange(change)
    else:
        #no change
        #print("No change.")
        return []

def machineRequest(coins: list, selection: int) -> str:
    """"fucntion to collect money and selection of the product"""
    if not checkCoins(coins):
        print(f"Returning: {coins}")
        raise Exception("Some of the coins are not legal.")
    changeList = checkMoneyAndPrice(coins, selection)
    
    return print(f"Product selected: {products.get(selection)[0]} \n Returning: {changeList}")

machineRequest([100,100,10,10,10,10,10],0)
machineRequest([100,100,10,10,10,10,10,100,100,50,5],0)
machineRequest([100,100,10,10,10,10,10,100,100,50,5],1)
machineRequest([100,100,10,10,10,10,10,100,100,50,5],2)
machineRequest([100,100,10,10,10,10,10,100,100,50,5],3)
machineRequest([100,100,10,10,10,10,10,100,100,50,5],4)
machineRequest([100,100,10,10,10,10,10,100,100,50,5],5)
machineRequest([100,100,10,10,10,10,10,100,100,50,5],6)
machineRequest([100,100,10,10,10,10,10,100,100,50,5,200,200,200,200],7)

