# General scripts
These are any scripts that don't fit into any specific category, or only
fit into some very large general category, or where it's ambiguous which
category they belong to... you get the point, they're hard to categorise.

## Descriptions
### Archlinux-specific scripts
* `pm` (shell script) is a multi-alias for the AUR helper
[yay](https://github.com/Jguer/yay) to carry out various common and/or useful
package manager tasks.
* `upmirror` (shell script) fetches the latest pacman mirrors, tests which ones are fastest
for you using `rankmirrors` from `pacman-contrib`.

### Others
* `batchrename` (ruby, **WIP**) is tool for batch renaming files using regexps
and naming patterns.
* `igdl` (ruby) is a tool for asynchronously downloading images of instagram.
Requires [cli-ui](https://github.com/Shopify/cli-ui).
* `editorrenamer` (ruby) is a tool for batch renaming files using the users
`$VISUAL` or `$EDITOR`.
* `track_renamer.py` is a tool for batch renaming music files. It will
probably be replaced by batchrename in the near future.
* `transadd` (shell script) is a tool for adding torrent files to
[transmission](https://transmissionbt.com/) using `transmission-remote`.
