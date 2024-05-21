from database.DB_connect import DBConnect
from model.areoporto import Airport
from model.volo import Flight

class DAO():
    @staticmethod
    def getAllAirports():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "select * from airports "
        cursor.execute(query)

        for row in cursor:
            result.append(Airport(row["ID"], row["AIRPORT"], row["IATA_CODE"], row["CITY"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdge(distanza):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = 'select f.ID ,f.ORIGIN_AIRPORT_ID, f.DESTINATION_AIRPORT_ID, avg(f.DISTANCE) as distanza from flights f group by f.ORIGIN_AIRPORT_ID, DESTINATION_AIRPORT_ID HAVING distanza >= %s'
        cursor.execute(query, (int(distanza),))
        for row in cursor:
            result.append(Flight(row["ID"],row["ORIGIN_AIRPORT_ID"], row['DESTINATION_AIRPORT_ID'], row['distanza']))
        cursor.close()
        conn.close()
        return result