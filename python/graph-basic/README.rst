Instructions
============

First steps
-----------
Activate the virtual environment

> $ . env/bin/activate

and install the package:

> (env)$ python setup.py install

To do the linting, use

> (env)$ python setup.py lint

To execute test cases, use

> (env)$ python setup.py test

Examples
--------
### jsongraph.py
To test the `jsongraph.py`, open the interpreter and give the following commands:

> (env)$ python
> >>> import graph.jsongraph as jsong
> >>> jsong.main()

The last command should return something like

> Does JSON Graph Schema validate?
>     Schema Validates!
> ...

### Handle json graphs

Open a graph:

> >>> import graph.jsongraph as jsong
> >>> import json
> >>> f = open( "tests/assets/graph_kruskal_wiki.json", "r")
> >>> g = json.load(f)
> >>> f.close()
> >>> graphs = jsong.load_graphs( g )
> >>> graph = graphs.next()

To fetch the nodes for example, use

> >>> graph[ 'nodes' ]

