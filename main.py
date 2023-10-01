import requests

print("Welcome to Random Quote Reader!")

print("               ")
print("               ")
print(
    "You have 3 different API URLs that give Random Quotes from various Categories."
)
print("Select an API to unravel the random quotes underneath it.")
print("Let's Begin!")
print("               ")
print("               ")

Proceed = input("Proceed by typing (y): ")

print("               ")
print("               ")

# Define the three API URLs
api_urls = [
    "https://api.quotable.io/quotes?tags=technology,famous-quotes",
    "https://api.quotable.io/quotes/?tags=history|civil-rights",
    "https://api.quotable.io/quotes/?tags=love|happiness",
]


# Function to make a choice and retrieve data from the selected API URL
def get_data_from_api(choice):
  if choice >= 1 and choice <= 3:
    try:
      # Get data from the web API
      # python index starts from 0
      # Convert the user's input ( from 1, 2, or 3) into a valid index for the api_urls list.
      response = requests.get(api_urls[choice - 1])
      # Checks if request is successful
      if response.status_code == 200:
        # Convert the JSON data object into Python-friendly format
        data = response.json()
        return data
      else:
        # If there is a problem with the API request & retrieval was unsuccessful:
        return "Failed to retrieve data from the API."
    except Exception as error:
      return f"An error occurred. {str(error)}:"
  elif choice == 4:
    return "Goodbye!"
  else:
    return "Invalid choice. Please select a number between 1 and 4."


# Display API menu and get user's choice
while True:
  print("Choose an API to retrieve data:")

  # Use "enuumerate" to keep track of the number of iterations in the loop.
  for i, url in enumerate(api_urls, start=1):
    print(f"{i}. API {i}")
  print("4. Quit")
  print("               ")
  # User makes a choice
  choice = input("Enter your choice (1, 2, 3, or 4): ")

  # Check if the input is a valid integer between 1 and 4
  if choice.isdigit() and 1 <= int(choice) <= 4:
    choice = int(choice)
    if choice == 4:
      print("Quit!")
      # Exit the loop if the user selects Quit
      break
    else:
      # Exit the loop if the input is valid
      break

  else:
    print("Invalid choice!! Please enter a number between 1 and 4.")
    print("               ")

if choice == 1:
  print("Genius! You selected Random Famous Quotes on Science and Technology")
  print("               ")
elif choice == 2:
  print("Awesome! You selected Random Quotes on History/Civil Rights")
  print("               ")
elif choice == 3:
  print("Lovely! You selected Random Quotes on Love/Happiness")
  print("               ")

# Get data based on the user's choice
result = get_data_from_api(choice)

# Check if the result is a string (indicating an error message)
# API 2 gives 1 and 3 is a string; API 2 is not
if isinstance(result, str):
  print(result)
else:
  # Assuming 'result' contains the provided dictionary
  # the quotes required in API 2 is in the 'results key' under 'result'
  # Access the list of quotes from the 'results' key
  quotes = result.get('results', [])

  # Checks if the variable 'quotes' list is empty or contains no elements
  if not quotes:
    print("No quotes found.")
  else:
    # Go through each item in the list of quotes
    for item in quotes:
      print("            ")
      print("............")
      print("Quote: " + item['content'])
      print("Author: " + item['author'])
      print("Category: " + ", ".join(item['tags']))  # Join tags into a string
      print("............")
      print("            ")

# NOTES:

# "if response.status_code == 200:" is a conditional statement that checks whether the HTTP response status code received from a web server is successful (equal to 200).
# if  response is 200,  the code within this 'if' block can proceed to handle the response data.
# if not, it means there was some sort of error or problem.

# item['tags'] in 'result' is not a single string but a list.
# one cannot concatenate a list directly with a string using the "+" operator.
# To fix this, the elements in the "tags" list is joined into a string before printing it.
# join() was used to achieve this.
