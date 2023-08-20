```{epigraph}
$\large \mathbf{\text{NANOTERMODINAMIKA: Sistema Txikien TermodinamikaS}}$
```

```{epigraph}
_Classical thermodynamics... is the only physical theory of universal content which I am convinced that, within the framework of the applicability of its basic concepts, will never be overthrown._

-- Albert Einstein
```

(sarrera)=
## Sarrera eta helburuak

Termodinamika, ezbairik gabe, zientzian hedadura handieneko teoria da gaur-gaurkoz, bere postulatuak alor orotara barreiatzen baitira, atomoen barnetik hasiz eta unibertsora zabalduz. Izan ere, Fisika Estatistikoa bidelagun duela, zientzialariak naturaren izaera termikoa ulertzeko nahitaezkoak diren hurbilketez eta lanabesez zuzkitzen ditu. Hain zuzen, jakina denez, edozein sistemak erakusten duen portaerak Termodinamikaren oinarrizko bi legeri segitzen die; energiaren kontserbazioari, alde batetik, eta entropiaren etengabeko igoerari, bestetik. Azken puntu horren ondorio da, hein handi batean, Einsteinek bere baieztapenean azaltzen duen irmotasuna.

Era berean, aintzakotzat izan beharrekoa da ezen sistema batean burutzen diren azterketa termodinamikoak bi hurbilketa nagusitan oinarritzen direla eskuarki; sistema hori makroskopikotzat eta homogeneotzat hartzean, alegia. Bada, esan beharrekoa da, baldintza horiek dakartzaten mugei eutsita ere, kasu gehientsuetan teoria horrek egundoko arrakasta izan duela, arestian aipatutakoa indartuz.

Dena dela ere, historikoki izan da hasiera batean tinkoak ziruditen irizpideok kolokan jarri dituen zenbait gertaera. XIX. mende amaieran, esaterako, erreakzio kimikoetan lehen legea hausten zela ohartu ziren. Horren harira, Gibbs-ek 1876an zuzenketa garrantzitsua txertatu zuen, $\mu$ potentzial kimikoak ezaugarritzen duen molekulen gehikuntzaren ondoriozko energiarako ekarpena, preseski {cite}`nanointro`. Horrek, energiaren kontserbazioa berrezartzeaz gain, Termodinamikaren eremua handitu egin zuen. XX. mendea heldutakoan, teoria kuantikoaren sorkuntzak eta garapenak sistema are txikiagoen azterketa ahalbidetu zuen. Hori dela eta, faktore eragile berriak azaldu ziren, esate baterako, _simetria lokala_ eta _tamaina finituko efektuak_. Baina haien eragina ez zegoen ordura arteko Termodinamika klasikoaren bitartez erabat azaltzerik. Adibidez, saiakuntza espektroskopiko batzuetan nanometroen eskalan tenperatura-banaketa heterogeneoak aurkitu dira {cite}`t_ez_hom`. Horrek, zer esanik ez, lege makroskopikoek $T$ tenperaturari ematen dioten izaera homogeneoa eta intentsiboa zapuzten du.

Arazo horiei irtenbidea emateko, teoria klasikoari zuzenketak gehitu dizkioten tresnak sortu dira, hala nola fluktuazio-teoremak zein Termodinamika Estokastikoa, zeintzuek ekarpen eta ospe esanguratsua izan baitute. Baina teoria horiek sistema betiere bero-iturri homogeneo batekin ukipen termikoan egotea eskatzen dute, eta material gehienen kasuan (likidoak, kristalak, polimeroak...) ez da posible azken baldintza hori betearaztea {cite}`multiscale`.

Dena den, badago efektu horiei beste ikuspuntu batetik heltzen dien teoria, zeina, tamalez, hain entzutetsua izan ez den. Lan honetan aztergai izango dugun teoria horrek **_Sistema Txikien Termodinamika_** du izena, eta __Terrell Leslie Hill__ fisikari eta biologoak (1917-2014) garatu zuen 1960ko hamarkadaren hasieran.

```{figure} hill.jpg
---
height: 200px
name: hill
---
T. L. Hill
```

Hill-ek 1962an _Thermodynamics of Small Systems_ artikulua {cite}`hill_art`, eta, hortik bi urtera, izen bera daraman liburu parea {cite}`hill` plazaratu zituen, Nanotermodinamikaren oinarri matematikoak zein aplikazioak azaltzeko.

