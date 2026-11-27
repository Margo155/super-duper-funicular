# Facts, source map and animation guardrails

Checked for this handoff: 26 November 2026. These are paraphrased factual notes, not a licence to reuse the sources' photographs, audio or narration.

## Primary and official references

### S1 — UK Parliament: Great Clock facts
https://www.parliament.uk/about/living-heritage/building/palace/big-ben/facts-figures/great-clock-facts/

Supports: four clock dials; mechanism about five tonnes; pendulum physical length 4.4 m; a beat lasts two seconds; adding an old pre-decimal penny gives approximately +0.4 seconds per 24 hours. Do not confuse that with a 0.4-second correction per swing.

### S2 — UK Parliament: Great Clock adjustments, 25 August 2015
https://www.parliament.uk/business/news/news-by-year/2015/august/great-clock-adjustments/

Supports adjustment through old penny weights and the change in rate when they are added/removed. The text describes reducing pendulum length; our spoken explanation uses **effective** length. It does not show someone sawing or telescoping the rod. Do not present the article's dated accuracy measurements as a measurement made today.

### S3 — UK Parliament: Audio Transcripts
https://www.parliament.uk/visiting/online-tours/virtualtours/bigben-tour/big-ben-podcast/

The clock-keeper interview describes adding a penny to speed the rate and removing one to slow it. It also identifies Big Ben as the Great Bell. We paraphrase the practice; no interview quotation or original recording is included or requested for reuse.

### S4 — UK Parliament: Elizabeth Tower virtual tour
https://virtualtours-assets.parliament.uk/elizabeth-tower/index.html

Mechanism Room / Pendulum / Clock mechanics' log book: layout and mechanical context; top of the pendulum visible in the room, remainder below in a shaft; coins used on the pendulum. Use as geometric guidance, not as an exact as-built model specification. Different official pages give different bob masses, so the episode does not state the bob's weight.

### S5 — Royal Mint Museum: 101 Uses of Coins
https://www.royalmintmuseum.org.uk/podcast/101/

Contains a photograph of coins on the pendulum shelf and explains the use of pre-decimal coins. Direct photograph reference for inspection:
https://www.royalmintmuseum.org.uk/siteassets/podcast/pendulum-big-ben.jpg

The museum marks the account of a keeper forgetting weights as something thought to have happened. That origin anecdote is omitted from the factual narration. Do not invent dialogue, a documented first inventor, a rare coin date or a price paid for the coins.

### S6 — OpenStax, University Physics Volume 1, §15.4 Pendulums
https://openstax.org/books/university-physics-volume-1/pages/15-4-pendulums

Physical pendulum model: for small swings, T = 2*pi*sqrt(I/(M*g*d)), where I is moment of inertia about the pivot, M is mass, and d is pivot-to-centre-of-mass distance. Equivalent simple-pendulum length is L_eff = I/(M*d). The real clock has a distributed mass, escapement and corrections; it is not a point bob on a massless string.

## What our explanation means

For a small coin of mass m at distance r below the pivot:

- I becomes I + m*r^2.
- M*d becomes M*d + m*r.
- L_eff becomes (I + m*r^2)/(M*d + m*r).
- When 0 < r < L_eff, L_eff decreases and the period shortens. Position and mass distribution matter; adding weight anywhere does not always make a pendulum faster.

This algebra is an explanatory inference from the physical-pendulum equation, not a measured reconstruction of this clock's exact geometry. Animate a labelled simplified model. Do not claim a measured coin-shelf height, a measured centre-of-mass shift or a physical rod shortened by a visible amount. A simple centre-of-mass-only rule is insufficient for arbitrary rigid pendulums.

The documented +0.4 s/day is a rate increment relative to the previous setting, not an absolute accuracy guarantee. A clock already running fast would become faster if another penny were added. The keeper selects the direction after checking the rate.

## Numerical animation checks

- Approximate full period: 4 s (two seconds per beat / half cycle). Thus about 21,600 full cycles in a day.
- Relative rate increment: 0.4 / 86400 = 0.00000462963, about 4.63 parts per million.
- For a 4-second model cycle, the corresponding shortened period is 4 / (1 + 0.4/86400), about 3.99998148 s. This is roughly 18.5 microseconds difference per full cycle.
- Those calculations are educational consequences of the documented rate, not a measurement of the actual escapement.
- The change must NOT become a dramatic faster swing, a spinning clock face, a larger swing amplitude, a leap forward in time, or a difference plainly visible after one normal swing.
- To show accumulated gain, label a 24-hour comparison TIME COMPRESSED; show +0.4 s / day. If comparing phases graphically at a larger scale, label DIFFERENCE EXAGGERATED.

## Staging versus documented fact

Documented: coin adjustment practice, direction of rate change, approximate daily increment, four faces, five-tonne mechanism, pendulum timing.

Original staging: our mascot acting as a keeper, room dressing, specific gestures, camera paths, explanatory overlays and the order of demonstrations. They are not a reconstruction of a named person's particular working day. No claim of sabotage, clock failure, a miraculous instant repair or a historical conversation is needed.

No source images or original interview audio are packaged as reusable media. The reference URLs support factual/geometric inspection. Create original 3D geometry, diagrams and sound, and retain any asset licences actually used.
