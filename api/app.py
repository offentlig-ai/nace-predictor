import flask
from flask import Flask, Response, request, abort
from flask_cors import CORS
import fasttext
from fasttext import load_model
import json
import sys
import os

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'model')

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
model = None

def load_fasttext_model():
    global model
    mf = f'{MODEL_PATH}/nace_model.bin'
    try:
        model = load_model(mf)
    except IOError as e:
        print(f'I/O error {e.errno},{e.strerror}')
    except ValueError as e:
        print(f'Value error {e}')
    except:
        print(f'Unexpected error: {sys.exc_info()[0]}')


@app.route('/isReady', methods=['GET'])
def isReady():
    return "OK"


@app.route('/isAlive', methods=['GET'])
def isAlive():
    return "OK"


@app.route('/api', methods=['GET'])
def api():
    if 'q' in request.args:
        query = request.args['q']
        if not isinstance(query, str):
            abort(406)
        if len(query) < 3:
            abort (406)
    else:
        return

    if model is None:
        load_fasttext_model()
    result = model.predict(query, k=5)

    # Making a mock result, since we have no model at the moment:
    ##result = []
    ##labels = ['00.000','01.110','01.210','01.220']
    ##probabilities = [1, 0.75, 0.5, 0.25, 0.1]
    ##result.append(labels)
    ##result.append(probabilities)

    ret = []
    for i, pred in enumerate(result[0]):
        ret.append({'nace':pred.replace('__label__','').replace('"',''),'value':str(result[1][i])})
    return Response(json.dumps(ret), mimetype='application/json')


if __name__ == '__main__':
    load_fasttext_model()
    app.run(host='0.0.0.0', port=8081, debug=True)
