# Continuity — characters, locations and height states

## Hero and references

Inspect assets/hero_reference.png and assets/continuity/APPROVED_ODDPLOT_V3.mp4. PNGs extracted from that V3 at 3.20, 4.80 and 12.40 seconds show grounded legs, prop contact and expression. They are 540x960 reference views; do not stretch them across the horizontal frame as film backgrounds.

Same face, hair, orange vest, navy clothing and body proportions. No name or real historical identity is assigned to the homeowner. His expressive head and hands are flat; set geometry and camera are volumetric. Front/three-quarter views should keep the silhouette readable; avoid turning a camera-facing card edge-on or mirroring hair asymmetry between shots.

## Shoe gag: deliberate exception

Ordinary rule: ankles, feet and footwear remain connected; no shoe sliding or legs lifting away from planted shoes. The failure seen in earlier test versions must not return.

In S004–S006 only, one shoe/boot deliberately sticks in the mud. Show the foot inside it before pulling, the foot/sock coherently coming out, the loose shoe remaining in mud, its retrieval and putting it back on. This is an explicit prop-attachment transition, not a glitch. By the end of scene 02 both feet are shod again. All later walks show normal footwear. Scene 18 uses a muddy FOOTPRINT by the door; it does not remove a shoe. The shoe held by the neighbour in scene 20 is a separate labelled prop.

## Fixed building identities

House A: modest two-storey fictional brick/wood house, recognisable dark door and small orange marker beside it, same window/table/shelf inside. House B: distinct neighbour facade and low doorway. Keep both positions, frontage dimensions and room layout fixed throughout.

The street surface, House A and House B have separate parent/root transforms. Parent House A's room floor, walls, windows, handle and furniture to its building root. During the lift, the building does not stretch, rotate or leave its floor behind. A character standing inside is constrained to the local floor; a worker outside stays on the external platform/ground.

## Illustrative model coordinates

These are production coordinates for the fictional block, not survey data for a real Chicago address.

- Old street/floor reference: z=0.00.
- New street reference: z=1.40 m.
- Hero eye height in the old doorway: about z=1.40 m; adjust the rig/set together to make the opening readable.
- House A lift: root delta z from 0.00 to 1.40 m.
- House B remains at the old root height through the ending.
- Indoor furniture stays fixed relative to the moving House A floor.

| State | Street | House A | Usage |
|---|---|---|---|
| OLD_GRADE | old | low | Mud flashback |
| STREET_HIGH_HOUSE_LOW | high | low | Opening mystery and return in scene 06 |
| SUPPORTED_PRELIFT | high | low, fully supported | Preparation |
| LIFTING_EARLY | high | 0.00 to ~0.15 m | First small gap |
| LIFTING_MIDDLE | high | ~0.15 to ~0.65 m | Checks and rising |
| LIFTING_LATE | high | ~0.65 to 1.40 m | Time-compressed work |
| HOUSE_HIGH_FOUNDATION_COMPLETE | high | high | Load transferred to permanent foundation |
| HOUSE_AND_STREET_HIGH | high | high | Door payoff |
| MIXED_NEIGHBOURHOOD | high | A high, B low | Final comparison and neighbour |

No need to animate a single jack extending 1.4 m in one stroke. Use staged short movements with temporary support/cribbing and progressive foundation work. Maintain a visible load path; avoid a floating house unsupported above workers. The cutaway is a simplified educational reconstruction, not an executable lifting specification.

## Matched opening and ending

Save one camera setup in House A local coordinates for S001 and S055. Same lens, door hinge direction, handle height, window and props. In S001 the raised street cuts the exterior view at face height. In S055–S057 the same house/camera are at the new elevation and the threshold meets the street. The contrast comes from transforms, not from remodelling the doorway.

## Period and secondary cast

Background Chicago: 1850s–1860s low-rise streets, carts and horses, timber/brick, manual equipment. No modern cars, cranes, hydraulic car jacks or skyscrapers. The branded hero remains a stylised mascot; do not claim his costume is a historic uniform. The real named engineers appear as names on contextual graphics, without invented portraits or dialogue.

A small reusable crew and passers-by provide scale. Foreman signals are fictional staging. Historical insert Lake Street 1860 has a clearly labelled separate location and uses modular facades; it is not the hero's block. Never show all Chicago rising at once.
