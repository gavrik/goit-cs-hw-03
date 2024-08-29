import psycopg2


def get_connection(host, user, passwd, db):
    conn = None
    try:
        conn = psycopg2.connect(
            host=host,
            port=5432,
            user=user,
            password=passwd,
            database=db,
            application_name="neoversity",
            options="-c search_path={}".format("public")
        )
        conn.set_session(autocommit=True)
    except psycopg2.OperationalError as e:
        print("Unable to connect! {0}".format(e))
        return conn
    return conn


def execute_query(conn, query, is_result=False):
    with conn.cursor() as curr:
        curr.execute(query)
    return None, None
