# import requests module 
import requests

# Asking user for food for pairing rec
food = input("What food would you like to find a wine pairing for? This can be an ingredient like 'shrimp', a dish like 'spaghetti' or a cuisine type like 'Caribbean': ")

# Asking user for wine rec budget
budget = input("In USD, what is the maximum price of wine you'd like to see recommended? $")
print()

# Defining endpoint where API request will be made
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/food/wine/pairing"

# Defining parameters; using food and budget variables from user input
querystring = {"food":food,"maxPrice":budget}

# Authentication from RapidAPI site
headers = {
	"x-rapidapi-key": "18d990b270msh117af6574795831p1ca7eejsn6f8361b48d2f",
	"x-rapidapi-host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
}

# Making an API GET request and saving the output to variable named response
response = requests.get(url, headers=headers, params=querystring)


# Saving request data in .json format to variable named output
output = response.json()

print(food+"? Great choice!")
print()

# Print the pairing text for food input by user
print(output.get("pairingText"))
print()

# For all items in the productMatches dictionary (within the output dictionary where Product Matches is a key)
for items in output["productMatches"]:
    
  #save each value of the corresponding key to a variable
	productTitle = (items["title"])
	productDescription = (items["description"])
	productPrice = (items["price"])
	productLink = (items["link"])

# Print out results for user in a convenient way
print(f"You can find",productTitle,"for "+productPrice,"at",productLink+".")
print()
print(f"This fits your budget of under or equal to $"+budget+"!")
print()
print(f"Here's a helpful description of",productTitle+":",productDescription)
