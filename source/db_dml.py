import sqlite3
import datetime
import time
from sqlite3 import Error
import db_dql
import City_Geocoding
from Sunrise_Sunset_Time import Sunrise_Sunset_Time as Sun

# for city table
'''Krakow = tuple(City_Geocoding.Krakow.values())
Sydney = tuple(City_Geocoding.Sydney.values())
NewYork = tuple(City_Geocoding.NewYork.values())
Tokyo = tuple(tuple(City_Geocoding.Tokyo.values()) + ('',))'''

#for sunrise_sunset table
Krakow_lat = db_dql.city_lat(City_Geocoding.Krakow_name)
Krakow_lng = db_dql.city_lng(City_Geocoding.Krakow_name)


def create_connection(db_file):
    
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


def create_sunrise_sunset(conn, task):
    
    sql = '''INSERT INTO sunrise_sunset(city_id,date,sunrise,sunset,first_light,last_light,dawn,dusk,solar_noon,golden_hour,day_light,timezone)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"E:\Python\sqlite\db\Hudson_sollutions_shade.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # city
        '''city_Krakow = Krakow
        city_Krakow_id = create_city(conn, city_Krakow)

        city_Sydney = Sydney
        city_Sydney_id = create_city(conn, city_Sydney)

        city_NewYork = NewYork
        city_NewYork_id = create_city(conn, city_NewYork)

        city_Tokyo = Tokyo
        city_Tokyo_id = create_city(conn, city_Tokyo)

        '''# sunrise_sunset
        Krakow_id = (db_dql.city_id(City_Geocoding.Krakow_name),)
        date_start = datetime.date(2023,7,14)
        date_end = datetime.date(2024,1,1)
        days = [date_start + datetime.timedelta(days=x) for x in range((date_end - date_start).days)]
        for day in days :
            Krakow_sunrise_sunset = tuple(Sun(Krakow_lat, Krakow_lng, day.strftime('%Y%m%d')).sunrise_sunset_time().values())
            date = (day.strftime('%Y%m%d'),)
            sunrise_sunset = Krakow_id + date + Krakow_sunrise_sunset
            create_sunrise_sunset(conn, sunrise_sunset)
            time.sleep(2)


if __name__ == '__main__':
    main()