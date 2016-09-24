from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Event(Model):
    id = Column(Integer, primary_key=True)
    data = Column(Text)



class Classroom(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name



class Student(Model):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    classroom_id = Column(Integer, ForeignKey('classroom.id'))
    classroom = relationship("Classroom")

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)


