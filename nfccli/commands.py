from nfccli import nfc
import time

def read(**kwargs):
    message = None
    while message == None:
        try:
            message = nfc.read_nfctag()
            print('NFC-Tag:{}'.format(message).strip())
        except AssertionError:
            time.sleep(.5)

        if kwargs.get('--continuous'):
            time.sleep(.5)
            message = None


def write(**kwargs):
    successful = False
    while not successful:
        try:
            nfc.write_nfctag(kwargs.get('--string'))
            successful = True
        except AssertionError:
            time.sleep(.5)

        if kwargs.get('--continuous'):
            time.sleep(.5)
            successful = False

