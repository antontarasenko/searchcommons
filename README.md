# Custom Search Lists

This repository helps to create a custom web search engine.

A custom search engine restricts search results to certain domains. How does it help?

* Restricted search protects from blog spam, promotional websites, SEO rings, low-effort social networks, and unreliable sources.
* Custom search focuses on websites you have used to, whether it's official documentation or Stack Overflow
* Search can be narrowed down to specialized websites: dataset aggregators, code repositories, press releases, regulatory filings

Search engines that provide custom search service:

* Google [Programmable Search Engine][1] (previously known as Custom Search Engine)
* Microsoft [Bing Custom Search][2]

Examples that follow use Google's engine.


## Usage

### Search Web with a Public Custom Search Engine

* [index.html][index.html]

### Create a Personal Custom Search Engine

You can fork one of the public custom search engines and adjust it for your needs.

1. Create a new Custom Search Engine at [programmablesearchengine.google.com]
2. Create  and add your search engine to `websitesLocal.json` (if necessary, create the file following the format of `websites.json`)
3. Start a local server from the root of this repository
4. Open `index.html` via this server address
5. Find your search engine in the list and export its annotations
6. Upload annotations to your Custom Search Engine account

## Project Structure

### `index.html`

Browser UI to list available engines, perform quick search, and export annotations.

### `websites/`

The directory contains the lists of websites included in particular search engine.

### `websites.json`

The file contains public search engines built with lists from the `websites` directory.

### `websitesLocal.json` (excluded)

The file contains your personal search engines. Identical to `websites.json` in structure. Excluded from the repository to avoid version control conflicts.


## Contributions



  [1]: https://programmablesearchengine.google.com/
  [2]: https://www.customsearch.ai/
