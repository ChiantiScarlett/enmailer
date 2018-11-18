import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from os import path


class ENMailer:
    def __init__(self, **kwargs):
        self._subject = kwargs.get('title', None)
        self._dispatcher = kwargs.get('dispatcher', None)
        self._recipient = kwargs.get('recipient', None)
        self._contents = kwargs.get('contents', "")
        self._tags = kwargs.get('tags', [])
        self._notebook = kwargs.get('notebook', None)
        self._SMTP_host = kwargs.get('SMTP_host', 'localhost')
        self._SMTP_port = kwargs.get('SMTP_port', 25)
        self._attachments = []

    def send(self):
        message = MIMEMultipart()
        message['From'] = self._dispatcher
        message['To'] = self._recipient

        # Set notebook destination and tags if necessary.
        title = [self._subject]
        title.append('@' + self._notebook) if self._notebook else None
        title += list(" #" + tag for tag in self._tags)
        message['Subject'] = "".join(title)

        body = self._contents
        message.attach(MIMEText(body, 'plain'))

        # Attach file if necessary.
        for filepath in self._attachments:
            filename = path.basename(filepath)
            fp = open(filepath, 'rb')

            part = MIMEBase('application', 'octet-stream')
            part.set_payload((fp).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename= {}'.format(filename))

            message.attach(part)

        # Send mail via local `sendmail` using `self._SMTP_port`
        server = smtplib.SMTP(self._SMTP_host, self._SMTP_port)
        server.sendmail(self._dispatcher,
                        self._recipient, message.as_string())
        server.quit()

    def attach(self, filepath):
        self._attachments.append(filepath)

    def add_tag(self, tag):
        self._tags.append(tag)

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
