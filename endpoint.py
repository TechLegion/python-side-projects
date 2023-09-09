from flask import *
import json
import datetime
from datetime import date
current_utc_time = str(datetime.datetime.utcnow())
day = date.today()
weekday = day.weekday()
today = day.strftime('%A')

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
    json_dump = json.dumps(user_details)
    return json_dump


if __name__ == '__main__':
    app.run(port=5000)
