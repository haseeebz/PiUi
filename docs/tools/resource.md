
# Resource

Object for handling assets like images and icons. Also for styling the app.

## Methods

### addResource
Takes a directory and adds it to it's "To Search" directory list. It recursively adds directories so you can categorize your assets folder too.
+ directory : The absolute or relative path of the directory you want to add.

### get
Get the relative path of an asset from the added resources. Automatically resolves the path if the asset is found in some nested directory.
+ asset : The asset name without its full path. Just the name and the extension.

### has 
Checks whether an asset exists within the added resources.
+ asset : The asset name

### find
Finds all assets with a specific name or extension or both.
+ extension : The specific extension including the dot.
+ name : The specific name you want to find excluding the dot and the path.

### applyStylesheet
Obvious enough. Takes a bunch of stylesheet paths and applies it to the app.
+ *stylesheets: path to stylesheets
