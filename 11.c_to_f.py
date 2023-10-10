# Program to Convert Celsius (°C) to Fahrenheit (°F) _ 攝氏(°C)轉換成華氏(°F)程式
# 讓使用者輸入 攝氏溫度(°C)，然後印出華氏溫度(°F)
# C TO F --- F = C * 9 / 5 + 32
# F TO C --- C = (F - 32) * 5 / 9

c = input('請輸入攝氏溫度: ')
c = float(c) # 因使用者可能會輸入小數點，故先轉換成浮點數
f = c * 9 / 5 + 32
print('華氏溫度為: ', f)

# Program to Convert Fahrenheit (°F) to Celsius (°C) _ 華氏(°F)轉換成攝氏(°C)程式
# 讓使用者輸入 華氏溫度(°F)，然後印出攝氏溫度(°C)
# C TO F --- F = C * 9 / 5 + 32
# F TO C --- C = (F - 32) * 5 / 9

f = input ("請輸入華氏溫度: ")
f = float(f)
c = (f - 32) * 5 / 9
print('華氏溫度為: ' , c)
