#!/usr/bin/env ruby
# Bash script that parses a logfile and displays the
# [sender], [receiver], and [flags] used

puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
