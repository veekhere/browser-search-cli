import webbrowser
from sys import argv
from core import get_browser, get_filters, get_query, get_search_engine

args = argv[1:]

def execute():
  if (len(args) == 0):
    return

  browser = get_browser(args)
  url = ''.join(filter(None, (get_search_engine(args), get_query(args), get_filters(args))))

  if (browser):
    webbrowser.get("open -a" + browser).open_new_tab(url)
  else:
    webbrowser.open_new_tab(url)

execute()
