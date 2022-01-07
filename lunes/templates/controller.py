from lunes.utilities import Model,params
from flask import abort
from app import r
import uuid

class {{ module.capitalize() }}(Model):
    permit =[{{all_fields_names}}]
    def __init__(self, params):
        self.id = uuid.uuid4().hex
        self.update_params(params)

{{module}}_repository= []

def get_{{module}}_by_id(id):
    for i in {{module}}_repository:
        if str(i.id) == str(id) :
            return i
    abort(404)

@r.render('/{{module}}', methods=['GET']) #index
def {{module}}_index():
    return {{module}}_repository 

@r.render('/{{module}}/new', methods=['GET']) #new
def {{module}}_new():
    pass

@r.render('/{{module}}', methods=['POST']) #create
def {{module}}_create():
    {{module}}= {{ module.capitalize() }}( params)
    {{module}}_repository.append({{module}})
    return {{module}} 

@r.render('/{{module}}/<id>/edit', methods=['GET']) #edit
def {{module}}_edit(id):
    return get_{{module}}_by_id(id)

@r.render('/{{module}}/<id>', methods=['GET']) #show
def {{module}}_show(id):
    return get_{{module}}_by_id(id)

@r.render('/{{module}}/<id>', methods=['POST']) #update
def {{module}}_update(id):
    {{module}} = get_{{module}}_by_id(id)
    return {{module}}.update_params(params)

@r.render('/{{module}}/<id>',methods=['DELETE'])
def {{module}}_delete(id):
    {{module}} = get_{{module}}_by_id(id)
    {{module}}_repository.remove({{module}})
    return {{module}}_repository 


