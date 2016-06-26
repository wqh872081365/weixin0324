import sys
import os.path
  
os.environ['DJANGO_SETTINGS_MODULE'] = 'weixin0324.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'weixin0324'))
  
import sae
from weixin0324 import wsgi
  
application = sae.create_wsgi_app(wsgi.application)