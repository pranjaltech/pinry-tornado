from handlers.base import BaseHandler
from models import *

import logging
logger = logging.getLogger('boilerplate.' + __name__)

class NewPinHandler(BaseHandler):
  def get(self):
    logger.debug('Rendering the NewPin page')
    self.render("newpin.html", error="False", error_messages="None")
    
  def post(self):
    #in a try-except block, store the new pin. If it succeeds, redirect to the HOME Page. 
    #If it fails, set error=true, and render the newpin.html page with an error message. 
    url = ''
    description = ''
    try:
      url = self.get_argument("url")
      description = self.get_argument("description")
    except: 
      pass
    try:
      new_pin = Pin(url=url, description=description)
      new_pin.validate()
      new_pin.save()
      self.redirect('/')
    except ValidationError as e: 
      logger.debug(e)
      self.render("newpin.html", error="True", error_messages=e)