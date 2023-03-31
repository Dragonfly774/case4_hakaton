from workwithdoc import document

answer = "2, Иван Иванов, 1000 рублей"
answer = answer.split(",")
number_doc = answer[0]
names = answer[1]
money = answer[2]
# if "рублей" in money:
#     money = money.split(" ")[1]
#     print(money)
print(document(number_doc, names, money))
