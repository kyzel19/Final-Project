gold = 0

miner = input("What is your name: ")

isGold = input("Did you mine gold today?")

if isGold.lower()=="yes":
	gold += 1
	print(f"Hi {miner}, Today you have a total of {gold} gold.")
else: 
	print(f"Hi {miner}, Today you have a total of {gold} gold.")