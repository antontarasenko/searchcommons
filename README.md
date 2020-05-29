# Search Commons

Search Commons collects domains you can narrow your web search to.


## Why Narrow Search?

Protect search from blog spam, promotional websites, SEO rings, low-effort social networks, and unreliable sources.

Focus on the websites you have used to, whether official documentation or Stack Overflow.

Narrow search down to specialized websites: dataset aggregators, code repositories, press releases, regulatory filings.


## Search the Web with Our Public Search Engines

Search Commons maintains a public search engine for every website collection we have.

They are powered by Google [Custom Search][1] and available at [searchcommons.org][4].


## Create a Private Search Engine

You can use the collections provided by Search Commons to create a personal search engine on:

* Google [Programmable Search Engine][1] (also known as Custom Search Engine)
* Microsoft [Bing Custom Search][2]


## Explore Website Collections

The collections are stored in the [`websites`](websites/) directory. Each collection contains a search engine specification:

* `include.txt`: Restrict search to these URL patterns
* `exclude.txt`: Exclude these URL patterns from search
* `README.md`: How to reproduce `include.txt` and `exclude.txt`

The directories sometimes contain other relevant files.


## Contribute to Search Commons

Search Commons can't wait for your contribution. It can be:

* A request for a new website collection or search engine
* A new collection of websites
* An edit to existing collections

For this or that, please, create a GitHub issue or send an [email][3].


## Good to Know: Search Commons is Open and Reproducible

Search Commons is self-contained in this repository. Searchcommons.org serves the master branch.

All collections are stored in the `websites` directory and supplied with replication instructions.

The metadata for public search engines is in `engines.json`. Search engines use the default Google Custom Search configuration. No ads, no tracking, except what Google injects in search results as part of its free Custom Search service.


## Contacts

[antontarasenko@gmail.com][3]


## Acknowledgements

[Wikidata](https://www.wikidata.org/) provided data for search engine specifications. It's an excellent source of open data organized as graphs.


## License

[Apache License 2.0](LICENSE.txt)


  [1]: https://programmablesearchengine.google.com/
  [2]: https://www.customsearch.ai/
  [3]: mailto:antontarasenko@gmail.com
  [4]: https://searchcommons.org/
