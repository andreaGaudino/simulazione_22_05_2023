from database.DB_connect import DBConnect
from model.player import Player


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getGiocatori(anno, salario):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct p.playerID as id, p.nameFirst as name, p.nameLast as surname, s.salary as salary
                    from lahmansbaseballdb.people p, lahmansbaseballdb.salaries s 
                    where p.playerID = s.playerID 
                    and s.`year` = %s
                    and s.salary > %s """

        cursor.execute(query, (anno, salario))

        for row in cursor:
            result.append(Player(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(anno, salario):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinctrow a.playerID as p1, a2.playerID as p2
                from lahmansbaseballdb.appearances a , lahmansbaseballdb.appearances a2 , lahmansbaseballdb.salaries s , lahmansbaseballdb.salaries s2 
                where a2.`year` = %s
                and a.`year`= a2.`year` 
                and s2.`year` = a.`year`
                and s2.playerID = a.playerID
                and s2.salary >%s
                and a.playerID < a2.playerID
                and a.teamID = a2.teamID
                and s.salary > %s
                and s.`year` = a2.`year` 
                and s.playerID = a2.playerID 
                """

        cursor.execute(query, (anno, salario, salario))

        for row in cursor:
            result.append((row["p1"], row["p2"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSquadreGiocatore(n, anno):
        conn = DBConnect.get_connection()

        result = {}

        cursor = conn.cursor(dictionary=True)
        query = """select  distinctrow a.playerID, a.teamID 
                    from lahmansbaseballdb.appearances a
                    where a.`year` = %s
                    and a.playerID = %s"""

        cursor.execute(query, (anno, n))

        for row in cursor:
            if row["playerID"] not in result:
                result[row["playerID"]] = [row["teamID"]]
            else:
                result[row["playerID"]].append(row["teamID"])

        cursor.close()
        conn.close()
        return result

