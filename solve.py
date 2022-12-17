import os # For getting the current working directory and making directories
import sys # For getting command line arguments
from enum import Enum # For the enum class
from selenium import webdriver # For getting the HTML of the problem
import requests # For downloading images
from bs4 import BeautifulSoup # For parsing HTML
import markdownify as md # For converting HTML to Markdown
sys.path.append("utils") # Add the utils directory to the path
import pytermgui_tui as tui # Import the TUI
from data import Data # Import the Data class
from projcets_helpers import * # Import the projects creation methods

BASE_URL = "https://leetcode.com/problems/" # The base URL of the problem

BASE_URL = BASE_URL + "merge-two-sorted-lists" # The URL of the problem for testing

# Stup the tui
tui.setup()

# Check if user provided a URL as an argument
if len(sys.argv) < 2:
    # If not, ask for one
    problem_url = tui.get_the_url(BASE_URL)
else:
    # If so, use it
    problem_url = sys.argv[1]
    # Check if user provided a problem title instead of a URL, if so, add the base URL
    if not problem_url.startswith(BASE_URL) and not problem_url.startswith("http"):
        problem_url = BASE_URL + problem_url

# Check if the URL is valid
if not problem_url.startswith(BASE_URL):
    print("Invalid URL, please enter a valid URL(LeeCode problem URL)")
    exit(1)

# Setup the driver (firefox)
driver = webdriver.Firefox()

driver.get(problem_url) # Open the URL in the browser

soup = BeautifulSoup(driver.page_source, "lxml") # Parse the HTML

driver.quit() # Close the driver

# Get the main div (the problem details are in this div)
main_div = soup.find("div", {"class": "ssg__qd-splitter-primary-w"}).find("div", {"class": "ssg__qd-splitter-primary-h"})

# Get the title of the problem
title = soup.title.string.lower().replace(" - leetcode", "").replace(" ", "_")

level = main_div.find("div", {"class": "mt-3 flex space-x-4"}).find("div", {"class": "py-1"}).text.lower()

# Check if the level directory exists, if not, create it
if not os.path.exists(level):
    os.mkdir(level)

# Check if the problem directory exists, if not, create it
problem_path = os.path.join(level, title)
if not os.path.exists(problem_path):
    os.mkdir(problem_path)

# Get the description of the problem
discription = main_div.find("div", {"class": "_1l1MA"})

# Show the tui for confirm the data and choose the language to solve the problem
data = Data(title, level, problem_path)
tui.confirm_data(data)
print(data)
exit(0)

# Download the images if there are any
for img in discription.find_all("img"):
    src = img["src"]
    req = requests.get(src)
    if req.status_code == 200:
        img_name = src.split("/")[-1]
        img_path = os.path.join(data.problem_path, "images", img_name)
        if not os.path.exists(img_path):
            if not os.path.exists(os.path.dirname(img_path)):
                os.makedirs(os.path.dirname(img_path))
            with open(img_path, "wb") as f:
                f.write(req.content)
        img["src"] = img_path.replace(data.problem_path, ".")

# Convert the discription to Markdown
discription = md.markdownify(str(discription), heading_style="ATX")

# Add the title to the discription
discription = "# " + data.title.capitalize().replace("_", " ") + "\n" + discription

# Add the problem URL to the discription
discription = discription + "\n- [Problem URL](" + problem_url + ")"

# Write the discription to the README.md file, if it doesn't exist
if not os.path.exists(os.path.join(data.problem_path, "README.md")):
    with open(os.path.join(data.problem_path, "README.md"), "w") as f:
        f.write(discription)

# Create the NOTE.md file, if it doesn't exist
if not os.path.exists(os.path.join(data.problem_path, "NOTE.md")):
    with open(os.path.join(data.problem_path, "NOTE.md"), "w") as f:
        f.write("## There is no note for this problem yet ¯⁠⁠⁠\(⁠ツ⁠)⁠⁠/⁠¯")

# Create the solution project for each language
for lang in data.solve_with:
    lang_path = os.path.join(data.problem_path, lang)
    if not os.path.exists(lang_path):
        os.mkdir(lang_path)
    match lang:
        case "python" | "py":
            create_python_project(lang_path)
        case "java":
            create_java_project(lang_path)
        case "c++" | "cpp":
            create_cpp_project(lang_path)
        case "c":
            create_c_project(lang_path)
        case "rust":
            create_rust_project(lang_path)
        case "go":
            create_go_project(lang_path)
        case _: # If other language, do nothing
            pass

