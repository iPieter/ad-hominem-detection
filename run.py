import os
from app import app

app.run(port=5000, threaded=False)

# To Run:
# python run.py
# or
# python -m flask run