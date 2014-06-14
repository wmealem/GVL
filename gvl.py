#!/usr/bin/python3
from itertools import islice


KEYS = {'C major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
        'C melodic minor': ['C', 'D', 'E♭', 'F', 'G', 'A', 'B'],
        'C harmonic minor': ['C', 'D', 'E♭', 'F', 'G', 'A♭', 'B']}
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
MSRP = {'triad': {'cycle2': 'CAGFDCBGFECBAFEDBAGED',
                  'cycle3': 'CBBBAAAGGGFFFEEEDDDCC',
                  'cycle4': 'CCDEEFGGABBCDDEFFGAAB',
                  'cycle5': 'CBAAGFFEDDCBBAGGFEEDC',
                  'cycle6': 'CCCDDDEEEFFFGGGAAABBB',
                  'cycle7': 'CDEGABDEFABCEFGBCDFGA'}}


def generate_voice_lead(cycle, starting_degree):
    if starting_degree == 'root':
        return islice(MSRP['triad'][cycle], 0, 7)
    elif starting_degree == 'fifth':
        return islice(MSRP['triad'][cycle], 7, 14)
    elif starting_degree == 'third':
        return islice(MSRP['triad'][cycle], 14, 21)
    else:
        raise ValueError('unknown starting degree')


def pretty_print(cycle, voicing_type):
    if voicing_type == 'close':
        print('║ ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'fifth'))))
        print('║:↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'third'))))
        print('║ ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'root'))))
        print()
        print('  ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'third'))))
        print('  ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'root'))))
        print('  ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'fifth'))))
        print()
        print('  ↘  {} ↘  ║'.format(' ↘  '.join(generate_voice_lead(cycle, 'root'))))
        print('  ↘  {} ↘ :║'.format(' ↘  '.join(generate_voice_lead(cycle, 'fifth'))))
        print('  ↘  {} ↘  ║'.format(' ↘  '.join(generate_voice_lead(cycle, 'third'))))
    elif voicing_type == 'spread':
        print('║ ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'third'))))
        print('║:↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'fifth'))))
        print('║ ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'root'))))
        print()
        print('  ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'root'))))
        print('  ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'third'))))
        print('  ↘  {} ↘'.format(' ↘  '.join(generate_voice_lead(cycle, 'fifth'))))
        print()
        print('  ↘  {} ↘  ║'.format(' ↘  '.join(generate_voice_lead(cycle, 'fifth'))))
        print('  ↘  {} ↘ :║'.format(' ↘  '.join(generate_voice_lead(cycle, 'root'))))
        print('  ↘  {} ↘  ║'.format(' ↘  '.join(generate_voice_lead(cycle, 'third'))))
    else:
        raise ValueError('Unknown voicing type requested')

if __name__ == '__main__':
    print('C Major triads, Cycle 2, Close Voicings')
    pretty_print('cycle2', 'close')
    print()
    print('C Major triads, Cycle 2, Spread Voicings')
    pretty_print('cycle2', 'spread')
