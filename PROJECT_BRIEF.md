# Oddplot — Episode 002

## Result and scope

Russian subject: **Монетка, которая ускоряет огромные часы**.
Working English title: **A Penny Makes This Giant Clock Run Faster**.
Produce the complete English-language Short. The episode 001 V3 technical test was accepted as the continuity reference; a fourth test of that old episode is not requested.

Master format: 1080x1920, square pixels, progressive, 30 fps, H.264 MP4 with AAC audio. Nominal storyboard: 54.00 seconds / 1620 frames. The measured text has 153 spoken words: at a PLANNED 195 words/minute plus six seconds of visual pauses, the estimate is 53.08 seconds. This is not a recorded performance. Match the final cut to actual voice; 50–60 seconds is acceptable. All final times must fall on the 30 fps frame grid.

## Continuity and appearance

- Channel: Oddplot. Tagline: Small Stories. Unexpected Turns.
- Brand accents: midnight navy #101A32, orange #FF870D, ivory. These do not replace natural lighting or restrict every environment to a single colour.
- Head identity: assets/hero_reference.png. Body, outline, footwear and expressions: assets/continuity/ approved V3 video and extracted PNGs. These are supplied in this package; do not assume another chat is accessible.
- Same ivory rounded face, dark swept hair with tuft, dark oval eyes, navy clothing, orange vest with belt, slim dark limbs and small dark shoes. Keep the existing vest design for continuity; do not redesign the body or add a helmet, moustache or realistic human hands.
- The hero plays an original fictional clock keeper for a visual reconstruction. He is not a named historical person. Third-person narration; lip-sync is not required. Mouth shapes convey reaction rather than following every narrator phoneme.
- Reuse the approved rig if its source is present. Otherwise build a flat articulated rig from these references. Link each shoe to its foot/leg assembly; a planted shoe and its ankle may not separate when a knee bends.
- assets/continuity/ODDPLOT_APPROVED_TEST_001_V3.mp4 is a visual/voice reference, not footage to paste into episode 002. Do not carry the ship, sea, life-saving context or sideways sink into the clock episode.

## Set and props

One economical 3D clock mechanism room inspired by Elizabeth Tower: pale stone/plaster walls, dark painted metal frame, brass/steel gears, clock dial visible from inside, timber or stone floor and warm directional window light. Show believable scale and moving connected parts without claiming an exact engineering survey.

The real pendulum extends into a shaft below the room: show its upper section, fixed pivot and coin shelf, with a guarded cutaway/educational view for the lower portion. Consult the official virtual tour and Royal Mint Museum photo links in FACTS_AND_SOURCES.md. Do not substitute a tabletop grandfather clock for the Westminster mechanism.

Model a small shelf attached to the pendulum's upper visible assembly, above its main lower mass. Coins ride the shelf as the pendulum moves; they are not floating independently. Use several consistent old pre-decimal British pennies, not modern US cents or current UK pennies. A modest bronze coin with a simple original period-inspired relief is sufficient; do not invent a specific rare date or claim an exact numismatic replica.

Minimum useful props: connected pendulum assembly and shelf, a short coin stack, a rigged coin in the hero's hand, two or three meshing gear pairs, recognisable clock dial, keeper's reference watch/logbook, an explanatory graphic for effective length, and a 24-hour rate comparison. Big Ben is the bell; the Great Clock is the mechanism. The bell can be omitted entirely.

## Composition, motion and light

- Motivated dolly/push/side move with real parallax. Static set dressing is fine; the main action must animate. Avoid a single still with a zoom.
- Macro coin opening, medium hero action, wide mechanism, close tray, simplified explanatory view, daily-rate graphic, return to keeper, macro-to-wide closing callback. Detailed anchors are in STORYBOARD.md.
- Feet stay attached to the fixed room floor. Use small weight shifts and blinks; remove automatic looping jumps. Hand follows the coin to the moving shelf, releases on contact, then withdraws.
- Connect gears with opposite rotation at each external mesh; no interpenetrating teeth or independently random rotations. An educational simplified linkage is acceptable. Do not label it an exact reproduction of Denison's escapement.
- Warm side light, cool gentle fill, clean highlights on coins, readable ivory face, coherent floor/contact shadows. Use denoising and sufficient quality to avoid the grain of episode 001 V1. Do not hide details in glare.

## Narration, timing and sound

Use audio/VOICEOVER_EN.txt exactly. Voice should be curious, clear and conversational, with room for the physical explanation and the phrase 'two fifths of a second'. Reuse episode 001's actual narrator/voice ID if its settings exist in the production project. The included V3 audio is a continuity reference, not an authorisation for voice cloning. If that ID is unavailable, choose an already available suitable English voice and record the choice.

The included text is not a recording of episode 002. Generate/record it during production. Export a clean voice track separately. Add a restrained mechanical ambience, soft coin-on-metal clicks, and ticking compatible with the real two-second beat. No rapid ticking change after a penny is added. Optional quiet music should leave the words intelligible.

Allow approximately six seconds total for coin contact, explanatory graphics and the closing expression, distributed through the edit. These are not six seconds of empty silence. Keep the scene alive during holds.

## Captions and callouts

English, 1–4 words per caption, white bold with dark stroke, straight horizontal baseline. At 1080x1920, begin with about 52–60 px type and 4–5 px stroke; fit the actual font and width. Keep essential text within x=0.10–0.88 of frame, centred around y=0.72, rather than V3's low ~0.86 position. Move the hero/props within composition so captions do not obscure the hand/coin or important expression.

Callouts are separate from spoken subtitles: '+0.4 s / day', '24 HOURS', 'TIME COMPRESSED', 'SIMPLIFIED MODEL', 'DIFFERENCE EXAGGERATED', 'ROD LENGTH UNCHANGED', '5 tonnes'. Use only the ones called for by the shot. Do not show metres of rod shortening or a suddenly spinning clock face. Subtitle source and schedule are drafts until aligned to the actual voice.

## Required output

1. output/EPISODE_002_FINAL.mp4 — complete narrated Short, actual 1080x1920 and 30 fps.
2. output/EPISODE_002_VOICEOVER.wav — clean narration, preferably 48 kHz PCM; retain the native export too if converted.
3. output/EPISODE_002_SUBTITLES.srt — final audio-aligned short caption groups.
4. output/control_frames/ — one representative frame from each of the 11 storyboard blocks.
5. output/review_sheets/ — all frames covered, 60 frames per sheet, final partial sheet if required.
6. source/ — editable scene/rig, scripts, materials, needed assets and exact render/edit commands.
7. output/QA_REPORT.json and output/QA_AUDIO_CHECK.txt, plus VISUAL_QA.md with actual checks and corrections.
8. RENDER_NOTES.md — renderer/version, voice/ID, timing, resolution, frame count, settings, limitations, source paths and rerender command.

Do not publish. Report the result honestly if a required renderer or speech dependency is missing, while preserving completed source work.
