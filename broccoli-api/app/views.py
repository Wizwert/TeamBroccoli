
#	Stdlib
import json

#	3rd party
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, AppBuilder, expose, BaseView

#	Custom project
from app import appbuilder, db

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404

db.create_all()



class APIView(BaseView):
    route_base = "/api"

    @expose('/list_meals')
    def list(self, **params):
    	meals = []
    	doc = {
    		'message': 'Meals for {}'.format('today'),
    		'meals': meals,
    		'misc': params
    	}
        doc_str = json.dumps(doc)
        return doc_str

    @expose('/add_meal/<string:id>')
    def add_meal(self, id, **params):
        # do something with id
        # and render it
        doc = {
        	'id': id,
        	'message': 'Added a meal',
        	'misc': params
        }
        doc_str = json.dumps(doc)
        return doc_str


appbuilder.add_view_no_menu(APIView())
