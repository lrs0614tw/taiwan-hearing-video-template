---
name: taiwan-hearing-video-template
description: Apply the user's reusable Taiwanese legislative-hearing visual system to 1920x1080 horizontal videos, 1080x1920 vertical social cuts, and matching 1920x1080 covers. Use for this hearing style's grid header, rising-right blue subtitle band, geometric artwork, bundled Traditional Chinese fonts, participant labels, or cover composition; do not apply it to unrelated videos by default.
---

# Taiwanese hearing video template

Use the supplied text-free PNGs and bundled fonts as the visual source of truth.
Choose the asset that matches the requested deliverable; never stretch one
aspect ratio into another. Read [references/layout-spec.md](references/layout-spec.md)
when positioning dynamic text, labels, captions, or cover elements.

## Assets

### 16:9 video at 1920x1080

- [Header](assets/header.png): grid information bar and upper-right decoration.
- [Subtitle band](assets/subtitle-band.png): rising-right blue band and lower-left artwork.
- [Combined overlay](assets/full-overlay.png): header and subtitle band combined.

Use either the separate layers or the combined overlay, never both.

### 9:16 video at 1080x1920

- [Vertical header](assets/vertical-header.png): two-row metadata area and fixed decoration.
- [Vertical subtitle band](assets/vertical-subtitle-band.png): rising-right lower band and lower-left artwork.
- [Vertical combined overlay](assets/vertical-full-overlay.png): vertical header and band combined.

Use either the separate vertical layers or the combined vertical overlay, never
both. Keep the central transparent area for recomposed source footage.

### 16:9 cover at 1920x1080

- [Cover background](assets/cover-background.png): opaque grid background,
  geometric artwork, and lower topic band. Add cutout participants and all copy
  as dynamic layers.

## Fonts

Use the bundled files directly; do not substitute Noto Sans CJK TC.

- `assets/fonts/SweiMarkerLegCJKtc-Bold.ttf`: date, event title, participant
  labels, ordinary captions, and most metadata.
- `assets/fonts/SweiMarkerLegCJKtc-Black.ttf`: heavier metadata, topic tags,
  and forceful emphasis that should remain in the same family.
- `assets/fonts/MantouSans-Regular.ttf`: a short cover headline or major
  emphasis card only. Do not use it for long metadata or ordinary captions.

Pass the exact font file to the renderer instead of depending on a system
family name. Verify Traditional Chinese glyphs, painted bounds, and line breaks
in the encoded output. Font license files are stored beside the fonts.

## Dynamic content

Never bake any of the following into a fixed PNG:

- date, committee, hearing, meeting type, or topic;
- participant name and role;
- spoken captions;
- emphasis-card copy;
- cover headline, topic tag, or hashtags.

Treat participant labels as shot state. Show a verified role-and-name label only
while that person is visible, reposition it after every crop or cut, and remove
it immediately when the person leaves the frame.

## Composition rules

- Anchor every fixed asset at `(0, 0)` at its native canvas size.
- Preserve the lower band's rising-right edge. Do not flatten or reverse it.
- Keep all faces, eyes, mouths, gestures, broadcaster marks, and source labels
  unobstructed.
- Recompose 9:16 footage around the active speaker while preserving useful
  hands, microphones, and conversational left/right relationships.
- Keep ordinary captions inside the appropriate lower band. Fit the longest
  phrase after outline and shadow are applied.
- A cover uses one dominant 6-12-character headline, one small metadata area,
  and at most one topic tag plus short hashtags. It does not use spoken
  captions.

The blue band hides a source timecode only when that timecode falls behind its
opaque area. Inspect the actual source and crop or cover an exposed timecode
deliberately.

## Workflow

1. Identify the deliverable as horizontal video, vertical video, or cover.
2. Inspect the source aspect ratio, participants, marks, and timecode.
3. Apply the matching native-size asset and add dynamic text with bundled
   fonts.
4. For a cover, select a sharp expressive frame or participant cutout before
   placing the headline.
5. Render representative previews for every requested aspect ratio.
6. Inspect the opening, each cut or crop change, every label transition, the
   widest caption or card, and the cover at full size and phone size.

Reject a render if a fixed asset is resized, a band slopes the wrong way, a
dynamic field is baked into the template, a label remains for an off-screen
person, any text or decoration is clipped, or the wrong font family appears.
