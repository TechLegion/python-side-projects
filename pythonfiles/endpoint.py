from flask import *
import json
import datetime
from datetime import date
# import the required directories

current_utc_time = str(datetime.datetime.utcnow())
day = date.today()
weekday = day.weekday()
today = day.strftime('%A')

# initialize flask app
app = Flask(__name__)


@app.route('/', methods=['GET'])
def request_page():
    user_query = str(request.args.get('slack_name', default="Enter query"))
    user_details = {
        'slack_name': f'{user_query}',
        'current_day': today,
        'utc_time': current_utc_time,
        'track': 'backend',
        'github_file_url': '',
        'github_repo_url': '',
        'status_code': 200
    }
    # convert the data to a json format
    json_dump = json.dumps(user_details)
    return json_dump


# server would run on your local host 5000, you can change the port any choice you want.
if __name__ == '__main__':
    app.run(port=5000)
