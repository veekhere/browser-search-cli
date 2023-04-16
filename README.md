# Browser Search CLI

###### Inspiration source - [Your Average Tech Bro](https://www.youtube.com/watch?v=6wwHv-cyOd0)

###### Crossplatform (alpha)

---

### Installation

- Make sure _Python_ is installed on your machine by running `python3 --version`
- Copy `search.py` wherever you want
- Open your `.zshrc`
- Add aliases for executing. Examples:
  - Safari search `alias ss="python3 ~/scripts/search.py --safari --query`
  - Chrome search `alias sc="python3 ~/scripts/search.py -chrome --query`
  - Safari Bing search `alias ssb="python3 ~/scripts/search.py --safari --bing --query`
  - Full custom search `alias s="python3 ~/scripts/search.py --query`
- Run `source ~/.zshrc` to reload (or reload your terminal)
- Try to run `YOUR_ALIAS how to make new spring project`
- Enjoy

---

### Available options

- `--query` + `space` + `your query after flag` — query area
- `--google` — use Google search engine
- `--duck` — use DuckDuckGo search engine
- `--bing` — use Bing search engine
- `--engine` + `space` + `https://my-search.engine/search?q=` — use custom search engine
- `--browser` + `space` + `absolute/path/to/custom/browser.exe` — use custom browser (alpha)
- `--dev` — use development search sources (stackoverflow.com, stackexchange.com, medium.com, reddit.com)
- `--sof` — use stackoverflow.com search source
- `--sxc` — use stackexchange.com search source
- `--medium` — use medium.com search source
- `--reddit` — use reddit.com search source
- `--filter` + `space` + `siteA.com site-B.de site.C.am` — use custom site filter

> **Warning**                                                                       
> MacOS flags only. Installed applications required

- `--safari` — use Safari browser
- `--chrome` — use Chrome browser
- `--firefox` — use Firefox browser
- `--opera` — use Opera browser
- `--brave` — use Brave browser
