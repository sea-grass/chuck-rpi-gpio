.1 => dac.gain;

SinOsc a => dac;

110.0 => a.freq;
0 => a.gain;

for (0 => int i; i < 5; i++) {
    1 => a.gain;
    1::second => now;
    0 => a.gain;
    1::second => now;
}