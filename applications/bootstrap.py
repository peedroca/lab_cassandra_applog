from cassandra.cluster import Cluster

# Create a connection to the Docker container running CassandraDB
cluster = Cluster(['localhost'])
session = cluster.connect()

# Create a keyspace

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS kslog
    WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
""")

# Create a table

session.execute("""
    CREATE TABLE IF NOT EXISTS kslog.application_log (
        id text, 
        name text,
        message text,
        status text,
        execution_date timestamp,
        application_info map<text, text>, 
        complementary_info map<text, text>,
        user_info map<text, text>,
        PRIMARY KEY (id)
    ) WITH default_time_to_live = 604800;
""")

# Create index

session.execute("CREATE INDEX IF NOT EXISTS application_log_name_idx ON kslog.application_log (name);")

# Create some data

# session.execute("""
#     INSERT INTO kslog.application_log (id, name, message, status, execution_date, application_info, user_info)
#     VALUES (
#         uuid(), 
#         'Test.Bootstrap', 
#         'Aplication has started sucessfully',
#         'Ok',
#         toTimestamp(now()),
#         { 
#             'application_type': 'Scheduler',
#             'description': 'Application responsible to notify BACEN about all payments realized.', 
#             'segment': 'Payment Integration',
#             'app_version': '1.0.0'
#         },
#         {
#             'name': 'Pedro MOREIRA',
#             'login': 'peedroca',
#             'role': 'admin'
#         }
#     )
# """)

# Verify if the structure was created correctly

describe = session.execute("describe kslog.application_log")

for row in describe:
    print(row)

# Close the connection  

session.shutdown()
cluster.shutdown()