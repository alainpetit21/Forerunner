import hashlib
import os
import os.path
import sqlite3

from src.CCC.Singleton import Singleton
from src.Model.FR_Report import FR_Report


@Singleton
class FR_Report_Repository:
    def __init__(self):
        if not (os.path.isfile('./data/forerunner.db')):
            connForerunner = sqlite3.connect('./data/forerunner.db')
            cursor = connForerunner.cursor()

            objReportFake = FR_Report()
            cursor.execute("CREATE TABLE Report (" + objReportFake.getReportDatabaseDefinitionList() + ");")
            connForerunner.commit()
            connForerunner.close()

    def _convertRowToReport(self, row) -> FR_Report:
        objReport = FR_Report()
        objReport.loadFromList(row)
        return objReport

    def exists(self, objReport: FR_Report) -> bool:
        hashStr = objReport.getProductID()

        connection = sqlite3.connect('./data/forerunner.db')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Report WHERE product_id = '" + hashStr + "'")
        lstRows = cursor.fetchall()

        return len(lstRows) > 0

    def save(self, objReport: FR_Report):
        objReport.title = objReport.title.replace('"', '\"')
        objReport.title = objReport.title.replace("'", "\'")

        objReport.getProductID()
        strCommand = 'REPLACE INTO Report (' + ', '.join(objReport.getReportDefinitionList()) + ')' \
                     ' VALUES ("' + '", "'.join(objReport.getReportValuesList()) + '");'

        connection = sqlite3.connect('./data/forerunner.db')
        cursor = connection.cursor()
        cursor.execute(strCommand)
        connection.commit()
        connection.close()

    def delete(self, objReport: FR_Report):
        strProductID = objReport.getProductID()
        strCommand = 'DELETE From Report WHERE product_id = "' + strProductID + '";'

        connection = sqlite3.connect('./data/forerunner.db')
        cursor = connection.cursor()
        cursor.execute(strCommand)
        connection.commit()
        connection.close()

    def searchInTitle(self, searchTerm: str) -> list:
        connection = sqlite3.connect('./data/forerunner.db')
        cursor = connection.cursor()
        sqlCommand = 'SELECT * FROM Report WHERE title LIKE "%' + searchTerm + '%"'
        cursor.execute(sqlCommand)
        lstRows = cursor.fetchall()

        results = []
        for row in lstRows:
            results.append(self._convertRowToReport(row))

        return results

    def searchInTitleLatest(self, searchTerm: str, nTailRecords: int) -> list:
        pass

    def findByProductID(self, strProductID: str) -> FR_Report:
        connection = sqlite3.connect('./data/forerunner.db')
        cursor = connection.cursor()
        sqlCommand = 'SELECT * FROM Report WHERE product_id = "' + strProductID + '"'
        cursor.execute(sqlCommand)
        lstRows = cursor.fetchall()

        return self._convertRowToReport(lstRows[0])
