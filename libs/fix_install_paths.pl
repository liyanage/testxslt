#!/usr/bin/perl

use warnings;
use strict;


my ($filename, $basedir) = @ARGV;
my ($libname) = $filename =~ m!/([^/]+)$!;

my %paths =
	map {m!/(lib\w+)\..*\.dylib!; $_ => "\@executable_path/../Frameworks/$1.dylib"}
	grep {/^$basedir/}
	map {/^\s+(.+)\s+\(compatibility/}
	grep {/^\s+/}
	`otool -L "$filename"`;

system('install_name_tool', '-change', $_, $paths{$_}, $filename) foreach (keys(%paths));
system('install_name_tool', '-id', "\@executable_path/../Frameworks/$libname", $filename);

