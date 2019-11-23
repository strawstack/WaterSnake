import os
import sys

# Choose Python3 if no version number
arg1 = "3"

if len(sys.argv) == 2:
    # Get the version number
    arg1 = sys.argv[1]

# Run Docker command
os.system(f'docker run -it -v ${{PWD}}:/opt -w="/opt" python:{arg1} bash -c "pip install -r requirements.txt && bash"')
