from data import db_session
from data.forms import AddForm
from data.resourses import FormulasResourceList, FormulasResource, DataWorker, CompareResource
from flask import Flask, render_template, redirect
from flask_restful import Api, abort
from requests import get, post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
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


@app.route('/add_formula', methods=['GET', 'POST'])
def add_formula():
    form = AddForm()
    if form.validate_on_submit():
        post('http://localhost:5000/api',
             data={'name': form.name.data,
                   "definition": form.definition.data,
                   'section': form.section.data})
        return redirect('/success')
    return render_template('formula_adding.html', form=form)


@app.route('/success')
def success():
    return '<h3>success</h3>'

@app.route('/compare/<string:name>')
def compare(name):
    resp = get(f'http://localhost:5000/api/compare/{name.lower()}').json()
    if not resp or not resp.get('message') is None:
        abort(404, message=f'Value such as <{name}> not found.')
    return render_template('compare.html', forms_list=resp['formulas'])


if __name__ == '__main__':
    db_session.global_init("db/formulas.db")
    api.add_resource(FormulasResourceList, '/api/<string:section>')
    api.add_resource(FormulasResource, '/api/<string:section>/<string:name>')
    api.add_resource(DataWorker, '/api')
    api.add_resource(CompareResource, '/api/compare/<string:name>')

    app.run(port=5000, host='localhost')
