#!/usr/bin/env crystal
# vim: ft=ruby
# Output the current time in decimal time / metric time.
# Decimal time is a system of time keeping where there are 10 hours in
# a day, 100 minutes in an hour and 100 seconds in a minute.
#
# Seconds in a day:             86400
# Seconds in a decimal hour:    8640
# Seconds in a decimal minute:  86.4
# The decimals of the decimal minute will be used as decimal seconds.
now = Time.local
secondsPassed = (now.to_unix + now.offset) % 86400
decimalHour, secondsPassed = secondsPassed.divmod(8640)
decimalMinute = secondsPassed / 86.4

puts "#{decimalHour}:#{"%05.2f" % decimalMinute}"
