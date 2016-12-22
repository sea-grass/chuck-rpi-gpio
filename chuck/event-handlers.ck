//Declare an event to use for signalling
Event evt;
Event evt2;

OscIn oin;
6449 => oin.port;

OscMsg msg;

oin.addAddress("/myChucK/OSCNote");

fun void foo(Event anEvent, float freq)
{
    Impulse imp => ResonZ rez => dac;
    50 => rez.Q;
    while (true)
    {
        // wait
        anEvent => now;
        // action
        <<< "Hey!!!", now / second >>>;
        freq => rez.freq;
        50 => imp.next;
    }
}

//snare
spork ~ foo(evt, 900);
//kick
spork ~ foo(evt2, 400);

while (true)
{
    oin => now;
    
    while (oin.recv(msg) != 0)
    {
        msg.getInt(0) => int note;
        msg.getFloat(1) => float velocity;
        msg.getString(2) => string howdy;
        if (note == 0) {
            evt.signal();
        } else {
            evt2.signal();
        }
        <<< howdy, note, velocity >>>;
    }
    
    .1::second => now;
}