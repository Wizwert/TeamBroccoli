from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Meal(Model):
	id = Column(Integer, primary_key=True)
	student_id = Column(Integer)
	date = Column(Date)
	meal_type_id = Column(Integer)
	meal_location_id = Column(Integer)
	meal_setting_id = Column(Integer)
	rating = Column(Double)
	
class MealSetting(Model)
	id = Column(Integer, primary_key=True)
	description = Column(String(400)
	
class MealPart(Model)
	id = Column(Integer, primary_key=True)
	meal_id = Column(Integer)
	part_id = Column(part_id)
	
class Student(Model)
	id = Column(Integer, primary_key=True)
	first_name = Column(String(400))
	last_name = Column(String(400))
	class_id = Column(Integer)
	
class MealType(Model)
	id = Column(Integer, primary_key=True)
	description = Column(String(400))
	
class MealLocation(Model)
	id = Column(Integer, primary_key=True)
	description = Column(String(400))
	
class MealPart(Model)
	id = Column(Integer, primary_key=True)
	description = Column(String(400))