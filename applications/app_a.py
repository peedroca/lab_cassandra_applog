import time
import uuid
from cassandra.cluster import Cluster
from log_package import *

application_info = {
    "app_name": "app_a",
    "application_type": "Service",
    "app_version": "1.0.0",
    "description": "Integrate payments on database",
    "segment": "Internal Integrations",
}

user_info = {
    "fullname": "Pedro MOREIRA",
    "username": "pedro.moreira",
    "role": "Developer",
}

def do_import(lastExecutionId):
    cluster = Cluster(['localhost'])
    session = cluster.connect('kslog')
    create_log_success(session, lastExecutionId, application_info["app_name"], "New payment registred on " + str(uuid.uuid4()),  application_info, user_info)
    
    session.shutdown()
    cluster.shutdown()


while True:
    lastExecutionId = uuid.uuid4()

    filename = 'last_execution_' + application_info["app_name"] + ".txt"
    with open(filename, 'w') as f:
        f.write(str(lastExecutionId) + " " + application_info["app_name"])
        f.close()

    do_import(lastExecutionId)
    time.sleep(5)
