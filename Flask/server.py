from flask import *
import scraper

app = Flask(__name__)

@app.route('/')
def hello():
    stmt = scraper.getGarageData()
    return render_template('index.html', response=json.dumps(stmt)) # send all db info, constants.json
