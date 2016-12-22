SinOsc s;

s => dac;

.2 => s.gain;

400 => s.freq;

[400, 500, 300, 400, 500] @=> int freqs[];
0 => int i;
while (true) {
    freqs[i] => s.freq;
    .5::second => now;
    
    i++;
    if (i >= freqs.cap()) 0 => i;
}