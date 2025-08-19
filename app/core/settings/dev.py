from .base import *
import socket

DEBUG = 1
ENVIRONMENT = "DEVELOPMENT"
SITE_DOMAINE = "http://localhost:1340/appname"
URL = "http://localhost:1340/appname"
SITE_NAME = "localhost/appname"

STATIC_URL = "/appname/static/"
MEDIA_URL = "/appname/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

INTERNAL_IPS = [
    "127.0.0.1",
]
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]
