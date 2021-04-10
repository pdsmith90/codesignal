sub checkPalindrome {
  my ($inputString) = @_;
  if ($inputString eq reverse $inputString ) {return 1}
  else {return 0};
}
