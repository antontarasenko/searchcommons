# Search Commons

Search Commons contains lists of domains you can narrow your web search to.


## Why Narrow Search?

* Protect search from blog spam, promotional websites, SEO rings, low-effort social networks, and unreliable sources
* Focus on the websites you have used to, whether official documentation or Stack Overflow
* Narrow search down to specialized websites: dataset aggregators, code repositories, press releases, regulatory filings


## Search Engines

You can use the lists provided by Search Commons to create a custom search engine on:

* Google [Programmable Search Engine][1] (also known as Custom Search Engine)
* Microsoft [Bing Custom Search][2]


## Project Structure

### `websites`

Each subdirectory in `websites` contains a search engine specification:

* `include.txt`: Restrict search to these URL patterns
* `exclude.txt`: Exclude these URL patterns from search
* `README.md`: How to reproduce `include.txt` and `exclude.txt`

The subdirectory may contain other files.

### `index.html`

An interface for the search engines created from the specifications in `websites`.


## Contributing

Search Commons can't wait for new lists and edits.

Please, create a GitHub issue or send Anton Tarasenko an [email][3].


## Contacts

[antontarasenko@gmail.com][3]


## Acknowledgements

[Wikidata](https://www.wikidata.org/) provided data for search engine specifications. It's an excellent source of open data organized as graphs.


## License

[Apache License 2.0](LICENSE.txt)


  [1]: https://programmablesearchengine.google.com/
  [2]: https://www.customsearch.ai/
  [3]: mailto:antontarasenko@gmail.com
