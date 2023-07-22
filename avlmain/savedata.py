import update
import sheets

import cgi
form = cgi.FieldStorage()
with open ('fileToWrite.txt','w') as fileOutput:
    fileOutput.write(form.getValue('email'))
