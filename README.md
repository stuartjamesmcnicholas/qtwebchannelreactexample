# React + QWebChannel + Python QWebEngineView

A small example of using QWebChannel to communicate between a PySide application
and a react app within it.

You need a Python3 with PySide2 or PySide6 installed in it.

* `npm install`
* `npm run dev`
* `python3 scripts/WebEngineExample.py http://localhost:5173` (or whatever address `npm run dev` serves on).

Note: uses the `qwebchannel` NPM module which is LGPL-3.0 licensed.
