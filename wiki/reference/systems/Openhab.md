---
tags:
  - systems
  - reference
type: reference
source: raw/notes/systems/Openhab.md
author: user
---

**Summary:** The live home-automation setup: very old, nothing updates, GUI reachable at the admin option on the local server. Decision recorded — keep using old openHAB until it breaks. Includes thermostat control, the /etc/openhab dev layout, Debian install gotcha (use the DVD ISO), and the Alexa/myopenhab debugging step.

Related: [[Home Assistant]] · [[Mac]] · [[TV]]

#homeautomation

Existing is soo old, nothing updates. ~~The GUI is all gone so, not sure how to update anything anymore.  ~~Can go to http://debra:8080 and click the admin option bottom. Can change things around using the GUI and add new stuff. 

Contintue to use old openhab until it breaks. 

## Temperature Thermostat
Slider on habpanel can set temp


## Development
Main folder is /etc/openhab¦
Openhab extension for VSCode works well too.
## Migrate?

New one doesn't seem to have a much better GUI. Also the tuya extensions seems to be clumbersome relying on working locally and MITM the connection. 

Seems like a pain to setup my script again.

Try Home Assistant, I think that's where I got the stuff for the script in the first place. So might be more streamlined. Wouldn't boot. Maybe need to run on Raspberry Pi

# Debian
Make sure you get the DVD iso, the min distro couldn't connected to network and has no GUI making it hard to fix things.

# Debugging

# Alexa doesn't connect

If https://myopenhab.org is offline then restart and it might take a while for this to work
`sudo systemctl status openhab.service`

# TODO

- Migration was considered and rejected: the new GUI isn't much better and the Tuya extensions rely on MITM'ing the connection locally. Home Assistant wouldn't boot.
- Running an unpatched, unsupported automation stack is a standing security risk; worth a decision date.
