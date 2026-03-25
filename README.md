# React + QWebChannel + Python QWebEngineView

A small example of using QWebChannel to communicate between a PySide application
and a react app within it.

You need a Python3 with PySide2 or PySide6 installed in it.

Running the development server only seems to work with PySide6 and can be done like this:

* `npm install`
* `npm run dev`
* `python3 scripts/WebEngineExample.py http://localhost:5173` (or whatever address `npm run dev` serves on).

PySide2 seems to require the package to be built and then served with a normal server. e.g.:

* `npm install`
* `npm run build`
* `cd dist`
* `python3 -m http.server 8000 &`
* `python3 ../scripts/WebEngineExample.py http://localhost:8000`

This will also work with PySide6.

Note: uses the `qwebchannel` NPM module which is LGPL-3.0 licensed.
