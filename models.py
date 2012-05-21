#
# @author Pranjal Kumar Singh
#
from mongoengine import *
import Image
import urllib2

connect('pinry_db')

import logging
logger = logging.getLogger('boilerplate.' + __name__)

class Pin(Document):
  url = URLField(unique=True)
  description = StringField()
  image = FileField()
  image_thumbnail = FileField()
  
  def __unicode__(self):
    return self.url
  
  def save(self):
    #TODO: Add validation that checks if the URL corresponds to an Image
    if not self.image:
      self.image = urllib2.urlopen(self.url).read()
      image_temp = Image.open(self.image)
      image_temp_org = image_temp
      image_temp.thumbnail((200, 1000), Image.ANTIALIAS)
      self.image_thumbnail.new_file()
      self.image.content_type='image/jpeg'
      self.image_thumbnail.content_type='image/jpeg'
      image_temp.save(self.image_thumbnail, 'jpeg', quality=85)
      self.image_thumbnail.close()
    super(Pin, self).save()
  
  def validate(self):
    # Find the url in the database. If it is not present, then proceed. Otherwise, raise a ValidationError. 
    try: 
      super(Pin, self).validate()
    except ValidationError as e:
      raise ValidationError('Invalid URL!')
    logger.debug('Custom Validation in progress... ')
    logger.debug('URL: ', self.url)
    if len(self.url.strip()) <= 0:
      raise ValidationError('URL is empty!')
    elif Pin.objects(url=self.url).count() > 0: 
      raise ValidationError('URL already exists!')
    else:
      logger.debug('Successfully validated...')