#!/usr/bin/env perl

sub shapeArea {
    my ($n) = $_[0];
    if ( $n == 1 ) { 
        $area = 1; 
        }
    else { 
        $area = ($n - 1) * 4 + shapeArea( $n - 1 ); 
        }
    return $area;
