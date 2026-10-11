# AuraTable

Interactive dining experience with four Python Arcade scenes.

## Setup

Use Python 3.12. In the extracted project folder run:

```sh
python -m pip install -r requirements.txt
python main.py
```

In VS Code select your Python 3.12 interpreter and open `main.py` to run.
Arcade 3.3.3 was used for the automated rendering checks.

## Controls

Follow the on-screen hints. Welcome: move using the shown keys, interact and choose a meal. Preparation: drag ingredients to the sink, then the board; press Space or click the board when the timing indicator is green. Cooking: click all three ingredient tokens, use Left/Right to control heat, use S or circle the mouse near the pan to stir. Reach 100% cooking progress, then press Enter. Plating: drag food and garnish, wipe spills with the cloth, press Enter to carry; use arrows/WASD and press E near Sol. Results: R to restart, Escape to exit. Press M in any scene to toggle audio.

## Audio

Included WAV files are original synthetic placeholders, not realistic recordings. Replace files in `audio/` with your own WAV clips using these names:

- `background.wav`: looping music or ambience
- `chop.wav`: knife/chopping
- `wash.wav`: running water
- `stir.wav`: stirring/utensil
- `sizzle.wav`: ingredient entering hot pan
- `success.wav`: completion chime

Audio is optional: missing files or unavailable sound devices do not prevent play. Keep background loops seamless and use short effects. M controls both music and effects.
`generate_placeholder_audio.py` regenerates interaction placeholders and overwrites matching files; do not run it after adding your own recordings.

## Scores

Welcome contributes 20 (Spicy) or 15 (Herbal), preparation up to 40, cooking up to 30 (from a raw /40 score), and plating up to 10 (from a raw /30 score). Spicy can reach 100; Herbal can reach 95 because the existing story gives Sol a preference for the warming spicy meal. Replay replaces scene scores and clears later scores.

## Project versions and assets

`main.py` runs the Arcade project. `index.html` is an independent browser prototype; its code and audio are separate and were not changed in this debugging update.
See `ASSET_INDEX.md` for existing assets. Keep the group's original asset sources, licensing/attribution records and AI Declaration Log; the source archive does not establish ownership or licences for all images.

Read `FIXES.md` for the changes and validation limits. Review and understand the fixes as a group before submission.
