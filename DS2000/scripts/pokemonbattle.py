import random as rnd
import requests
import json

class Pokemon:
	def __init__(self, name, health, power):
		self.name = name
		self.health = health
		self.power = power

	def conscious(self):
		return self.health > 0

	def attack(self, other_pokemon):
		other_pokemon.health -= self.power

	def __str__(self):
		s = self.name + "\n"
		s += "Health: " + str(self.health) + "\n"
		s += "Attack: " + str(self.power)
		return s

def create_pokemon(name):
	r = requests.get("https://pokeapi.co/api/v2/pokemon/" + name)
	poke_dict = json.loads(r.text)

	health = 0
	power = 0
	for statistic in poke_dict["stats"]:
		if statistic["stat"]["name"] == "hp":
			health = statistic["base_stat"]
		if statistic["stat"]["name"] == "attack":
			power = statistic["base_stat"]
	
	pokemon = Pokemon(name, health, power)
	return pokemon

def main():
	print("Pokemon Battle!")

	one = create_pokemon(input("Enter a Pokemon: "))
	two = create_pokemon(input("Enter another Pokemon: "))

	while one.conscious() and two.conscious():
		one.attack(two)
		two.attack(one)

		print(one)
		print(two)
		print("\n")

if __name__ == "__main__":
	main()