class Scale:
    _notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    @staticmethod
    def next_to(note):
        """Returns the notes neighboring the argument"""
        index = Scale._notes.index(note)
        if index == 0:
            return [Scale._notes[-1], Scale._notes[1]]
        elif index == -1 or index == len(Scale._notes) - 1:
            return [Scale._notes[-2], Scale._notes[0]]
        else:
            return [Scale._notes[index - 1], Scale._notes[index + 1]]
