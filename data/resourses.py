from flask_restful import Resource, abort, reqparse
from flask import jsonify

from . import db_session
from .formulas import Formula


class FormulasResourceList(Resource):
    def get(self, section):
        db_sess = db_session.create_session()
        formulas = db_sess.query(Formula).filter(Formula.section.like('%{0}%'.format(section)))
        if not formulas:
            abort(404, message=f'Value such as <{section}> not found.')
        return jsonify({'section': section, 'formulas': [{'name': item.name,
                                                          'definition': item.definition}
                                                         for item in formulas]})


class FormulasResource(Resource):
    def get(self, section, name):
        db_sess = db_session.create_session()
        formulas = db_sess.query(Formula).filter(Formula.section.like('%{0}%'.format(section))).first()
        if not formulas:
            abort(404, message=f'Value such as <{name}> not found.')

        return jsonify({'formula': {'name': formulas.name, 'definition': formulas.definition,
                                    'section': formulas.section, 'id': formulas.id}})


class DataWorker(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')
    parser.add_argument('definition')
    parser.add_argument('section')

    def post(self):
        args = self.parser.parse_args()
        db_sess = db_session.create_session()
        formula = Formula(name=args['name'],
                          definition=args['definition'],
                          section=args['section'])
        db_sess.add(formula)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def delete(self, id):
        args = self.parser.parse_args()
        db_sess = db_session.create_session()
        formula = db_sess.query(Formula).get(id)
        if not formula:
            abort(404, mesage=f'Value with such id <{id}> not found.')
        db_sess.delete(formula)
        db_sess.commit()
        return jsonify({'success': 'OK'})


