#!/usr/bin/env perl

sub commonCharacterCount {
    my ($s1, $s2) = @_;
  
    foreach $e (@s1, @s2) { $isect{$e}++ }

    @isect = keys %isect;
    print scalar @isect
  
}
