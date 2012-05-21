from handlers.base import BaseHandler
from models import *
from tornado.escape import json_encode
import json, hashlib

import logging
logger = logging.getLogger('boilerplate.' + __name__)

class PinHandler(BaseHandler):
  def get(self, page):
    logger.debug('Asking for Pins')
    start_pin = abs(int(page) - 1) * 25
    end_pin = int(page) * 25
    
    pins = Pin.objects.order_by('-id')[start_pin:end_pin]
    logger.debug(pins)
    recent_pins = []
    itr = 0
    for pin in pins:
      h = hashlib.md5(str(pin.id)).hexdigest()
      recent_pins.append({
        'id': str(pin.id),
        'thumbnail': 'img/t/%(id)s?v=%(h)s' % {'id':str(pin.id), 'h':h[:5]},
        'original': 'img/%(id)s?v=%(h)s' % {'id':str(pin.id), 'h':h[-5:]},
        'description': pin.description,
        })
      itr = itr + 1
    logger.debug(recent_pins)
    recent_pins = {0:recent_pins}
    logger.debug('Is recent_pins an instance of a dict?')
    logger.debug(isinstance(recent_pins, dict))
    self.write(recent_pins)