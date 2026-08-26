---
tags:
  - systems
  - reference
type: reference
source: raw/notes/systems/TV.md
author: user
---

**Summary:** Apple TV / Stremio setup: Omni sync, TorBox via AIOStreams with English as a required language, Cinemeta as the metadata provider so anime seasons work, plus the older Real-Debrid/Torrentio configuration and a CDN speed record.

Related: [[Mac]] · [[VLC]] · [[Films]] · [[Headphones]]

# Apple TV

## Omni

Omni on the mac should sync to tv

Set up torbox using aiostreams since you can select english as required language
https://aiostreams.elfhosted.com/stremio/configure?menu=save-install&service-tab=posters&addons-tab=addons&filter=visual-tag

To delete add owns use apple tv not desktop

Use **Cinemeta** as the media provider to give proper seasons to anime, otherwise they were all season 1 and that didn't work.




# Old

The real debrid-config is through the addons like 
https://torrentio.strem.fun/configure

If films don't load
- Check real-debrid
- Clear cache


Torbox to replace reldebrid
Comet Torrentio

CDN

{"maxSpeedMbps":865.0257184248901,"maxSpeed":865.0257184248901,"averageSpeedMbps":766.0829223744292,"averageSpeed":766.0829223744292,"ping":45,"date":1780297566862,"region":"seur","server":"nexus-140","closest":false,"multithreaded":true,"userCountry":""}

# TODO

- The setup depends on paid debrid services and third-party addons; note which are currently active.
- The CDN JSON blob is a one-off speed test with no context.
