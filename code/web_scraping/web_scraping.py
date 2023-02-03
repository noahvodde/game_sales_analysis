"""
This script searches the game database on www.vgchartz.com for 25,000 entries and creates a csv file that can
be used for further processing.
"""

# Import necessary libraries
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup, element
import time

# Setup variables
start_page = 1
pages = 26
count = 0
rank = []
name = []
platform = []
year = []
genre = []
critic_score = []
user_score = []
publisher = []
developer = []
na_sales = []
pal_sales = []
jp_sales = []
other_sales = []
total_sales = []
# Default page
url_head = "https://www.vgchartz.com/games/games.php?page="
# Url_tail
url_tail = "&results=1000&order=Sales&ownership=Both&direction=DESC&showtotalsales=1&shownasales=1&showpalsales=1"
url_tail += "&showjapansales=1&showothersales=1&showpublisher=1&showdeveloper=1&showreleasedate=1&showlastupdate=1"
url_tail += "&showvgchartzscore=0&showcriticscore=1&showuserscore=1&showshipped=0"
# Scraping the website
for page in range(start_page, pages):
    try:
        # Retrieve a list of all internal links found on the page
        url = url_head + str(page) + url_tail
        with requests.get(url, stream=True) as r:
            soup = BeautifulSoup(r.text, features="html.parser")
            print(f"Page: {page}")
            games = list(
                filter(
                    lambda x: "href" in x.attrs
                    and x.attrs["href"].startswith("https://www.vgchartz.com/game/"),
                    soup.find_all("a"),
                )
            )
        # Get the different attributes from each game
        for game in games:
            time.sleep(2)
            name.append(" ".join(game.string.split()))
            data = game.parent.parent.find_all("td")
            rank.append(int(data[0].string))
            platform.append(data[3].find("img").attrs["alt"])
            publisher.append(data[4].string)
            developer.append(data[5].string)
            critic_score.append(
                float(data[6].string)
                if not data[6].string.startswith("N/A")
                else np.nan
            )
            user_score.append(
                float(data[7].string)
                if not data[7].string.startswith("N/A")
                else np.nan
            )
            total_sales.append(
                float(data[8].string[:-1])
                if not data[8].string.startswith("N/A")
                else np.nan
            )
            na_sales.append(
                float(data[9].string[:-1])
                if not data[9].string.startswith("N/A")
                else np.nan
            )
            pal_sales.append(
                float(data[10].string[:-1])
                if not data[10].string.startswith("N/A")
                else np.nan
            )
            jp_sales.append(
                float(data[11].string[:-1])
                if not data[11].string.startswith("N/A")
                else np.nan
            )
            other_sales.append(
                float(data[12].string[:-1])
                if not data[12].string.startswith("N/A")
                else np.nan
            )
            release_year = data[13].string.split()[-1]
            # Create a uniform format for the years
            if release_year.startswith("N/A"):
                year.append(np.nan)
            else:
                if int(release_year) >= 80:
                    add = int("19" + release_year)
                else:
                    add = int("20" + release_year)
                year.append(add)
            try:
                # Get the genre info of each game
                url_to_game = game.attrs["href"]
                with requests.get(url_to_game, stream=True) as site:
                    game_soup = BeautifulSoup(site.text, features="html.parser")
                    h2s = game_soup.find("div", {"id": "gameGenInfoBox"}).find_all("h2")
                    temp_tag = element.Tag
                    for h2 in h2s:
                        if h2.string == "Genre":
                            temp_tag = h2
                            genre_name = temp_tag.find_next("p").contents[0]
                            genre.append(str(genre_name))
            except AttributeError as e:
                genre.append(np.nan)
                print("An attribute error occurred...")
                time.sleep(6)
            except requests.exceptions.ChunkedEncodingError as chunkError:
                genre.append(np.nan)
                print(
                    "The server declared chunked encoding but sent an invalid chunk..."
                )
                time.sleep(6)
            except ConnectionError as e:
                genre.append(np.nan)
                print("A connection error occurred...")
                print("Sleep for 5 minutes and continue...")
                time.sleep(300)
                continue
            count += 1
            print(f"{count} Fetch data for game {name[-1]}")
    except AttributeError as e:
        print("An attribute error occurred...")
        time.sleep(6)
    except requests.exceptions.ChunkedEncodingError as chunkError:
        print("The server declared chunked encoding but sent an invalid chunk...")
        time.sleep(6)
    except ConnectionError as e:
        print("A connection error occurred...")
        print("Sleep for 5 minutes and continue...")
        time.sleep(300)
        continue
print(f"Data retrieved for {count} games")
# Building a dataframe and save it as csv file
df = pd.DataFrame(
    {
        "Rank": rank,
        "Name": name,
        "Platform": platform,
        "Year": year,
        "Genre": genre,
        "Critic_Score": critic_score,
        "User_Score": user_score,
        "Publisher": publisher,
        "Developer": developer,
        "NA_Sales": na_sales,
        "PAL_Sales": pal_sales,
        "JP_Sales": jp_sales,
        "Other_Sales": other_sales,
        "Total_Sales": total_sales,
    }
)
df.to_csv("game_sales.csv", sep=",", encoding="utf-8", index=False)
print("CSV file saved successfully...")
