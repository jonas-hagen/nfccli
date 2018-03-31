from smartcard.scard import *


def connect_nfctag():
    hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)
    assert hresult == SCARD_S_SUCCESS
    hresult, readers = SCardListReaders(hcontext, [])
    assert len(readers) > 0
    reader = readers[0]
    hresult, hcard, dwActiveProtocol = SCardConnect(
        hcontext,
        reader,
        SCARD_SHARE_SHARED,
        SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1,
    )
    return hresult, hcard, dwActiveProtocol


def read_nfctag():
    hresult, hcard, dwActiveProtocol = connect_nfctag()
    assert 0 != hcard, 'No card available'
    response = []
    for i in range(4):
        hresult, _response = SCardTransmit(
            hcard,
            dwActiveProtocol,
            [0xFF, 0xB0, 0x00, 0x04 + 4 * i, 0x10],
        )
        response += filter(lambda x: 0 < x < 128, _response)
    response = ''.join(map(chr, response))
    assert response != 'c' * len(response)
    return response


def write_nfctag(message):
    hresult, hcard, dwActiveProtocol = connect_nfctag()
    assert 0 != hcard, 'No card available'
    for i in range(len(message) / 16 + int(len(message) % 16 != 0)):
        message_part = message[16*i:16*(i+1)]
        message_part = message_part + " " * (16 - len(message_part))
        data = map(ord, message_part)
        hresult, _response = SCardTransmit(
            hcard,
            dwActiveProtocol,
            [0xFF, 0xD6, 0x00, 0x04 + 4*i, 0x10] + data,
        )
