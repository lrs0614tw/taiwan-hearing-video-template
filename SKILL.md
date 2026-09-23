---
name: taiwan-hearing-video-template
description: Apply the user's reusable 1920×1080 Taiwanese legislative-hearing video layout based on the supplied human-edited reference, with a grid header, rising-right blue subtitle band, and lower-left geometric artwork. Use when the user asks to reuse this hearing style or its overlay assets; do not apply it to unrelated videos by default.
---

# Taiwanese hearing video template

Use the supplied transparent PNGs as the visual source of truth. The header was taken from the user's human-edited reference; the lower-left shapes were redrawn from that flattened video so they can be reused cleanly. Preserve the approved geometry instead of drawing a plain blue rectangle or reversing the slope.

## Assets

- [Header](assets/header.png): blank grid information bar and upper-right decoration.
- [Subtitle band](assets/subtitle-band.png): opaque pale-blue band with lower-left circles, fine stripes, and cream stars.
- [Combined overlay](assets/full-overlay.png): the two layers composited for a simple application.

All assets are transparent RGBA PNGs at **1920×1080**. The center remains transparent. Use either the separate header and band or the combined overlay, never both at once. Keep their full-frame dimensions and anchor them at (0, 0), with no cropping or resizing on a 16:9 1920×1080 output.

## Composition

Layer from bottom to top: edited source footage; the supplied PNG overlay; replaceable date/topic and participant labels; replaceable spoken captions and occasional emphasis cards if requested. Keep text out of the fixed-art assets so later videos can change their words without redrawing the artwork.

- The header occupies approximately y=0–145. Put the date and topic at the upper left, aligned with its thin black rule. The reference uses dark, heavy Chinese sans lettering; a practical local substitute is Noto Sans TC in a bold weight. Check the actual font's painted bounds before rendering.
- The pale-blue subtitle band's *upper edge rises from left to right*: around y=1016 at x=0 and y=914 at x=1920. Its left-hand disk, striped circle, and two outlined stars intentionally extend above that edge. This direction and these shapes are part of the approved template.
- Center ordinary cream/yellow captions with a dark navy offset shadow inside the lower band. Fit each phrase to the band rather than clipping long text; set timing to the audible speech. The exact typeface in the flattened reference is unverified, so match its visual weight and spacing by comparing a frame, not by claiming an exact font.
- Place verified role-and-name labels vertically near the outer edges only while each identified person is visible. In the reference, the left label is navy; the right label is white with a dark edge. Update or remove labels after a shot change.
- Keep the hearing footage's left/right participant relationship and central separator when present. The fixed overlay should not be used to hide a mismatch in framing.

The band is fully opaque where blue. It hides a source timecode only if that timecode falls behind its blue area. Inspect the actual source frame; if the timecode is elsewhere or above the sloping edge, crop or cover that region deliberately rather than assuming this asset hides it.

## Workflow

For a new video, inspect the source and identify participants, source timecode, aspect ratio, and useful framing. Edit the footage, apply the provided overlay, add changeable text, and inspect representative stills against the human-edited look. Verify the subtitle band's edge is low on the left and high on the right, the geometric art is visible, the source timecode is handled, and no caption or label is clipped. Follow the user's chosen review/preview checkpoints for the wider edit.
