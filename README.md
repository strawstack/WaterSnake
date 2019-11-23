# WaterSnake

This helper utility allows a user to simply type `watersnake [version-number]` and automatically load-up any version of Python inside an isolated Docker container, with the current directory mounted, and requirements.txt installed.   

# Files

`ws.py` this is the WaterSnake program code. Assign it to an `alias` and run it as per below.

# Create alias

    alias watersnake="python3 ws.py"

# Run WaterSnake

    watersnake [version-number]

version-number: optional argument, defaults to latest

# Demo

This project contains a demo `requirements.txt` file and `plot.py` which will install matplotlib automatically when the container starts, and if `ploy.py` is run a png plot will be created.
