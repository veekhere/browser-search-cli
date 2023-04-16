import webbrowser
from sys import argv
from core import get_browser, get_filters, get_query, get_search_engine, flags, print_help

args = argv[1:]

def execute():
  query = get_query(args)
  if (len(args) == 0 or query == ""):
    print("Incorrect or empty query. Make sure you did this properly")
    print_help()
    return
  if (flags.get("help") in args):
    print_help()
    return

  browser = get_browser(args)
  url = ''.join(filter(None, (get_search_engine(args), query, get_filters(args))))

  if (browser):
    webbrowser.get("open -a" + browser).open_new_tab(url)
  else:
    webbrowser.open_new_tab(url)

execute()
