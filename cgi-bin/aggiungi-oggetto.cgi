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
use Scalar::Util qw(looks_like_number);

my $page = new CGI;

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


#trovo il nuovo ID
my @ids       = $radice->findnodes( '//' . "oggetto" );
my $max_id    = 0;

foreach my $id (@ids) {
    my $curr_id = $id->findvalue( '@' . "id" );
    $max_id = $curr_id if $max_id < $curr_id;
}
$max_id = $max_id + 1;

$check = 1; #questa varibaile mi serve per controllare se c'è almeno un campo non definito 
$var_oggetto = "";#stringa dove concateno tutti i campi definiti e, nel caso ne mancasse qualcuno, 
				  #invio tramite GET nuovamente al form di partenza

#RIcavo tutti i valori inseriti nel form
$id = $max_id;

$in_vista = $page->param('in_vista');
$var_oggetto .= "in_vista=".$in_vista;

$nome = encode_entities($page->param('nome'));
if(not($nome))
{
	$check = true;
}
else
{
	$var_oggetto .= "&nome=".$nome;
}
$tipo_categoria = $page->param('categoria');
if(not($tipo_categoria))
{
	$check = true;
}
else
{
	$var_oggetto .= "&tipo_categoria=".$tipo_categoria;
}
@tipo = split(' ', $tipo_categoria);
$categoria = $tipo[0];
shift(@tipo);
$immagine = sanitize_filename( $page->param('image') );
if(not($page->param('image')))
{
	$check = true;
}
else
{
	$var_oggetto .= "&image=1";#se l'immagine è stata inserita non posso salvarmi il percorso 
}							   #però posso allertare l'utente di inserirla di nuovo con una sentinella 

$altezza = encode_entities($page->param('altezza'));
if(not($altezza) || !looks_like_number($altezza))
{
	$check = true;
}
else
{
	$var_oggetto .= "&altezza=".$altezza;
}
$lunghezza = encode_entities($page->param('lunghezza'));
if(not($lunghezza) || !looks_like_number($lunghezza))
{
	$check = true;
}
else
{
	$var_oggetto .= "&lunghezza=".$lunghezza;
}
$larghezza = encode_entities($page->param('larghezza'));
if(not($larghezza) || !looks_like_number($larghezza))
{
	$check = true;
}
else
{
	$var_oggetto .= "&larghezza=".$larghezza;
}
$descrizione = encode_entities($page->param('descrizione'));
if(not($descrizione))
{
	$check = true;
}
else
{
	$var_oggetto .= "&descrizione=".$descrizione;
}
$list_materiali = encode_entities($page->param('materiali'));
if(not($list_materiali))
{
	$check = true;
}
else
{
	$var_oggetto .= "&materiali=".$list_materiali;
}
@materiali = split(' ', $list_materiali);
$colore = encode_entities($page->param('colore'));
if(not($colore))
{
	$check = true;
}
else
{
	$var_oggetto .= "&colore=".$colore;
}
$prezzo = encode_entities($page->param('prezzo'));
if(not($prezzo) || !looks_like_number($prezzo))
{
	$check = true;
}
else
{
	$var_oggetto .= "&prezzo=".$prezzo;
}


