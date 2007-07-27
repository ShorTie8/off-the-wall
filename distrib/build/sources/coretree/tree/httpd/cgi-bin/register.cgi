#!/usr/bin/perl
#
# SmoothWall CGIs
#
# This code is distributed under the terms of the GPL
#
# (c) The SmoothWall Team

use lib "/usr/lib/smoothwall";
use header qw( :standard );
use IO::Socket;

my %ownership;
&readhash( "/var/smoothwall/main/ownership", \%ownership );

my (%settings,$errormessage);
&getcgihash(\%settings);

my $sysid = &getsystemid();

if ($settings{'ACTION'} eq $tr{'no thanks'} ){
	#&dont_register();
	print "Status: 302 Moved\nLocation: /cgi-bin/index.cgi\n\n";
	exit(0);
} else {
	&showhttpheaders();
	&openpage($tr{'register title'}, 1, "", 'register');
	&openbigbox();
	&register_page();
}

&alertbox($errormessage);

&closebigbox();
&closepage();

sub dont_register
{
	my ( $settings ) = @_;
	
	$ownership{ 'ADDED_TO_X3' } = -1;
	&writehash( "/var/smoothwall/main/ownership", \%ownership );
}

sub register_page
{

	&openbox();

print <<END
<div align="center"><h2>SmoothWall Express $version</h2>
<p>Express $version $webuirevision
</div>
END
;

	&closebox();

# START x3 add bit
#print "<form method='post'>\n";
&openbox( $tr{'x3 reg'} );

print <<END
<table class='centered'>
	<tr>
		<td colspan='2'>
			<br/>
			$tr{'x3 reg info'}
			<br/>
			<br/>
		</td>
	</tr>
</table>
END
;

if ( not defined $ownership{'ADDED_TO_X3'} or $ownership{'ADDED_TO_X3'} ne "1" ){
	print <<END
	<table class='centered'>
		<tr>
	<form method='post' action='https://my.smoothwall.org/cgi-bin/signin.cgi' target='_new'>
	<input type="hidden" name=id value='$sysid'>
			<td style='text-align: center;'><input name="ACTION" type='submit' value='$tr{'register'}'></td>
	</form>
END
;

	if ( not defined $ownership{'ADDED_TO_X3'} or $ownership{'ADDED_TO_X3'} ne "-1" ){
		print <<END
	<form method='post'>
			<td style='text-align: center;'><input name="ACTION" type='submit' value='$tr{'no thanks'}'></td>
	</form>
END
;
	}

print <<END
		</tr>
	</table>
END
;
}

print "</form>\n";

&closebox();
# END x3 add bit

&openbox( $tr{'credits and legal'} );

print <<END
<div align="center">
<table border="0" cellpadding="3" cellspacing="0" width="90%">

<tr><td width="50%" align="left" valign="top">
<center>
SmoothWall Express $version<br>
Copyright &copy; 2000 - 2007 the <a href="http://smoothwall.org/team/" target="_breakoutWindow">SmoothWall Team</a>
</center>
<p>
A full team listing can be found <a href="http://smoothwall.org/team/"
 target="_breakoutWindow">on our website</a>.
Portions of this software are copyright &copy; the original
authors, the source code of such portions are 
<a href="http://smoothwall.org/sources.html"
 target="_breakoutWindow">available under the terms of the appropriate 
licenses</a>.
</p>
</td>
<td width="50%" align="left" valign="top">
<p>
For more information about SmoothWall Express, 
please visit our website at
<a href="http://smoothwall.org/"
 target="_breakoutWindow">http://smoothwall.org/</a>
</p>
<p>
For more information about SmoothWall products, please visit 
our website at <a href="http://www.smoothwall.net/"
 target="_breakoutWindow">http://www.smoothwall.net/</a>
</p>
</td>
</table>

<p>
SmoothWall&trade; is a trademark of SmoothWall Limited.
Linux&reg; is a registered trademark of Linus Torvalds.
All other trademarks and copyrights are property of their
respective owners.
Stock photography used courtesy of
<a href="http://istockphoto.com/">iStockphoto.com</a>.
</p>
</div>
END
;

&closebox();
}
