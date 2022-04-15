import unittest

from src.Model.FR_Report import FR_Report
from src.Repository.FR_Report_Repository import FR_Report_Repository


class TestFRReport(unittest.TestCase):

    def test_FR_ReportCreationAndSavingWorks(self):
        objReport = FR_Report()
        objReport.title = "test"
        objReport.date_report = "2022/04/12"

        objRepoReport = FR_Report_Repository()
        self.assertFalse(objRepoReport.exists(objReport))

        objRepoReport.save(objReport)
        self.assertTrue(objRepoReport.exists(objReport))

        objRepoReport.delete(objReport)
        self.assertFalse(objRepoReport.exists(objReport))


if __name__ == '__main__':
    unittest.main()