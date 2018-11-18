import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


class ENMailer:
    def __init__(self):
        self._subject = ""
        self._dispatcher = None
        self._recipient = None

        self._contents = ""
        self._tags = []
        self._sendmail_path = '/usr/sbin/sendmail'
        self._notebook = None

    def set_notebook(self, notebook):
        self._notebook = notebook

    def set_recipient(self, recipient):
        """Set Recipient"""
        self._recipient = recipient

    def set_dispatcher(self, dispatcher):
        """Set Sender"""
        self._dispatcher = dispatcher

    def set_title(self, title):
        """ Set Title """
        self._subject = title

    def write(self, contents):
        """ Write contents """
        self._contents += contents

    def confirm(self):
        """ Confirm the setting before processing """
        pass

    def send(self):

        msg = MIMEMultipart()
        msg['From'] = self._dispatcher
        msg['To'] = self._recipient
        msg['Subject'] = self._subject

        body = self._contents
        msg.attach(MIMEText(body, 'plain'))

        # filename = "NAME OF THE FILE WITH ITS EXTENSION"
        # attachment = open("PATH OF THE FILE", "rb")

        # part = MIMEBase('application', 'octet-stream')
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition',
        #                 "attachment; filename= %s" % filename)

        # msg.attach(part)

        server = smtplib.SMTP('localhost', 25)
        server.sendmail(self._dispatcher, self._recipient, msg.as_string())
        server.quit()
