
from flask import Flask, render_template, request, redirect, url_for, abort
from lunes.utilities import Renzo

app = Flask(__name__)
app.secret_key = 'super secret key'
r = Renzo(app)


import controller # replace with your module name
