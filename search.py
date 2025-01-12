import webbrowser
import sys

valid_websites = {"reddit.com", "stackoverflow.com", "stackexchange.com", "medium.com"}

url = "https://www.google.com/search?q="


def create_filter():
    filter = "("
    for index, website in enumerate(valid_websites):
        filter += "site:" + website
        if index == len(valid_websites) - 1:
            filter += ")"
        else:
            filter += " OR "
    return filter


def create_query():
    query = sys.argv[1:]
    return " ".join(query)


def create_url():
    if len(sys.argv[1:]) == 0:
        print("Error: Please enter a valid search")
    else:
        final_url = url + create_query() + " " + create_filter()
        print(final_url)
        webbrowser.open(final_url)


create_url()
