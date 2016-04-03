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
	$check = $page->param('check');
	if($check){#se ci sono campi mancanti setto le classi e la stringa di alert per avvertire l'utente
		
		$campi_mancanti = ""; #lista dei campi mancanti 
		#setto le classi per visualizzare il campo mancante nel form
		$nome_novalue_class = ""; 
		$tipo_categoria_novalue_class = "";
		$immagine_novalue_class = "error";
		$altezza_novalue_class = "";
		$lunghezza_novalue_class = "";
		$larghezza_novalue_class = "";
		$descrizione_novalue_class = "";
		$materiali_novalue_class = "";
		$colore_novalue_class = "";
		$prezzo_novalue_class = "";		

		$nome = $page->param('nome');
		if(not($nome))
		{
			$nome_novalue_class = "error";
			$campi_mancanti .= "nome ";
		}

		$tipo_categoria = $page->param('tipo_categoria');
		if(not($tipo_categoria))
		{
			$campi_mancanti .= "categoria ";
		}
		@tipo = split(' ', $tipo_categoria);
		$categoria = $tipo[0];
		shift(@tipo);

		$altezza = $page->param('altezza');
		if(not($altezza))
		{
			$altezza_novalue_class = "error";
			$campi_mancanti .= "altezza ";
		}

		$lunghezza = $page->param('lunghezza');
		if(not($lunghezza))
		{
			$lunghezza_novalue_class = "error";
			$campi_mancanti .= "lunghezza ";
		}

		$larghezza = $page->param('larghezza');
		if(not($larghezza))
		{
			$larghezza_novalue_class = "error";
			$campi_mancanti .= "larghezza ";
		}

		$campi_mancanti .= "immagine ";

		$descrizione = $page->param('descrizione');
		if(not($descrizione))
		{
			$descrizione_novalue_class = "error";
			$campi_mancanti .= "descrizione ";
		}

		$materiali = $page->param('materiali');
		if(not($materiali))
		{
			$materiali_novalue_class = "error";
			$campi_mancanti .= "materiali ";
		}

		$colore = $page->param('colore');
		if(not($colore))
		{
			$colore_novalue_class = "error";
			$campi_mancanti .= "colore ";
		}

		$prezzo = $page->param('prezzo');
		if(not($prezzo))
		{
			$prezzo_novalue_class = "error";
			$campi_mancanti .= "prezzo ";
		}

		$in_vista = $page->param('in_vista');

	}#if - check = true => campi mancanti

print "Content-type: text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Home - DaToSaAl Arredamenti</title>
		<meta name="title" content="Nuovo Prodotto - DaToSaAl Arredamenti"/>
		<meta name="author" content="Alberto Nicol&egrave;, Davide Tomasin, Guido Santi, Tommaso Zagni"/>
		<meta name="description" content="Pagina per inserimento prodotti dell'azienda DaToSaAl Arredamenti"/>
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
						<img src="../public_html/images/logo.png" alt="logo azienda DaToSaAl Arredamenti"/>
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
								<a href="./backend.cgi">Home</a>
							</li>
							<li class="menu-item ">
								<a href="./listing-prodotti.cgi">Prodotti</a>
							</li>
							<li class="menu-item corrente">
								<a href="javascript:void(0);">Aggiungi prodotto</a>
							</li>
							<li class="menu-item ">
								<a href="./logout.cgi">Esci</a>
							</li>
						</ul>
					</div>
				</div>
			</div>
			<div id="content" >
				<div class="main" >
					<div class="content-full-width" >
						<div id="breadcrumb">
							Ti trovi in: <a href="backend.cgi" ><span xml:lang="en">Home (backend)</span></a> &gt; <span id="currentPage">Nuovo Prodotto</span>
						</div>

						<h2>Nuovo prodotto</h2>
EOF
						if($check)
						{
							print '<p id="alert_message" >Campi obbligatori errati o mancanti: '.$campi_mancanti.'</p>';
						}
print <<EOF;

							<form enctype="multipart/form-data" method="post" id="modificaProdottoForm" action="./aggiungi-oggetto.cgi">
							<fieldset>
								<legend>Tutti i campi sono obbligatori</legend>
								<div class="block" >

									<label for="nome" accesskey="N">Nome prodotto: </label>
									<input class="$nome_novalue_class" tabindex="1" title="Inserisci il nome" type="text" id="nome" name="nome" value="$nome" />
								</div>
								
								<div class="block" >

									<label for="categoria" accesskey="S" >Seleziona una categoria: </label>
									<select tabindex="2" title="scegli categoria"  id="categoria" name="categoria" >
										<optgroup label="acconciatori">
