import os

# VKAPI data
TOKENS = os.environ.get('TOKENS').split()
GROUPID = os.environ.get('GROUPID')

# REST API data
RESTIP = os.environ.get('RESTIP')
RESTPORT = os.environ.get('RESTPORT')

# Logging data
EADRESS = os.environ.get('EADRESS')
EPASSWORD = os.environ.get('EPASSWORD')

# DB data
DBUSER = os.environ.get('DBUSER')
DBNAME = os.environ.get('DBNAME')
DBHOST = os.environ.get('DBHOST')
DBPASSWORD = os.environ.get('DBPASSWORD')
