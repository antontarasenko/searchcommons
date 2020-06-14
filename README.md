# Search Commons

Search Commons is an open source project that maintains a directory of websites you can restrict your search to.


## Usage

### Search the Web with Our Public Search Engines

Search Commons maintains a public search engine for every website collection we have.

They are powered by Google [Custom Search][1] and available at [SearchCommons.org][4].

### Create a Private Search Engine

You can use the collections provided by Search Commons to create a personal search engine on:

* Google [Custom Search Engine][1] (also known as Programmable Search Engine)
* Microsoft [Bing Custom Search][2]

The collections are stored in the [`websites`](websites/) directory.

### Request a Search Engine

You can tell us how Google fails you in GitHub Issues or by [email][3]. We will help you improve the search for your case and add it to our public search engines.


## Project Structure

### Website Collections

Each collection contains a search engine specification:

* `include.txt`: The URL patterns included in search
* `exclude.txt`: The URL patterns excluded from search
* `README.md`: Instructions for reproducing or maintaining the engine

### Public Search Engines

The metadata for public search engines is stored in [`engines.json`](engines.json). Search engines use the default Google Custom Search configuration. No ads, no tracking, except what Google injects in search results as part of its free Custom Search service.


## Contributing

Search Commons is open for contributions. You can discuss contributions in GitHub Issues or by [email][3].


## Contacts

Anton Tarasenko, [antontarasenko@gmail.com][3]


## Acknowledgements

[Wikidata](https://www.wikidata.org/) provided data for search engine specifications.


## License

[Apache License 2.0](LICENSE.txt)


  [1]: https://programmablesearchengine.google.com/
  [2]: https://www.customsearch.ai/
  [3]: mailto:antontarasenko@gmail.com
  [4]: https://searchcommons.org/
