sub makeArrayConsecutive2 {
    my ($statues) = @_;
    @$statues = sort { $a <=> $b } @$statues;
    my $prevStatue = shift(@$statues);
    my $missingStatue = 0;
    foreach (@$statues) {
        $missingStatue += $_ - $prevStatue - 1;
        $prevStatue = $_;
    }
    return($missingStatue);
}
