# escreva um laço que a cada um numero aleatório de segundos ele de um print de erro
import random
import time
import uuid
from cassandra.cluster import Cluster
from log_package import *

application_info = {
    "app_name": "app_b",
    "application_type": "API",
    "app_version": "1.5.0",
    "description": "Integrate stock on database",
    "segment": "External Integrations",
}

user_info = {
    "fullname": "PeMOStcok",
    "username": "pemo",
    "role": "Default",
}

def do_import(lastExecutionId):
    cluster = Cluster(['localhost'])
    session = cluster.connect('kslog')

    # Error chance 14,28%
    if random.randint(1, 7) == 1:
        create_log_error(session, lastExecutionId, application_info["app_name"], "Error on save stock registred on " + str(uuid.uuid4()),  application_info, user_info, " at save().connect() on line 230")
    else:
        create_log_success(session, lastExecutionId, application_info["app_name"], "New stock saved on " + str(uuid.uuid4()),  application_info, user_info)
    
    session.shutdown()
    cluster.shutdown()


while True:
    lastExecutionId = uuid.uuid4()

    filename = 'last_execution_' + application_info["app_name"] + ".txt"
    with open(filename, 'w') as f:
        f.write(str(lastExecutionId) + " " + application_info["app_name"])
        f.close()

    
    do_import(lastExecutionId)
    time.sleep(1)
