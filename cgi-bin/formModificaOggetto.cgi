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

my $index= $page->param('index');
my $query = "//oggetto[\@id=\"$index\"]";
my $elemento = $radice->findnodes($query)->get_node(1);
my $tipo = $elemento->find("tipo");
my $categoria = $elemento->find("categoria");
my $titolo = $elemento->find("nome");
my $descrizione = $elemento->find("descrizione");
my $prezzo = $elemento->find("prezzo");
my $list_materiali = $elemento->find("materiale");
@materiali = split(' ', $list_materiali);
my $immagine = $elemento->find("immagine");

my $altezza = $elemento->find("dimensione/altezza");
my $lunghezza = $elemento->find("dimensione/lunghezza");
my $larghezza = $elemento->find("dimensione/larghezza");

my $colore = $elemento->find("colore");


print "Content-type: text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Home - DaToSaAl Arredamenti snc</title>
		<meta name="title" content="Modifica prodotto - DaToSaAl Arredamenti"/>
		<meta name="author" content="Alberto Nicol&egrave;, Davide Tomasin, Guido Santi, Tommaso Zagni"/>
		<meta name="description" content="Pagina per la modifica dei prodotti dell'azienda DaToSaAl Arredamenti "/>
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
							<li class="menu-item">
								<a href="backend.cgi">Home</a>
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
							Ti trovi in: <a href="backend.cgi" xml:lang="en" ><span xml:lang="en">Home (backend)</span></a> &gt; <a href="listing-prodotti.cgi" >Listing prodotti</a> &gt; <span id="currentPage">Modifica prodotto</span>
						</div>

						<h2>Modifica prodotto</h2>

							<form enctype="multipart/form-data" method="post" id="modificaProdottoForm" action="./modifica-oggetto.cgi">
								<div class="block" >

									<label for="nome">Nome prodotto: </label>
									<input tabindex="1" title="inserisci nome" type="text" id="nome" name="nome" value ="$titolo" />
									<input type="hidden" name="index" id="index" value="$index"/>

								</div>
								
								<div class="block" >

									<label for="categoria" >Seleziona una categoria: </label>
	
									<select tabindex="2" title="scegli categoria" id="categoria" name="categoria" >
										<optgroup label="acconciatori">
											<option value="acconciatori Posti Lavoro" >Posti lavoro</option>
											<option value="acconciatori Poltrone" >Poltrone</option>
											<option value="acconciatori Lavaggi" >Lavaggi</option>
											<option value="acconciatori Attesa" >Attesa</option>
											<option value="acconciatori Reception" >Reception</option>
											<option value="acconciatori Mobili-Service" >Mobili-Service</option>
											<option value="acconciatori Accessori" >Accessori</option>
										</optgroup>
										<optgroup label="estetiche">
											<option value="estetiche Lettini" >Lettini</option>
											<option value="estetiche Poltrone" >Poltrone</option>
											<option value="estetiche Lavaggi" >Accessori</option>
											<option value="estetiche Attesa" >Attesa</option>
											<option value="estetiche Reception" >Reception</option>
											<option value="estetiche Mobili-Service" >Mobili-Service</option>
											<option value="estetiche Accessori" >Accessori</option>
										</optgroup>
									</select>
								</div>
								
								<fieldset>
									<legend>Dimensioni oggetto</legend>
									<ul>
										<li>
											<label for="altezza" >Altezza: </label>
											<input tabindex="3" title="insersci altezza" type="text" id="altezza" name="altezza" value="$altezza" />cm
										</li>
										<li>
											<label for="lunghezza" >Lunghezza: </label>
											<input tabindex="4" title="inserisci lunghezza" type="text" id="lunghezza" name="lunghezza" value="$lunghezza" />cm
										</li>
										<li>
											<label for="larghezza" >Larghezza: </label>
											<input tabindex="5" title="inserisci larghezza" type="text" id="larghezza" name="larghezza" value="$larghezza" />cm
										</li>
									</ul>
									
								</fieldset>

								<fieldset> 
									<legend>Immagini associate (caricando una nuova immagine, quella attuale verrà eliminata)</legend>
									<label for="image_insert" >Percorso immagine:  </label>
									<img src="../$immagine" alt="$alt" class="imgProdotto" />
									<input title="inserisci file immagine"  tabindex="6" type="file" name="image" id="image_insert" value="" />
								</fieldset>

								<fieldset>
									<legend >Descrizione prodotto</legend>
									<textarea title="inserisci descrizione" tabindex="7" rows="10" cols="120" id="descrizione" name="descrizione" >$descrizione</textarea>
								</fieldset>

								<fieldset>
									<legend>Materiali</legend>
									<label for="materiali" >Inserisci i materiali separati da uno spazio</label>
									<input tabindex="8" title="inserisci materiale" type="text" id="materiali" name="materiali" value ="@materiali" />
								</fieldset>
								
								<div class="block" >

									<label for="colore">Colore prodotto: </label>
									<input title="inserisci colore" tabindex="9" type="text" id="colore" name="colore" value = "$colore"/>

								</div>

								<div class="block" >
									<label for="prezzo" >Prezzo: </label>
									<input tabindex="10" title="inserisci prezzo" type="text" id="prezzo" name="prezzo" value = "$prezzo" />€
								</div>

								<div class="block" >
								<fieldset>
									<legend>Mostra prodotto in evidenza in Home Page</legend>
								</fieldset>
									si<input tabindex="11" title="metti oggetto in vista" type="radio" id="in_vista_1" name="in_vista" value="true" />
									no<input type="radio" tabindex="12" id="in_vista_2" title="metti oggetto non in vista" name="in_vista" value="false" checked="checked" />
								</div>
								<fieldset>
								<button type="submit" name="insert">Salva modifiche</button>	
								</fieldset>
							</form>
						
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
}
else {
	print "Content-type: text/html\n\n";
	print "<h2>Sessione scaduta</h2>";
	print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../public_html/html/formLogin.html\">";
}