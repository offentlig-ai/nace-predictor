import flask
from flask import Flask, Response, render_template, request, send_from_directory, url_for
from flask_cors import CORS
import fastText
from fastText import load_model
import json
import sys
import os

STATIC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

app = Flask(__name__,static_folder="./static/build/static", template_folder="./static/build")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
model = None

def load_fasttext_model():
    global model
    mf = f'{STATIC_PATH}/model.bin'
    try:
        model = load_model(mf)
    except IOError as e:
        print(f'I/O error {e.errno},{e.strerror}')
    except ValueError as e:
        print(f'Value error {e}')
    except:
        print(f'Unexpected error: {sys.exc_info()[0]}')
  

@app.route('/', methods=['GET', 'POST'])
def react():
    return render_template('index.html')


@app.route('/api', methods=['GET'])
def api():
    if 'q' in request.args:
        query = request.args['q']
    else:
        return "Feil: ingen tekst sent."

    if model is None:      
        load_fasttext_model()

    result = model.predict(query, k=5)
    ret = []
    for i, pred in enumerate(result[0]):
        ret.append({'nace':pred.replace('__label__','').replace('"',''),'value':str(result[1][i])})
    return json.dumps(ret)


if __name__ == '__main__':
    load_fasttext_model()
    app.run(host='0.0.0.0', port=8080, debug=True)

