import cherrypy

from src.CCC.WebApp import WebApp, CherryPyExposure
from src.Repository.FR_Report_Repository import FR_Report_Repository


# ======================================================================================================================
class MyCherryPyThread(CherryPyExposure):
    def __init__(self, pObjRESTfulService):
        super().__init__(pObjRESTfulService)
        self.repoReport = FR_Report_Repository()

    @cherrypy.expose
    def index(self):
        # return open('Web/index.html')
        return "Welcome to Web ForeRunner Engine"


# ======================================================================================================================
@cherrypy.expose
class MyCherryPyRestService:
    def __init__(self):
        self.repoReport = FR_Report_Repository()

    @cherrypy.tools.accept(media='text/plain')
    def POST(self):
        return "POST"

    @cherrypy.tools.accept(media='text/plain')
    def GET(self, keyword="", tail=""):
        if tail == "":
            objQueryResults = self.repoReport.searchInTitle(keyword)
            return str(objQueryResults)
        else:
            objQueryResults = self.repoReport.searchInTitleLatest(keyword, int(tail))
            return str(objQueryResults)

    def PUT(self):
        return "PUT"

    def DELETE(self):
        return "DELETE"


# ======================================================================================================================
class WebAppFR_Engine(WebApp):
    # Class attributes
    idx_my_model = None

    def __init__(self):
        super().__init__(strThreadName="AppMyCherryPyTest", objWebappExposure=MyCherryPyThread(MyCherryPyRestService()))

    def load(self):
        print("Welcome to Web Blowgun Engine")

    def on_manage(self, param1=None):
        self.is_running = False
