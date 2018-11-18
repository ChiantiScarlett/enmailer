from os import popen


class ENMailer:
    def __init__(self):
        self._subject = ""
        self._dispatcher = ""
        self._recipient = None

        self._contents = ""
        self._tags = []
        self._sendmail_path = '/usr/sbin/sendmail'
        self._notebook = None

    def set_recipient(self, recipient):
        """Set Recipient"""
        pass

    def set_dispatcher(slef, dispatcher):
        """Set Sender"""
        pass

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
        process = popen("{} -t".format(self._sendmail_path), 'w')
        process.write("From: {}\n".format(self._recipient))
        process.write("To: {}\n".format(self._recipient))
        process.write("Subject: {}\n".format(self._subject))
        process.write("\n")

        process.write(self._contents)

        status = process.close()
        if not status:
            print("[*] Successfully sent the mail.")
        else:
            print("[*] Sendmail :: status {}".format(status))
