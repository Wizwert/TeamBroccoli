
#	TBD: What view?
from flask.ext.appbuilder import IndexView


class CafeteriaView(IndexView):
	index_template = 'cafeteria.html'
