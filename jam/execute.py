import logging
import subprocess

from jam.config import get_config
from jam.midi import (
    extract_midi_data,
    MidiStatus,
)

logger = logging.getLogger(__name__)
config = get_config()


def lookup_and_run(data):
    status, bank, pitch, velocity = extract_midi_data(data)

    for cmd in commands_by_midi_status(status):

        if "note" in cmd and cmd["note"] != pitch:
            continue

        if "bank" in cmd and cmd["bank"] != bank:
            continue

        dispatch(cmd, status, bank, pitch, velocity)


def commands_by_midi_status(status):
    if status == MidiStatus.NOTE_ON:
        yield from config["on"]["press"]
    elif status == MidiStatus.CONTROL_CHANGE:
        yield from config["on"]["slider"]


def dispatch(cmd, status, bank, pitch, velocity):
    logger.debug(f"dispatching: {cmd}")

    if "log" in cmd:
        msg = cmd["log"].format(status=status, bank=bank, note=pitch, velo=velocity)
        logger.info(f"log: {msg}")

    if "exec" in cmd:
        line = cmd["exec"].format(status=status, bank=bank, note=pitch, velo=velocity)

        logger.info(f"running -> {line}")
        result = subprocess.call(line, shell=True)

        logger.info(f"result  -> {result}")
