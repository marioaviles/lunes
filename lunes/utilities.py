from flask import Flask, render_template, request, redirect, url_for, abort 
#import uuid
from functools import wraps
import inspect
from flask import Response
from werkzeug.local import LocalProxy
from functools import partial
from flask import current_app, _app_ctx_stack, url_for


params = LocalProxy(lambda: {**request.args, ** request.form})



class Model:
    permit =[]
    def update_params(self, params):
        for k in params.keys():
            if k in self.permit:
                setattr(self, k, params[k])
        return self 


class Renzo(object):

    def __init__(self, app=None):
        self.app = app

    def render(self,route, **k):
        # self.add_url_rule(rule, endpoint, f, **options)
        def decorate(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                context =fn(*args,   **kwargs )
                module, action =fn.__name__.split('_')
                if request.method =='GET':
                    return  render_template('/'+module+'/'+action+'.html',ctx=context,  **kwargs)
                elif request.method == 'POST':
                    #hotwire uses 303 redirection
                    return  render_template('/'+module+'/show.html',ctx=context,  **kwargs), 303
                elif request.method == 'DELETE':
                    return  render_template('/'+module+'/index.html',ctx=context,  **kwargs)
            self.app.add_url_rule(route, fn.__name__, wrapper,**k)
        return decorate






