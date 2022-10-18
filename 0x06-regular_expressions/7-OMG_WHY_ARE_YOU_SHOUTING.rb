#!/usr/bin/env ruby
# Ruby script that accepts one argument and pass it to a
# regular expression matching method
# The regular expression must matcha UPPERCASE characters only

puts ARGV[0].scan(/[A-Z]/).join
