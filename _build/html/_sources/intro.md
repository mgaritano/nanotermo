```{epigraph}
$\huge \mathbf{\text{NANOTERMODINAMIKA}}$
$\quad \quad \quad \quad \quad \quad \large Sistema \; \; Txikien \; \; Termodinamika$
```

```{epigraph}
_Classical thermodynamics... is the only physical theory of universal content which I am convinced that, within the framework of the applicability of its basic concepts, will never be overthrown._

-- Albert Einstein
```

(sarrera)=
# **1**. Sarrera

Termodinamika, ezbairik gabe, zientzian hedadura handieneko teoria da gaur-gaurkoz, bere postulatuak alor orotara barreiatzen baitira, atomoen barnetik hasiz eta unibertsora zabalduz. Izan ere, Fisika Estatistikoa bidelagun duela, zientzialariak naturaren izaera termikoa ulertzeko nahitaezkoak diren hurbilketez eta lanabesez zuzkitzen ditu. Hain zuzen, jakina denez, edozein sistemak erakusten duen portaerak Termodinamikaren oinarrizko bi legeei segitzen die; energiaren kontserbazioari, alde batetik, eta entropiaren etengabeko igoerari, bestetik. Azken puntu horren ondorio da, hein handi batean, Einsteinek bere baieztapenean azaltzen duen irmotasuna.

Era berean, aintzakotzat izan beharrekoa da ezen sistema batean burutzen diren azterketa termodinamikoak bi hurbilketa nagusitan oinarritzen direla eskuarki; sistema hori makroskopikotzat eta homogeneotzat hartzean, alegia. Bada, esan beharrekoa da, baldintza horiek dakartzaten mugei eutsita ere, kasu gehientsuetan teoria horrek egundoko arrakasta izan duela, arestian aipatutakoa indartuz.

Dena dela ere, historikoki izan da hasiera batean tinkoak ziruditen irizpideok kolokan jarri dituen zenbait gertaera. XIX. mende amaieran, esaterako, erreakzio kimikoetan lehen legea hausten zela ohartu ziren. Horren harira, Gibbs-ek 1876an zuzenketa garrantzitsua txertatu zuen, $\mu$ potentzial kimikoak ezaugarritzen duen molekulen gehikuntzaren ondoriozko energiarako ekarpena, preseski {cite}`nanointro`. Berorrek, energiaren kontserbazioa berrezartzeaz gain, Termodinamikaren eremua handitu egin zuen. XX. mendea heldutakoan, teoria kuantikoaren sorkuntzak eta garapenak sistema are txikiagoen azterketa ahalbidetu zuen. Hori dela eta, faktore eragile berriak azaldu ziren, esate baterako, _simetria lokala_ eta _tamaina finituko efektuak_. Baina berorien eragina ez zegoen ordura arteko Termodinamika klasikoaren bitartez erabat azaltzerik. Adibidez, saiakuntza espektroskopiko batzuetan nanometroen eskalan tenperatura-banaketa heterogeneoak aurkitu dira {cite}`t_ez_hom`. Horrek, zer esanik ez, lege makroskopikoek $T$ tenperaturari ematen dioten izaera homogeneoa eta intentsiboa zapuzten du.

Arazo horiei irtenbidea emateko, teoria klasikoari zuzenketak gehitu dizkioten tresnak sortu dira, hala nola fluktuazio-teoremak zein Termodinamika Estokastikoa, zeintzuek ekarpen eta ospe esanguratsua izan baitute. Baina teoria horiek sistema betiere bero-iturri homogeneo batekin ukipen termikoan egotea eskatzen dute, eta material gehienen kasuan (likidoak, kristalak, polimeroak...) ez da posible azken baldintza hori betearaztea {cite}`multiscale`.

Dena den, badago efektu horiei beste ikuspuntu batetik heltzen dien teoria, zeina, tamalez, hain entzutetsua izan ez den. Lan honetan aztergai izango dugun teoria horrek **_Sistema Txikien Termodinamika_** du izena, eta __Terrell Leslie Hill__ fisikari eta biologoak (1917-2014) garatu zuen 1960. hamarkadaren hasieran.

```{figure} hill.jpg
---
height: 200px
name: hill
---
T. L. Hill
```

Hill-ek 1962an _Thermodynamics of Small Systems_ artikulua {cite}`hill_art`, eta, hortik bi urtera, izen bera daraman liburu-parea {cite}`hill` plazaratu zituen, Nanotermodinamikaren oinarri matematikoak zein aplikazioak azalduz.

