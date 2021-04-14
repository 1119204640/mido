import mido
from mido import Message, MidiFile, MidiTrack, MetaMessage

bpm = 105
tempo = mido.bpm2tempo(bpm)
meta_time = MetaMessage('time_signature', numerator=6, denominator=8)
meta_tempo = MetaMessage('set_tempo', tempo = tempo, time=0)
meta_tone = MetaMessage('key_signature', key='C')

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0):
   meta_time = 60 * 60 * 10 / bpm
   major_notes = [0, 2, 2, 1, 2, 2, 2, 1]
   base_note = 60
   track.append(Message('note_on', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
   track.append(Message('note_off', note=base_note + base_num*12 + sum(major_notes[0:note]), velocity=round(64*velocity), time=round(meta_time*length), channel=channel))
    
#前奏
def prelude():
    play_note(1, 3, track, velocity=0)
    play_note(5, 3, track, -1)
    
    play_note(1, 3, track, velocity=0)
    play_note(5, 3, track, -1)

    play_note(1, 3, track, velocity=0)
    play_note(4, 3, track, -1)

    play_note(1, 3, track, velocity=0)
    play_note(5, 3, track, -1)

    play_note(1, 3, track, velocity=0)
    play_note(5, 3, track, -1)

    play_note(1, 3, track, velocity=0)
    play_note(4, 3, track, -1)

    play_note(1, 3, track, velocity=0)
    play_note(4, 3, track, -1)

    play_note(1, 3, track, velocity=0)
    play_note(4, 3, track, -1)

    play_note(1, 3, track, velocity=0)
    play_note(5, 3, track, -1)

    play_note(1, 6, track, velocity=0)

#主歌
def precorus():
    play_note(5, 3, track, -1)
    play_note(1, 3, track, velocity=0)

    play_note(1, 42, track, velocity=0)

    play_note(5, 3, track, -1)
    play_note(1, 3, track, velocity=0)

    play_note(1, 42, track, velocity=0)

#副歌
def corus():
    play_note(1, 54, track, velocity=0)

#尾奏
def postlude():
    play_note(1, 12, track, velocity=0)

    play_note(1, 6, track, velocity=0)

    play_note(1, 6, track)

    play_note(1, 6, track, velocity=0)

def verse(track):
    prelude()
    precorus()
    corus()
    corus()
    postlude()
    
verse(track)  

mid.save('chord_3.mid')