import json
import logging
import os

import sqlalchemy
from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("API_ENV", "testing")

    def get_db_uri(self):
        if self.environment in ["production", "staging", "testing", "dev"]:
            db_creds = os.getenv("db_creds")
            if db_creds is None:
                print("failed to read db_creds from env")
            db_creds = json.loads(db_creds)
            db_user = db_creds.get("user")
            db_password = db_creds.get("password")

            db_connection_name = os.getenv("DB_CONNECTION_NAME")
            db_database = os.getenv("DB_DATABASE")
        else:
            raise ValueError("Invalid API_ENV configuration.")

        db_config = {
            'drivername': 'postgresql+psycopg2',
            'username': db_user,
            'password': db_password,
            'database': db_database,
        }


        # NOTE: for now we will only allow production or staging to connect to the cloud dbs
        # for everything else run it via local postgerss
        if self.environment in ["production", "staging"]:
            db_config['host'] = f'/cloudsql/{db_connection_name}'
        else:
            db_config['host'] = os.getenv('DB_HOST')
            db_config['port'] = os.getenv('DB_PORT')
                
        print('generating db uri for environment: ', self.environment)
        url =  sqlalchemy.engine.URL.create(**db_config)
        return url
