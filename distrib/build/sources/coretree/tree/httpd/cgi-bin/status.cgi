#!/usr/bin/perl
#
# SmoothWall CGIs
#
# This code is distributed under the terms of the GPL
#
# (c) The SmoothWall Team

use lib "/usr/lib/smoothwall";
use header qw( :standard );

my %cgiparams;
# Maps a nice printable name to the changing part of the pid file, which
# is also the name of the program

my $iface = '';
if (open(FILE, "${swroot}/red/iface"))
{
	$iface = <FILE>;
	close FILE;
}


# build the list of services.

my %servicenames;
my %coreservices;

opendir(DIR, "/var/smoothwall/services/");
my @files = grep {!/\./} readdir(DIR);

foreach my $file ( sort @files ){
	open ( my $line, "</var/smoothwall/services/$file" ) or next;
	my ( $name, $rel ) = split /,/, <$line>;
	close $line;
	chomp $name;
	my $servicename = $file;
	$servicename =~s/\[RED\]/$iface/ig;
	chomp $rel;
	if ( defined $rel and $rel eq "core" ){
		$coreservices{ $tr{ $name } } = $servicename;
	} else {	
		$servicenames{ $tr{ $name } } = $servicename;
	}
}

&showhttpheaders();

&getcgihash(\%cgiparams);

&openpage($tr{'status information'}, 1, '', 'about your smoothie');

&openbigbox('100%', 'LEFT');

&alertbox($errormessage);

&openbox();

print <<END
<strong>$tr{'core services'}</strong>
<table class='centered' style='width: 60%;'>
END
;

my $lines = 0;

foreach my $key (keys %coreservices)
{
	if ($lines % 2) {
		print "<tr class='light'>\n"; }
	else {
		print "<tr class='dark'>\n"; }
	print "<td style='width: 60%; text-align: center;'>$key</td>\n";
	my $shortname = $coreservices{$key};
	my ( $status, $period ) = &isrunning($shortname);
	print "<td style='width: 10%; text-align: center; vertical-align: middle;'>$status</td>\n";
	print "<td style='width: 30%; text-align: center;'>$period</td>\n";
	print "</tr>\n";
	$lines++;
}

print <<END
</table>
<strong>$tr{'services'}</strong>
<table class='centered' style='width: 60%;'>
END
;

$lines = 0;

foreach my $key (keys %servicenames)
{
	if ($lines % 2) {
		print "<tr class='light'>\n"; }
	else {
		print "<tr class='dark'>\n"; }
	print "<td style='width: 60%; text-align: center;'>$key</td>\n";
	my $shortname = $servicenames{$key};
	my ( $status, $period ) = &isrunning($shortname);
	print "<td style='width: 10%; text-align: center;'>$status</td>\n";
	print "<td style='width: 30%; text-align: center;'>$period</td>\n";
	print "</tr>\n";
	$lines++;
}

print "</table>\n";

&closebox();

&alertbox('add','add');

&closebigbox();

&closepage();

sub status_line
{	
	my $status = $_[0];

	return "<img src='/ui/img/service_$status.png' alt='$status'>";
}


sub isrunning
{
	my $cmd = $_[0];
	my $status = status_line( "stopped" );
	my $pid = '';
	my $testcmd = '';
	my $exename;

	$cmd =~ /(^[a-z]+)/;
	$exename = $1;

	my $howlong = "";

	if (open(FILE, "/var/run/${cmd}.pid"))
	{
 		$pid = <FILE>; chop $pid;
		close FILE;
		if (open(FILE, "/proc/${pid}/status"))
		{
			while (<FILE>)
			{
				if (/^Name:\W+(.*)/) {
					$testcmd = $1; }
			}
			close FILE;
			if ($testcmd =~ /$exename/)
			{
				$status = status_line( "running" );

				my $age = time - (stat( "/var/run/${cmd}.pid" ))[9];
				my ( $days, $hours, $minutes, $seconds ) = (gmtime($age))[7,2,1,0];

				if ( $days != 0 ){
					$howlong = "$days days";
				} elsif ( $hours != 0 ){
					$howlong = "$hours hours $minutes mins";
				} else {
					$howlong = "$minutes:$seconds";
				}

				if (open(FILE, "/proc/${pid}/cmdline"))
				{
					my $cmdline = <FILE>;
					if (!$cmdline) {
						$status = status_line( "swapped" );
					}
				}
			}
		}
	}

	return ( $status, $howlong );
}
