# Debugging update

- Fixed Herbal recipe slot overflow and missing herb texture mapping. Both recipes now use three correct ingredients plus one distractor. Herbal uses mushroom, potato and herbs; Spicy uses beetroot, carrot and potato.
- Resolved asset working directory independently of where the Python launch command starts.
- Recalculated quality from score components, preventing replay accumulation. Replaying preparation clears cooking and plating; replaying cooking clears plating.
- Corrected preparation bonus so nine successful chops can achieve 40/40.
- Gated cooking progress and completion on all three ingredients; Enter requires full progress.
- Cooking score uses measured ideal-heat time instead of treating completed progress as proof of correct heat.
- Corrected mouse stirring by accumulating wrapped signed angle changes within the pan radius and clearing completed gestures. S remains the accessible alternative.
- Removed duplicate stirring method and retained the state check.
- Preserved burn status in shared game state for future visual improvements.
- Corrected plating cleanup bonus so three spills can achieve 30/30.
- Removed invented fallback results values; score bars use correct raw maximums and can show zero.
- Replaced global scheduled results callback with a per-view countdown, avoiding an abandoned view's timer changing state.
- Normalised diagonal carry speed and added subtle movement bobbing while retaining the carrying pose.
- Added synthetic interaction WAVs, quiet looping background music and M-key mute; audio is optional and missing files are tolerated.
- Added pinned dependency and setup/control/audio instructions.

## Validation

Python syntax compilation passed. Logic checks passed for perfect total, replay replacement, ingredient gating, measured heat scoring, burn detection and duplicate methods. Arcade 3.3.3 created and rendered all four views. Both recipe routes were programmatically completed and rendered through plating, carrying, completion and results, reaching the expected scores. Included sound loading/playback and mute toggling passed with a null audio driver.

Rendering used an offscreen graphics context. The Linux headless test harness disabled joystick discovery to work around a pyglet headless input error; no joystick workaround was added to the game. This is not a manual mouse/keyboard playthrough and does not establish speaker quality on Windows. Play both routes on the target laptop, deliberately mistime chops, burn food, replay stages and mute/unmute before submission.

## Scope

These are targeted fixes to the existing Arcade implementation. The separate HTML prototype remains unchanged. New recipe-specific effects, new dish artwork, serving balance obstacles and the proposed crystal finale are future group implementation tasks. Synthetic audio may be replaced with recordings. Narrative/storyboard and individual reports were not rewritten.
