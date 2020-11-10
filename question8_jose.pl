
# so from geeks for geeks in order to get dynamically scoped varible we just use keywords
# my keyword defines a statically scoped local variable
# and local defines dynamically scoped local variable
#
# link: https://www.geeksforgeeks.org/static-and-dynamic-scoping/

print "Hello World!\n";
$mainVar = 100;
$mainVar2 = 100;

sub showVar1
{
  return $mainVar;
}
sub dynamic
{
  # use local which gives us dynamically scoped var
  # here since we are dynamic we are grabbing from the closest place it was declared
  local $mainVar = 1;
  return showVar1();
}

sub showVar2
{
    return $mainVar2;
}
sub static
{
    # use my which gives us the statically scoped var
    # here instead of grabbing what is closest to us we are grabbing the value from the 'parent' function
    my $mainVar2 = 1;
    return showVar2();
}

print dynamic()." ------ DYNAMIC\n";
print static()." ------ STATIC\n";
print "---- Jose Diaz ----";
