

# Python Selenium Bot for Homework Automation

## Overview
This project is a fun side experiment to explore if a bot can automate the process of filling out simple homework website problems. It uses Python with the Selenium package to interact with web elements, simulate user actions, and perform tasks like filling forms and navigating through sections.

## Example Questions for Bot to AutoFill

![image](https://github.com/ThanksLogan/autofillBot/assets/89110766/0584b555-4944-435e-891f-223759115638)

![image](https://github.com/ThanksLogan/autofillBot/assets/89110766/b755eb7a-1d65-4e91-8bc6-00d41875bcec)

![image](https://github.com/ThanksLogan/autofillBot/assets/89110766/f7fa2f9d-80a3-4e39-bba1-90657d9611a7)


## Getting Started

### Prerequisites
- Python 3.x
- Selenium WebDriver
- ChromeDriver (compatible with the installed version of Google Chrome)

### Installation
1. Install Python 3.x on your machine.
2. Install Selenium package using pip:

```
pip install selenium
```
3. Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it's in your PATH.

### Running the Program
1. Clone or download this repository to your local machine.
2. Update the script with the relevant website URL, username, and password.
3. Execute the script:
```
python homework_bot.py
```

## Code Description

### `homework_bot.py`
- **Key Features**:
- Navigates to specific URLs.
- Logs in using provided credentials.
- Fills out short answer and multiple-choice questions by revealing and submitting answers.
- Interacts with animations and submits responses.

- **Classes and Methods**:
- `zyBot`: Main class for the bot.
 - `launch_browser()`: Initializes and opens the browser.
 - `navigate_to()`: Navigates to a specified URL.
 - `accept_alert()`: Handles browser alerts.
 - `click_button()`, `fill_form()`: Interact with web page elements.
 - `wait_for_landing_page()`: Waits for a specific element to ensure the page has loaded.
 - `PA_shortAnswer_fill()`, `PA_MC_fill()`, `PA_animation_fill()`: Functions to fill out different types of participation activities.
 - `login()`: Logs into the website.
 - `autoFill()`: Automates the process of filling out activities for multiple sections.
 - `print_info()`: Prints current bot settings.

- **Selenium WebDriver**:
- Utilizes the Selenium WebDriver to control the browser.
- Implements explicit waits to handle dynamic content.

## Disclaimer
This project was created for educational purposes and should not be used to violate academic integrity policies.

## Author
- Logan F