```{admonition} Oharra
Hill-ek ez du erabiltzen _Nanotermodinamika_ hitza bere lanetan. Izan ere, 1960ko hamarkadan oraindik sistema esperimental gutxi batzuen azterketari egokitu zekizkiokeen bere ideiak. Hala, autoreak gerora txertatu zuen termino hori (2000. urtean), bere lanari xarma berezia emango ziolakoan.
```
Hala ere, urte gutxiren buruan, esparru horretako lana bertan behera utzi, eta biologia molekularrean ikertzeari ekin zion. Zoritxarrez, azken sei hamarkadetan ez da bere lanari jarraipen nabarmena eman dion fisikaririk izan. Edonola ere, aipatu beharrekoa da, 2020az geroztik, Norvegiako NTNU unibertsitateko ikerlari-talde batek {cite}`noruegos` badiharduela Hill-en lana berrabiarazi eta bultzatu nahian, eta, teoria laburbiltzen duen liburua argitaratzeaz gain {cite}`nano`, saiakuntzetara eta simulazio molekularretara eraman dutela, emaitza adierazgarriak erdietsiz; adibidez, adsortzioaren kasuan {cite}`ads_t, ads`.

Funtsean, Hill-en teoria Termodinamikak sistema aske, heterogeneo eta nahi bezain txikiak zehaztasun handiagoz ezaugarritzea posible egiten duen orokorpena da. Bestela esanda, sistema txikiek baitezpadako dituzten hedapen finituko zuzenketak eta moldaketak eransten dizkie ekuazio klasikoei. Beroriek ezaugarritzeko, aurrerago aurkeztuko dugun potentzial termodinamiko berria sortu zuen. Nolanahi ere, sistemak handituz doazen heinean, ekarpenok ahulduz doaz, eta adierazpen makroskopikoak berreskuratzen dira.

Ildo horretatik, unitate didaktiko hau bereziki Termodinamika eta Fisika Estatistikoa irakasgaira dago bideratuta, eta, hain zuzen, lehengo paragrafoan aipatutakoan sakontzea du helburutzat. Azalpen teorikoak aurkeztuz, eta tarteka adibide eta aplikazio adierazgarriak sartuz, ikasleak _ohiko_ Termodinamikatik haratago eramatea, eta Nanotermodinamikak sistema txikien azterketan duen eraginaz ohartaraztea da xedea, teoria horren nondik norakoez jabetu daitezen bidenabar. Horiek horrela, euren ikaskuntzan aurrerapauso nabaria egingo dute.

Hasteko, {numref}`{number}. atalean <nanointro>` zubi-lanetan jardungo dugu, dagoeneko ikasia dugun Mekanika Estatistikoaren oinarriak gogora ekarri {cite}`callen, hebreos, pathria`, eta Nanotermodinamikarekin lotura ezartzeko. Behin ideia nagusiak finkatuz gero, {numref}`{number}. atalburuan <hillsec>` Hill-en  formalismoan sartuko gara {cite}`hill, nano`. Hortik abiatuz, {numref}`{number}. kapituluan <tpn>` garrantzi handia duen multzo isotermo-isobaroan lehenbiziko adibideak landuko ditugu, eta tamaina finituko ekarpenen ondorio bitxiei hurbiletik erreparatuko diegu. Jarraian, {numref}`{number}. gaian <fase>` etenaldi berezia egingo dugu, sistema txikietako fase-trantsizioak aztertzeko. Teoriaren zatia ixteko, {numref}`{number}. atalean <tpmu>` ildo nagusira bihurtuko gara. Termodinamikaz haratago doan multzo estatistiko _berria_ aurkezteaz bat, bertan adibide bereziak berraztertuko ditugu, esangura handiko emaitzak erdietsiz. Ondoren, {numref}`{number}. atalean <app>` adibide mardulagoa aztertuko dugu, {cite}`ads` artikuluari jarraikiz. Hura Hill-en teoriaren egungo erabilgarritasunaren adierazle garbia da, eta, zalantza izpirik gabe, 1960ko hamarkadaz haratago heltzen ari denaren seinale. Amaitzeko, {numref}`{number}. kapituluan <elek_mag>` sistema elektrikoei eta magnetikoei erreparatuko diegu; besteak beste, Ising-en ereduaren berrazterketarekin arituko gara. Horrez gain, {numref}`{number}. atal gehigarrian <osagarri>` {numref}`{number}. <tpmu>` gaiarekin lotutako adibide osagarri esanguratsuak daude.

Bada, luzamendutan ibili barik, _ohiko_ Termodinamikatik Nanotermodinamikara eramango gaituen zubia gurutzatzeari ekingo diogu. Hurrengo ataleko {numref}`{number}. irudia <multzo>` da horretarako abiapuntu aproposa.
