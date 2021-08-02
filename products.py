#二維清單
file = 'products.csv' #建議以 csv 檔案
products = [] #大清單
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input ('請輸入商品價格： ')
    price = int(price)
    #p = [] #小清單
    #p.append(name) #依序將 name 及 price 加入小清單
    #p.append(price)
    #p = [name, price] #list comprehension
    #products.append(p) #將小清單加入大清單
    products.append([name, price]) #list comprehension
print(products)

#依序存取大清單中的小清單
for p in products:
    print (p[0], '的價格是', p[1]) #依序印出小清單的第 0 位置及第 1 位置
    
#print(products[0][0]) #存取大清單第 0 位置中的小清單第 0 位置

with open(file, 'w') as f:
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') #將清單內資料寫入檔案，如沒有檔案則自動產生
    