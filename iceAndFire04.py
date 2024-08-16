import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

"""
• print the character's allegiances... if they have any
"""

def main():
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
        data = requests.get(AOIF_CHAR + got_charToLookup).json()

        if data["name"]:
            name = data["name"]
        else:
            name = data["aliases"][0]

        books = data["books"]
        povbooks = data["povBooks"]
        all_books = books + povbooks

        # what to do with list of links to books?
        book_titles = []
        house_titles = []
        # loop over book urls; grab name of book and add to list
        for book_url in all_books:
            bookdata = requests.get(book_url).json()
            bookname = bookdata["name"]
            book_titles.append(bookname)
        # loop over allegiance urls; grab name of house and add to list
        for house_url in data["allegiances"]:
            housedata = requests.get(house_url).json()
            housename = housedata["name"]
            house_titles.append(housename)

        print(f"NAME: {name}")
        print("BOOKS:")
        for book in book_titles:
            print(f"• {book}")

        if house_titles: # any houses in this list?
            print("HOUSES:")
            for house in house_titles:
               print(f"• {house}")

if __name__ == "__main__":
        main()
 









       
        


















