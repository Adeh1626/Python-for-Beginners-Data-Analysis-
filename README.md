# Python-for-Beginners
Snippets of code from the 'Python for Beginners'     

## Project Title:
Random Quote Reader

## Project Code:
https://replit.com/@MonsuratD/Entry-level-Portfolio-Random-Quote-Reader

## Description:
The program is designed to allow users to select an API URL for retrieving random quotes based on their choice. It provides the user with 3 different API URLs that give random quotes. The quotes from the 3 URLs include Random Famous Quotes on Science and Technology, Random Quotes on History/Civil Rights, and Random Quotes on Love/Happiness.  The public API for the random quotations was obtained from https://github.com/lukePeavey/quotable.  The purpose of the program is to read random quotes from a selection of APIs that have been handpicked by the programmer. When the user makes a choice, a list of random quotes is displayed together with the author and category the quotes fall under.

## How to Use:
The program is user-friendly and no special knowledge is required to operate it.  
1.	Launch the Program
The Random Quote Reader starts with the user running the program by clicking the “Run” button.
![image](https://github.com/Adeh1626/Python-for-Beginners-Data-Analysis-/assets/146608847/eae38ed9-8766-4678-a014-a816a5353ad3)

2.	Choose an Option
Upon launching, a welcome message and 3 lists of API is displayed. The user is asked to make a choice from the lists displayed. 
![image](https://github.com/Adeh1626/Python-for-Beginners-Data-Analysis-/assets/146608847/4b7195bc-902d-4c8f-b71b-b72353d80d3a)

3.	Retrieve Quotes
When the user picks a number, the program gets data based on the user’s choice. If the number falls between 1 and 3, it will display quotes. 
If the user enters 1, a message stating the type of quote is displayed. In this case, it is the Random Famous Quotes on Science and Technology.
![image](https://github.com/Adeh1626/Python-for-Beginners-Data-Analysis-/assets/146608847/62e3daf5-0d7d-461c-9059-a2fc3995fe48)
For each item in the list of quotes, the program iterates and prints its content, author, and category. This process applies when a user enters 2 or 3. If a user enters 2, Random Quotes on History/Civil Rights are shown, and if 3, Random Quotes on Love/Happiness are displayed. 

4.	Incorrect Choice:
If the user selects a number outside 1 – 4, it will display an error message and let the user try again.
![image](https://github.com/Adeh1626/Python-for-Beginners-Data-Analysis-/assets/146608847/0d5907b1-43d8-4744-ab56-b40a8621c750)
 
5.	Quit program:
To quit the program, the user selects 4 and it displays “Quit!”
![image](https://github.com/Adeh1626/Python-for-Beginners-Data-Analysis-/assets/146608847/7642d246-a0e7-44bf-9588-59c9708ce889)

 
## Technical Details:
*	Separators and line breaks were added to improve the display of the text output. 
*	To make it interactive, users are asked to make a choice from the 3 lists of APIs listed. By making a choice, they unravel the information about the API. 
*	When a user enters an incorrect choice, it displays an error message, and instead of exiting the program, it lets the user try again. 
*	Comments were added to explain the function of the code. 
*	The 3 API URLs used in the program were defined and a function to make a choice and retrieve data from the selected API URL was created.
*	Error handling was incorporated to deal with unexpected problems using the try and except statement. It looks out for errors on the API URL address. If there is an error, it displays "An error occurred. {str(error)}". “{str(error)}” is replaced with the actual error message.
Also "if response.status_code == 200:" statement was used to check if the HTTP response status code received from a web server was successful or not. If the status code is 200, the request is successful, and the code within this ‘if’ block proceeds to handle the response data. If otherwise, there is a problem with the request then it displays “Failed to retrieve data from the API”.
*	A "Quit" option was added to the menu. If a user selects 4 to quit, the program will exit the loop and display "Quit!" The code will proceed to fetch and display quotes if the user does not select the "Quit" option.

## Future Plans:
*	Flexibility with the number of quotes: Allow users to select the number of quotes they want to be displayed per API. Presently it displays all the quotes under each of the API URL
*	Keywords: Users can select the type of quote they want by typing in the category the quote falls under.
*	Feedback and Updates: Users are able to provide feedback, report issues, or check for program updates.

