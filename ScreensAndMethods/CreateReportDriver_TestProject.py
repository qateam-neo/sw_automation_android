import os
from pathlib import Path
from src.testproject.sdk.drivers import webdriver
def CreateReportDriver():
    while True:
        try:
            ReportDriver = webdriver.Chrome(token="pmJdhcUa9d1tA5a4Z1FA4uMOYjBjCKmY7b_ersaf0TY1",report_path=os.getcwd()+"\Reports",project_name=Path(__file__).stem ,report_name=Path(__file__).stem ,job_name=Path(__file__).stem)
            ReportDriver.report().disable_auto_test_reports(disabled=True)
            ReportDriver.close()
            print("Report driver Created")
            break
        except:
            print("Error in Running ReportDriver")
