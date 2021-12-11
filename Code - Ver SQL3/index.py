#!/usr/bin/env python3
import cgi 

Page = """<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

    <title>Base de donnees league of legends</title>
  </head>
  <body>
    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.6.0/dist/umd/popper.min.js" integrity="sha384-KsvD1yqQ1/1+IA7gi3P0tyJcT3vR+NdBTt13hSJ2lnve8agRGXTTyNaBYmCR/Nwi" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.min.js" integrity="sha384-nsg8ua9HAw1y0W1btsyWgBklPnCUAFLuTMS2G72MMONqmOymq585AcH49TLBQObG" crossorigin="anonymous"></script>
   -->
    <div class="p-3 mb-2 bg-dark text-white"> <h5>Base de donnees League of legends</h5>
      <hr></hr>
      Trier a partir de...
        <div class="btn-group">
            <button type="button" class="btn btn-outline-light">un nom de Champion</button>
            <button type="button" class="btn btn-light dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">
                  <form action="view_championA.py" method="post">
                    <input type="submit" value="A" name="ChampionA"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championF.py" method="post">
                    <input type="submit" value="F" name="ChampionF"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championI.py" method="post">
                    <input type="submit" value="I" name="ChampionI"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championJ.py" method="post">
                    <input type="submit" value="J" name="ChampionJ"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championK.py" method="post">
                    <input type="submit" value="K" name="ChampionK"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championM.py" method="post">
                    <input type="submit" value="M" name="ChampionM"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championN.py" method="post">
                    <input type="submit" value="N" name="ChampionN"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championR.py" method="post">
                    <input type="submit" value="R" name="ChampionR"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championS.py" method="post">
                    <input type="submit" value="S" name="ChampionS"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championT.py" method="post">
                    <input type="submit" value="T" name="ChampionT"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_championW.py" method="post">
                    <input type="submit" value="W" name="ChampionW"/>
                  </form>
                </a></li>
            </ul>
        </div>
        <div class="btn-group">
            <button type="button" class="btn btn-outline-secondary">un Skin de Champion</button>
            <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">
                <form action="view_skinA.py" method="post">
                  <input type="submit" value="A" name="SkinA"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinF.py" method="post">
                  <input type="submit" value="F" name="SkinF"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinI.py" method="post">
                  <input type="submit" value="I" name="SkinI"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinJ.py" method="post">
                  <input type="submit" value="J" name="SkinJ"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinK.py" method="post">
                  <input type="submit" value="K" name="SkinK"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinM.py" method="post">
                  <input type="submit" value="M" name="SkinM"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinN.py" method="post">
                  <input type="submit" value="N" name="SkinN"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinR.py" method="post">
                  <input type="submit" value="R" name="SkinR"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinS.py" method="post">
                  <input type="submit" value="S" name="SkinS"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinT.py" method="post">
                  <input type="submit" value="T" name="SkinT"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">
                <form action="view_skinW.py" method="post">
                  <input type="submit" value="W" name="SkinW"/>
                </form>
              </a></li>
            </ul>
        </div>
        <div class="btn-group">
            <button type="button" class="btn btn-outline-success">un Role</button>
            <button type="button" class="btn btn-success dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">
                <form action="view_roleTank.py" method="post">
                  <input type="submit" value="Tank" name="RoleTank"/>
                </form>
               </a></li>
               <li><hr class="dropdown-divider"></li>
               <li><a class="dropdown-item" href="#">
                 <form action="view_roleBruiser.py" method="post">
                   <input type="submit" value="Bruiser" name="RoleBruiser"/>
                 </form>
               </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_roleAssassin.py" method="post">
                    <input type="submit" value="Assassin" name="RoleAssassin"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_roleTireur.py" method="post">
                    <input type="submit" value="Tireur" name="RoleTireur"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_roleMage.py" method="post">
                    <input type="submit" value="Mage" name="RoleMage"/>
                  </form>
                </a></li>
            </ul>
        </div>
        <div class="btn-group">
            <button type="button" class="btn btn-outline-primary">une Arme</button>
            <button type="button" class="btn btn-primary dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">
                <form action="view_armeCornesCrocs.py" method="post">
                  <input type="submit" value="Cornes/Crocs" name="ArmesCornesCrocs"/>
                </form>
              </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_armeMagieFeuNeige.py" method="post">
                    <input type="submit" value="Magie/Feu/Neige" name="ArmesMagieFeuNeige"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_armeArcBoomerang.py" method="post">
                    <input type="submit" value="Arc/Boomerang" name="ArmesArcBoomerang"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_armeFaucilleLampadaire.py" method="post">
                    <input type="submit" value="Faucille/Lampadaire" name="ArmesFaucilleLampadaire"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_armePoingsHache.py" method="post">
                    <input type="submit" value="Poings/Hache" name="ArmesPoingsHache"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_armeEpeeLames.py" method="post">
                    <input type="submit" value="Epee/Lames" name="ArmesEpeeLames"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_armesSarbacaneCartes.py" method="post">
                    <input type="submit" value="Sarbacane/Cartes" name="ArmesSarbacaneCartes"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_armeCanonPistolets.py" method="post">
                    <input type="submit" value="Canon/Pistolets" name="ArmesCanonPistolets"/>
                  </form>
                </a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_armeKunaï" method="post">
                    <input type="submit" value="Kunaï" name="ArmesKunaï"/>
                  </form>
                </a></li>
            </ul>
        </div>
        <div class="btn-group">
            <button type="button" class="btn btn-outline-info">une Lane</button>
            <button type="button" class="btn btn-info dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">
                <form action="view_laneTop.py" method="post">
                  <input type="submit" value="Top" name="LaneTop"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_laneJungle.py" method="post">
                    <input type="submit" value="Jungle" name="LaneJungle"/>
                  </form>
                </a></li>
              <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_laneMid.py" method="post">
                    <input type="submit" value="Mid" name="LaneMid"/>
                  </form>
                </a></li>
              <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_laneAdc.py" method="post">
                    <input type="submit" value="Adc" name="LaneAdc"/>
                  </form>
                </a></li>
              <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_laneSupport.py" method="post">
                    <input type="submit" value="Support" name="LaneSupport"/>
                  </form>
                </a></li>
            </ul>
        </div>
        <div class="btn-group">
            <button type="button" class="btn btn-outline-warning">un Genre</button>
            <button type="button" class="btn btn-warning dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">
                <form action="view_genreF.py" method="post">
                  <input type="submit" value="Femme" name="GenreF"/>
                </form>
              </a></li>
              <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">
                  <form action="view_genreM.py" method="post">
                    <input type="submit" value="Homme" name="GenreM"/>
                  </form>
                </a></li>
            </ul>
        </div>
        <div class="btn-group">
            <button type="button" class="btn btn-outline-danger">Lancer une partie</button>
            <button type="button" class="btn btn-danger dropdown-toggle dropdown-toggle-split" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Toggle Dropdown</span>
            </button>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">
                <form action="view_simulationPartie.py" method="post">
                  <input type="submit" value="Lancer la Simulation" name="Partie"/>
                </form>
              </a></li>
            </ul>
        </div>
      <br></br>
      <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_0.jpg" class="d-block w-100" alt="image1">
              <div class="carousel-caption d-none d-md-block">
                <h5>Ashe</h5>
                <p>Archère de givre</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_11.jpg" class="d-block w-100" alt="image2">
              <div class="carousel-caption d-none d-md-block">
                <h5>Cosmique Ashe</h5>
                <p>Archère de givre</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_17.jpg" class="d-block w-100" alt="image3">
              <div class="carousel-caption d-none d-md-block">
                <h5>Ashe de l'ouest</h5>
                <p>Archère de givre</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Alistar_0.jpg" class="d-block w-100" alt="image4">
              <div class="carousel-caption d-none d-md-block">
                <h5>Alistar</h5>
                <p>Minotaure</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Alistar_29.jpg" class="d-block w-100" alt="image5">
              <div class="carousel-caption d-none d-md-block">
                <h5>Alistar bête lunaire</h5>
                <p>Minotaure</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Alistar_19.jpg" class="d-block w-100" alt="image6">
              <div class="carousel-caption d-none d-md-block">
                <h5>Alistar Hextech</h5>
                <p>Minotaure</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Annie_0.jpg" class="d-block w-100" alt="image7">
              <div class="carousel-caption d-none d-md-block">
                <h5>Annie</h5>
                <p>Enfant des ténèbres</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Annie_11.jpg" class="d-block w-100" alt="image8">
              <div class="carousel-caption d-none d-md-block">
                <h5>Super Annie intergalactique</h5>
                <p>Enfant des ténèbres</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Annie_9.jpg" class="d-block w-100" alt="image9">
              <div class="carousel-caption d-none d-md-block">
                <h5>Annie coeur tendre</h5>
                <p>Enfant des ténèbres</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kayle_0.jpg" class="d-block w-100" alt="image10">
              <div class="carousel-caption d-none d-md-block">
                <h5>Morgana/Kayle</h5>
                <p>Déchue/Vertueuse</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Morgana_3.jpg" class="d-block w-100" alt="image11">
              <div class="carousel-caption d-none d-md-block">
                <h5>Morgana la lame sinistre</h5>
                <p>Déchue</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Morgana_41.jpg" class="d-block w-100" alt="image12">
              <div class="carousel-caption d-none d-md-block">
                <h5>Morgana sorcière édition prestige</h5>
                <p>Déchue</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kayle_24.jpg" class="d-block w-100" alt="image13">
              <div class="carousel-caption d-none d-md-block">
                <h5>Kayle tueuse de dragons</h5>
                <p>Vertueuse</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Kayle_2.jpg" class="d-block w-100" alt="image14">
              <div class="carousel-caption d-none d-md-block">
                <h5>Kayle viridienne</h5>
                <p>Vertueuse</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Irelia_0.jpg" class="d-block w-100" alt="image15">
              <div class="carousel-caption d-none d-md-block">
                <h5>Irelia</h5>
                <p>Danseuse des lames</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Irelia_6.jpg" class="d-block w-100" alt="image16">
              <div class="carousel-caption d-none d-md-block">
                <h5>Irelia à l'épée divine</h5>
                <p>Danseuse des lames</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Irelia_3.jpg" class="d-block w-100" alt="image17">
              <div class="carousel-caption d-none d-md-block">
                <h5>Cyber Irelia</h5>
                <p>Danseuse des lames</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Neeko_0.jpg" class="d-block w-100" alt="image18">
              <div class="carousel-caption d-none d-md-block">
                <h5>Neeko</h5>
                <p>Caméléon curieux</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Neeko_10.jpg" class="d-block w-100" alt="image19">
              <div class="carousel-caption d-none d-md-block">
                <h5>Neeko gardienne des étoiles</h5>
                <p>Caméléon curieux</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Neeko_1.jpg" class="d-block w-100" alt="image20">
              <div class="carousel-caption d-none d-md-block">
                <h5>Neeko merveille hivernale</h5>
                <p>Caméléon curieux</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Soraka_0.jpg" class="d-block w-100" alt="image21">
              <div class="carousel-caption d-none d-md-block">
                <h5>Soraka</h5>
                <p>Enfant des étoiles</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Soraka_7.jpg" class="d-block w-100" alt="image22">
              <div class="carousel-caption d-none d-md-block">
                <h5>Soraka gardienne des étoiles</h5>
                <p>Enfant des étoiles</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Soraka_15.jpg" class="d-block w-100" alt="image23">
              <div class="carousel-caption d-none d-md-block">
                <h5>Soraka hérault de l'aube</h5>
                <p>Enfant des étoiles</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Teemo_0.jpg" class="d-block w-100" alt="image24">
              <div class="carousel-caption d-none d-md-block">
                <h5>Teemo</h5>
                <p>Scout de bantam</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Teemo_14.jpg" class="d-block w-100" alt="image25">
              <div class="carousel-caption d-none d-md-block">
                <h5>Teemo diablotin</h5>
                <p>Scout de bantam</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Teemo_25.jpg" class="d-block w-100" alt="image26">
              <div class="carousel-caption d-none d-md-block">
                <h5>Teemo fleur spirituelle</h5>
                <p>Scout de bantam</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jinx_0.jpg" class="d-block w-100" alt="image27">
              <div class="carousel-caption d-none d-md-block">
                <h5>Jinx</h5>
                <p>Gâchette folle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jinx_13.jpg" class="d-block w-100" alt="image28">
              <div class="carousel-caption d-none d-md-block">
                <h5>Jinx de l'odyssée</h5>
                <p>Gâchette folle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jinx_20.jpg" class="d-block w-100" alt="image29">
              <div class="carousel-caption d-none d-md-block">
                <h5>Project Jinx</h5>
                <p>Gâchette folle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Warwick_0.jpg" class="d-block w-100" alt="image30">
              <div class="carousel-caption d-none d-md-block">
                <h5>Warwick</h5>
                <p>Fureur déchaînée de zaun</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Warwick_6.jpg" class="d-block w-100" alt="image31">
              <div class="carousel-caption d-none d-md-block">
                <h5>Warwick de feu</h5>
                <p>Fureur déchaînée de zaun</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Warwick_35.jpg" class="d-block w-100" alt="image32">
              <div class="carousel-caption d-none d-md-block">
                <h5>Warwick dieu ancien</h5>
                <p>Fureur déchaînée de zaun</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sett_0.jpg" class="d-block w-100" alt="image33">
              <div class="carousel-caption d-none d-md-block">
                <h5>Sett</h5>
                <p>Patron</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sett_8.jpg" class="d-block w-100" alt="image34">
              <div class="carousel-caption d-none d-md-block">
                <h5>Sett dragon obsidienne</h5>
                <p>Patron</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sett_1.jpg" class="d-block w-100" alt="image35">
              <div class="carousel-caption d-none d-md-block">
                <h5>Sett du royaume des mechas</h5>
                <p>Patron</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MissFortune_0.jpg" class="d-block w-100" alt="image36">
              <div class="carousel-caption d-none d-md-block">
                <h5>Miss Fortune</h5>
                <p>Chasseuse de primes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MissFortune_20.jpg" class="d-block w-100" alt="image37">
              <div class="carousel-caption d-none d-md-block">
                <h5>Miss Fortune sorcière édition prestige</h5>
                <p>Chasseuse de primes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MissFortune_16.jpg" class="d-block w-100" alt="image38">
              <div class="carousel-caption d-none d-md-block">
                <h5>Miss Fortune déesse des flingues</h5>
                <p>Chasseuse de primes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/TwistedFate_0.jpg" class="d-block w-100" alt="image39">
              <div class="carousel-caption d-none d-md-block">
                <h5>Twisted fate</h5>
                <p>Maître des cartes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/TwistedFate_7.jpg" class="d-block w-100" alt="image40">
              <div class="carousel-caption d-none d-md-block">
                <h5>Twisted fate des enfers</h5>
                <p>Maître des cartes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/TwistedFate_4.jpg" class="d-block w-100" alt="image41">
              <div class="carousel-caption d-none d-md-block">
                <h5>Twisted fate tango</h5>
                <p>Maître des cartes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Akali_0.jpg" class="d-block w-100" alt="image42">
              <div class="carousel-caption d-none d-md-block">
                <h5>Akali</h5>
                <p>Assassin rebelle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Akali_15.jpg" class="d-block w-100" alt="image43">
              <div class="carousel-caption d-none d-md-block">
                <h5>True damage Akali</h5>
                <p>Assassin rebelle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Akali_7.jpg" class="d-block w-100" alt="image44">
              <div class="carousel-caption d-none d-md-block">
                <h5>Akali chasseuse de têtes</h5>
                <p>Assassin rebelle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Tristana_0.jpg" class="d-block w-100" alt="image45">
              <div class="carousel-caption d-none d-md-block">
                <h5>Tristana</h5>
                <p>Canonnière Yordle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Tristana_2.jpg" class="d-block w-100" alt="image46">
              <div class="carousel-caption d-none d-md-block">
                <h5>Tristana l'elfe sérieuse</h5>
                <p>Canonnière Yordle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Tristana_10.jpg" class="d-block w-100" alt="image47">
              <div class="carousel-caption d-none d-md-block">
                <h5>Tristana dragonnière</h5>
                <p>Canonnière Yordle</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nunu_0.jpg" class="d-block w-100" alt="image48">
              <div class="carousel-caption d-none d-md-block">
                <h5>Nunu et Willump</h5>
                <p>Le garçon et son Yeti</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nunu_16.jpg" class="d-block w-100" alt="image49">
              <div class="carousel-caption d-none d-md-block">
                <h5>Nunu et Willump astro-groove</h5>
                <p>Le garçon et son Yeti</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Nunu_2.jpg" class="d-block w-100" alt="image50">
              <div class="carousel-caption d-none d-md-block">
                <h5>Nunu et Willump du Solstice</h5>
                <p>Le garçon et son Yeti</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MasterYi_0.jpg" class="d-block w-100" alt="image51">
              <div class="carousel-caption d-none d-md-block">
                <h5>Maître Yi</h5>
                <p>Fine lame wuju</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MasterYi_1.jpg" class="d-block w-100" alt="image52">
              <div class="carousel-caption d-none d-md-block">
                <h5>Maître Yi l'assassin</h5>
                <p>Fine lame wuju</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MasterYi_10.jpg" class="d-block w-100" alt="image53">
              <div class="carousel-caption d-none d-md-block">
                <h5>Maître Yi lame cosmique</h5>
                <p>Fine lame wuju</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jax_0.jpg" class="d-block w-100" alt="image54">
              <div class="carousel-caption d-none d-md-block">
                <h5>Jax</h5>
                <p>Maître d'armes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jax_13.jpg" class="d-block w-100" alt="image55">
              <div class="carousel-caption d-none d-md-block">
                <h5>Jax au baton divin</h5>
                <p>Maître d'armes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jax_20.jpg" class="d-block w-100" alt="image56">
              <div class="carousel-caption d-none d-md-block">
                <h5>Jax conquérant</h5>
                <p>Maître d'armes</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jhin_0.jpg" class="d-block w-100" alt="image57">
              <div class="carousel-caption d-none d-md-block">
                <h5>Jhin</h5>
                <p>Virtuose</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jhin_5.jpg" class="d-block w-100" alt="image58">
              <div class="carousel-caption d-none d-md-block">
                <h5>Jhin démiurge cosmique</h5>
                <p>Virtuose</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Jhin_4.jpg" class="d-block w-100" alt="image59">
              <div class="carousel-caption d-none d-md-block">
                <h5>Project Jhin</h5>
                <p>Virtuose</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sivir_0.jpg" class="d-block w-100" alt="image60">
              <div class="carousel-caption d-none d-md-block">
                <h5>Sivir</h5>
                <p>Vierge martinale</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sivir_6.jpg" class="d-block w-100" alt="image61">
              <div class="carousel-caption d-none d-md-block">
                <h5>Sivir du blizzard</h5>
                <p>Vierge martinale</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sivir_16.jpg" class="d-block w-100" alt="image62">
              <div class="carousel-caption d-none d-md-block">
                <h5>Sivir lune de sang</h5>
                <p>Vierge martinale</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ryze_0.jpg" class="d-block w-100" alt="image63">
              <div class="carousel-caption d-none d-md-block">
                <h5>Ryze</h5>
                <p>Mage runique</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ryze_2.jpg" class="d-block w-100" alt="image64">
              <div class="carousel-caption d-none d-md-block">
                <h5>Ryze tribal</h5>
                <p>Mage runique</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ryze_11.jpg" class="d-block w-100" alt="image65">
              <div class="carousel-caption d-none d-md-block">
                <h5>Ryze du championnat</h5>
                <p>Mage runique</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sion_0.jpg" class="d-block w-100" alt="image66">
              <div class="carousel-caption d-none d-md-block">
                <h5>Sion</h5>
                <p>Colosse mort-vivant</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sion_5.jpg" class="d-block w-100" alt="image67">
              <div class="carousel-caption d-none d-md-block">
                <h5>Mecha Sion zéro</h5>
                <p>Colosse mort-vivant</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Sion_22.jpg" class="d-block w-100" alt="image68">
              <div class="carousel-caption d-none d-md-block">
                <h5>Sion des glaces noires</h5>
                <p>Colosse mort-vivant</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fiddlesticks_0.jpg" class="d-block w-100" alt="image69">
              <div class="carousel-caption d-none d-md-block">
                <h5>Fiddlesticks</h5>
                <p>Effroi nocturne</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fiddlesticks_9.jpg" class="d-block w-100" alt="image70">
              <div class="carousel-caption d-none d-md-block">
                <h5>Fiddlesticks prétorien</h5>
                <p>Effroi nocturne</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Fiddlesticks_8.jpg" class="d-block w-100" alt="image71">
              <div class="carousel-caption d-none d-md-block">
                <h5>Fiddlesticks réanimé</h5>
                <p>Effroi nocturne</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_0.jpg" class="d-block w-100" alt="image72">
              <div class="carousel-caption d-none d-md-block">
                <h5>Ahri</h5>
                <p>Renard à neuf queues</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_42.jpg" class="d-block w-100" alt="image73">
              <div class="carousel-caption d-none d-md-block">
                <h5>Ahri de l'assemblée</h5>
                <p>Renard à neuf queues</p>
              </div>
            </div>
            <div class="carousel-item">
              <img src="https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_17.jpg" class="d-block w-100" alt="image74">
              <div class="carousel-caption d-none d-md-block">
                <h5>Ahri sylvestre</h5>
                <p>Renard à neuf queues</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>"""

print(Page)