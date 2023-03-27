import sqlite3
from sqlite3 import Error


def __create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def __select_city_lat(conn, city):

    cur = conn.cursor()
    cur.execute(
        "SELECT latitude FROM city WHERE name = '{}'".format(city))

    return cur.fetchall()[0][0]

def __select_city_lng(conn, city):

    cur = conn.cursor()
    cur.execute(
        "SELECT longitude FROM city WHERE name = '{}'".format(city))

    return cur.fetchall()[0][0]


def city_lat(city):
    database = r"E:\Python\sqlite\db\Hudson_sollutions_shade.db"

    conn = __create_connection(database)
    with conn:
        return __select_city_lat(conn, city)
    

def city_lng(city):
    database = r"E:\Python\sqlite\db\Hudson_sollutions_shade.db"

    conn = __create_connection(database)
    with conn:
        return __select_city_lng(conn, city)
