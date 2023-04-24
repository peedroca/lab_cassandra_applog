import time
import os
from cassandra.cluster import Cluster
from log_package import *

cluster = Cluster(['localhost'])
session = cluster.connect('kslog')

os.system("cls")
rows = list_last_week(session)

rows_sorted = sorted(rows, key=lambda x: x.execution_date, reverse=True)
for row in rows_sorted:
    print(row)