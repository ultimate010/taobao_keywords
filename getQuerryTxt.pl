#!/usr/bin/perl
use strict;
use utf8;
use Encode;
use open ":encoding(utf8)", ":std";

if (@ARGV != 3){
	die "Useage: ".$0." orgfile newfile outfile\n";
}
my %wordBag;
my %newWords;
open(in,$ARGV[0]) or die $!;
while(my $line = <in>){
	chomp $line;
	#print $line;
	for(my $i = 1;$i <= length($line);$i++){
		for(my $j = 0;$j <= length($line) - $i;$j++){
			$wordBag{substr($line,$j,$i)}++;
		}
	}
}
close(in);
open(in,$ARGV[1]) or die $!;
open(out,">$ARGV[2]") or die $!;
while(my $line = <in>){
	chomp $line;
	#print $line;
	for(my $i = 1;$i <= length($line);$i++){
		for(my $j = 0;$j <= length($line) - $i;$j++){
			my $word = substr($line,$j,$i);
			next if exists $wordBag{$word};
			$wordBag{$word}++;
			$newWords{$word}++;
		}
	}
}
foreach my $key(sort keys %newWords){
	print out "$key\n";
}
close(out);
close(in);


