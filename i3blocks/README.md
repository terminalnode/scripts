# i3blocks scripts
[i3blocks](https://github.com/vivien/i3blocks) is a nifty little tool for use
with the i3 statusbar (and by extension, swaybar) to display short text snippets
that might be of interest for the user such as IP addresses, remaining battery
percentage and so on.

It accomplishes this by executing a collection of scripts and commands on regular
intervals, and as such I've created a small collection of such scripts.

Most of these scripts read system information from somewhere in `/sys/class`.

# Descriptions
* `battery` (shell script) reads battery status from `/sys/class/power_supply/BAT0/`
and outputs a percentage based on the information found there. Outputs different
nerdfonts glyphs depending on the status (e.g. charging etc) and power level
of the battery.
* `brightness` (shell script) reads current and maximum brightness from
`/sys/class/backlight/intel_backlight` and calculates the current percentage.
* `cpu_load` (python) reads the CPU power usage and load average using the
python `os` and `psutil` modules.
* `lan` (shell script) uses `netctl`, `hostname` and `ip addr show` to get
the name of the SSID and IP of the current network connection.
* `memory` (shell script) uses `free` to generate how much memory and swap
is currently in use.
* `pulsevolume` (shell script) uses `pacmd` to get the status (muted or not
muted) of the currently active sink. Outputs different nerdfont glyphs
depending on the status and volume of the sink.
