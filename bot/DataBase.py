import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError

load_dotenv(dotenv_path="C:\\Users\\nikit\\PycharmProjects\\habit_tracker_bot\\.evn")
db_name = str(os.getenv("db_name"))
db_user = str(os.getenv("db_user"))
db_password = str(os.getenv("db_password"))
db_host = str(os.getenv("db_host"))
db_port = int(os.getenv("db_port"))


async def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
        return connection
    except OperationalError as e:
        print(f"The error '{e}' occurred")


async def Registri(userID):
    try:
        conn = await create_connection(db_name, db_user, db_password, db_host, db_port)
        cursor = conn.cursor()

        cursor.execute(f"SELECT tgid FROM users WHERE tgid={userID}")
        stat = bool(cursor.fetchone())
        if stat:
            cursor.close()
            conn.close()
        else:
            cursor.execute(f"INSERT INTO users (tgid, testnew) VALUES ({userID}, '1')")
            conn.commit()
            cursor.close()
            conn.close()

    except psycopg2.DatabaseError as error:
            print(f"Error while working with the database: {error}")

    finally:
        if conn:
            cursor.close()
            conn.close()

