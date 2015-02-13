__author__ = 'Taio'

from azure.storage import TableService

ts = TableService()

ts.create_table('spimage')