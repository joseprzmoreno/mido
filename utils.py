import mido
import time
from mido import MidiFile, MidiTrack, Message
import threading
import uuid

def play_seq(instrument, times, notes, durs, vels):

    output_port = get_port(instrument)
    output_port = mido.open_output(output_port)
    count = 0
    events = build_events(times, notes, durs, vels)

    try:
        for event in events:
            print(event)
            msg = Message(event['type'], note=event['note'], velocity=event['vel'])
            output_port.send(msg)
            if count == len(events) - 1:
                waiting_time = 0
            else:
                waiting_time = events[count + 1]['t'] - event['t']
            time.sleep(waiting_time)
            count += 1

    except KeyboardInterrupt:
        pass

    finally:
        output_port.close()

def orchestrate(funs):
    threads = []
    for fun in funs:
        threads.append(threading.Thread(target=fun))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def get_port(instrument):
    for port_name in mido.get_output_names():
        if instrument in port_name:
         return port_name
    return None

def build_events(times, notes, durs, vels):
    events = []
    for i in range(0, len(times)):
        if isinstance(notes[i], list):
            for note in notes[i]:
                events.append({'type': 'note_on', 'note': note, 'vel': vels[i], 't': times[i]})
                events.append({'type': 'note_off', 'note': note, 'vel': vels[i], 't': float(times[i]) + float(durs[i])})   
        else:
            events.append({'type': 'note_on', 'note': notes[i], 'vel': vels[i], 't': times[i]})
            events.append({'type': 'note_off', 'note': notes[i], 'vel': vels[i], 't': float(times[i]) + float(durs[i])})
    events = sorted(events, key=lambda x: x["t"])
    return events