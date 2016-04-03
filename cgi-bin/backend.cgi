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

my $file = '../data/utenti.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my $radice = $doc->getDocumentElement;

$nodo = $radice->findnodes("//utente[username=\"$nome_utente\"]")->get_node(0);
$nome = $nodo->find("persona/nome/text()");
$cognome = $nodo->find("persona/cognome/text()");

print "Content-type: text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Home Backend - DaToSaAl Arredamenti </title>
		<meta name="title" content="Home Backend - DaToSaAl Arredamenti"/>
		<meta name="author" content="Alberto Nicol&egrave;, Davide Tomasin, Guido Santi, Tommaso Zagni"/>
		<meta name="description" content="Pagina per la visualizzazione e gestione dei prodotti dell'azienda DaToSaAl Arredamenti"/>
		<meta name="keywords" content="arredamenti, parrucchiere, profumerie, estetiste"/>
		<meta name="language" content="italian it"/>
		<meta name="viewport" content="width=device-width, initial-scale=1"/>

		<link type="text/css" rel="stylesheet" href="../public_html/css/main.css" media="handheld, screen"/>
		<link type="text/css" rel="stylesheet" href="../public_html/css/responsive.css" media="handheld, screen"/>
		<link type="text/css" rel="stylesheet" href="../public_html/css/print.css" media="print"/>

		<script type="text/javascript" src="../public_html/js/jquery-2.1.4.min.js" ></script>
		<script type="text/javascript" src="../public_html/js/script.js" ></script>
	</head>
	<body class="home">
		<div id="all">
			<div id="header">
				<div class="main">
					<a href="javascript:void()" id="logo">					
						<img src="../public_html/images/logo.png" alt="Logo azienda DaToSaAl"/>
					</a>
					<div id="headerText">
						<h1>DaToSaAl Arredamenti</h1>
					</div>
					<div class="btn-responsive-menu">
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
						<span class="icon-bar"></span>
					</div>
					<div id="salta"><a href="#content">Vai al contenuto</a></div>
					<div id="mainmenu">
						<ul id="menu">
							<li class="menu-item corrente">
								<a href="javascript:void(0);">Home</a>
							</li>
							<li class="menu-item ">
								<a href="listing-prodotti.cgi">Prodotti</a>
							</li>
							<li class="menu-item ">
								<a href="nuovo_prodotto.cgi">Aggiungi prodotto</a>
							</li>
							<li class="menu-item ">
								<a href="logout.cgi">Esci</a>
							</li>
						</ul>
					</div>
				</div>
			</div>
			<div id="content" >
				<div class="main" >
					<div class="content-full-width" >
						<div id="breadcrumb">
							Ti trovi in: <span xml:lang="en">Home (backend)</span>
						</div>
						<div id="benvenuto">
							Benvenuto/a $nome $cognome nell'area riservata, da qui puoi gestire i tuoi prodotti 
						</div>
					</div>
				</div>
			</div>
			<div id="freccia">
				<a href="#">torna su</a>
			</div>
			<div id="footer">
				<div class="bottom">
					<div class="main">
						<p>DaToSaAl arredamenti - <span xml:lang="en">Made by</span> iSantiMembri</p>
					</div>
				</div>

			</div>
		</div>
	</body>
</html>
EOF
exit;
}
else {
	print "Content-type: text/html\n\n";
	print "<h2>Sessione scaduta</h2>";
	print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../public_html/html/formLogin.html\">";
}