version = "1.0.2"

flags = {
  "query": "--query",
  "useGoogle": "--google",
  "useDuck": "--duck",
  "useBing": "--bing",
  "useEngineSearchURL": "--engine",
  "useBrowser": "--browser",
  "useSafari": "--safari",
  "useChrome": "--chrome",
  "useFirefox": "--firefox",
  "useOpera": "--opera",
  "useBrave": "--brave",
  "siteFilter": "--filter",
  "useStackOverflow": "--sof",
  "useStackExchange": "--sxc",
  "useMedium": "--medium",
  "useReddit": "--reddit",
  "devMode": "--dev",
  "help": "--help",
}

flag_help = [
  "--query text\t\t:query flag",
  "--google\t\t:use Google search engine",
  "--duck\t\t:use DuckDuckGo search engine",
  "--bing\t\t:use Bing search engine",
  "--engine url\t\t:use custom search engine. Engine example: --engine https://example.com/search?q=",
  "--browser abs_path\t:use custom browser (alpha)",
  "--safari\t\t:use Safari browser (installed app required. MacOS only)",
  "--chrome\t\t:use Chrome browser (installed app required. MacOS only)",
  "--firefox\t\t:use Firefox browser (installed app required. MacOS only)",
  "--opera\t\t:use Opera browser (installed app required. MacOS only)",
  "--brave\t\t:use Brave browser (installed app required. MacOS only)",
  "--filter filter\t:use site filter. Filter example: --filter site-a.com siteB.de",
  "--sof\t\t:use stackoverflow.com resources",
  "--sxc\t\t:use stackexchange.com resources",
  "--medium\t\t:use medium.com resources",
  "--reddit\t\t:use reddit.com resources",
  "--dev\t\t:use stackoverflow.com, stackexchange.com, medium.com, reddit.com resources",
]

search_engines = {
  "google": "https://google.com/search?q=",
  "duck": "https://duckduckgo.com/?q=",
  "bing": "https://www.bing.com/search?q=",
}

sources = {
  "stackOverFlow": "stackoverflow.com",
  "stackExchange": "stackexchange.com",
  "medium": "medium.com",
  "reddit": "reddit.com",
}

osx_browsers = {
  "safari": "/Applications/Safari.app %s",
  "chrome": "/Applications/Google\ Chrome.app %s",
  "firefox": "/Applications/Firefox.app %s",
  "opera": "/Applications/Opera.app %s",
  "brave": "/Applications/Brave\ Browser.app %s",
}

def print_help():
  print("\nBrowser Search CLI v." + version + ":\n")
  for i, item in enumerate(flag_help):
    print(''.join(["", str(i + 1), ". ", item]))
  print("\n")


def get_search_engine(arg_list):
  if (flags.get("useGoogle") in arg_list):
    return search_engines.get("google")
  if (flags.get("useDuck") in arg_list):
    return search_engines.get("duck")
  if (flags.get("useBing") in arg_list):
    return search_engines.get("bing")
  if (flags.get("useEngineSearchURL") in arg_list):
    return arg_list[arg_list.index(flags.get("useEngineSearchURL")) + 1]
  return search_engines.get("google")

def get_browser(arg_list):
  if (flags.get("useSafari") in arg_list):
    return osx_browsers.get("safari")
  if (flags.get("useChrome") in arg_list):
    return osx_browsers.get("chrome")
  if (flags.get("useFirefox") in arg_list):
    return osx_browsers.get("firefox")
  if (flags.get("useOpera") in arg_list):
    return osx_browsers.get("opera")
  if (flags.get("useBrave") in arg_list):
    return osx_browsers.get("brave")
  if (flags.get("useBrowser") in arg_list):
    return arg_list[arg_list.index(flags.get("useBrowser")) + 1] + "%s"

def get_query(arg_list):
  if (flags.get("query") in arg_list):
    query_index = arg_list.index(flags.get("query")) + 1
    next_arg_index = get_next_arg_index(arg_list, query_index)
    return '+'.join(arg_list[query_index:next_arg_index])
  
def get_next_arg_index(arg_list, start_index):
  all_next_arg_indexes = [ i for i, part in enumerate(arg_list[start_index:]) if part.startswith("--") ]
  if (len(all_next_arg_indexes) == 0):
    return
  return all_next_arg_indexes[0] + start_index
  
def make_filters(arg_list):
  filters = set()
  if (flags.get("devMode") in arg_list):
    filters = set(sources.values())
  if (flags.get("useStackOverflow") in arg_list):
    filters.add(sources.get("stackOverFlow"))
  if (flags.get("useStackExchange") in arg_list):
    filters.add(sources.get("stackExchange"))
  if (flags.get("useMedium") in arg_list):
    filters.add(sources.get("medium"))
  if (flags.get("useReddit") in arg_list):
    filters.add(sources.get("reddit"))
  if (flags.get("siteFilter") in arg_list):
    filter_index = arg_list.index(flags.get("siteFilter")) + 1
    next_arg_index = get_next_arg_index(arg_list, filter_index)
    custom_sites = arg_list[filter_index:next_arg_index]
    for website in custom_sites:
      filters.add(website)

  return filters

def get_filters(arg_list):
  filters = make_filters(arg_list)
  filters_len = len(filters)
  if (filters_len == 0):
    return

  filter_string = ' ('
  for index, website in enumerate(filters):
    filter_string += "site:" + website
    if index == filters_len - 1:
        filter_string += ')'
    else:
        filter_string += "+OR+"

  return filter_string;
