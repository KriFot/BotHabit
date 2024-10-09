import os
import psycopg2
from dotenv import load_dotenv
from psycopg2 import OperationalError

load_dotenv(dotenv_path="C:\\Users\\nikit\\PycharmProjects\\habit_tracker_bot\\.evn")
URLconnectFirst = os.getenv("URLconnectFirst")

async def create_connection(URL):
    connection = None
    try:
        connection = psycopg2.connect(URL)
        print("Connection to PostgreSQL DB successful")
        return connection
    except OperationalError as e:
        print(f"The error '{e}' occurred")



async def Registri(userID):
    conn = None
    cursor = None
    try:
        conn = await create_connection(URLconnectFirst)
        cursor = conn.cursor()

        cursor.execute(f"SELECT tgid FROM usersid WHERE tgid={userID}")
        stat = bool(cursor.fetchone())
        if stat:
            cursor.close()
            conn.close()
        else:
            cursor.execute(f"INSERT INTO usersid (tgid, stats) VALUES ({userID}, '1')")
            conn.commit()
            cursor.close()
            conn.close()

    except psycopg2.DatabaseError as error:
            print(f"Error while working with the database: {error}")

    finally:
        if conn:
            cursor.close()
            conn.close()



async def HabitList(userID):
    try:
        conn = await create_connection(URLconnectFirst)
        cursor = conn.cursor()

        cursor.execute(f"SELECT habitname FROM Habit WHERE idU = {userID};")
        habits = cursor.fetchall()
        HabitsList = [habit[0] for habit in habits]

        return HabitsList

    except psycopg2.DatabaseError as error:
        print(f"Error: {error}")
        return []
