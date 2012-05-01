from handlers.index import IndexHandler
from handlers.foo import FooHandler

url_patterns = [
  (r"/", IndexHandler),
  (r"/foo/*", FooHandler),
]
