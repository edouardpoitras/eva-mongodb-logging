"""
This plugin will only be able to start logging after it has been enabled.
It may not reveal issues with parsing the plugins directories, the config files,
and may not catch any plugin errors that occur before this plugin's instantiation.
"""
import datetime
import gossip
from eva import conf
from eva.util import get_mongo_client
from pymongo import ASCENDING

mongo_client = get_mongo_client()
db_name = conf['mongodb']['database']
logging_collection = conf['plugins']['mongodb_logging']['config']['log_mongo_collection']
db = mongo_client[db_name]
logs = db[logging_collection]
logs.ensure_index([('timestamp', ASCENDING)])

def get_data(message, log_type):
    return {'timestamp': datetime.datetime.utcnow(),
            'type': log_type,
            'message': message}

@gossip.register('eva.logger.debug')
def debug(message):
    logs.insert(get_data(message, 'debug'))

@gossip.register('eva.logger.info')
def info(message):
    logs.insert(get_data(message, 'info'))

@gossip.register('eva.logger.warning')
def warning(message):
    logs.insert(get_data(message, 'warning'))

@gossip.register('eva.logger.error')
def error(message):
    logs.insert(get_data(message, 'error'))

@gossip.register('eva.logger.fatal')
def fatal(message):
    logs.insert(get_data(message, 'fatal'))
