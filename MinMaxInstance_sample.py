import adminfunctions

#Parameters
AGSRestEndpoint = "http://myserver.mysite.com/arcgis/rest"
username = "admin"
password = "admin"

###Script execution - Where functions are executed.
endpoints = adminfunctions.defineEndpoints(AGSRestEndpoint)
token = adminfunctions.getToken(endpoints["TokenUrl"],username,password)["token"]

services = adminfunctions.getServiceAdminEndpoints(endpoints["Admin"], token)
for service in services:
    print "Editing " + service + "..."
    result = adminfunctions.updateMinMaxInstance(service,token,0,2)
    print result
    print ""
