
# Styling

Qt based applications are styled using QSS but I recommend  using CSS with just the simple properties since it has better intellisense.

You can style using the Pi.resource object.
```python
Pi.resource.applyStylesheet("path/to/style.css", "path/to/style2.css", ...)
```
You can also set the style sheets in the Pi.init()

Using the command line you can reapply the stylesheets. This is useful if you don't want to restart the app and are just testing colors and fonts etc.
```bash
pi-ctl reload_style
```