from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from views import index_views, admin_views
