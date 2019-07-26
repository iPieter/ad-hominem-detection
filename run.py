import os
from app import app
import sys

if len(sys.argv) != 4:
    print("Required format: {}.py broker account password".format(sys.argv[0]))
else:
    app.run(broker=sys.argv[1], account=sys.argv[2], password=sys.argv[3])

# To Run:
# python run.py
# or
# python -m flask run
