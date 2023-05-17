import cx_Oracle

class Connect:
    def __init__(self, db_username, db_password, db_host, db_port, db_service_name):
        self.db_username = db_username
        self.db_password = db_password
        self.db_host = db_host
        self.db_port = db_port
        self.db_service_name = db_service_name

    def connect(self):
        try:
            dsn = cx_Oracle.makedsn(self.db_host, self.db_port, service_name=self.db_service_name)
            db_connection = cx_Oracle.connect(self.db_username, self.db_password, dsn)
            return db_connection
        except cx_Oracle.Error as e:
            print(f"Error connecting to Oracle database: {e}")
            return None

    
    
