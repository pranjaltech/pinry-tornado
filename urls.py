from handlers.index import IndexHandler
from handlers.newpin import NewPinHandler

url_patterns = [
  (r"/", IndexHandler),
  (r"/newpin/*", NewPinHandler),
]
