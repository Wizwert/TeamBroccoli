
#   Stdlib
import json

#   3rd party
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, AppBuilder, expose, BaseView

#   Custom project
from app import appbuilder, db
from app.models import Classroom, Student, Event, MealSetting, MealType, MealLocation, MealPart

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
    route_base = "/data/api"

    @expose('/v1/list_meals')
    def list(self, **params):
        meals = []
        doc = {
            'message': 'Meals for {}'.format('today'),
            'meals': meals,
            'misc': params
        }
        doc_str = json.dumps(doc)
        return doc_str

    @expose('/v1/add_meal/<string:id>')
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



class StudentModelView(ModelView):
    datamodel = SQLAInterface(Student)

    label_columns = {'classroom':'Classroom'}
    list_columns = ['first_name','last_name']

    show_fieldsets = [
        ('Summary',{'fields':['first_name', 'last_name']}),
        # ('Personal Info',{'fields':['birthday','personal_phone','personal_celphone'],'expanded':False}),
        ]

appbuilder.add_view(StudentModelView, "List Students",icon = "fa-envelope",category = "Students")



class ClassroomModelView(ModelView):
    datamodel = SQLAInterface(Classroom)
    related_views = [StudentModelView]

appbuilder.add_view(ClassroomModelView, "List Classes",icon = "fa-folder-open-o",category = "Students",
                category_icon = "fa-envelope")



class EventModelView(ModelView):
    datamodel = SQLAInterface(Event)

    # label_columns = {'classroom':'Classroom'}
    list_columns = ['id','data']

    show_fieldsets = [
        ('Summary',{'fields':['id', 'last_name']}),
        ('Data',{'fields':['data'],'expanded':False}),
    ]

appbuilder.add_view(EventModelView, "List Events",icon = "fa-folder-open-o",category = "Events",
                category_icon = "fa-envelope")


class MealSettingView(ModelView):
    datamodel = SQLAInterface(MealSetting)

    list_columns = ['id', 'description']

    show_fieldsets = [
        ('Summary', {'fields': ['id', 'description']})
    ]

appbuilder.add_view(MealSettingView, "List Settings", icon="fa-folder-open-o", category="Meals",
                category_icon = "healthy-food-icon")



class MealTypeView(ModelView):
    datamodel = SQLAInterface(MealType)

    list_columns = ['id', 'description']

    show_fieldsets = [
        ('Summary', {'fields': ['id', 'description']})
    ]

appbuilder.add_view(MealTypeView, "List Types",icon = "fa-folder-open-o",category = "Meals",
                category_icon = "healthy-food-icon")


class MealLocationView(ModelView):
    datamodel = SQLAInterface(MealLocation)

    list_columns = ['id', 'description']

    show_fieldsets = [
        ('Summary', {'fields': ['id', 'description']})
    ]

appbuilder.add_view(MealLocationView, "List Locations",icon = "fa-folder-open-o",category = "Meals",
                category_icon = "healthy-food-icon")


class MealPartView(ModelView):
    datamodel = SQLAInterface(MealPart)

    list_columns = ['id', 'description']

    show_fieldsets = [
        ('Summary', {'fields': ['id', 'description']})
    ]

appbuilder.add_view(MealPartView, "List Parts",icon = "fa-folder-open-o",category = "Meals",
                category_icon = "healthy-food-icon")
