from scale import Scale

class ChordIdentifier:
    _chords = [
            {
                'name': 'Cmaj',
                'notes': ['C', 'E', 'G']
            },
            {
                'name': 'Cmin',
                'notes': ['C', 'D#', 'G']
            },
            {
                'name': 'C#maj',
                'notes': ['C#', 'F', 'G#']
            },
            {
                'name': 'C#min',
                'notes': ['C#', 'E', 'G#']
            },
            {
                'name': 'Dmaj',
                'notes': ['D', 'F#', 'A']
            },
            {
                'name': 'Dmin',
                'notes': ['D', 'F', 'A']
            },
            {
                'name': 'D#maj',
                'notes': ['D#', 'G', 'A#']
            },
            {
                'name': 'D#min',
                'notes': ['D#', 'F#', 'A#']
            },
            {
                'name': 'Emaj',
                'notes': ['E', 'G#', 'B']
            },
            {
                'name': 'Emin',
                'notes': ['E', 'G', 'B']
            },
            {
                'name': 'Fmaj',
                'notes': ['F', 'A', 'C']
            },
            {
                'name': 'Fmin',
                'notes': ['F', 'G#', 'C']
            },
            {
                'name': 'F#maj',
                'notes': ['F#', 'A#' 'C#']
            },
            {
                'name': 'F#min',
                'notes': ['F#', 'A', 'C#']
            },
            {
                'name': 'Gmaj',
                'notes': ['G', 'B', 'D']
            },
            {
                'name': 'Gmin',
                'notes': ['G', 'A#', 'D']
            },
            {
                'name': 'G#maj',
                'notes': ['G#', 'C', 'D#']
            },
            {
                'name': 'G#min',
                'notes': ['G#', 'B', 'D#']
            },
            {
                'name': 'Amaj',
                'notes': ['A', 'C#', 'E']
            },
            {
                'name': 'Amin',
                'notes': ['A', 'C', 'E']
            },
            {
                'name': 'A#maj',
                'notes': ['A#', 'D', 'F']
            },
            {
                'name': 'A#min',
                'notes': ['A#', 'C#', 'F']
            },
            {
                'name': 'Bmaj',
                'notes': ['B', 'D#', 'F#']
            },
            {
                'name': 'Bmin',
                'notes': ['B', 'D', 'F#']
            }
    ]

    @staticmethod
    def identify(o_notes, o_uncertainty):
        """Tries to identify which chord is being played
        Returns:
            (str) - the chord being played
        """
        o_notes = [i[1][:-1] for i in o_notes]
        chord_certainties = []
        for chord in ChordIdentifier._chords:
            counter = 0
            certainty = 0

            for i, note in enumerate(o_notes):
                if note in chord['notes']:
                    certainty += 1 - o_uncertainty[i]
                elif any(v in chord for v in Scale.next_to(note)):
                    certainty += o_uncertainty[i]

                counter += 1

            chord_certainties.append(certainty / counter)

        return ChordIdentifier._chords[chord_certainties.index(
            max(chord_certainties))], max(chord_certainties)
