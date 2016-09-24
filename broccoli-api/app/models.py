
from flask import url_for
from flask.ext.appbuilder import Model
from flask.ext.appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
# from flask_appbuilder.models import Markup

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
    # photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))

    # def photo_img(self):
    #     im = ImageManager()
    #     if self.photo:
    #         return Markup('<a href="' + url_for('StudentModelView.show',pk=str(self.id)) +\
    #          '" class="thumbnail"><img src="' + im.get_url(self.photo) +\
    #           '" alt="Photo" class="img-rounded img-responsive"></a>')
    #     else:
    #         return Markup('<a href="' + url_for('StudentModelView.show',pk=str(self.id)) +\
    #          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    # def photo_img_thumbnail(self):
    #     im = ImageManager()
    #     if self.photo:
    #         return Markup('<a href="' + url_for('StudentModelView.show',pk=str(self.id)) +\
    #          '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +\
    #           '" alt="Photo" class="img-rounded img-responsive"></a>')
    #     else:
    #         return Markup('<a href="' + url_for('StudentModelView.show',pk=str(self.id)) +\
    #          '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)


