from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

class ChordWav:
    """Represents a chord wav file used for analysis
    
    Arguments:
        f - path to the actual file
    """
    def __init__(self, f, mono=False):
        self._fs, wav_arr = wavfile.read(f)
        if mono:
            wav_arr_mono = wav_arr
        else:
            wav_arr_mono = []
            wav_arr = wav_arr.T
            for i in range(0, len(wav_arr[0])):
                wav_arr_mono.append((wav_arr[0][i] + wav_arr[1][i]) / 2)
        self._samples = len(wav_arr_mono)
        self._times = np.linspace(0, len(wav_arr_mono) / self._fs, 
                len(wav_arr_mono))
        self._amplitudes = np.array(wav_arr_mono)

    _dft = np.array([])
    def dft(self, force=False):
        if force or self._dft.size == 0:
            self._dft = np.fft.fft(self._amplitudes) / self._samples
            self._dft = self._dft[range(int(self._samples / 2))]
        return self._dft

    _abs_dft_freq = np.array([])
    _abs_dft = np.array([])
    def abs_dft(self, force=False):
        if force or not self._abs_dft.size or not self._abs_dft_freq.size:
            frq = np.arange(self._samples) * self._fs / self._samples
            self._abs_dft_freq = frq[range(int(self._samples / 2))]
            self._abs_dft = abs(self.dft())
        return self._abs_dft_freq, self._abs_dft

    def fft_peaks(self, cutoff=0.30, leway=15):
        """Returns an array at which the frequencies are above the mode of the 
        array returned by self.abs_dft()"""
        x, y = self.abs_dft()
        y = y / np.amax(y) # Normalizes so that the maximum value is 1
        peaks = []
        for i, val in enumerate(y):
            if val > cutoff:
                peaks.append(x[i])

        plt.plot(x, y)
        plt.plot(x, np.full(y.size, cutoff))

        peaks_final = []
        y_final = []
        for peak_a in peaks:
            if not any(np.abs(peak_a - peak_b) < leway 
                    for peak_b in peaks_final):
                peaks_final.append(peak_a)
            else:
                closest_value_index = (np.abs(peaks_final - peak_a)).argmin()
                peaks_final[closest_value_index] = \
                        (peaks_final[closest_value_index] + peak_a) / 2

        return peaks_final, y_final

    def plot(self):
        plt.plot(self._times, self._amplitudes)

    def plot_ft(self):
        x, y = self.abs_dft()
        plt.plot(x, y)
