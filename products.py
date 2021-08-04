#二維清單
file = 'products.csv' #建議以 csv 檔案
products = [] #大清單

#讀取檔案
with open(file, 'r') as f:
    for line in f:
        if '商品,價格' in line: #跳過存取標題
            continue #跳過此回進入下一回
        #name, price = line.strip().split(',')
        #products.append([name, price])
        products.append(line.strip().split(',')) #list comprehension
print(products)

#讓使用者輸入
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

#印出購買紀錄
for p in products:#依序存取大清單中的小清單
    print (p[0], '的價格是', p[1]) #依序印出小清單的第 0 位置及第 1 位置
    
#print(products[0][0]) #存取大清單第 0 位置中的小清單第 0 位置

#將新增品項寫入檔案
with open(file, 'w') as f: #encoding='utf-8' 如需解決亂碼問題則在'w'後最後加入
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') #將清單內資料寫入檔案，如沒有檔案則自動產生
    