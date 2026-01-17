#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import re #regular expressions
import argparse
import sys
from datetime import datetime

#adiciona a data e o horario atual no final do nome dos arquivos
now = datetime.now().strftime("%Y%m%d_%H%M%S")

def website_cloning(param):
    create_html = open(f"clone_file{now}.html", "w", encoding="utf8") 
    print(param.prettify())

    option = input("Do you wish to write this to a file ? (y/n): ").lower()
    if option == "y":
        create_html.write(param.prettify())
        print("Cloning done ! \n")
    elif option == "n":
        print("Operation halted \n")
    else:
        print("Invalid command ! \n")

#funcão que retorna conteudo de uma tag HTML como texto e a disponibiliza como um arquivo txt
def fetch_tag_contents(tags, param):
    tag_type = param.find_all(tags)
    create_txt = open(f"tag_contents{now}.txt", "w", encoding="utf-8")
    file_txt = ""

    #Loop que printa o texto da tag HTML e o adiciona a variavel file_txt
    if tags == "a":
        #Só busca por links que contenham https://
        tag_type = param.find_all(tags, attrs={'href': re.compile("^https://")})
        for href in tag_type:
            if href.get("href") != None:
                print(href.get("href"))
                file_txt += (href.get("href") + "\n")
    else:
        for text in tag_type:
            print("\n", text.get_text(strip=True))
            file_txt += (text.get_text(strip=True)+ "\n")

    file_option = input("Do you wish to write this to a file ? (y/n): ").lower()
    if file_option == "y":
        create_txt.write(file_txt)
        print("File created ! \n")
    elif file_option == 'n':
        print("Operation halted \n")
        return
    
def option_handling():
    break_point = input("Do you wish to exit the program ? (y/n): ").lower()
    if break_point == "y":
        return False
    elif break_point == "n":
        return True
    else:
        print("Invalid Command ! \n")
        return False

#-----------------------------------------------------------------------------------------

def tui_interaction():
    banner = r"""
__   __ ___        ______
\ \ / // \ \      / / ___|
 \ V // _ \ \ /\ / /\___ \
  | |/ ___ \ V  V /  ___) |
  |_/_/   \_\_/\_/  |____/
"""
    print(banner)
    print("Yet Another Web-Scraper")
    print("\033]8;;https://github.com/Mechaspirit1\033\\A tool by Pablo Loschi (Mechaspirit1)\033]8;;\033\\")

    while True:
        try:
            print("1-Scrape raw HTML | 2-Search by HTML tag")
            mode_select = int(input("-> "))

            url_input = input("Insert URL here: ")
            headers = {"User-Agent": "Mozilla/5.0"}

            response = requests.get(f"{url_input}", headers=headers)
            response.raise_for_status() #evita a continuação do programa caso a pagina retorne um erro
            res_parsed = response.content 
            soup = BeautifulSoup(res_parsed, 'html.parser')

            if mode_select == 1:
                website_cloning(soup)
                if not option_handling():
                    break

            elif mode_select == 2:
                tag_input = input("Fetch specific HTML tag: ")
                fetch_tag_contents(tag_input, soup)
                if not option_handling():
                    break
            
        except requests.RequestException:
            print("\nNetwork or input error, try again...")
            continue
        except KeyboardInterrupt:
            print("\nProgram interrupted, exiting...")
            break
        except EOFError:
            print("\nInput process interrupted, exiting...")
            break
        except ValueError:
            print("Input only accepts numbers !")
            continue

#---------------------------------------------------------------------
#Argumentos

def cli_mode(param):
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(param.url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    if param.mode == "raw":
        website_cloning(soup)

    elif param.mode == "tag":
        fetch_tag_contents(param.tag, soup)

def main():
    parser = argparse.ArgumentParser(description="Yet Another Web-Scraper | \033]8;;https://github.com/Mechaspirit1\033\\A tool by Pablo Loschi (Mechaspirit1)\033]8;;\033\\")

    parser.add_argument("--url", help="URL to be scraped (must contain https://)")
    parser.add_argument("--mode", choices=["raw", "tag"], help="Scrape mode")
    parser.add_argument("--tag", help="HTML tag to be scraped, used with tag mode - (<a> tags will fetch only the contents of href)")

    args = parser.parse_args()

    #Seleciona o modo TUI caso nenhum argumento seja passado ao comando
    if len(sys.argv) == 1:
        tui_interaction()
    else:
        if args.mode == "tag" and not args.tag:
            parser.error("--tag is required when using mode=tag")

        cli_mode(args)

if __name__ == "__main__":
    main()
