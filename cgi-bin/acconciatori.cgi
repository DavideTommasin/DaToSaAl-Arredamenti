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

my $query = "//acconciatori/oggetto";
my @acconciatori = $radice->findnodes($query);
@posti;
@poltrone;
@lavaggi;
@attesa;
@reception;
@mobili;
@accessori;
$categoria="acconciatori";

$number = @acconciatori;
for($i=0; $i <$number; $i++) {
	$tipo = $acconciatori[$i]->find("tipo");
	if($tipo eq "Posti Lavoro") { push(@posti, $acconciatori[$i]);}
	elsif($tipo eq "Poltrone") { push(@poltrone, $acconciatori[$i]);}
	elsif($tipo eq "Lavaggi") { push(@lavaggi, $acconciatori[$i]);}
	elsif($tipo eq "Attesa") { push(@attesa, $acconciatori[$i]);}
	elsif($tipo eq "Reception") { push(@reception, $acconciatori[$i]);}
	elsif($tipo eq "Mobili-Service") { push(@mobili, $acconciatori[$i]);}
	elsif($tipo eq "Accessori") { push(@accessori, $acconciatori[$i]);}
}

print "Content-type: text/html\n\n";
print <<EOF;
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="it" lang="it">
   <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
      <title>Home - DaToSaAl Arredamenti snc</title>
      <meta name="title" content="Acconciatori - DaToSaAl Arredamenti"/>
      <meta name="author" content="Alberto Nicol&egrave;, Davide Tomasin, Guido Santi, Tommaso Zagni"/>
      <meta name="description" content="Pagina acconciatori dell'azienda DaToSaAl Arredamenti"/>
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
               <a href="index.cgi" id="logo">
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
                         <li id="acconciatori" class="menu-item corrente">
                            <a href="javascript:void(0);">Acconciatori</a>
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
                     Ti trovi in: <a href="index.cgi" ><span xml:lang="en">Home</span></a> &gt; <span id="currentPage">Prodotti acconciatori</span>
                  </div>
                  <h2 id="title" >
                     Prodotti acconciatori
                  </h2>
                  <ul id="list-categorie" >
                     <li>
                        <a id="PostiLavoro" href="sottocategoria.cgi?categoria=$categoria&amp;tipo=Posti Lavoro">Posti lavoro</a>
                        
EOF

$number = @posti;
for($i=0; $i <$number; $i++) {
	$nome = $posti[$i]->find("nome");
	$immagine = $posti[$i]->find("immagine");
	$alt = $immagine->get_node(1)->find("\@alt");
	$descrizione = $posti[$i]->find("descrizione");
	$index = $posti[$i]->find("\@id");
		
	print <<EOF;
					<ul>
						<li class="modulo" >
							<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">
								<img src="../$immagine" alt="$alt"/>
							</a>
							<div>
								<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">$nome</a>
								<p class="desc_modulo_black" >$descrizione</p>
							</div>
						</li>
						</ul>
EOF
}
print <<EOF;
                        
                     </li>
                     <li>
                        <a id="Poltrone" href="sottocategoria.cgi?categoria=$categoria&amp;tipo=Poltrone">Poltrone</a>
                       
EOF

$number = @poltrone;
for($i=0; $i <$number; $i++) {
	$nome = $poltrone[$i]->find("nome");
	$immagine = $poltrone[$i]->find("immagine");
	$alt = $immagine->get_node(1)->find("\@alt");
	$descrizione = $poltrone[$i]->find("descrizione");
	$index = $poltrone[$i]->find("\@id");
		
	print <<EOF;
		 			<ul>
						<li class="modulo" >
							<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">
								<img src="../$immagine" alt="$alt"/>
							</a>
							<div>
								<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">$nome</a>
								<p class="desc_modulo_black" >$descrizione</p>
							</div>
						</li>
					</ul>
EOF
}
print <<EOF;
                        
                     </li>
                     <li>
                        <a id="Lavaggi" href="sottocategoria.cgi?categoria=$categoria&amp;tipo=Lavaggi">Lavaggi</a>
EOF

