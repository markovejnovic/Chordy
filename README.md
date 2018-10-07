# Chordy

Chordy is a small research project of which the main goal is to create an 
algorithm for identifying triad chords. It is my internal assessment paper for 
the Higher Level Mathematics course for the International Baccalaureate diploma
program.

## Requirements

You need `matplotlib`, `numpy`, `scipy`.

## Getting started

To give the algorithm a spin, clone the repository:
```bash
git clone git@github.com:markovejnovic/Chordy.git
```
Next, add execution privileges to the script
```bash
cd Chordy
chmod +x ./src/plot_chord.py
```

You can use the samples provided in the directory to test the algorithm. The
samples in `outdir/` are mono, whereas, the ones in `Chords/` are stereo. The
algorithm does not work on stereo `.wav`s.

```bash
./src/plot_chord.py ./src/Chords/outdir/NYL-Cmin.wav
```

Or the whole directory
```bash
./src/plot_chord.py ./src/Chords/outdir/
```

## Acknowledgments

* Just [PurpleBooth](https://github.com/PurpleBooth) for showing me how to make a [good README.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) file.


