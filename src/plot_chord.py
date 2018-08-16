#!/usr/bin/python
"""This script plots the played chord and its rFFT"""

from chord_wav import ChordWav
import sys
import matplotlib.pyplot as plt
from note_identifier import NoteIdentifier
from chord_identifier import ChordIdentifier
from os import listdir, path
from numpy import linspace

if __name__ == "__main__":
    if '-r' in sys.argv:
        success_rates = []
        cutoff_values = []
        for i in linspace(0.02, 0.8, 25):
            print('Trying cutoff value of ' + str(i))
            success_rate = 0
            counter = 0
            for f in listdir(sys.argv[-1]):
                if not f.endswith('.wav'):
                    continue
                counter += 1
                chord_wav = ChordWav(path.join(sys.argv[-1], f), mono=True)
                peaks, heights = chord_wav.fft_peaks(cutoff=i)
                notes = []
                uncertainties = []
                for peak in peaks:
                    fn, unc = NoteIdentifier.identify(peak)
                    notes.append(fn)
                    uncertainties.append(unc)
                ch, unc = ChordIdentifier.identify(notes, uncertainties)
                print('Identified file ' + str(f) + ' as a ' + str(ch) + 
                        ' with ' + str(unc) + ' uncertainty.')
                if ch['name'] == f[4:-4]:
                    success_rate += 1
            cutoff_values.append(i)
            success_rates.append(success_rate / counter)
            print(cutoff_values)
            print(success_rates)
        
        print('Final')
        print(cutoff_values)
        print(success_rates)
    else:
        chord_wav = ChordWav(sys.argv[-1], mono=True)
        peaks, heights = chord_wav.fft_peaks()
        notes = []
        uncertainties = []
        for peak in peaks:
            fn, unc = NoteIdentifier.identify(peak)
            notes.append(fn)
            uncertainties.append(unc)
        
        ch, unc = ChordIdentifier.identify(notes, uncertainties)
        print(ch)
        print(unc)
