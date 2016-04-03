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



my $query = "//oggetto[\@in_vista=\"true\"]";
my @elemento = $radice->findnodes($query);

print "Content-type: text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Home - DaToSaAl Arredamenti</title>
		<meta name="title" content="Home - DaToSaAl Arredamenti"/>
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
					<a href="javascript:void()" id="logo">
						<img src="../public_html/images/logo.png" title="logo" alt="Logo azienda DaToSaAl Arredamenti"/>
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
	                      <li id="home" class="menu-item corrente">
	                         <a href="javascript:void(0)">Home</a>
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
				</div>
			</div>
			<div id="content" >
				<div class="main" >
					<div class="content-full-width" >
						<div id="breadcrumb">
                     		Ti trovi in: <span xml:lang="en">Home</span>
                  		</div>
						<img class="full-width center" src="../public_html/images/immagine-home.jpg" alt="centro parrucchiere arredato da DaToSaAl" />
						<p>
							L'acconciatore, con la complessa variet&agrave; delle sue esigenze &eacute; al centro dell'impegno progettuale della DaToSaAl arredamenti.
							Un impegno di continuo sviluppo che ci porta come azienda leader del settore. Una grande variet&agrave; di articoli con espressioni
							tecniche innovative in grado di risolvere ogni Vostro problema d'arredo e di logistica. Richiedete l'esclusivo marchio che ne
							garantisce l'originalit&agrave; del prodotto con l'apposita firma a titolo di garanzia.
						</p>
					</div>
				</div>
			</div>
			<div id="prodotti-evidenza" >
				<div class="main" >
					<h2>Prodotti in primo piano</h2>
					<ul id="moduli_home" >
EOF
$number = @elemento;
for($i=0; $i <$number; $i++) {
	$nome = ($elemento[$i])->find("nome");
	$immagine = ($elemento[$i])->find("immagine");
	$alt = $immagine->get_node(1)->find("\@alt");
	$descrizione = ($elemento[$i])->find("descrizione");
	$index = ($elemento[$i])->find("\@id");

print <<EOF;
						<li class="modulo" >
							<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">
								<img src="../public_html/$immagine" alt="$alt"/>
							</a>
							<div>
								<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">$nome</a>
								<p class="desc_modulo_black" >$descrizione</p>
							</div>
						</li>
EOF
}	
print <<EOF;
					</ul>
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