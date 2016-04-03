#!/usr/bin/perl

use CGI;
use CGI qw(Link Title);
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use CGI::Session qw/-ip-match/;
use XML::LibXML;
use HTML::Template;
use File::Copy;
use utf8;
use HTML::Entities;

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

use File::Basename;

sub sanitize_filename {
    my $filename = $_[0];

    # rimozione di cartelle dal nome del file
    my ($name, $path, $extension) = fileparse($filename, '..*');
    $filename = $name . $extension;

    # sistemazione del nome del file
    $filename =~ tr/ /_/;
    $filename =~ s/^a-zA-Z0-9_.-//g;
    return $filename;
}

my $index= $page->param('index');

my $query = "//oggetto[\@id=\"$index\"]";
my $elemento = $radice->findnodes($query)->get_node(1);


if($elemento){#se l'indice è corretto
	$new_in_vista = $page->param('in_vista');
	$in_vista = $elemento->find("\@in_vista")->get_node(1);
	$in_vista->setValue("$new_in_vista");
		
	$new_nome = encode_entities($page->param('nome'));
	$nome = $elemento->find('nome/text()')->get_node(1);
	unless($new_nome eq $nome) {
		$nome = $elemento->find('nome')->get_node(1);
		$nome->removeChildNodes();
		$nome->appendText("$new_nome");
	}
	
	$tipo_categoria = $page->param('categoria');
	@new_tipo = split(' ', $tipo_categoria);
	$categoria = $new_tipo[0];
	shift(@new_tipo);
	$tipo = $elemento->find('tipo/text()')->get_node(1);
	unless(@new_tipo eq $tipo) {
		$tipo = $elemento->find('tipo')->get_node(1);
		$tipo->removeChildNodes();
		$tipo->appendText("@new_tipo");
	}
	
	$new_produttore = encode_entities($page->param('produttore'));
	$produttore = $elemento->find('produttore/text()')->get_node(1);
	unless($new_produttore eq $produttore) {
		$produttore = $elemento->find('produttore')->get_node(1);
		$produttore->removeChildNodes();
		$produttore->appendText("$new_produttore");
	}
	
	$new_altezza = encode_entities($page->param('altezza'));
	my $altezza = $elemento->findnodes('./dimensione/altezza/text()')->get_node(1);
	unless($new_altezza eq $altezza) { 
		$altezza = $elemento->find('./dimensione/altezza')->get_node(1);
		$altezza->removeChildNodes();
		$altezza->appendText("$new_altezza");
	}
	
	$new_lunghezza = encode_entities($page->param('lunghezza'));
	$lunghezza = $elemento->find('./dimensione/lunghezza/text()')->get_node(1);
	unless($new_lunghezza eq $lunghezza) {
		$lunghezza = $elemento->find('./dimensione/lunghezza')->get_node(1);
		$lunghezza->removeChildNodes();
		$lunghezza->appendText("$new_lunghezza");
	}
	
	$new_larghezza = encode_entities($page->param('larghezza'));
	$larghezza = $elemento->find('./dimensione/larghezza/text()')->get_node(1);
	unless($new_larghezza eq $larghezza) {
		$larghezza = $elemento->find('./dimensione/larghezza')->get_node(1);
		$larghezza->removeChildNodes();
		$larghezza->appendText("$new_larghezza");
	}
	
	@new_materiali = split(' ', $page->param('materiali'));
	$list_materiali = $elemento->find("materiale")->get_node(1);
	@materiali = split(' ', $list_materiali);
	unless(@new_materiali eq @materiali) {
		$n = @new_materiali;
		for($i=0; $i<5; $i++){
			$materiale = $elemento->find("materiale/nome[\@id_materiale =\"$i\"]")->get_node(1);
			if($materiale) {$materiale->removeChildNodes();}
			if($new_materiali[$i]) {$materiale->appendText("$new_materiali[$i]");}
		}
	}
	
	$new_colore = encode_entities($page->param('colore'));
	$colore = $elemento->find('colore/text()')->get_node(1);
	unless($new_colore eq $colore) { 
		$colore = $elemento->find('colore')->get_node(1);
		$colore->removeChildNodes();
		$colore->appendText("$new_colore");
	}
	
	$new_prezzo = encode_entities($page->param('prezzo'));
	$prezzo = $elemento->find('prezzo/text()')->get_node(1);
	unless($new_prezzo eq $prezzo) {
		$prezzo = $elemento->find('prezzo')->get_node(1);
		$prezzo->removeChildNodes();
		$prezzo->appendText("$new_prezzo");
	}
	
	$new_descrizione = encode_entities($page->param('descrizione'));
	$descrizione = $elemento->find('descrizione/text()')->get_node(1);
	unless($new_descrizione eq $descrizione) {
		$descrizione = $elemento->find('descrizione')->get_node(1);
		$descrizione->removeChildNodes();
		$descrizione->appendText("$new_descrizione");
	}


	$filehandle = $page->upload('image');
	if($filehandle)
	{
		$new_immagine_nome = sanitize_filename( $page->param('image') );
		$new_immagine = 'public_html/images/'. $new_immagine_nome;
		$immagine_nome = $elemento->find('immagine/text()')->get_node(1);
		$immagine = $elemento->find('immagine')->get_node(1);
		$immagine->removeChildNodes();
		if( not(unlink("../".$immagine_nome)))
		{
			print $page->header();
			print "Errore nell'eliminazione dell'immagine";#stampo un messaggio d'errore
	        exit;
		}
			
		$immagine->appendText("$new_immagine");

		

		# per l'upload dell'immagine
	    $CGI::POST_MAX = 1024 * 2000;    # 2MB
	    $filehandle = $page->upload('image');

	    #procedo con l'upload
	    copy( $filehandle, '../public_html/images/' . $new_immagine_nome );
    
    }#if 

	
	open OUT,">$file" || die("error");
	print OUT $doc->toString;
	close OUT;
}#if indice corretto
else {#indice scorretto
	#print "Content-type: text/html\n\n";
	print "Oggetto con id $index non esistente ";
}#else
print "Content-type: text/html\n\n";
print "<h1>Oggetto modificato con successo</h1>";
print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=./listing-prodotti.cgi\">";



}#controllo sessione 
else {
	print "Content-type: text/html\n\n";
	print "<h2>Sessione scaduta</h2>";
	print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../public_html/html/formLogin.html\">";
}