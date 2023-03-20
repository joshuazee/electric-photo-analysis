from pymongo import MongoClient
from urllib.parse import quote_plus

str_conn = "mongodb://%s:%s@%s" % (quote_plus("sssAdmin"), quote_plus("sss123456"), "119.45.71.239:2777")
db_client = MongoClient(str_conn)

db_database = db_client["py_oa_project"]
