#!/usr/bin/env python3
"""
Batch file renamer for music files.

This is a script for batch renaming files, specifically music files.
Contrary to most renaming scripts, it acts on whole folders selecting
only the files ending in common audio file extensions. The syntax
for renaming has names for certain types of elements (i.e. artist name,
album name, track name, track number and so on). Basically these can be
divided into two types, numerical fields and generic text fields.
"""

import argparse
import copy
import os
import re
import sys

# Argument specifications + help output.
help_description = """Rename files in designated folders according to a certain schema.

FORMATTING SYNTAX:
  Text fields:
  %B     Artist/Band name
  %A     Album name
  %T     Track name

  Number fields:
  %N     Track number
  %Y     Release year
  %M     Release month
  %D     Release day
  %C     CD/Disc number

INPUTS:
This is the naming scheme tracks and folders have before renaming, important for gathering data.
The default values are:
  Folders: %B - [%Y] - %A
  Files:   %B - %A - %N %T (This is the default used for files from Bandcamp.com)

OUTPUTS:
This is what your tracks will look like after processing. Folders are not changed.
  Default:   %N - %T

For duplicate information (such as artist name being in both folder and file name), folder info takes precedence."""

parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=help_description,
        epilog=(
            "Fingers crossed! Be mindful of file input vs output " +
            "naming schemes.\nDon't forget to use quotation marks " +
            "around naming schemes."
        )
)

# Folders to process
parser.add_argument(
    'folders',
    metavar='Folder',
    type=str,
    nargs='+',
    help='the folder(s) to process'
)

# Folder naming scheme (used to collect info, set to empty string to ignore).
parser.add_argument(
    '-f',
    '--folder',
    metavar='FN',
    default="%B - [%Y] - %A",
    help='folder naming scheme (see syntax for default)'
)

# File/track output scheme (used to determine a file's new name).
parser.add_argument(
    '-o',
    '--output',
    metavar='OUT',
    default="%N - %T",
    help='track OUTPUT naming scheme (see syntax for default)'
)

# File/track input naming scheme
# (used to collect info, set to empty string to ignore).
parser.add_argument(
    '-i',
    '--input',
    metavar='IN',
    default="%B - %A - %N %T",
    help='track INPUT naming scheme (see syntax for default)'
)

# Don't actually rename files, just show what
# the results would've been if we did.
parser.add_argument(
    '-t',
    '--test',
    action='store_true',
    help='do a test run (no renaming)'
)

# Be verbose, or don't be.
parser.add_argument(
    '-q',
    '--quiet',
    action='store_true',
    help='only print errors'
)

args = parser.parse_args()
if args.test:
    print("\nTest run! No files will be renamed!")

# Retriving all the arguments we've got.
in_folder = args.folder
in_file = args.input
out_file = args.output
in_folder_order = re.findall('%[BATNYMDC]', in_folder)
in_file_order = re.findall('%[BATNYMDC]', in_file)
out_file_order = re.findall('%[BATNYMDC]', out_file)

template = copy.copy(out_file)
for placeholder in out_file_order:
    template = template.replace(placeholder, '{}')

# See if input provides all the data needed for output.
provided = set(in_folder_order).union(set(in_file_order))
required = set(re.findall('%[BATNYMDC]', out_file))
missing = required - provided
if len(missing) != 0:
    print("Some of the variables you want to include" +
          "in your filenames are missing from the input, namely:" +
          "\n {}".format(missing.__str__()))
    sys.exit()

# Creating suitable regexes.
# Entries in num_args and str_args are replaced
# with the strings in num_arg and str_arg respectively.
# str_arg catches everything, num_arg catches only numbers.
num_args = ('%B', '%A', '%T')
str_args = ('%N', '%Y', '%M', '%D', '%C')
num_arg = r'(\d+)'
str_arg = r'(.*)'

# This list contains all reserved regex characters,
# these need to be escaped if they're in the query.
# Omitted characters: \
esc_chars = '. ^ $ * + ? { } [ ] | ( )'.split(' ')

# Escape characters first so we don't escape the ones we need. Obviously.
for char in esc_chars:
    in_folder = in_folder.replace(char, '\\{}'.format(char))
    in_file = in_file.replace(char, '\\{}'.format(char))

for arg in num_args:
    in_folder = in_folder.replace(arg, str_arg)
    in_file = in_file.replace(arg, str_arg)

for arg in str_args:
    in_folder = in_folder.replace(arg, num_arg)
    in_file = in_file.replace(arg, num_arg)

in_folder = re.compile(in_folder)
in_file = re.compile(in_file)

# Check that the user input are valid folders.
# Start collecting failed folders.
folders = [(i, []) for i in args.folders if os.path.isdir(i)]
failed  = [(i, 'not a folder') for i in args.folders if not os.path.isdir(i)]

# For each folder, create a list of the music files in that folder.
# All other files will be ignored. Music files are defined by the regex below.
# If you need support for more music files, just add them.
music_formats = re.compile(r'(.+)\.(flac|m4u|mp3|ogg|wav)$')
for folder in folders:
    files = list()
    for file in os.listdir(folder[0]):
        match = music_formats.match(file)
        if match is not None:
            # [filename, without extension, extension]
            entry = [file]
            entry.extend(match.groups())
            files.append(entry)
    folder[1].extend(files)

# Moment of truth, let's parse these names.
for folder in folders:
    fill_info = copy.copy(out_file_order)

    # Retrieve information from folder name. Replace those values in fill_info.
    # Skip if folder naming scheme isn't said to contain any variables.
    if len(in_folder_order) != 0:
        folder_name = folder[0].split('/')[-1]
        folder_info = in_folder.match(folder_name)

        if folder_info is not None:
            for i in range(len(in_folder_order)):
                # If any of the variables in fill_info are in folder_info,
                # replace the variables by those values.
                # Otherwise leave them as is.
                if in_folder_order[i] in fill_info:
                    fill_info = [
                        j if j != in_folder_order[i]
                        else folder_info[i+1]
                        for j in fill_info
                    ]

        else:
            failed.append((folder_name, "doesn't match folder naming scheme"))
            continue

    # Go through the tracks and fill out the gaps.
    file_fail = False
    for file in folder[1]:
        track_info = copy.copy(fill_info)
        file_info = in_file.match(file[1])
        if file_info is not None:
            for i in range(len(in_file_order)):
                # Same as for folders, let's fill out the track info
                # using information from the file name.
                if in_file_order[i] in track_info:
                    track_info = [
                        j if j != in_file_order[i]
                        else file_info[i + 1]
                        for j in track_info
                    ]

        else:
            file_fail = True
            failed.append((
                folder_name,
                "one or more tracks didn't match track naming scheme"
                )
            )
            break

        # Update file info so file[0] is current path/file name,
        # file[1] is new path/file name.
        track_name = template.format(*track_info) + '.' + file[2]
        file[0] = folder[0] + '/' + file[0]
        file[1] = folder[0] + '/' + track_name

    if file_fail:
        # One or more tracks failed to be named, to avoid errors and
        # inconsistencies that may be hard to fix no files will be renamed.
        continue

    # Let's rename!
    for file in folder[1]:
        try:
            if not args.test:
                os.rename(file[0], file[1])
            if not args.quiet or args.test:
                print("Renamed:\n{}\n{}\n".format(file[0], file[1]))
        except Exception:
            print("Failed to rename\n{}\n{}\n".format(file[0], file[1]))

# Finally, print all the folders that couldn't be processed.
if len(failed) != 0:
    print("The following folders could not be processed:")

for failure in failed:
    print("{} {}".format(failure[0], failure[1]))
