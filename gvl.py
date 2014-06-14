#!/usr/bin/python3
from itertools import islice


KEYS = {'C major': {'1': 'C', '2': 'D', '3': 'E', '4': 'F', '5': 'G', '6': 'A', '7': 'B'},
        'C melodic minor': {'1': 'C', '2': 'D', '3': 'E♭', '4': 'F', '5': 'G', '6': 'A', '7': 'B'},
        'C harmonic minor': {'1': 'C', '2': 'D', '3': 'E♭', '4': 'F', '5': 'G', '6': 'A♭', '7': 'B'}}

_STD_FORMAT = '↘  {:<2}↘  {:<2}↘  {:<2}↘  {:<2}↘  {:<2}↘  {:<2}↘  {:<2}↘'
'''
 C major scale
 triads
 cycle 2 - MSRP (Melodic Strand Replication Procedure)
  𝄆 CAG FDC BGF ECB AFE DBA GED 𝄇
   ↓        ↓        ↓
   1        5        3

 If triad is stacked 1-3-5 (closed voicing) from bottom
 to top, start reading the sequence to generate desired
 output.  Sequence can also be produced from triad stacked
 1-5-3 (spread voicing)
 Note: Only the MSRP changes for the different cycles
'''
MSRP = {'triad': {'cycle2': '165421754317643276532',
                  'cycle3': '177766655544433322211',
                  'cycle4': '112334556771223445667',
                  'cycle5': '176654432217765543321',
                  'cycle6': '111222333444555666777',
                  'cycle7': '123567234671345712456'}}


def generate_voice_lead(the_key, cycle, starting_degree):
    if starting_degree == 'root':
        start, end = 0, 7
    elif starting_degree == 'fifth':
        start, end = 7, 14
    elif starting_degree == 'third':
        start, end = 14, 21
    else:
        raise ValueError('unknown starting degree')
    fragment = islice(MSRP['triad'][cycle], start, end)
    return [KEYS[the_key][c] for c in fragment]


def pretty_print(the_key, cycle, voicing_type):
    if voicing_type == 'close':
        print(('║ ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'fifth')))
        print(('║:' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'third')))
        print(('║ ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'root')))
        print()
        print(('  ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'third')))
        print(('  ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'root')))
        print(('  ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'fifth')))
        print()
        print(('  ' + _STD_FORMAT + '  ║').format(*generate_voice_lead(the_key, cycle, 'root')))
        print(('  ' + _STD_FORMAT + ' :║').format(*generate_voice_lead(the_key, cycle, 'fifth')))
        print(('  ' + _STD_FORMAT + '  ║').format(*generate_voice_lead(the_key, cycle, 'third')))
    elif voicing_type == 'spread':
        print(('║ ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'third')))
        print(('║:' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'fifth')))
        print(('║ ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'root')))
        print()
        print(('  ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'root')))
        print(('  ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'third')))
        print(('  ' + _STD_FORMAT).format(*generate_voice_lead(the_key, cycle, 'fifth')))
        print()
        print(('  ' + _STD_FORMAT + '  ║').format(*generate_voice_lead(the_key, cycle, 'fifth')))
        print(('  ' + _STD_FORMAT + ' :║').format(*generate_voice_lead(the_key, cycle, 'root')))
        print(('  ' + _STD_FORMAT + '  ║').format(*generate_voice_lead(the_key, cycle, 'third')))
    else:
        raise ValueError('Unknown voicing type requested')

if __name__ == '__main__':
    print('C Major triads, Cycle 2, Close Voicings')
    pretty_print('C major', 'cycle2', 'close')
    print()
    print('C Major triads, Cycle 2, Spread Voicings')
    pretty_print('C major', 'cycle2', 'spread')
    print()
    print('C Harmonic Minor, Cycle 2, Spread Voicings')
    pretty_print('C harmonic minor', 'cycle2', 'spread')
