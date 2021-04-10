sub centuryFromYear {
  my ($year) = @_;
  $year += -1 ;
  my $fouryear = $year;
  if (length($year)<4) {$fouryear =  '0' . $fouryear} ;
  if (length($year)<3) {$fouryear =  '0' . $fouryear} ;
  if (length($year)<2) {$fouryear =  '0' . $fouryear} ;

    
  my $firsttwo = substr $fouryear, 0, 2 ;
  return $firsttwo + 1 ;
  
}
