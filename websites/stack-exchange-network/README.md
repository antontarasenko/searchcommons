# Stack Exchange Network

This list contains official Stack Exchange websites.

File `include.txt` can be reproduced by running the following code from the developer console while being on <https://stackexchange.com/sites>:

```javascript
Array.from(
    new Set(Array.from(
        document.getElementsByClassName('lv-info'))
        .map(title => title.children[0].children[0].href)
        .map(href => href.replace(/(.*)[\.\/](.*)\.(\w+)[\/]?/, "*.$2.$3/*"))
    )
).join('\n');
```
