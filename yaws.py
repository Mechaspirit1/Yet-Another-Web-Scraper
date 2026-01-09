#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

#todo
def website_cloning(param):
    create_html = open("clone_file.html", "w")
    create_html.write(param.prettify())

#funcão que retorna conteudo de uma tag HTML como texto e a disponibiliza como um arquivo txt
def fetch_tag_contents(tags, param):
    tag_type = param.find_all(tags)
    create_txt = open("tag_contents.txt", "w")
    file_txt = ""

    #Loop que printa o texto da tag HTML e o adiciona a variavel file_txt
    if tags == "a":
        for href in tag_type:
            if href.get("href") != None:
                print(href.get("href").replace("#", ""))
                file_txt += (href.get("href").replace("#", "") + "\n")
    else:
        for text in tag_type:
            print(text.get_text(strip=True))
            file_txt += (text.get_text(strip=True)+ "\n")

    file_option = input("Do you wish to write this to a file ? (y/n): ")
    if file_option == "y" or file_option == "Y":
        create_txt.write(file_txt)
        print("File created ! \n")
    elif file_option == 'n' or file_option == "N":
        return

#-----------------------------------------------------------------------------------------
#todo - clean up this entire section
banner = r"""
__   __ ___        ______
\ \ / // \ \      / / ___|
 \ V // _ \ \ /\ / /\___ \
  | |/ ___ \ V  V /  ___) |
  |_/_/   \_\_/\_/  |____/
"""

print(banner)
print("Yet Another Web-Scraper")

while True:
    try:

        print("1-Scrape raw HTML | 2-Search by HTML tag")
        mode_select = int(input("-> "))

        url_input = input("Insert URL here: ")
        headers = {"User-Agent": "Mozilla/5.0"}

        response = requests.get(f"{url_input}", headers=headers)
        res_parsed = response.content
        soup = BeautifulSoup(res_parsed, 'html.parser')

        if mode_select == 1:
            print(soup.prettify())
            option = input("Do you wish to write this to a file ? (y/n): ")
            if option == "y" or option == "Y":
                website_cloning(soup)
                print("Cloning done ! \n")
            elif option == "n" or option == "N":
                print("Operation halted \n")
            else:
                print("Invalid command !")

            break_point = input("Do you wish to exit the program ? (y/n): ")
            if break_point == "y" or break_point == "Y":
                break
            elif break_point == "n" or break_point == "N":
                continue
            else:
                print("Invalid Command !")
                break

        elif mode_select == 2:
            tag_input = input("Fetch specific HTML tag: ")
            fetch_tag_contents(tag_input, soup)

            break_point = input("Do you wish to exit the program ? (y/n): ")
            if break_point == "y" or break_point == "Y":
                break
            elif break_point == "n" or break_point == "N":
                continue
            else:
                print("Invalid Command !")
                break
        else:
            print("Invalid command !")
            continue

    except requests.RequestException:
        print("Error !")
        continue
