![Banner](attachments/video-game-banner.png)
![Python version](https://img.shields.io/badge/Python-3.9-blue)
![NumPy version](https://img.shields.io/badge/NumPy-1.24-blue)
![Pandas version](https://img.shields.io/badge/Pandas-1.5-blue)
![Matplotlib version](https://img.shields.io/badge/Matplotlib-3.6-blue)
![Plotly version](https://img.shields.io/badge/Plotly-5.13-blue)
![Beautiful Soup version](https://img.shields.io/badge/BeautifulSoup4-4.11-blue)
![Requests version](https://img.shields.io/badge/Requests-2.28-blue)
![License](https://img.shields.io/badge/License-MIT-blue)

# Game Sales Analysis
## Author
- [@novotz](https://github.com/novotz)

## Table of contents
- [Project description](#1)
- [Data source](#2)
- [Explore the web scraper](#3)
- [Explore the notebook](#4)
- [Explore the dashboard](#5)
- [Repository structure](#6)

<a id='1'></a>
## Project description
The aim of this project was initially to test my visualisation skills. I was 
already familiar with the Matplotlib library, but wanted to expand my knowledge 
of this and other new libraries. In this context, I became aware of the Plotly 
library, which looked very promising when browsing the documentation. Originally,
I wanted to use a dataset for analysis that was freely available through the 
usual common platforms like Kaggle or Google Cloud. However, many of these 
datasets did not appeal to me and had already been used too many times for 
analysis, so this was nothing new. Finally, I created my own dataset on video 
game sales, which is described in more detail in the next chapter. I also set 
myself the task of using Excel to create an interactive dashboard from the data 
to test my Excel skills and gain additional insight into the data. Thus, a simple
visualisation project was divided into several subprojects.

<a id='2'></a>
## Data Source
To create the dataset, I used the BeautiflulSoup and Requests libraries to code 
a web scraper that searches the www.vgchartz.com website for video game sales. 
Not only are the sales figures recorded, but also the game platform or the 
publisher and many other attributes. At the end, all data is saved in a CSV file 
so that it can be used for further processing. The data scraping was done on my 
Raspberry Pi 3 Model B so that the script could run in the background without 
any obstruction.

<a id='3'></a>
## Explore the web scraper
Click [here](code/web_scraping/web_scraping.py) to see the code for the web scraper.

<a id='4'></a>
## Explore the notebook
Click [here](code/notebooks/exploratory_data_analysis.ipynb) to view the visualisations in a notebook.

<a id='5'></a>
## Explore the dashboard
Click [here](dashboard/dashboard.xlsx) to explore the dashboard.

<a id='6'></a>
## Repository structure
```
📦game_sales_analysis
 ┣ 📂attachments
 ┃ ┗ 📜video-game-banner.png
 ┣ 📂code
 ┃ ┣ 📂notebooks
 ┃ ┃ ┣ 📜clean_game_sales.csv
 ┃ ┃ ┣ 📜clean_game_sales.xlsx
 ┃ ┃ ┣ 📜data_cleaning.ipynb
 ┃ ┃ ┣ 📜exploratory_data_analysis.ipynb
 ┃ ┃ ┗ 📜requirements.txt
 ┃ ┗ 📂web_scraping
 ┃ ┃ ┣ 📜game_sales.csv
 ┃ ┃ ┣ 📜requirements.txt
 ┃ ┃ ┗ 📜web_scraping.py
 ┣ 📂dashboard
 ┃ ┗ 📜dashboard.xlsx
 ┗ 📜README.md
```
