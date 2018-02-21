def calculateTax(price, tax_rate):
    total = price + (price * tax_rate)
    return total

my_price = float(input('输入你的价格：'))

total_price = calculateTax(my_price, 0.06)
print ('价格是：', my_price, '总共价格是：', total_price)
