import psycopg2
from psycopg2 import OperationalError


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
        conn = await create_connection("UsersID_DatBas", "postgres", "", "127.0.0.1", 5432)
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

