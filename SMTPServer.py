import smtpd
import asyncore


class FakeSMTPServer(smtpd.SMTPServer):
    # Code from https://stackoverflow.com/questions/24270715 #
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)

    def process_message(*args, **kwargs):
        pass


if __name__ == "__main__":
    smtp_server = FakeSMTPServer(('localhost', 25), None)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        smtp_server.close()
