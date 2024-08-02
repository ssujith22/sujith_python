My_stocks = {}#empty dictionary
My_stocks = {"TCS":2700,"Infosys":3000,"IDBI":140,"IDFC":100,"NTPC":220}
#print(My_stocks[0]) #error as dictionary items can't be accessed via index
print(type(My_stocks),My_stocks)
My_stocks["SBI"] = 1700
print(My_stocks)
print("no of stocks",len(My_stocks))
print("All stock names",My_stocks.keys())
print("All stock names",My_stocks.values())
print("The stock price of Infosys is",My_stocks["Infosys"])
print("*" *70)
for stock in My_stocks:
    print(stock,"has price",My_stocks[stock])
print("*" *70)
for stock in My_stocks.items():
    print(stock)
    print(stock[0],"has price",stock[1])
print("*" *70)
for stock,price in My_stocks.items():
    print(stock,"has price",price)
print("*" *70)

My_stocks.pop("Infosys")
print(My_stocks)
My_stocks.popitem()
print(My_stocks)
del My_stocks["TCS"]
print(My_stocks)
print("*" *70)
swapped = {}
for key,value in My_stocks.items():
    swapped[value] = key
print(swapped)




