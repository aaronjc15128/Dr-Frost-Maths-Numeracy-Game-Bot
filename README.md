# Dr-Frost-Maths-Numeracy-Game-Bot
A simple python bot that uses selenium to automatically get the max score on the Dr Frost Maths Numeracy game.

The game can be found [here](https://www.drfrostmaths.com/timestables.php).

The max score is 70 and the bot can get it everytime.

## Installs:
*Python*, *selenium*, *webdriver_manager* all need to be installed. 

## Setup:
The window will prompt you to give your login details.

After that, you will be prompted to give bot details. In the *QUESTION DELAY TIME* field, type a float anything less than 0.3 to achieve max score.
*QUESTION DELAY TIME* is simply the time the bot waits for before the current question is calculated and solved.

In the *USE ENTER* field type either *true* or *false*. If set to *true*, the bot will press the enter key after typing the answer to the current question.
If set to *false*, the bot won't press the enter key and let dfm forward on to the next question.

## Process:
Selenium will print many logs during the process that the bot is running.

Note: After the game has ended, close the chrome window before closing the python window.
