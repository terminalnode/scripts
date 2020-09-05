# General scripts
These are any scripts that don't fit into any specific category, or only
fit into some very large general category, or where it's ambiguous which
category they belong to... you get the point, they're hard to categorise.

## Archlinux
Scripts useful for arch system maintenance, but not much else.

* `pm` (shell script) is a multi-alias for the AUR helper
[yay](https://github.com/Jguer/yay) to carry out various common and/or useful
package manager tasks.
* `upmirror` (shell script) fetches the latest pacman mirrors, tests which
ones are fastest for you using `rankmirrors` from `pacman-contrib`.


## Ruby
Scrits written in Ruby. Ruby is amazing, we should use ruby for everything.

* `decimal_time` output the current time in decimal time (sometimes called
metric time), that is with 10 hours in a day and 100 minutes in an hour.
* `editorrenamer` is a tool for batch renaming files using the users
`$VISUAL` or `$EDITOR`.
* `igdl` is a tool for asynchronously downloading images of instagram.
Requires [cli-ui](https://github.com/Shopify/cli-ui).


## Shell script
Scripts written in shell script.

* `scalevid` is a tool for using ffmpeg to scale videos.
* `transadd` is a tool for adding torrent files to
[transmission](https://transmissionbt.com/) using `transmission-remote`.


## Python
Scripts written in Python.

* `track_renamer.py` is a tool for batch renaming music files. It will
probably be replaced by batchrename in the near future.


## Unfinished / WIP
Scripts that are or were works in progress.

* `batchrename` (ruby) is tool for batch renaming files using regexps
and naming patterns.
