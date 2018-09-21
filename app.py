from flask import Flask
import json
import os
import cadmv


app = Flask('cadmv')


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/app/<int:officeID>', methods=['GET'])
def get_appointment(officeID):
    office,firstDate = cadmv.getOfficeById(officeID)
    res = {'office' :office, 'date': firstDate.strip()}
    return json.dumps(res)


@app.route('/all', methods=['GET'])
def get_all():
    results = cadmv.getAllOffices()
    res = [{'office' :office, 'date': firstDate.strip()} for office,firstDate in results]
    return json.dumps(res)


if os.environ.get('FLASK_ENV'):
    config = {
        'address': {'host': '0.0.0.0', 'port': 5000}
    }
else:
    config = {
    'DEBUG': True,
    'address': {'host': '127.0.0.1', 'port': 5000}
    }
app.config.update(config)

if __name__=='__main__':
    # print app.config
    app.run(**app.config['address'])
