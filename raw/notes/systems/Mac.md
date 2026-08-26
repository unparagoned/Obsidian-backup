
Window management and multi-tasking recommended from reddit
	-better touch - can configure hot corners to be spotlight
	- magnet
	- [https://bentoboxapp.com/](https://bentoboxapp.com/)
	- Alt-Tab: [https://alt-tab-macos.netlify.app](https://alt-tab-macos.netlify.app/) -shows the image of the tab 


# Keys

| Keys             | Action                          |
| ---------------- | ------------------------------- |
| Ctrl  ->         | move between desktops           |
| Ctrl  1-9        | Switch to desktop number        |
| Ctrl  Alt 1-6    | Switch to desktop numbers 11-16 |
| Ctrl Shift z/x/c | Move window to screen           |
| Cmd Ctrl <-      | left half of screen             |
| Cmd Ctrl m       | Maximise                        |
| Cmd + option +v  | makes the paste a cut and paste |

Set up dev to be beginning desktops on a screen, so it's easier to remember those numbers. Can't move or rename the desktops, 
1
6
11-12

# Mount smb

Automounter can keep them mounted



# Keyboard

Had to add special type of british -PC keyboard  on input

Cmd  + Alt + f - find in onenote

22/10/2025 18:30

# Gaming

Some games don't work

Parallels worked well with chos gate demonhunters

Could use clouddeck to play those games remotely

[https://clouddeck.app/blog/warhammer-40000-chaos-gate-daemonhunters-mac/](https://clouddeck.app/blog/warhammer-40000-chaos-gate-daemonhunters-mac/)

Or maybe CrossOver, they are level level, but probably not as good as parallels.

![[raw/assets/62bf5ad47046472e4540436dec23f46d_MD5.png]]

In parralels worked

# Displays

Mac night mode only works with some displays and not TV and stuff. Use flux instead

HDMI passthrough only works on the main apple apps. VLC and others don't have it yet.

The resolution isn't real, it's kind of like a scaling. So a lower resolution keeps the quality but makes things bigger.

The thunderbolt to hdmi gives flickering output to dennon, maybe that cable is bad or can't handle the resolution, which might be causing the other issues with it not working when coming out of sleep.

# Tensorflow keras

pip install tensorflow-macos==2.15.0 tensorflow-metal==1.1.0

# Flux

In the menu on the top right

# LLM

LM Studio supports MLX and seems better performance than Ollama

# Dock

If you bring the mouse down the middle of the screen slowly to the bottom it will bring up the dock there.

Using terminal commands to make the dock appear instantly makes all the difference,

# Pictures iCloud iphone sync

They are in the pictures app, it doesn't sync to the folder.

# Display issues - hdmi seems separate

Click the top right option , check the screen mirroring option and disable it or something

# Hardrive speed test

External is half the speed of the internal drive. This is probably because the external mount is 40Gbs rather than 80Gbps. Maybe should have spent £120 more for the faster one, but it's fast enough.

Got faster 80gbps external and it's about as fast as internal, read is faster but write is slower.

Mac harddrive

![[raw/assets/a25d1274ed12f7a81859e63aa6068ce8_MD5.png]]

Satechi - half the speed but that's but meets advertised specs.

![[raw/assets/dd2dd241174799b26307689bfa1c7c5a_MD5.png]]

U Green with Samsung 990, faster read but slower writes than internal. But all fairly similar, great.

![[raw/assets/84a8b0f7abe6537940e35c99ac7aaba2_MD5.png]]

# Browsers

The 2FA autocomplete stuff works well on Safari but not other browsers.

I think there was an issue with lastpass extension, but don't remember the details.

Safari doesn't support using perplexity as search, but can set it to homepage for new tabs

# Snapshot screen shot

Cmd + Ctrl + Shift + 4

# Terminal from finder

Need to click a folder, then terminal option comes up

Or from Jeese's Mac Studio, can right click USB DISK and terminal option is there

# Network

Mac -> PC

If you write

Smb://unpar@CRONE/g

Then windows default passwork can access that network drive

## PC -> Mac

You need tocreate users with the exact same name and pass as windows users then that secret option in group to select user as windows user125

# Passwords saving and syncing

Backup keys, hardrive keys, and all that snas.

Put it on a veracrypt volume passwords.vc on a usb drive on the keys.  Then have a script that copies it to icloud and onedrive. Need to touch it just before so the rsync and cloud syncing works realising it's different.

Three useful scripts

Unlock.command

Lock.command

Sync_onedrive_cloud.command

That way either I have it one me, or I can get into at least one of the apple or MicrosoftÏ systems.


# Hang login

Rebooted three times, then logged into jkjk, which worked then logged out and logged into unparagoned

# Sound

Middle speaker stopped working

Set AVR to pure

Maybe **Audio MIDI Setup**