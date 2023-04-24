import datetime

def create_log_success(session, id, name, message, application_info, user_info):
    query = """INSERT INTO application_log (id, name, message, status, execution_date, application_info, user_info) 
        VALUES (
            %s, 
            %s, 
            %s, 
            'success', 
            toTimestamp(now()),
            {
                'application_type': %s,
                'app_version': %s,
                'description': %s,
                'segment': %s
            },
            {
                'fullname': %s,
                'username': %s,
                'role': %s
            }
        )"""

    print(id, name, message, datetime.datetime.now())

    session.execute(query, (str(id), name, message, application_info['application_type'], application_info['app_version'],
                            application_info['description'], application_info['segment'], user_info['fullname'],
                            user_info['username'], user_info['role'],))


def create_log_error(session, id, name, message, application_info, user_info, stack_trace):
    query = """INSERT INTO application_log (id, name, message, status, execution_date, application_info, user_info, complementary_info) 
        VALUES (
            %s, 
            %s, 
            %s, 
            'error', 
            toTimestamp(now()),
            {
                'application_type': %s,
                'app_version': %s,
                'description': %s,
                'segment': %s
            },
            {
                'fullname': %s,
                'username': %s,
                'role': %s
            },
            {
                'stack_trace': %s
            }
        )"""

    print(id, name, message, datetime.datetime.now())

    session.execute(query, (str(id), name, message, application_info['application_type'], application_info['app_version'],
                            application_info['description'], application_info['segment'], user_info['fullname'],
                            user_info['username'], user_info['role'],stack_trace,))


def create_log_api(session, id, name, message, application_info, user_info, body, request_type, endpoint):
    query = """INSERT INTO application_log (id, name, message, status, execution_date, application_info, user_info, complementary_info) 
        VALUES (
            %s, 
            %s, 
            %s, 
            'error', 
            toTimestamp(now()),
            {
                'application_type': %s,
                'app_version': %s,
                'description': %s,
                'segment': %s
            },
            {
                'fullname': %s,
                'username': %s,
                'role': %s
            },
            {
                'body': %s,
                'request_type': %s,
                'endpoint': %s
            }
        )"""

    print(id, name, message, datetime.datetime.now())

    session.execute(query, (str(id), name, message, application_info['application_type'], application_info['app_version'],
                            application_info['description'], application_info['segment'], user_info['fullname'],
                            user_info['username'], user_info['role'],stack_trace,body,request_type,endpoint))


def list_last_week(session):
    query = """
        SELECT message, status, execution_date FROM application_log
    """

    return session.execute(query)
