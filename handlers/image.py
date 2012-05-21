from handlers.base import BaseHandler
from models import *

import logging
logger = logging.getLogger('boilerplate.' + __name__)

class ImageHandler(BaseHandler):
  def get(self, id):
    logger.debug('Called the ImageHandler with id= %s' % id)
    p = Pin.objects.with_id(id)
    self.set_header("Content-Type", 'image/jpeg')
    self.set_header("Content-Length", p.image.length)
    self.write(p.image.read())

class ImageThumbnailHandler(BaseHandler):
  def get(self, id):
    logger.debug('Called the ImageThumbnailHandler with id= %s' % id)
    p = Pin.objects.with_id(id)
    self.set_header("Content-Type", 'image/jpeg')
    self.set_header("Content-Length", p.image_thumbnail.length)
    self.write(p.image_thumbnail.read())