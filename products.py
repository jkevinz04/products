#二維清單
products = [] #大清單
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input ('請輸入商品價格： ')
    #p = [] #小清單
    #p.append(name) #依序將 name 及 price 加入小清單
    #p.append(price)
    #p = [name, price] #list comprehension
    #products.append(p) #將小清單加入大清單
    products.append([name, price]) #list comprehension
print(products)

print(products[0][0]) #存取大清單第 0 位置中的小清單第 0 位置