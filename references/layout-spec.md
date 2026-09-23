# Layout specification

All fixed PNG assets are full-canvas RGBA images anchored at `(0, 0)`. Text,
participant pills, footage, captions, and emphasis cards are dynamic layers.

## 16:9 video

- Canvas: 1920 x 1080.
- Fixed asset: `assets/full-overlay.png`, or the separate horizontal header and
  subtitle band.
- Header: approximately `y=0-145`.
- Subtitle-band upper edge: approximately `y=1016` at the left and `y=914` at
  the right.
- Put the date and event title at the upper left. Keep participant labels next
  to the people they identify.

## 9:16 video

- Canvas: 1080 x 1920.
- Fixed asset: `assets/vertical-full-overlay.png`, or the separate vertical
  header and subtitle band.
- Header: `y=0-204`.
- Header text has two available rows around `y=48` and `y=115`; shorten or
  reduce type before allowing it to touch the upper-right circles.
- Subtitle-band upper edge: approximately `y=1794` at the left and `y=1729` at
  the right.
- Keep captions above platform controls and inside the blue band. A vertical
  participant pill is dynamic and should appear only while that person is in
  frame.

## 16:9 cover

- Canvas: 1920 x 1080.
- Start with `assets/cover-background.png`.
- Add one or two expressive participant cutouts, leaving the face and gesture
  unobstructed.
- Place date and event metadata at the upper left.
- Use one dominant 6-12-character headline and, only when helpful, one
  secondary line. The large headline can use Mantou Sans; metadata uses Swei
  Marker Leg CJK TC.
- Use the bottom band for one topic tag plus short hashtags. Do not place spoken
  captions on a cover.

## Dynamic-layer order

1. Source footage or cover background.
2. Fixed overlay asset.
3. Date, event, and meeting-type metadata.
4. Participant labels.
5. Spoken captions.
6. Emphasis cards or cover headline.

Never bake names, dates, meeting titles, subtitles, or topic copy into a fixed
overlay PNG.