$number = @lavaggi;
for($i=0; $i <$number; $i++) {
	$nome = $lavaggi[$i]->find("nome");
	$immagine = $lavaggi[$i]->find("immagine");
	$alt = $immagine->get_node(1)->find("\@alt");
	$descrizione = $lavaggi[$i]->find("descrizione");
	$index = $lavaggi[$i]->find("\@id");
		
	print <<EOF;
					<ul>
						<li class="modulo" >
							<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">
								<img src="../$immagine" alt="$alt"/>
							</a>
							<div>
								<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">$nome</a>
								<p class="desc_modulo_black" >$descrizione</p>
							</div>
						</li>
					  </ul>
EOF
}
print <<EOF;
                     
                     </li>
                     <li>
                        <a id="Attesa" href="sottocategoria.cgi?categoria=$categoria&amp;tipo=Attesa">Attesa</a>
EOF

$number = @attesa;
for($i=0; $i <$number; $i++) {
	$nome = $attesa[$i]->find("nome");
	$immagine = $attesa[$i]->find("immagine");
	$alt = $immagine->get_node(1)->find("\@alt");
	$descrizione = $attesa[$i]->find("descrizione");
	$index = $attesa[$i]->find("\@id");
		
	print <<EOF;
		 			<ul>
						<li class="modulo" >
							<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">
								<img src="../$immagine" alt="$alt"/>
							</a>
							<div>
								<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">$nome</a>
								<p class="desc_modulo_black" >$descrizione</p>
							</div>
						</li>
					</ul>
EOF
}
print <<EOF;

                     </li>
                     <li>
                        <a id="Reception" href="sottocategoria.cgi?categoria=$categoria&amp;tipo=Reception">Reception</a>
EOF

$number = @reception;
for($i=0; $i <$number; $i++) {
	$nome = $reception[$i]->find("nome");
	$immagine = $reception[$i]->find("immagine");
	$alt = $immagine->get_node(1)->find("\@alt");
	$descrizione = $reception[$i]->find("descrizione");
	$index = $reception[$i]->find("\@id");
		
	print <<EOF;
					<ul>
						<li class="modulo" >
							<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">
								<img src="../$immagine" alt="$alt"/>
							</a>
							<div>
								<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">$nome</a>
								<p class="desc_modulo_black" >$descrizione</p>
							</div>
						</li>
					 </ul>
EOF
}
print <<EOF;
                     </li>
                     <li>
                        <a id="Mobili" href="sottocategoria.cgi?categoria=$categoria&amp;tipo=Mobili-Service">Mobili - Service</a>
                       
EOF

$number = @mobili;
for($i=0; $i <$number; $i++) {
	$nome = $mobili[$i]->find("nome");
	$immagine = $mobili[$i]->find("immagine");
	$alt = $immagine->get_node(1)->find("\@alt");
	$descrizione = $mobili[$i]->find("descrizione");
	$index = $mobili[$i]->find("\@id");
		
	print <<EOF;
				 	<ul>
						<li class="modulo" >
							<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">
								<img src="../$immagine" alt="$alt"/>
							</a>
							<div>
								<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">$nome</a>
								<p class="desc_modulo_black" >$descrizione</p>
							</div>
						</li>
					  </ul>
EOF
}
print <<EOF;
                     
                     </li>
                     <li>
                        <a id="Accessori" href="sottocategoria.cgi?categoria=$categoria&amp;tipo=Accessori">Accessori</a>
EOF

$number = @accessori;
for($i=0; $i <$number; $i++) {
	$nome = $accessori[$i]->find("nome");
	$immagine = $accessori[$i]->find("immagine");
	$alt = $immagine->get_node(1)->find("\@alt");
	$descrizione = $accessori[$i]->find("descrizione");
	$index = $accessori[$i]->find("\@id");
		
	print <<EOF;
					<ul>
						<li class="modulo" >
							<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">
								<img src="../$immagine" alt="$alt"/>
							</a>
							<div>
								<a href="./print-oggetto.cgi?index=$index" class="titolo_modulo titolo_black">$nome</a>
								<p class="desc_modulo_black" >$descrizione</p>
							</div>
						</li>
					</ul>
EOF
}
print <<EOF;
                     </li>
                  </ul>
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