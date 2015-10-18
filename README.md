# Auto
Fast way to launch a load of different URLs, organized in a tree structure.

###Info###
To add items into the shortcut tree, edit catalog.xml in data/

Each <group> tag is a node in the tree. It can have an optional url to be able to be directly launched.
Each <item> tag is a leaf in the tree. It must have a url attribute to do anything.

To launch anything, type its path in the tree separated by spaces. For example, `gh auto` in the default configuration will launch this page. Typing just `gh` will launch the Github homepage.

Wildcards are also supported. To launch all items in the `gh` group, type `gh *`. This works at any depth in the tree, so you could also type `* stuff` and it would launch all 2nd-level items named stuff.
