import struct


class MidiStatus:
    NOTE_OFF = 0x08
    NOTE_ON = 0x09
    POLYPHONIC_AFTERTOUCH = 0x0A
    CONTROL_CHANGE = 0x0B


def extract_midi_data(data):
    status, pitch, velocity = struct.unpack("3B", data)

    bank = status & 0xF
    status >>= 4

    return status, bank, pitch, velocity
