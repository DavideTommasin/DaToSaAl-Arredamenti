#!/usr/bin/perl

use CGI;
use CGI qw(Link Title);
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use CGI::Session qw/-ip-match/;
use XML::LibXML;
use HTML::Template;
use utf8;

$page = new CGI;

my $file = '../data/nostroCatalogo.xml';
my $parser = XML::LibXML->new();
my $doc = $parser->parse_file($file);
my $radice = $doc->getDocumentElement;

$index= $page->param('index');
my $query = "//oggetto[\@id=\"$index\"]";
my $elemento = $radice->findnodes($query)->get_node(1);
my $tipo = $elemento->find("tipo");
my $categoria = $elemento->parentNode->nodeName;
my $titolo = $elemento->find("nome");
my $descrizione = $elemento->find("descrizione");
my $prezzo = $elemento->find("prezzo");
my $list_materiali = $elemento->find("materiale");
@materiali = split(' ', $list_materiali);
my $immagine = $elemento->find("immagine");
my $alt = $immagine->get_node(1)->find("\@alt");

my $altezza = $elemento->find("dimensione/altezza");
my $lunghezza = $elemento->find("dimensione/lunghezza");
my $larghezza = $elemento->find("dimensione/larghezza");

my $colore = $elemento->find("colore");

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

print "Content-type: text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Home - DaToSaAl Arredamenti</title>
		<meta name="title" content="Posti lavoro - DaToSaAl Arredamenti"/>
		<meta name="author" content="Alberto Nicol&egrave;, Davide Tomasin, Guido Santi, Tommaso Zagni"/>
		<meta name="description" content="Pagina principale dell'azienda DaToSaAl Arredamenti"/>
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
				 <a href="backend.cgi" id="logo">
                  <img src="../public_html/images/logo.png" alt="Logo azienda DaToSaAl Arredamenti"/>
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
EOF
					if($nome_utente) {
print <<EOF;
						<div id="mainmenu">
							<ul id="menu">
								<li class="menu-item">
									<a href="backend.cgi">Home</a>
								</li>
								<li class="menu-item ">
									<a href="listing-prodotti.cgi">Prodotti</a>
								</li>
								<li class="menu-item ">
									<a href="./nuovo_prodotto.cgi">Aggiungi prodotto</a>
								</li>
								<li class="menu-item ">
									<a href="logout.cgi">Esci</a>
								</li>
							</ul>
						</div>
EOF
					}
					else {
print <<EOF;
	                   <div id="mainmenu">
	                      <ul id="menu">
	                         <li id="home" class="menu-item">
	                            <a href="index.cgi">Home</a>
	                         </li>
	                         <li id="contatti" class="menu-item ">
	                            <a href="../public_html/html/contatti.html">Contatti</a>
	                         </li>
	                         <li id="chiSiamo" class="menu-item ">
	                            <a href="../public_html/html/chi-siamo.html">Chi siamo</a>
	                         </li>
	                         <li id="estetiche" class="menu-item sub-menu-item" >
	                            <a href="estetiche.cgi">Estetiche</a>
	                            <ul>
	                               <li id="esteticheLettini" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=estetiche&amp;tipo=Lettini">Lettini</a>
	                               </li>
	                               <li id="esteticheSPA" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=estetiche&amp;tipo=SPA">SPA</a>
	                               </li>
	                               <li id="esteticheAttesa" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=estetiche&amp;tipo=Attesa">Attesa</a>
	                               </li>
	                               <li id="esteticheReception" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=estetiche&amp;tipo=Reception">Reception</a>
	                               </li>
	                               <li id="esteticheMobili" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=estetiche&amp;tipo=Mobili-Service">Mobili-Service</a>
	                               </li>
	                               <li id="esteticheAccessori" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=estetiche&amp;tipo=Accessori">Accessori</a>
	                               </li>
	                            </ul>
	                         </li>
	                         <li id="acconciatori" class="menu-item ">
	                            <a href="acconciatori.cgi">Acconciatori</a>
	                            <ul>
	                               <li id="acconciatoriPostiLavoro" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=acconciatori&amp;tipo=Posti Lavoro">Posti Lavoro</a>
	                               </li>
	                               <li id="acconciatoriPoltrone" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=acconciatori&amp;tipo=Poltrone">Poltrone</a>
	                               </li>
	                               <li id="acconciatoriLavaggi" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=acconciatori&amp;tipo=Lavaggi">Lavaggi</a>
	                               </li>
	                               <li id="acconciatoriAttesa" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=acconciatori&amp;tipo=Attesa">Attesa</a>
	                               </li>
	                               <li id="acconciatoriReception" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=acconciatori&amp;tipo=Reception">Reception</a>
	                               </li>
	                               <li id="acconciatoriMobili" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=acconciatori&amp;tipo=Mobili-Service">Mobili-Service</a>
	                               </li>
	                               <li id="acconciatoriAccessori" class="menu-item sub-menu-item">
	                                  <a href="sottocategoria.cgi?categoria=acconciatori&amp;tipo=Accessori">Accessori</a>
	                               </li>
	                            </ul>
	                         </li>
	                      </ul>
	                   </div>
EOF
                   }
print <<EOF;
            	</div>
			</div>
			<div id="content" >
				<div class="main" >
					<div class="content-full-width" >
						<div id="breadcrumb">
EOF
							if($nome_utente) {
print <<EOF;
								Ti trovi in: <a href="backend.cgi" ><span xml:lang="en">Home (backend)</span></a> &gt; <a href="listing-prodotti.cgi" >Listing prodotti</a> &gt; <span id="currentPage">$titolo</span>
EOF
							}
							else{
print <<EOF;
								Ti trovi in: <a href="index.cgi" ><span xml:lang="en">Home</span></a> &gt; <a href="$categoria.cgi" >$categoria</a> &gt; <a href="sottocategoria.cgi?categoria=$categoria&amp;tipo=$tipo" >$tipo</a> &gt; <span id="currentPage">$titolo</span>
EOF
							}
print <<EOF;
						</div>

						<h2 id="title-prodotto" >
							$titolo
						</h2>

						<img src="../$immagine" alt="$alt" class="imgProdotto" />

						<p class="descrizioneProdotto" >
							$descrizione
						</p>

						<dl class="materiali" >
							<dt class="carat" >Materiali:</dt>
							<dd>$materiali[0]</dd>
							<dd>$materiali[1]</dd>
							<dd>$materiali[2]</dd>
							<dd>$materiali[3]</dd>
							<dd>$materiali[4]</dd>
						</dl>
						
						<dl class="dimensioni" >
							<dt class="carat" >Dimensioni:</dt>
							<dd>Altezza: $altezza</dd>
							<dd>Lunghezza: $lunghezza</dd>
							<dd>Larghezza: $larghezza</dd>
						</dl>

						<p class="prezzo" >
							<span class="carat" >Prezzo:</span> <span class="valore" >$prezzo €</span>
						</p>
						
						<p class="colore" >
							<span class="carat" >Colore:</span> $colore
						</p>

					</div>
				</div>
			</div>
			<div id="freccia">
				<a href="#">torna su</a>
			</div>
			<div id="footer">
				<div class="bottom">
					<div class="main">
						<p>DaToSaAl arredamenti -<span xml:lang="en">Made by</span> iSantiMembri</p>
					</div>
				</div>

			</div>
		</div>
	</body>
</html>
EOF
exit;