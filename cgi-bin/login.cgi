#!/usr/bin/perl

use CGI;
use CGI qw(Link Title);
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use CGI::Session qw/-ip-match/;
use XML::LibXML;
use HTML::Template;
use utf8;

$page = new CGI;

$file = '../data/utenti.xml';
$parser = XML::LibXML->new();
$doc = $parser->parse_file($file);
$radice = $doc->getDocumentElement;

$user= $page->param('username');
$pass = $page->param('password');
$utente = $radice->find("//utente[username=\"$user\"]/username/text()");
$pwd = $radice->find("//utente[username=\"$user\"]/password/text()");

if($user eq $utente and ($pass eq $pwd)){
	$session = CGI::Session->load() or die('problemi nel caricamento della sessione');
	if(not($session->is_empty) and not($session->is_expired)){
		$name = $session->param('utente');
		unless($name eq $user){
			$session->delete();
			$session->flush();
			$session = new CGI::Session();
			$session->param('utente', $user);;
		}
	}
	else{
		$session = new CGI::Session();
		$session->param('utente', $user);
	}
	print $session->header();
	print "Stai venendo reindirizzato alla home del backend, aspetta qualche istante";
	print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=./backend.cgi\">\n";
	
	#$session->expire('+10m');
	#$session->flush();
}
else{
	print $page->header();
	unless($user eq $utente){
		print "<h1>Username inesistente.</h1>";
		print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../public_html/html/formLogin.html\">\n";
	}
	else {
		unless($pass eq $pwd){
			print "<h1>Password errata.</h1>";
			print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../public_html/html/formLogin.html\">\n";
		}
	}
}