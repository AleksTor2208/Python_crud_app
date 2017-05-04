
import sqlite3

class SQL:
    """ sql class containing all methods, which connects the project to database """
    @staticmethod
    def sql_connection(database="database"):
        """ create database connection """
        return sqlite3.connect(database)

    @staticmethod
    def execute_query(query, params=""):
        """ execute query with specific params, return list of objects or None, if list is empty """
        conn = SQL.sql_connection()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()
        conn.close()
        result = cur.fetchall()
        if result:
            return result

    