import sys
import os

class Notifications:
    def funcname(self):
        pass

    def sendEmail(self,mails,issue,message):
        for mail in mails:
            comando = "echo " + issue + " | mail -s \"" + message + "\" " + mail
            os.system(comando)
        return 0