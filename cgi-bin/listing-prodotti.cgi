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

print "Content-type: text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
		<title>Prodotti - DaToSaAl Arredamenti snc</title>
		<meta name="title" content="Lista prodotti - DaToSaAl Arredamenti"/>
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
					<a href="backend.cgi" id="logo">
						<img src="../public_html/images/logo.png" alt="definire"/>
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
							<li id="definire1" class="menu-item">
								<a href="backend.cgi">Home</a>
							</li>
							<li id="definire2" class="menu-item corrente">
								<a href="javascript:void(0);">Prodotti</a>
							</li>
							<li id="definire3" class="menu-item ">
								<a href="nuovo_prodotto.cgi">Aggiungi prodotto</a>
							</li>
							<li id="definire4" class="menu-item ">
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
							Ti trovi in: <a href="backend.cgi" ><span xml:lang="en">Home (backend)</span></a> &gt; <span id="currentPage">Prodotti</span>
						</div>

						<h2 id="title" >
							Prodotti
						</h2>

						<form id="formRicercaProdotti" action="./listing-prodotti.cgi?=0">
							<div class="per lui">
							<label for="categoriaVisualizzata" >Categoria prodotti visualizzati</label>
							<select id="categoriaVisualizzata" name="categoriaVisualizzata" >
								<option value="" >Tutti</option>
								<optgroup label="acconciatori">
EOF
										$tipo_categoria = $page->param("categoriaVisualizzata");
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

							<button type="submit" >Ricerca</button>
						</div>


						</form>

						<table id="productsList" summary="La tabella mostra tutti i prodotti presenti nel sito. Ogni riga mostra un prodotto, la prima colonna mostra l'ID, la seconda il nome, la terza la categoria, la quarta &egrave; un link alla pagina per modificare il prodotto e la quinta permette l'eliminazione del prodotto ">
								<tr>
									<th scope="col">ID</th>
									<th scope="col">Nome Prodotto</th>
									<th scope="col">Categoria</th>
									<th scope="col">Modifca</th>
									<th scope="col">Elimina</th>
								</tr>
							
EOF
$categoriaVisualizzata=$page->param("categoriaVisualizzata");
if($categoriaVisualizzata) {
	@new_tipo = split(' ', $categoriaVisualizzata);
	$categoria= $new_tipo[0];
	shift(@new_tipo);
	$newTipo = join(' ', @new_tipo);
	@elemento = $radice->findnodes("//$categoria/oggetto");
}
else {
	@elemento = $radice->findnodes("//oggetto");

}
$number = @elemento;

for($i=0; $i <$number; $i++) {
	$tipo=$elemento[$i]->find("tipo");
	if(!$categoriaVisualizzata or ($newTipo eq $tipo)){
		$id =$elemento[$i]->find("\@id");
		$nome=$elemento[$i]->find("nome");
		$index = $elemento[$i]->find("\@id");
		print<<EOF;
								<tr>
								
									<td scope="row" class="idProdotto" >#$id</td>
									<td scope="row" class="nomeProdotto" >
										<a href="./print-oggetto.cgi?index=$index">$nome</a>
									</td>
									<td scope="row" class="catProdotto" >$tipo</td>
									<td scope="row"><a class="modificaProdotto" href="formModificaOggetto.cgi?index=$id">Modfica</a></td>
									<td scope="row"><a class="eliminaProdotto" href="rimuovi-oggetto.cgi?index=$id">Elimina</a></td>
								</tr>
								
EOF
	}
}
print <<EOF;
								
						</table>
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