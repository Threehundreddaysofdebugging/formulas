from flask import Flask, render_template
from flask_restful import Api, abort
from requests import get
from data.resourses import FormulasResourceList, FormulasResource, DataWorker
from data import db_session

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<string:section>')
def formulas_list(section):
    resp = get(f'http://localhost:5000/api/{section}').json()
    if not resp:
        abort(404, message=f'Value such as <{section}> not found.')
    print(resp)
    return render_template('formulas_list.html', form_list=resp['formulas'], section=section)


@app.route('/<string:section>/<string:name>')
def formula(section, name):
    resp = get(f'http://localhost:5000/api/{section}/{name}').json()
    if not resp:
        abort(404, message=f'Value such as <{name}> not found.')
    print(resp)
    return render_template('formula.html', formula=resp['formula'])


if __name__ == '__main__':
    db_session.global_init("db/formulas.db")
    api.add_resource(FormulasResourceList, '/api/<string:section>')
    api.add_resource(FormulasResource, '/api/<string:section>/<string:name>')
    api.add_resource(DataWorker, '/api')

    app.run(port=5000, host='localhost')
