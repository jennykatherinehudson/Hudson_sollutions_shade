import sqlite3
from sqlite3 import Error
import City_Geocoding

Krakow = tuple(City_Geocoding.Krakow.values())
Sydney = tuple(City_Geocoding.Sydney.values())
NewYork = tuple(City_Geocoding.NewYork.values())
Tokyo = tuple(tuple(City_Geocoding.Tokyo.values()) + ('',))

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_city(conn, project):

    sql = ''' INSERT INTO city(name,latitude,longitude,country,state)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


'''def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' '''INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
              VALUES(?,?,?,?,?,?) ''''''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid'''


def main():
    database = r"E:\Python\sqlite\db\Hudson_sollutions_shade.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new city
        city_Krakow = Krakow
        city_Krakow_id = create_city(conn, city_Krakow)

        city_Sydney = Sydney
        city_Sydney_id = create_city(conn, city_Sydney)

        city_NewYork = NewYork
        city_Krakow_id = create_city(conn, city_NewYork)

        city_Tokyo = Tokyo
        city_Krakow_id = create_city(conn, city_Tokyo)

        '''# tasks
        task_1 = ('Analyze the requirements of the app', 1, 1, city_id, '2015-01-01', '2015-01-02')
        task_2 = ('Confirm with user about the top requirements', 1, 1, city_id, '2015-01-03', '2015-01-05')

        # create tasks
        create_task(conn, task_1)
        create_task(conn, task_2)'''


if __name__ == '__main__':
    main()