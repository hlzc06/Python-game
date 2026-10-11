"""Generate original synthetic feedback sounds; no third-party recordings."""
from pathlib import Path
import math, random, struct, wave

def main():
    root = Path(__file__).resolve().parent / 'audio'
    root.mkdir(exist_ok=True)
    rng = random.Random(42)
    for name, duration, frequency, noise in [('chop',.12,180,.6),('wash',1.7,550,.8),('stir',.25,270,.35),('sizzle',.7,900,.85),('success',.65,660,0)]:
        samples = []
        rate = 22050
        for i in range(int(rate*duration)):
            t = i/rate
            envelope = min(1,t/.01) * max(0,1-t/duration)
            freq = frequency * (1 if name != 'success' else [1,1.25,1.5][min(2,int(t/duration*3))])
            value = ((1-noise)*math.sin(2*math.pi*freq*t) + noise*rng.uniform(-1,1)) * envelope * .3
            samples.append(struct.pack('<h',int(value*32767)))
        with wave.open(str(root/(name+'.wav')),'wb') as out:
            out.setparams((1,2,rate,0,'NONE','not compressed'))
            out.writeframes(b''.join(samples))
if __name__ == '__main__':
    main()
