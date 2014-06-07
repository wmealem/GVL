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

 If triad is stacked 1-3-5 from bottom to top, start
 reading the sequence to generate desired output
'''
MSRP = {'cycle2': 'CAGFDCBGFECBAFEDBAGED'}


def generate_voice_lead(starting_degree):
    if starting_degree == 'root':
        return islice(MSRP['cycle2'], 0, 7)
    elif starting_degree == 'fifth':
        return islice(MSRP['cycle2'], 7, 14)
    elif starting_degree == 'third':
        return islice(MSRP['cycle2'], 14, 21)
    else:
        raise ValueError('unknown starting degree')


def pretty_print():
    print('↘  ' + ' ↘  '.join(generate_voice_lead('fifth')) + ' ↘  ')
    print('↘  ' + ' ↘  '.join(generate_voice_lead('third')) + ' ↘  ')
    print('↘  ' + ' ↘  '.join(generate_voice_lead('root')) + ' ↘  ')

if __name__ == '__main__':
    pretty_print()
