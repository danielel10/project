from flask import Flask, jsonify
from flask_cors import CORS
from flask import Flask, jsonify, request

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


molecules = [
    {
        'fName': 'On the Road',
        'Mass': 'Jack Kerouac',
        'Plot': True
    },
    {
        'fName': 'Harry Potter and the Philosopher\'s Stone',
        'Mass': 'J. K. Rowling',
        'Plot': False
    },
    {
        'fName': 'Green Eggs and Ham',
        'Mass': 'Dr. Seuss',
        'Plot': True
    }
]


@app.route('/Molecules', methods=['GET'])
def all_molecules():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        molecules.append({
            'fName': post_data.get('fName'),
            'Mass': post_data.get('Mass'),
            'Plot': post_data.get('Plot')
        })
        response_object['message'] = 'molecule added!'
    else:
        response_object['molecules'] = molecules
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
