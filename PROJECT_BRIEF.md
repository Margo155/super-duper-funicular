# Oddplot — production brief, episode 001 test

## Brand and scope

- Channel: **Oddplot**.
- Tagline: **Small Stories. Unexpected Turns.**
- Brand colours: midnight navy #101A32, tangerine orange #FF870D, ivory-white.
- Audience: general-audience English-language curious storytelling, history,
  inventions, science and surprising explanations.
- Full episode: **They Flooded This Vessel on Purpose**.
- Current production: opening **15 seconds only**; the full episode is context.
- Output: portrait 9:16, 30 fps, 450 frames. Render a 540x960 preview first;
  1080x1920 is a later/final-resolution target when practical.

## The approved hero and the new body

`assets/hero_reference.png` is the approved avatar and authoritative reference
for the head: ivory round face, dark side-swept hair, dark oval eyes, raised
expressive eyebrow, small curious smile and simple outlined hands. Read the
actual image; a prose description alone is insufficient for identity matching.

The avatar does not define a complete standing body. For this test, use a
clearly identified working body design: simple navy torso, thin dark limbs,
small dark shoes and an orange life jacket. Keep proportions consistent across
shots. Face and hair should remain recognisable. The orange O ring belongs to
the channel icon; it does not need to travel with the character in the story.

The hero and other human figures are original fictional representations of
crew or witnesses. They do not impersonate named real researchers. Narration
is in the third person; visible lip-sync is not required for this test.

## Image construction

- Volumetric ocean environment, deck, railings, valve and interior sink.
- Flat outlined 2D mascot on a plane or a genuinely flat rig inside that 3D scene.
- Actual camera translation/parallax and consistent perspective.
- Feet attached to the correct local deck surface. Use local coordinates or a
  foot/ground constraint during hull motion; avoid shoe sliding and floating.
- Directional late-afternoon sunlight, cooler ambient fill and legible face.
- Soft, coherent contact shadows under the shoes and cast shadows on props.
- Navy/orange are branding accents; sea and sky can use natural blues.
- A light ocean surface with a simple animated wave representation is enough.
  Keep geometry and materials economical; a heavy fluid simulation is unnecessary.
- Model FLIP as the distinctive long, narrow platform with an inhabited end,
  not as a cruise liner or a generic cargo ship. Use the official references
  in FACTS_AND_SOURCES.md if geometry needs clarification.

## Opening story

Witnesses mistake controlled deployment for a sinking vessel. Crew deliberately
fill ballast tanks. The stern descends and the bow rises. A sideways sink looks
like a construction mistake. The test ends before the complete explanation.
The complete 90-degree transformation and science explanation belong later
in the full episode and should not be forced into these first 15 seconds.

Exterior shots keep the ocean horizon level while the platform pitches.
The inhabited part stays dry; water enters separate ballast tanks. Use a modest
early tilt in the opening. The real operation took approximately half an hour;
the later full-episode transformation must communicate that time compression.

## Narration and sound

Use the exact text in `audio/TEST_15S_VOICEOVER.txt`.
It has 47 spoken words by the preparation tool's tokenization. At a planned
220 words/min, spoken duration is about 12.82 seconds, leaving about 2.18
seconds in a 15-second edit for pauses and visual emphasis. This is an estimate,
not a timed recording. Fit the cut to the actual TTS output.

Voice: clear English, conversational, curious, light irony; readable consonants,
no trailer shouting. A male or female narrator is acceptable for the technical
test; record the choice in RENDER_NOTES.md so the owner can approve a permanent
channel voice later. No real-person voice clone is requested.

The source text is not an existing audio file. Use available TTS or an already
authorised service. State if the voice is a rough offline placeholder. If no
usable voice is available, preserve the scene and name the missing dependency;
do not declare the audiovisual test complete.

Background: restrained ocean wash, a valve click and gentle water noise.
Keep these below intelligible narration. A short comic accent can accompany
the sideways sink. Music is optional for the technical test and must not
obscure speech. Keep an audio-only narration export.

## Captions

- English only; white bold text with a dark stroke.
- Short groups, typically 1–4 words, approximately centred around 70% of frame
  height, adjusted for face/prop visibility and mobile UI.
- Straight horizontal baseline, consistent size and no skew.
- `subtitles/TEST_15S_DRAFT.srt` is a provisional schedule. Align it to the
  actual narration before delivering a file labelled final.

## Deliverables

1. `TEST_001_15s.mp4`, encoded portrait video with audible English narration.
2. `TEST_001_VOICEOVER.wav` or another clearly identified audio format.
3. `TEST_001_SUBTITLES.srt`, aligned to actual narration.
4. Four control frames corresponding to storyboard shots.
5. Editable original scene/project, script/code, required assets and a repeatable
   render/export command.
6. `RENDER_NOTES.md`: installed tools/versions, actual renderer, TTS/voice,
   dimensions, duration, frame count, quality settings and limitations.

Use the current project output folder and save important source changes in its
version history. Keep the original imported reference image unchanged.