```{admonition} Oharra
Hill-ek ez du erabiltzen _Nanotermodinamika_ hitza bere lanetan. Izan ere, 1960. hamarkadan oraindik sistema esperimental gutxi batzuen azterketari egokitu zekizkiokeen bere ideiak. Hala, autoreak gerora txertatu zuen termino hori (2000. urtean), bere lanari xarma berezia emango ziolakoan.
```
Hala ere, urte gutxiren buruan, esparru horretako lana bertan behera utzi, eta biologia molekularrean ikertzeari ekin zion. Zoritxarrez, azken sei hamarkadetan ez da bere lanari jarraipen nabarmena eman dion fisikaririk izan. Edonola ere, aipatu beharrekoa da, 2020az geroztik, Norvegiako NTNU unibertsitateko ikerlari-talde batek {cite}`noruegos` badiharduela Hill-en lana berrabiarazi eta bultzatu nahian, eta, teoria laburbiltzen duen liburua argitaratzeaz gain {cite}`nano`, berori saiakuntzetara eta simulazio molekularretara eraman dutela, emaitza adierazgarriak erdietsiz; adibidez, adsortzioaren kasuan {cite}`ads_t, ads`.

Funtsean, Hill-en teoria Termodinamikak sistema aske, heterogeneo eta nahi bezain txikiak zehaztasun handiagoz ezaugarritzea posible egiten duen orokorpena da. Bestela esanda, sistema txikiek baitezpadako dituzten hedapen finituko zuzenketak eta moldaketak eransten dizkie ekuazio klasikoei. Beroriek ezaugarritzeko, aurrerago aurkeztuko dugun potentzial termodinamiko berria sortu zuen. Nolanahi ere, sistemak handituz doazen heinean, ekarpenok ahulduz doaz, eta adierazpen makroskopikoak berreskuratzen dira.

Ildo horretatik, Gradu Amaierako Lan honen bertsio digitalaren lehenengo zatia ([2](nanointro) - [6](tpmu) atalak) bereziki Termodinamika eta Fisika Estatistikoa irakasgaira dago bideratuta, eta, hain zuzen, lehengo paragrafoan aipatutakoan sakontzea du helburutzat. Azalpen teorikoak aurkeztuz, eta tarteka adibide adierazgarriak sartuz, ikasleak _ohiko_ Termodinamikatik haratago eramatea, eta Nanotermodinamikak sistema txikien azterketan duen eraginaz ohartaraztea da xedea, teoria horren nondik norakoez jabetu daitezen bidenabar. Horiek horrela, euren ikaskuntzan aurrerapauso nabaria egingo dute.

Hasteko, [2.](nanointro) zatian zubi-lanetan jardungo dugu, dagoeneko ikasia dugun Mekanika Estatistikoaren oinarriak gogora ekarri {cite}`callen, hebreos, pathria`, eta berorrek Nanotermodinamikarekin duen lotura ezartzeko. Behin ideia nagusiak finkatuz gero, [3.](hillsec) atalburuan Hill-en  formalismoan sartuko gara {cite}`hill, nano`. Hortik abiatuz, [4.](tpn) kapituluan garrantzi handia duen multzo isotermo-isobaroan lehenbiziko adibideak landuko ditugu, eta tamaina finituko ekarpenen ondorio bitxiei hurbiletik erreparatuko diegu. Jarraian, [5.](fase) gaian etenaldi berezia egingo dugu, sistema txikietako fase-trantsizioak aztertzeko. Teoriarekin amaitzeko, [6.](tpmu) atalean ildo nagusira bihurtuko gara. Termodinamikaz haratago doan multzo estatistiko _berria_ aurkezteaz bat, bertan adibide bereziak berraztertuko ditugu, esangura handiko emaitzak erdietsiz. Amaitzeko, [7.](app) atalean adibide mardulagoa aztertuko dugu, {cite}`ads` artikuluari jarraikiz. Berori Hill-en teoriaren egungo erabilgarritasunaren adierazle garbia da, eta, zalantza izpirik gabe, 1960. hamarkadaz haratago heltzen ari denaren seinale.

Bada, luzamendutan ibili barik, _ohiko_ Termodinamikatik Nanotermodinamikara eramango gaituen zubia gurutzatzeari ekingo diogu. Honako hauek dira jorratuko ditugun gaiak:

```{tableofcontents}
```
