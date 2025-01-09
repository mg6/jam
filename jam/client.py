import binascii
import logging

import jack

from jam.execute import lookup_and_run

logger = logging.getLogger(__name__)


client = jack.Client("jam")
port = client.midi_inports.register("in")


@client.set_process_callback
def process(frames):
    for offset, data in port.incoming_midi_events():
        time = client.last_frame_time + offset
        data_dec = binascii.hexlify(data).decode()

        logger.debug(f"raw midi: time={time} data=0x{data_dec}")
        lookup_and_run(data)
