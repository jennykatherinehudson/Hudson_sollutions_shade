import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"E:\Python\sqlite\db\Hudson_sollutions_shade.db"
    sql_create_city_table = """ CREATE TABLE IF NOT EXISTS city (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        latitude DOUBLE NOT NULL,
                                        longitude DOUBLE NOT NULL,
                                        country text NOT NULL,
                                        state text
                                    ); """

    sql_create_sunrise_sunset_table = """CREATE TABLE IF NOT EXISTS sunrise_sunset (
                                    id integer PRIMARY KEY,
                                    city_id integer NOT NULL,
                                    date text NOT NULL,
                                    sunrise text NOT NULL,
                                    sunset text NOT NULL,
                                    first_light text ,
                                    last_light text ,
                                    dawn text ,
                                    dusk text ,
                                    solar_noon text ,
                                    golden_hour text ,
                                    day_light text ,
                                    timezone text ,                                    
                                    FOREIGN KEY (city_id) REFERENCES city (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create city table
        create_table(conn, sql_create_city_table)

        # create sunrise_sunset table
        create_table(conn, sql_create_sunrise_sunset_table)

    else:
        print("Error! cannot create the database connection.")



if __name__ == '__main__':
    main()
