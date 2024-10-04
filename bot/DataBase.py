import psycopg2

async def Registri(userID):
    conn = psycopg2.connect(dbname="metanit", user="postgres", password="123456", host="127.0.0.1")
    cursor = conn.cursor()

    cursor.execute(f"SELECT stat FROM UserTgID WHERE id={userID}")
    stat = bool(cursor.fetchone())
    if stat:
        return 0
    else:
        cursor.execute(f"INSERT INTO UserTgID (#вписать перменные строки бд) VALUES ({userID}, дописать остальные перменные бд)")
        return 0



