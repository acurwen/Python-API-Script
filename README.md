# Python-API-Script


I chose a wine pairing API from RapidAPI that takes two parameters: your meal (ie. steak) and your maximum budget (ie. $50) and returns back a wine that would pair well with your meal of choice, a link to buy it and the price of it. It also returns a short description of the wine chosen and why it was chosen.



## Process:

When picking APIs, I scrolled through a few and looked at their "Example Responses" to get a sense of the data output, based on whatever API I had chosen (ie. Get, Post, etc). 

I settled on the "GET Wine Pairing API" from "Recipe - Food - Nutrition", because it had two straightforward parameters and a interesting output.

https://rapidapi.com/spoonacular/api/recipe-food-nutrition/playground/5a00c7dbe4b06d2e9b6cf764

## Parameters:
The two parameters were "food" and "maxPrice". The food is what you'd want to get a pairing for and could be either a dish name, an ingredient or a type of cuisine. The page gave examples of each option and I noticed that not all API parameter pages gave definitive options on what you could input. I liked that this was very straightforward.

The second parameter was the maximuim price you'd want the wine recommendation to cost, and this parameter is optional. Also this parameter measures in USD. 

![image](https://github.com/user-attachments/assets/6ce43561-a7f1-44be-9731-12d0a5d4e344)

## Output:
The "Example Responses" output shows a dictionary with three keys with various value types (ie. list, string, and a list with dictionary items as its items).

![image](https://github.com/user-attachments/assets/d3da6211-dc06-457f-b692-d3e6f4ec1357)

## Process:
First, I copied the code from "Code Snippets" into my script. I noticed that the parameters in the query string were variables I can turn into input from the user and noted that for later.

![image](https://github.com/user-attachments/assets/7f292e78-50f1-4d18-94d7-95fa4001c5e8)

Next, I printed the .json format of the response data to understand the output. It looked like a large dictionary. To confirm, I printed the type to confirm it's a dictionary -- it was.

![image](https://github.com/user-attachments/assets/a5865d4d-445b-432e-a2e2-167287f80132)
![image](https://github.com/user-attachments/assets/d9acd465-c006-4477-93b1-fb39a495c058)

Then, I focused on what output I wanted to print and how. If a person types in "salmon" and "20" as the parameters, based off the output, I wanted to return the dictionary values of the "pairedWines", "pairingText" keys and some information from the "productMatches" key. The other information was what wine(s) $20 or less would pair best with salmon, the description of the wine, the link to buy it and the price. 

To start I saved the .json output to a variable called "output". Then I used the .get method with each "key" to print out each value so:

```
print(output["pairedWines"])
print(output.get("pairingText"))
print(output.get("productMatches"))
```

I noticed that the output for `print(output["pairedWines"])` gave the exact same text as the first sentence in the output for `print(output.get("pairingText"))`, so I decided to take that print statement out.

![image](https://github.com/user-attachments/assets/931d9913-4f1e-465c-877c-ea66a138ec6a)

Then for the output of `print(output.get("productMatches"))`, I got the entire dictionary which included the product id, the name or "title" of the product, product description, the price, the URL to the image of the product, it's average rating, rating count, and score, as well as a link to find and purchase the product. 

Instead for the output, I only wanted the name of the wine, the description, price and URL for where to find it, so I wrote a for loop:

For all the items in the output dictionary, only print the values for the following keys:
```
for items in output["productMatches"]:
	print(items["title"])
  	print(items["description"])
	print(items["price"])
	print(items["link"])

```
This gave me the output I wanted.

Then, instead of printing these dictionaries, I saved each one to variables to use in print statements.
![image](https://github.com/user-attachments/assets/de1099e8-e2bb-421d-ad6b-844c13d920a0)

## Print Statements:

In my print statements, I wrote a line where the user can find the product recommended, for what price and the link. 
`print(f"You can find",productTitle,"for "+productPrice,"at",productLink+".")`

I added another line that said the product was under or equal to the budget they entered.
`print(f"This fits your budget of under or equal to $"+budget+"!")`

Lastly, I added in a line that introduced the description the response.json() variable had for whatever wine product was selected. 
`print(f"Here's a helpful description of",productTitle+":",productDescription)`

I added `print()` after each print statement to skip a line before the next output for clearer formatting.

Previously, I tested with my own paramters. At this point, I added input statements to read the food and budget from the user to then pass through as my parameters in the request command and also in other print statements.
![image](https://github.com/user-attachments/assets/f7a037e5-e26e-43ab-bd5e-a23f12b80cec)

Then I tested out the script with various food and budget types and tweaked the print statements as I tested for clearer formatting/convenient messsaging. 

**Food: Crab; Budget: $50**
![image](https://github.com/user-attachments/assets/220e5808-423c-48d8-8ce7-a7dd1a4111be)


**Food: Caribbean; Budget: $40**
![image](https://github.com/user-attachments/assets/75721f60-f90f-42c8-9294-2d1a81cafc82)

## Troubleshooting:

Early on, I faced difficulties choosing an API that would handle numerous requests calls (for testing) without reaching the monthly quota alloted to the free plan. Originally, I chose other APIs that interested me like one that returned your horoscope based off your sign and time period desired (ie. today, tomorrow, etc) or one that returned recipes based on ingredients you ordered. However, due to only a limited number of requests allowed, I couldn't go far with those APIs.
![image](https://github.com/user-attachments/assets/23cfad90-4ab2-4700-8cfe-055f44a6aa03)

So I ask kept looking for APIs, I made note of how many calls the free subscription allowed. I found the wine pairing one, which offered more request calls for the free subscription. so I felt more comfortable choosing it and testing it out. However, knowing that I still had a limited amount of test chances made me check over my code thoroughly before running it each time.

Secondly, I noticed that in the output for the pairingText (second key in output dictionary), three types of wines would print in the first line as "top picks" for whatever food was entered. However, at times only the first wine was an actual wine and the next two were non-wines like "alcoholic drink" or "ingredient". 

<img width="1344" alt="image" src="https://github.com/user-attachments/assets/45870790-72c8-431a-a849-30ae1411156a">

However, the recommendation shown would always be for the first value (which was always a proper wine) so the output still made enough sense for the user.