EOF
										if($tipo_categoria eq "acconciatori Posti Lavoro" )
										{
											print '<option value="acconciatori Posti Lavoro" selected >Posti lavoro</option>';
										}
										else
										{
											print '<option value="acconciatori Posti Lavoro">Posti lavoro</option>';
										}	
										if($tipo_categoria eq "acconciatori Poltrone" )
										{
											print '<option value="acconciatori Poltrone" selected >Poltrone</option>';
										}
										else
										{
											print '<option value="acconciatori Poltrone" >Poltrone</option>';
										}	
										if($tipo_categoria eq "acconciatori Lavaggi" )
										{
											print '<option value="acconciatori Lavaggi" selected >Lavaggi</option>';
										}
										else
										{
											print '<option value="acconciatori Lavaggi" >Lavaggi</option>';
										}	
										if($tipo_categoria eq "acconciatori Attesa" )
										{
											print '<option value="acconciatori Attesa" selected >Attesa</option>';
										}
										else
										{
											print '<option value="acconciatori Attesa" >Attesa</option>';
										}	
										if($tipo_categoria eq "acconciatori Reception" )
										{
											print '<option value="acconciatori Reception" selected >Reception</option>';
										}
										else
										{
											print '<option value="acconciatori Reception" >Reception</option>';
										}	
										if($tipo_categoria eq "acconciatori Mobili-Service" )
										{
											print '<option value="acconciatori Mobili-Service" selected >Mobili-Service</option>';
										}
										else
										{
											print '<option value="acconciatori Mobili-Service" >Mobili-Service</option>';
										}	
										if($tipo_categoria eq "acconciatori Accessori" )
										{
											print '<option value="acconciatori Accessori" selected >Accessori</option>';
										}
										else
										{
											print '<option value="acconciatori Accessori" >Accessori</option>';
										}	
														print '</optgroup>
														<optgroup label="estetiche">';
										if($tipo_categoria eq "estetiche Lettini" )
										{
											print '<option value="estetiche Lettini" selected >Lettini</option>';
										}
										else
										{
											print '<option value="estetiche Lettini" >Lettini</option>';
										}	
										if($tipo_categoria eq "estetiche SPA" )
										{
											print '<option value="estetiche SPA" selected >SPA</option>';
										}
										else
										{
											print '<option value="estetiche SPA" >SPA</option>';
										}	
										if($tipo_categoria eq "estetiche Attesa" )
										{
											print '<option value="estetiche Attesa" selected >Attesa</option>';
										}
										else
										{
											print '<option value="estetiche Attesa" >Attesa</option>';
										}	
										if($tipo_categoria eq "estetiche Reception" )
										{
											print '<option value="estetiche Reception" selected >Reception</option>';
										}
										else
										{
											print '<option value="estetiche Reception" >Reception</option>';
										}	
										if($tipo_categoria eq "estetiche Mobili-Service" )
										{
											print '<option value="estetiche Mobili-Service" selected >Mobili-Service</option>';
										}
										else
										{
											print '<option value="estetiche Mobili-Service" >Mobili-Service</option>';
										}	
										if($tipo_categoria eq "estetiche Accessori" )
										{
											print '<option value="estetiche Accessori" selected >Accessori</option>';
										}
										else
										{
											print '<option value="estetiche Accessori" >Accessori</option>';
										}	
print <<EOF;
										</optgroup>
									</select>
								</div>
								
								<fieldset>
									<legend>Dimensioni oggetto</legend>
									<ul>
										<li>
											<label for="altezza" accesskey="A" >Altezza: </label>
											<input class="$altezza_novalue_class" value="$altezza" tabindex="3" title="inserisci altezza" type="text" id="altezza" name="altezza"  />cm
										</li>
										<li>
											<label for="lunghezza" accesskey="L" >Lunghezza: </label>
											<input class="$lunghezza_novalue_class" value="$lunghezza" tabindex="4" title="inserisci lunghezza" type="text" id="lunghezza" name="lunghezza" />cm
										</li>
										<li>
											<label for="larghezza" accesskey="L" >Larghezza: </label>
											<input class="$larghezza_novalue_class" value="$larghezza" tabindex="5" title="insersci larghezza" type="text" id="larghezza" name="larghezza" />cm
										</li>
									</ul>
									
								</fieldset>

								<fieldset>
									<legend>Immagini associate</legend>
									<label for="image_insert" >Percorso immagine:  </label>
									<input class="$immagine_novalue_class" tabindex="6" title="insersci file" type="file" name="image" id="image_insert" />
								</fieldset>

								<fieldset>
									<legend >Descrizione prodotto</legend>
									<textarea class="$descrizione_novalue_class" title="inseriscie descrizione" tabindex="7" rows="10" cols="120" id="descrizione" name="descrizione" >$descrizione</textarea>
								</fieldset>

								<fieldset>
									<legend>Materiali</legend>
									<label for="materiali" accesskey="M">Inserisci i materiali separati da uno spazio</label>
									<input class="$materiali_novalue_class" value="$materiali" tabindex="8" title="inserisci materiali" type="text" id="materiali" name="materiali" />
								</fieldset>
								
								<div class="block" >

									<label for="colore" accesskey="C">Colore prodotto: </label>
									<input class="$colore_novalue_class" value="$colore" tabindex="9" title="inserisci colore" type="text" id="colore" name="colore" />

								</div>

								<div class="block" >
									<label for="prezzo" accesskey="P" >Prezzo: </label>
									<input class="$prezzo_novalue_class" value="$prezzo" tabindex="10" title="inserisci prezzo" type="text" id="prezzo" name="prezzo" />€
								</div>

								<div class="block" >
								<fieldset>
									<legend>Mostra prodotto in evidenza in Home Page</legend>
EOF
									if($in_vista eq "true")
									{
										print '
											<input tabindex="9" title="metti oggetto in vista"  type="radio" id="in_vista_1" name="in_vista" value="true" checked="checked" />si
												<input title="metti oggetto non in vista" tabindex="10" type="radio" id="in_vista_2" name="in_vista" value="false"  />no';
									}
									else
									{
										print '<input tabindex="11"  type="radio" id="in_vista_3" title="metti oggetto in vista" name="in_vista" value="true"  />si
												<input tabindex="12" type="radio" id="in_vista_4" title="metti oggetto non in vista" name="in_vista" value="false" checked="checked" />no';
									}
	
									
print <<EOF;

								</fieldset>	
								</div>

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
	print "<META HTTP-EQUIV=refresh CONTENT=\"2;URL=../public_html/html/formLogin.html\">\n";
}