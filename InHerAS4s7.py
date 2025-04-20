import os
from pathlib import Path

def inA5S(nekje) :
    paths = sorted(Path(nekje.rsplit('\\', 1)[0]).iterdir(), key=os.path.getmtime)

    for path in paths:
        os.rename(path, path.rsplit('\\', 1)[0] + str(int(len(os.listdir(nekje))) + 1) + ". " + "") #####+ path.split('-', 1)[0].rsplit('\\', 1)[1] + path.split('-', 1)[0].rsplit('\\', 1)[1] )