from flask import *
import json
import datetime
from datetime import date
# import the required directories

day = date.today()


def today_date():
    return day.strftime('%A')


def utc_time():
    return datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")


utc_time()

# initialize flask app
app = Flask(__name__)


@app.route('/api', methods=['GET'])
def request_page():
    user_query = request.args.get('slack_name')
    track = request.args.get('track')
    user_details = {
        'slack_name': user_query,
        'current_day': str(today_date()),
        'utc_time': str(utc_time()),
        'track': track,
        'github_file_url': 'https://github.com/Daezee/HNG-stage-1/edit/master/pythonfiles/endpoint.py',
        'github_repo_url': 'https://github.com/Daezee/HNG-stage-1.git',
        'status_code': 200
    }
    # convert the data to a json format
    json_dump = json.dumps(user_details)
    return json_dump


# server would run on your local host 5000, you can change the port any choice you want.
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
