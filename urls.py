from handlers.index import IndexHandler
from handlers.newpin import NewPinHandler
from handlers.api import PinHandler
from handlers.image import ImageHandler, ImageThumbnailHandler

url_patterns = [
  (r"/", IndexHandler),
  (r"/newpin/*", NewPinHandler),
  (r"/pins/recent/(.*)", PinHandler),
  (r"/img/t/(.*)", ImageThumbnailHandler),
  (r"/img/(.*)", ImageHandler),
]
