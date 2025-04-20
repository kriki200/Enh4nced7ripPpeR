import os
import sys

from pathlib import Path

if len(sys.argv) == 2:
	os.system('/bin/bash -c "source ' + os.path.join(str(Path( __file__ ).parent.absolute()), 'bin/activate') + ' && python3 ' + os.path.join(str(Path( __file__ ).parent.absolute()), 'EnhancedTripperBЯaiN.py ') + sys.argv[1] + '"')
else:
	os.system('/bin/bash -c "source ' + os.path.join(str(Path( __file__ ).parent.absolute()), 'bin/activate') + ' && python3 ' + os.path.join(str(Path( __file__ ).parent.absolute()), 'EnhancedTripperBЯaiN.py') + '"')