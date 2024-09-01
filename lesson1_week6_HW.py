import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")

json_data = response.text

poke_data = response.json()

print(poke_data["name"].title())

print(poke_data["abilities"][0]['ability']['name'], poke_data["abilities"][1]['ability']['name'])

#---------------------------------------------------------------------------------------#

def fetch_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/")
    
    if response.status_code == 200:
        poke_data = response.json()

        poke_dict = {
            "forms": poke_data["forms"],
            "weight": poke_data["weight"],
            "type": poke_data["types"][0]["type"]["name"],
            "id": poke_data["id"]
        }    
        
        for pokemon_name in pokemon_names:
            print(pokemon_name)
            print(poke_dict)
    else:
        return "Bad response, try again!"
    
pokemon_names = ["pikachu", "bulbasaur", "charmander"]

def calculate_average_weight(pokemon_names):
    total_weight = 0
    count = 0
    
    for name in pokemon_names:
        poke_data = fetch_pokemon_data(name)
        if poke_data != "Bad response, try again!":
            total_weight += poke_data["weight"]
            count += 1
    
    if count == 0:
        return "No valid Pokémon data found."
    
    average_weight = total_weight / count
    return average_weight

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
average_weight = calculate_average_weight(pokemon_names)
print(f"The average weight of the Pokémon is: {average_weight}")
    
    
fetch_pokemon_data(pokemon_names)

#---------------------------------------------------------------------#
# Question 2
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    bodies = response.json()['bodies']
    
    #process each planet info
    planet_info = []
    
    for body in bodies:
        if body['isPlanet']:
            name = body["englishName"]
            mass = body["mass"]["massValue"] if body["mass"] else 0
            orbit_period = body["sideralOrbit"]
            planet_info.append({"name": name, "mass": mass, "orbit_period": orbit_period})
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

# fetch_planet_data()


def find_heaviest_planet(planets):
    heaviest_planet = None
    max_mass = 0

    for planet in planets:
        if planet["mass"] > max_mass:
            heaviest_planet = planet
            max_mass = planet["mass"]

    return heaviest_planet

# Fetch planet data
planets_data = fetch_planet_data()

# Find the heaviest planet
heaviest = find_heaviest_planet(planets_data)
print(f"The heaviest planet is {heaviest['name']} with a mass of {heaviest['mass']} kg.")

find_heaviest_planet(planets)

    
    




# planets = fetch_planet_data()

# name, mass = find_heaviest_planet(planets)


# find_heaviest_planet(planets)






# planets = fetch_planet_data()

#     all_planets = []

#     for name, mass in planets:
#         name = planet["englishName"]
#         mass = planet['mass']['massValue']
#         all_planets.append(name)