#!/usr/bin/perl

use CGI;
use CGI qw(Link Title);
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use CGI::Session qw/-ip-match/;
use XML::LibXML;
use HTML::Template;
use utf8;

$page = new CGI;

$session = CGI::Session->load() or die $!;
$SID = $session->id();
$session->close();
$session->delete();
$session->flush();
print "Content-type: text/html\n\n";
print "Stai venendo reindirizzato alla home del sito, aspetta qualche istante";
print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=./index.cgi\">";

