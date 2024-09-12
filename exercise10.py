from typing import Dict, List
from datetime import datetime
from requests import Response, get

API_KEY = "6fbaa7887b3d41edb74a5f69a00ca378"
BASE_URL = "https://newsapi.org/v2/"

LANGUAGE = "en"
PAGE_SIZE = 5


def main():
    run = True

    header = {"X-Api-Key": API_KEY}
    query = ""

    while run:
        endpoint = ""
        parameters = {"language": LANGUAGE, "pageSize": PAGE_SIZE}

        print()
        if query:
            print(f"\nCurrent Topic: {query}")
        else:
            query = input("What news your looking for: ")

        match (print_menu()):
            case 1:
                endpoint = "top-headlines"
            case 2:
                endpoint = "everything"
            case 3:
                query = input("Enter keyword or topic that you search: ")
            case 0:
                print("Exiting...")
                run = False

        if query:
            if endpoint:
                parameters["q"] = query
                res = get(BASE_URL + endpoint, headers=header, params=parameters)
                articles = parse_response(res)
                if len(articles) == 0:
                    print("Found Nothing")
                else:
                    for art in articles:
                        print()
                        print_article(art)
        else:
            print("Please select a topic first")


def print_menu() -> int:
    print(
        "=== Main Menu ===",
        "1. Top Headlines",
        "2. Everything",
        "3. Change Topic",
        "0. Exit",
        sep="\n",
    )
    return int(input("Enter your choice: "))


def parse_response(res: Response) -> List[Dict]:
    jsn: Dict = res.json()
    if jsn["status"] == "ok":
        return jsn["articles"]
    else:
        print("Something went wrong.")
        print("Status Code:", jsn["code"])
        print("Error Msg:", jsn["message"])
        return []


def print_article(article):
    dt = datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
    print("Title:", article["title"])
    print("Description:", article["description"])
    print("Source:", article["source"]["name"])
    print("Publish at:", dt.strftime("%H:%M %d/%m/%Y"))
    print("Link:", article["url"])


if __name__ == "__main__":
    main()