#verifico se il prodotto inserito esiste già
$esistente = $radice->find("//oggetto[nome=\"$nome\"]/nome/text()");
#se esiste
if($esistente){
	print $page->header();
	print "<h1>Oggetto esistente nel database</h1>";#stampo un messaggio d'errore
}
elsif($check != 1){#se manca qualche campo obbligatorio
	print $page->header();
	print "<h1>Campo obbligatorio nome mancante</h1>";#stampo un messaggio d'errore
	$var_oggetto .= "&check=true";
	print "<META HTTP-EQUIV=refresh CONTENT=\"0;URL=./nuovo_prodotto.cgi?$var_oggetto\">";
}
else {#se il prodotto non esiste già, e sono stati inseriti tutti i campi del form

	#comincio a creare la stringa new_ogetto che conterra tutti i dati del prodotto formattato seconda l'xml schema
	$new_oggetto = "\t\t<oggetto id=\"$id\" in_vista=\"$in_vista\">\n\t\t\t<nome>$nome</nome>\n";
	$new_oggetto = $new_oggetto."\t\t\t<tipo>@tipo</tipo>\n";
	$new_oggetto = $new_oggetto."\t\t\t<dimensione>\n\t\t\t\t<altezza um=\"cm\">$altezza</altezza>\n\t\t\t\t<lunghezza um=\"cm\">$lunghezza</lunghezza>\n\t\t\t\t<larghezza um=\"cm\">$larghezza</larghezza>\n\t\t\t</dimensione>\n";

	$new_oggetto = $new_oggetto."\t\t\t<materiale>\n";
	$n = @materiali;
	for($i=0; $i <5; $i++) {
		$new_oggetto = $new_oggetto."\t\t\t\t<nome id_materiale=\"$i\">$materiali[$i]</nome>\n";
	}
	$new_oggetto = $new_oggetto."\t\t\t</materiale>\n";
	

	$new_oggetto = $new_oggetto."\t\t\t<colore>$colore</colore>\n";
	$new_oggetto = $new_oggetto."\t\t\t<prezzo valuta=\"euro\">$prezzo</prezzo>\n";
	$new_oggetto = $new_oggetto."\t\t\t<descrizione>$descrizione</descrizione>\n";
	$new_oggetto = $new_oggetto."\t\t\t<immagine>public_html/images/$immagine</immagine>\n";
	$new_oggetto = $new_oggetto."\t\t</oggetto>\n";

	# per l'upload dell'immagine
    $CGI::POST_MAX = 1024 * 2000;    # 2MB
    my $filehandle = $page->upload('image');

    # stampiamo una pagina di errore se c'è
    # qualche problema
    if ( !$filehandle ) {
		print $page->header();
		print 'Impossibile caricare l\'immagine. Forse hai inserito un file più grande di 2<abbr title="Megabyte" xml:lang="en">MB</abbr>?';#stampo un messaggio d'errore
        exit;
    }
    #altrimenti procedo con l'upload'
    copy( $filehandle, '../public_html/images/' . $immagine );


	my $padre = $doc->findnodes("//catalogo/$categoria");
	if ($padre) {
		my $nodo = $parser->parse_balanced_chunk($new_oggetto) || die("frammento non ben formato");
		$padre->get_node(1)->appendChild($nodo) || die("non riesco a trovare il padre");
	}
	else{
		my $nonno = $doc->findnodes("//catalogo");
		if($nonno) {
			$new_oggetto = "\t<$categoria>\n\t\t$new_oggetto\n\t</$categoria>";
			my $nodo = $parser->parse_balanced_chunk($new_oggetto) || die("frammento non ben formato");
			$radice->appendChild($nodo) || die("no append");
		}
		else {
			$new_oggetto = "<catalogo>\n\t<$categoria>\n\t\t$new_oggetto\n\t</$categoria>\n</catalogo>";
			my $nodo = $parser->parse_balanced_chunk($new_oggetto) || die("frammento non ben formato");
			$radice->appendChild($nodo) || die("no append");
		}
		$new_oggetto = "<catalogo>\n".$new_oggetto."</catalogo>";
		my $nodo = $parser->parse_balanced_chunk($new_oggetto) || die("frammento non ben formato");
		$radice->appendChild($nodo) || die("no append");
	}

	open OUT,">$file" || die("error");
	print OUT $doc->toString;
	close OUT;
	print "Content-type: text/html\n\n";
	print "<h1>Oggetto inserito con successo</h1>";
	print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=./listing-prodotti.cgi\">"; 
}
}
else {
	print "Content-type: text/html\n\n";
	print "<h2>Sessione scaduta</h2>";
	print "<META HTTP-EQUIV=refresh CONTENT=\"1;URL=../public_html/html/formLogin.html\">";
}
