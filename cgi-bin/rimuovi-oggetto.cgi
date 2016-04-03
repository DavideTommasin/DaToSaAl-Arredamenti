#!/usr/bin/perl

use CGI;
use CGI qw(Link Title);
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use CGI::Session qw/-ip-match/;
use XML::LibXML;
use HTML::Template;
use utf8;

$page = new CGI;

sub getSession() {
	$session = CGI::Session->load() or die $!;
	if ($session->is_expired || $session->is_empty ) {
		return undef;
	} 
	else {
		my $utente = $session->param('utente');
		return $utente;
	}
}

$nome_utente = getSession();
if($nome_utente) {

my $file = '../data/nostroCatalogo.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my $radice = $doc->getDocumentElement;

#importo un parametro numerico e lo inserisco nella variabile $index
$index= $page->param('index');
my $query = "//oggetto[\@id=\"$index\"]";
my $elemento = $radice->findnodes($query)->get_node();
$immagine_nome = $elemento->find('immagine/text()')->get_node(1);
if( not(unlink("../".$immagine_nome)))
{
	print $page->header();
	print "Errore nell'eliminazione dell'immagine";#stampo un messaggio d'errore
    exit;
}

my $padre = $elemento->parentNode; 
$padre->removeChild($elemento);

open OUT,">$file" || die("error");
print OUT $doc->toString;

print "Content-type: text/html\n\n";
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=./listing-prodotti.cgi\">";
}
else {
	print "Content-type: text/html\n\n";
	print "<h2>Sessione scaduta</h2>";
	print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../public_html/html/formLogin.html\">";
}