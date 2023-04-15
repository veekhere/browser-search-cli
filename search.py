import webbrowser
import sys

base_search_url = "https://google.com/search?q="
safari_path = "open -a /Applications/Safari.app %s"
chrome_path = "open -a /Applications/Google\ Chrome.app %s"

preferred_sources = [
    "stackoverflow.com",
    "stackexchange.com",
    "medium.com",
]

def create_filter():
    filter = '('
    for index, website in enumerate(preferred_sources):
        filter += "site:" + website
        if index == len(preferred_sources) - 1:
            filter += ')'
        else:
            filter += "+OR+"

    return filter;

def create_query():
    query = sys.argv[2:]
    return '+'.join(query)

def get_browser():
    match sys.argv[1]:
        case "-c":
            return chrome_path
        case "-s":
            return safari_path
        case _:
            return safari_path

def execute():
    if (len(sys.argv[2:]) == 0):
        return;
    final_url = base_search_url + create_query() + create_filter()
    browser = get_browser()
    webbrowser.get(browser).open_new_tab(final_url)

execute()
