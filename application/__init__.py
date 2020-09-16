from flask import Flask
import os
template_dir = os.path.abspath('../templates')
app = Flask(__name__, template_folder = template_dir)
app.config.from_pyfile('../config.py')
