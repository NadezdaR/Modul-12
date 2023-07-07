per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int (input ("Введите сумму денежных средств:"))
tkb = int ((per_cent['ТКБ'])*(money)/100)
ckb = int ((per_cent['СКБ'])*(money)/100)
vtb = int ((per_cent['ВТБ'])*(money)/100)
sber = int ((per_cent['СБЕР'])*(money)/100)
deposit = [tkb, ckb, vtb, sber]
print(deposit)
i = max(deposit)
print("Максимальная сумма, которую вы можете заработать-" + str(i))
