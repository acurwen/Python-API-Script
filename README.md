# Python-API-Script

Choose an API from RapidAPI that interests you—make sure it has a free tier and simple authentication. Write a Python script that makes a request to your selected API, using the appropriate endpoint and parameters to retrieve data. Save the response data to a variable, and handle it as JSON to work with nested structures. Extract a specific item from the nested dictionary in the response, and print a statement that meaningfully displays this information. Have fun exploring the data you retrieve!


I chose a wine pairing API from RapidAPI that takes two parameters: your meal (ie. steak) and your maximum budget (ie. $50) and returns back a wine that would pair well with your meal of choice, a link to buy it and the price of it. It also returns a short description of the wine chosen and why it was chosen.
![image](https://github.com/user-attachments/assets/23cfad90-4ab2-4700-8cfe-055f44a6aa03)

## Process:

When picking APIs, I scrolled through a few and looked at their "Example Responses" to get a sense of the data output, based on whatever API I had chosen (ie. Get, Post, etc). 
https://rapidapi.com/spoonacular/api/recipe-food-nutrition/playground/5a00c7dbe4b06d2e9b6cf764
I settled on the "GET Wine Pairing API" from "Recipe - Food - Nutrition", because it had two straightforward parameters and a interesting output.

## Parameters:
The two parameters are "food" and "maxPrice". The food is what you'd want to get a pairing for and could be either a dish name, an ingredient or a type of cuisine. The page gave examples of each option and I noticed that not all API parameter pages gave definitive options on what you could input. I liked that this was very straightforward.

The second parameter was the maximuim price you'd want the wine recommendation to cost, and this parameter is optional. Also this parameter measures in USD. 

![image](https://github.com/user-attachments/assets/6ce43561-a7f1-44be-9731-12d0a5d4e344)

## Output:
The "Example Responses" output shows three 

![image](https://github.com/user-attachments/assets/d3da6211-dc06-457f-b692-d3e6f4ec1357)

## Process:
First, I copied the code from "Code Snippets" into my script. I noticed that the parameters in the query string were variables I can turn into input from the user and noted that for later.
![image](https://github.com/user-attachments/assets/ac619064-b282-4870-8502-3b6b963989e8)
![image](https://github.com/user-attachments/assets/7f292e78-50f1-4d18-94d7-95fa4001c5e8)

Next, I printed the .json format of the response data to understand the output. It looked like a large dictionary. To confirm, I printed the type to confirm it's a dictionary -- it was.

![image](https://github.com/user-attachments/assets/a5865d4d-445b-432e-a2e2-167287f80132)
![image](https://github.com/user-attachments/assets/d9acd465-c006-4477-93b1-fb39a495c058)

Then, I focused on what output I wanted to print and how. If a person types in "salmon" and "20" as the parameters, based off the output, I wanted to return the dictionaries "pairedWines", "pairingText" and some information from the "productMatches" dictionary. In other words, what wine(s) $20 or less would pair best with salmon, the description of it, the link to buy it and the price. 

To start I saved the .json output to a variable called "output". Then I used the .get method with each "key" to print out each value so:

```
print(output["pairedWines"])
print(output.get("pairingText"))
print(output.get("productMatches"))
```

I noticed that the output for `print(output["pairedWines"])` gave the exact same text as the first sentence in the output for `print(output.get("pairingText"))`, so I decided to take that print statement out.

Then in the output for `print(output.get("productMatches"))`, I got the entire dicitionary which included the product id, the name or "title" of the product, product description, the price, the URL to the image of the product, it's average rating, rating count, and score, as well as a link to find and purchase the product. 

For the output, I only wanted the name of the wine, the description, price and URL for where to find it. 
So I wrote a for loop:

For all the items in the output dictionary, only print the values for the following keys:
```
for items in output["productMatches"]:
	print(items["title"])
  print(items["description"])
	print(items["price"])
	print(items["link"])

```
This gave me the output I wanted:

Then, instead of printing these dictionaries, I saved each one to variables to use in print statements.
![image](https://github.com/user-attachments/assets/de1099e8-e2bb-421d-ad6b-844c13d920a0)

In my print statements, I wrote a line where the user can find the product recommended, for what price and the link. 
I added another line that said the product was under or equal to the budget they entered.
Then I added in a line that introduced the description the response.json() variable had for whatever wine product was selected. 

I added `print()` after each print statement to skip a line before the next output for clearer reading.

I added input statements to read the food and budget from the user to then pass through as my parameters in the request command and also in other print statements.
![image](https://github.com/user-attachments/assets/f7a037e5-e26e-43ab-bd5e-a23f12b80cec)


Then I tested out the script with various food and budget types and tweaked the print statements for clearer formatting/convenient messsaging. 

## Troubleshooting:

Early on, I faced difficulties choosing an API that would handle numerous requests calls (for testing) without reaching the monthly quota alloted to the free plan. Originally, I chose other APIs that interested me like one that returned your horoscope based off your sign and time period desired (ie. today, tomorrow, etc) or one that returned recipes based on ingredients you ordered.

However, when I found the wine pairing one, I had many requests at my disposal so I felt comfortable testing it out. However, knowing htat I had limited amount of test chances made me check over my code thoroughly before running it each time.

Secondly, I noticed that in the output for the pairingText (second key in output dictionary), three types of wines would print in the first line as "top picks" for whatever food was entered. However, at times the first wine was an actual wine and the next two were non-wines like "alcoholic drink" or "ingredient". 


<img width="1344" alt="image" src="https://github.com/user-attachments/assets/45870790-72c8-431a-a849-30ae1411156a">



However, the recommendation would be for the first value (which was always a proper wine) so the output still made enough sense for the user.

