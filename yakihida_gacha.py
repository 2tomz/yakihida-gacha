# coding:utf-8
import os, json, random, sys

#JSONメニュー表を読み込む
LoadMenuJSON = open(os.path.dirname(os.path.abspath(__file__))+"/menu.json", "r")
MenuDictionary = json.load(LoadMenuJSON)

#トータル金額を設定する
Balance = 1000
print("\n-----\n持ち金は" + str(Balance) + "円です")
print("(メニュー名に＊が付いているものは各店舗オススメメニュー)\n-----\n")

#アルコールを一つ選びだす
AlcoholTotal = len(MenuDictionary["alcohol"])
AlcoholGacha = random.randint(0,AlcoholTotal-1)
Balance = Balance-MenuDictionary["alcohol"][AlcoholGacha]["price"]

print("今日のお酒は『" + str(MenuDictionary["alcohol"][AlcoholGacha]["name"]) + "』（" + str(MenuDictionary["alcohol"][AlcoholGacha]["price"]) + "円）です")
print("残高は" + str(Balance) + "円です\n\n-----\n")

#つまみを残高から選び尽くす
FoodsTotal = len(MenuDictionary["foods"])
while Balance >= 120:
	FoodsGacha = random.randint(0,FoodsTotal-1)
	
	if Balance-MenuDictionary["foods"][FoodsGacha]["price"] < 0:
		continue
	else:
		Balance = Balance-MenuDictionary["foods"][FoodsGacha]["price"]
		
	print("おつまみは『" + str(MenuDictionary["foods"][FoodsGacha]["name"]) + "』（" + str(MenuDictionary["foods"][FoodsGacha]["price"]) + "円）です")
	print("残高は" + str(Balance) + "円です\n")


print("-----\n\nもうお金なくて頼めるものがない\n\n")
sys.exit()
