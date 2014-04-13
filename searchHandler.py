import blpapi
from optparse import OptionParser


class SearchHandler(object):
    def __init__(self):
        pass


    def search(self,keyword):

        options = parseCmdLine()

        # Fill SessionOptions
        sessionOptions = blpapi.SessionOptions()
        sessionOptions.setServerHost(options.host)
        sessionOptions.setServerPort(options.port)

        print "Connecting to %s:%s" % (options.host, options.port)
        # Create a Session
        session = blpapi.Session(sessionOptions)

        # Start a Session
        if not session.start():
            print "Failed to start session."
            return

        try:
            # Open service to get historical data from
            if not session.openService("//blp/refdata"):
                print "Failed to open //blp/refdata"
                return

            # Obtain previously opened service
            refDataService = session.getService("//blp/refdata")

            # Create and fill the request for the historical data
            request = refDataService.createRequest("HistoricalDataRequest")
            request.getElement("securities").appendValue(keyword + " US Equity")

            request.getElement("fields").appendValue("PX_LAST")
            request.getElement("fields").appendValue("OPEN")
            request.set("periodicityAdjustment", "ACTUAL")
            request.set("periodicitySelection", "MONTHLY")
            request.set("startDate", "20060101")
            request.set("endDate", "20061231")
            request.set("maxDataPoints", 100)

            print "Sending Request:", request
            # Send the request
            session.sendRequest(request)
            with open('example.txt', 'w') as the_file:

                # Process received events
                while(True):
                    # We provide timeout to give the chance for Ctrl+C handling:
                    ev = session.nextEvent(500)
                    for msg in ev:
                        the_file.writable(msg+"\n")

                if ev.eventType() == blpapi.Event.RESPONSE:
                    # Response completly received, so we could exit
                    break
        finally:
            # Stop the session
            session.stop()


def parseCmdLine():
    parser = OptionParser(description="Retrieve reference data.")
    parser.add_option("-a",
                      "--ip",
                      dest="host",
                      help="server name or IP (default: %default)",
                      metavar="ipAddress",
                      default="localhost")
    parser.add_option("-p",
                      dest="port",
                      type="int",
                      help="server port (default: %default)",
                      metavar="tcpPort",
                      default=8194)

    (options, args) = parser.parse_args()
    return options