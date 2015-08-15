from app import app
from flask import render_template


@app.route('/')
def index():
    user     = {'nickname': 'HB6H057'}
    title    = 'logStream'
    subtitle = "Still haven't turned in your log!?"

    return render_template('index.html', user=user, title=title, subtitle=subtitle)
