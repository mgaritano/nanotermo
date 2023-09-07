(fase)=
## Sistema txikietako fase-trantsizioak

Aparteko zati honetan, tamaina finituko efektuek bi oreka-egoeren arteko fase-trantsizioaren jokamoldeari dakarzkioten berezitasunen gainean jardungo dugu.

```{dropdown} __Oharra__

Atal honetan ez da ariketarik egongo. 😎

Hala ere, komenigarria da garapen batzuk norberak egitea... 🙃
```

(itzul)=
### Itzulgarritasuna eta oreka-baldintzak

Hill-en teoriari segituz, $\mathscr{N}(\rightarrow \infty)$ aldakiz osaturiko multzo makroskopikoa aztertuko dugu. Azpisistemei ez diegu askatasun-gradurik abiaraziko, hau da, erabat isolatuta daude, eta $(E,V,N)$ sorta esleituko diegu. Termodinamikaren bigarren legeak dioenez  {cite}`st`, sistemak, lehen oreka-egoeratik bigarreneranzkora bidean, prozesu infinitesimal itzulezinak pairatuko ditu. Beroriek entropiari ekarpen positiboak sorraraziko dizkiote $(\mathrm{d}S_{t}>0)$, harik eta oreka berrezartzen den arte $(\mathrm{d}S_{t}=0)$. Aurrerantzean jazoko den aldaketa oro itzulgarria izango da, sistemak oreka-egoera berriari eutsiko baitio.

Oro har, prozesu espontaneo bat {numref}`{number}. irudiaren <esp>` bidez ereduzta daiteke. Hasiera batean, kanpo-oztopo baten eraginpean dago sistema. Ondorioz, egoera kuantiko posible guztietatik soilik batzuk edukiko du eskuragai: $\Omega_{i}(E,V,N)$.
Kanpo-galarazpen hori kenduz gero, sistemaren egoera aldatu egingo da. Hain zuzen, aldakiek aurrez debekatuta egon diren egoeretara ere sarbidea izango dute; hortaz, bukaeran, $\Omega_{f}(E,V,N) > \Omega_{i}(E,V,N)$ izango dugu. Aktibazio-energiaren gutxitzearen edo potentzial baten minimizazioaren bidez gauzatu daiteke prozesu hori.
Hasierako eztabaidaren harira, entropia maximizatzeak energia askea minimizatzea dakar.

```{figure} esp.PNG
---
height: 200px
name: esp
---
  Prozesu espontaneoaren ereduztapena.  Gasak kutxaren ezkerraldetik alde egitea ekiditen du bereizte-hormak. Amaieran ez dago hormarik, eta, horren eraginez, bolumenaren osotasunera hedatu da gasa, era espontaneoan. Hasieratik bukaerara, entropia igo egin da.
```

Entropiak $S_{t} = \mathscr{N}k_{\mathrm{B}}\ln \Omega$ betetzen duenez, prozesu finitu eta espontaneoa amaitutakoan,

$$
\Delta S_{t} = S_{f}^{t} - S_{i}^{t} = \mathscr{N}k_{\mathrm{B}}\ln\left(\frac{\Omega_f}{\Omega_i}\right) > 0 \; .
$$ (sesp)

Termodinamikaren lege garrantzitsuenetariko baten esangura biltzen du ekuazio horrek. Hain zuzen, aurkako prozesua era espontaneoan jazoko balitz, $\Delta S_{t} < 0$ izango genuke, eta bigarren printzipioa hautsiko litzateke. Hala eta guztiz ere, $\mathscr{N} \rightarrow \infty$ onartu dugunez, **multzoan**, alegia, sistema guzti-guztietan,  horrelakorik gertatzeko probabilitatea kasik nulua da, hau da,

$$
 P_{f \rightarrow i}^{t} := \frac{\Omega_{i}}{\Omega_{f}} = \exp\left(-\frac{\Delta S_{t}}{\mathscr{N}k_{\mathrm{B}}}\right) \rightarrow 0 \; .
 $$ (probcont)

 Alabaina, **azpisistemetan**, $\mathscr{N}$ barik $N$ izango genuke, eta, beraz, $ P_{f\rightarrow i}\propto e^{-N}$. Bada, $N$ magnitudeak ez du zertan izan adierazpenaren balioa baztergarri bihurrarazteko bezain handia. Hori dela eta, $N$ oso txikia bada, baliteke sistema txiki jakin batzuetan bigarren printzipioa urratzen duen $(\Delta S < 0)$ aurkako prozesua era espontaneoan behatzea! Nolanahi ere, dakargun gogora aldakien propietateak multzotik ondorioztatzean datzala Hill-en teoria. Beraz, hasteko, multzo osoaren entropiaren aldakuntzari erreparatu beharko diogu, eta bertatik sistema txikietara igaro, $\Delta S = \Delta S_{t}/\mathscr{N}$  betetzen dela aintzat hartuz.

 Eztabaida honen harira, {numref}`{number}. atalean <stabeps>` sistema txikiz osatutako multzoaren banatze-prozesua aztertuko dugu. Berebat, $\mathscr{E}$ banatze-potentzialak prozesu horren itzulgarritasunean duen eraginari erreparatuko diogu.


 (fase1order)=
 ### Lehen ordenako fase-trantsizioak, $(T,p,N)$ sistema txikietan

Demagun sistema makroskopiko bat hasierako faseko egoeratik  bukaerako beste batera eraman nahi dugula. Lehenbiziko  egoeran, bere egoera-ekuazioa funtzio jarraitua eta deribagarria da, hots, zuzen definituta dago. Alabaina, aldiuneren batean bigarren faserako bat-bateko aldakuntza jasango du, ez-jarraitutasun bortitzak pairatuz; alegia, sisteman lehen ordenako fase-trantsizioa gertatuko da ({numref}`{number}a irudia <faseirudi>`).


```{figure} faseirudi.PNG
---
height: 250px
name: faseirudi
---
  $(a)$ Limite termodinamikoan, lehen ordenako fase-trantsizioan sistemak $p-\overline{V}$ __lerro isotermoari__ jarraitzen dio, $A$ egoeratik $B$-ra zuzenean igaroz. Hain zuzen, __kurba etena__ egonkortasunaren aurka doa, bertan komprimagarritasuna negatiboa baita, hots, $\kappa_{T} = -\left(\partial p/\partial V\right)_{T} < 0$. $(b)$ __Sistema txikien kasuan__,  $A$ eta $B$ egoerak aldi berean egongo dira $\Delta p$ gunean. Limite makroskopikoan, argi eta garbi, $\Delta p \rightarrow p_{0}$ beteko da.
```

Sistema txikia baldin balitz, aldiz, trantsizioa ez litzateke hain zorrotza izango. Aurki ikusiko dugunez, $\Delta p$ presio-tartearen hedadurak lotura zuzena du sistemaren tamainarekin $(N)$. Baina horri ekin aurretik, bada ildo beretik doan argitu beharreko beste kontu bat. Izan ere, {numref}`{number}b irudiak <faseirudi>` aditzera ematen duenez, hasierako $\overline{V} _ {A}$ eta bukaerako $\overline{V}_ {B}$ bolumenen inguruan agertzen diren fluktuazioak hautemangarriak dira. Beste hitzez esateko, $\overline{V}_ {A}$ eta $\overline{V}_{B}$ bolumenen inguruetara ere zertxobait aldenduko da $P(V)$ probabilitatea. Bada, azaldutako eboluzioaren isla {numref}`{number} irudia <prob>` da.

```{figure} prob.PNG
---
height: 250px
name: prob
---
Limite termodinamikoan probabilitateak $P(V)=\delta(V-\overline{V}_{A}) + \delta(V-\overline{V}_{B})$ betetzen du. Sistema txiki batean, aldiz, kurba zabalagoak lortzen dira. Hortaz, _bi egoeren hurbilketa_ deritzonari ez dio hertsiki segituko. Edonola ere, tarteko edozein $\overline{V}_{0}$ bolumenean $P(\overline{V}_{0})$ baztergarria da. Hori guztia dela eta, fase-trantsizioaren eremua $A$ eta $B$ egoeren arteko konbinazioa dela esan daiteke.
```

Aurrekoaren harira, $Q(T,V,N)$ partizio-funtzio kanonikotik abiatuz, sistemak $V_{i}$ bolumena izateko probabilitatea definituko dugu:

$$
P(V_{i}) := \frac{Q(T,V_{i},N)e^{- pV_{i}/k_{\mathrm{B}}T}}{\sum_{V_{i}}Q(T,V_{i},N)e^{-pV_{i}/k_{\mathrm{B}}T}} = \frac{Q(T,V_{i},N)e^{-pV_{i}/k_{\mathrm{B}}T}}{\Delta(T,p,N)}\;.
$$ (pvi)

Orain, {numref}`{number} irudiaren <prob>` inguruko iruzkinei jarraikiz,  $P(\overline{V} _ {A,B})/P(\overline{V} _ {0})$ erlazioa kalkulatuko dugu, zeina _bi egoeren hurbilketaren_ erabileraren zilegitasunaren adierazlea izango den. Azterketa Fisika Estatistikotik bideratuko dugu, {cite}`sm` liburuaren laguntzaz. Kontua da $A$ eta $B$ egoeren erdian dagoen egoera batean jatorrizko biak ere azalduko direla, bereizte-geruza baten bidez bananduta. Bertako molekula-kopuruaren magnitude-ordena $N^{2/3}$ izango da, eta, hortaz, molekula horien arteko elkarrekintzek $A(T,V,N)$ energiarako ekarpena izango dute, zeina, hain zuzen, $N^{2/3}k_{\mathrm{B}}T$ ordenakoa izango den. Puntu horren inguruko partizio-funtzioak, hartara, itxura hau izango du:

$$
Q(T,\overline{V} _ {0},N) = e^{-A(T,V,N)/k_{\mathrm{B}}T-N^{2/3}} = Q(T,V,N)e^{-N^{2/3}} \; .
$$

Berori, {eq}`pvi` adierazpenari jarraituz, probabilitatearekiko proportzionala denez, honakoa beteko da, puntu kritiko baten inguruan izan ezik:

$$
\frac{P(\overline{V}_{A,B})}{P(\overline{V}_{0})} \propto e^{N^{2/3}}  \; .
$$

Beraz, puntu kritikoak bazter utzita, sistema txikiegia ez bada, probabilitate-banaketarako ekarpen soilak $A$ eta $B$ egoerenak izango dira, eta onartutako hurbilketa zuzena izango da.


Horiek horrela, darabilgun orain Sistema Txikien Termodinamikaren tresnerian oinarritutako arrazoibidea, lorturiko ondorioak berresteko. Eraiki dezagun $\mathscr{N}$ aldaki duen multzo isotermo-isobaroa. $A$ eta $B$ egoeretan, hurrenez hurren, $\mathscr{N}_ {A}$ eta $\mathscr{N}_ {B}$ azpisistema dago. Bada, aurreko {numref}`{number} ataletik <tpn_azter>`, aldakiko Gibbs-en energia askea $F_{A,B} := N\; \widehat{\mu}_{A,B}$ dela gogora ekarriz,
eta banaketa posible guztien ekarpena kontuan hartuz (konfigurazio-mailako entropia), energia totala hauxe dugu:

$$
F_{t} = \mathscr{N}_ {A}\left(N\;\widehat{\mu}_ {A}\right) +  \mathscr{N}_ {B}\left(N\;\widehat{\mu}_ {B}\right) - k_{\mathrm{B}}T\ln\left(\frac{\mathscr{N}!}{\mathscr{N}_ {A}!\;\mathscr{N}_{B}!}\right) \; .
$$ (gibbstot)

Multzoak orekan izango duen $\mathscr{N}_ {A}/\mathscr{N}_ {B}$ frakzioari erreparatzea da gure jomuga, bertatik eskuratuko baitugu bigarren analisi honetarako beharrezkoa izango dugun informazioa. Multzoa bera makroskopikoa denez, zilegi izango zaigu Stirling-en hurbilketaz baliatzea, hau da, $\ln \mathscr{N}! \approx \mathscr{N}\ln \mathscr{N} - \mathscr{N}$ idatziko dugu. Hala, oreka-egoeran izango dugu $\mathscr{N}_ {A}$ kopurua finkatuz, eta $\mathscr{N}_ {B} = \mathscr{N}- \mathscr{N}_{A}$ idatziz,

$$
\left(\frac{\partial F_{t}}{\partial \mathscr{N}_ {A}}\right)_{T,p,N,\mathscr{N}} = 0
$$
betearazi, eta, horrela,

$$
\frac{\mathscr{N}_ {A}}{\mathscr{N}_ {B}} = \left(\exp\frac{\widehat{\mu}_ {B} - \widehat{\mu}_ {A}}{k_{\mathrm{B}}T}\right)^N
$$ (fracnanb)
berdintzara iritsiko gara. So egin diezaiogun berorri.

Oro har, {numref}`{number} ataleko <tpn_azter>` azalpenei jarraituz, potentzial kimiko integrala ingurune-aldagaien funtzioa da, hau da, $\widehat{\mu}_ {A,B} = \widehat{\mu}_ {A,B}(T,p,N)$. Hortaz, $p$ presioa finka dezakegu, halako moldez non bi potentzialak bat etorriko diren $(\widehat{\mu}_ {A} = \widehat{\mu}_ {B})$. Presioaren balio hori {numref}`{number}a irudiko <faseirudi>` $p_{0}$ delakoa da. Era berean, {eq}`fracnanb` ekuazioaren arabera, $\mathscr{N}_ {A} = \mathscr{N}_ {B}$  beteko da. Baina, $p_{0}$ baliotik zertxobait aldenduko balitz presioa, halako moduan non $\widehat{\mu}_ {A} \gtrsim \widehat{\mu}_ {B}$ edo $\widehat{\mu}_ {B} \gtrsim \widehat{\mu}_ {A}$, $N\rightarrow\infty$ limitean sistema ia guztiek $B$ eta $A$ egoeretara egingo lukete jauzi, hurrenez hurren, eta $\mathscr{N}_ {B} \gg \mathscr{N}_ {A}$ edo $\mathscr{N}_ {A} \gg \mathscr{N}_ {B}$ beteko litzateke. Bestela esanda, {eq}`fracnanb` ekuazioaren limite makroskopikoa bateragarria da _bi egoeren hurbilketarekin_. Edonola ere, $N$ behar bezain handia ez balitz, aurrekoa behatzeko presioa nabarmen aldendu beharko litzateke $p_{0}$ puntutik. Hori dela eta, $\Delta p$ presio-tarte aski zabal batean $\mathscr{N} _ {B} \gtrsim \mathscr{N}_ {A}$ edo $\mathscr{N}_ {A} \gtrsim \mathscr{N}_{B}$ behatuko genuke, eta egoera batetik besterako jauzia leunagoa litzateke.


Fase-trantsizioen azterketari buru emateko, aipatu beharrekoa da $p=p_{0}$ puntuan $(T,p,N)$ ingurune-aldagaiek konstante iraun behar dutela. Orduan, berdintza manten dadin, balio horien inguruko aldakuntzek $\mathrm{d}\widehat{\mu} _ {A}=\mathrm{d}\widehat{\mu}_{B}$ bete behar dute nahitaez. Baldintza hori eta {eq}`dmuhat` ekuazioa erabiliz, hona helduko gara:

$$
\frac{S_{A}-S_{B}}{N}\;\mathrm{d}T + \frac{V_{B}-V_{A}}{N}\;\mathrm{d}p + \frac{(\mu_{B}-\mu_{A}) + (\widehat{\mu} _ {A} - \widehat{\mu}_{B})}{N}\;\mathrm{d}N = 0 \; .
$$ (sasb)

Jakina, aztergai dugun puntuan $\Delta \widehat{\mu} = \widehat{\mu} _ {B}-\widehat{\mu}_{A}=0$ betetzen da. Hori kontuan izanik, gainontzeko magnitudeen aldakuntzekin honako erlazioak lortuko ditugu:


$$
\boxed{\left(\frac{\partial p}{\partial T}\right)_ {N} = \frac{\Delta S}{\Delta V}\quad ; \quad \left(\frac{\partial T}{\partial N}\right)_ {p} = \frac{\Delta \mu}{N\Delta \mathrm{s}}\quad ; \quad \left(\frac{\partial p}{\partial N}\right)_{T} = -\frac{\Delta \mu}{N\Delta \mathrm{v}}} \quad ,
$$ (neweq)
non $\mathrm{v} = V/N$ eta $\mathrm{s} = S/N$ diren. Ekuazio-sortako bigarren eta hirugarren erlazioak ez dira Termodinamikan ageri. Beroriek argiro iradokitzen dute tenperatura eta presioa ez direla, oro har, magnitude intentsiboak. Bada, ildo beretik, eta, aurrerapen gisara, {numref}`{number} adibidean <cryst_melt>` tamainarekiko menpekoa den $T$ tenperatura lortuko dugu.


(fase_simple)=
#### Adibide erraza

_Bi egoeren hurbilketaren_ zuzentasuna era kuantitatiboan adieraztea da adibide honen xedea. Demagun $A$ eta $B$ egoeretako $\overline{\mathrm{v}}_ {A}$ eta $\overline{\mathrm{v}}_ {B}$ bolumenak $p$ eta $N$ aldagaiekiko askeak direla. Berebat, $\widehat{\mu} = \widehat{\mu}_ {A,B}(p=p_{0})$ idatziko dugu. Bada, {eq}`dmuhat` ekuaziotik $\partial \widehat{\mu}_ {A,B}/\partial p = \overline{V}_ {A,B}/N = \overline{\mathrm{v}}_{A,B}$ erlazioa erauziz eta berori integratuz,

$$
\widehat{\mu}_ {A,B} = \widehat{\mu} + \overline{\mathrm{v}}_ {A,B}\left(p-p_{0}\right)
$$ (muhatab)
berdintzetara iritsiko gara. Ekuazio horren bidez {eq}`fracnanb` erlazioa berridatziko dugu:

$$
\frac{\mathscr{N}_ {A}}{\mathscr{N}_ {B}} = \exp\left[-N\frac{\left(\overline{\mathrm{v}}_ {A} - \overline{\mathrm{v}}_ {B}\right)\left(p-p_{0}\right)}{k_{\mathrm{B}}T}\right]\; .
$$ (nanbex)
Era berean, ekuazio beretik guztizko bolumena idatziz,

$$
\left(\frac{\partial F}{\partial p}\right)_{T,N
} := \overline{V} = \frac{\mathscr{N}_ {A}}{\mathscr{N}}\overline{V}_ {A} + \frac{\mathscr{N}_ {B}}{\mathscr{N}}\overline{V}_ {B}\equiv P_{A}\overline{V}_ {A} +  P_{B}\overline{V}_{B} \; ,
$$ (vtotex)
eta, $P_{A} = (\overline{\mathrm{v}} - \overline{\mathrm{v}}_ {B}) / (\overline{\mathrm{v}}_ {A} - \overline{\mathrm{v}}_ {B})$ eta $P_{B}=1-P_{A}$ direla ohartuz, hona iritsiko gara:

$$
\frac{(\overline{\mathrm{v}}_ {A} - \overline{\mathrm{v}}_ {B})(p-p_{0})}{k_{\mathrm{B}}T} = -\frac{1}{N}\ln\left[\frac{(\overline{\mathrm{v}} - \overline{\mathrm{v}}_ {B})/(\overline{\mathrm{v}}_ {A} - \overline{\mathrm{v}}_ {B})}{1-(\overline{\mathrm{v}} - \overline{\mathrm{v}}_ {B})/(\overline{\mathrm{v}}_ {A} - \overline{\mathrm{v}}_{B})}\right] \; .
$$ (fasesimplegraph)

Eraiki dezagun {eq}`fasesimplegraph` ekuazioaren grafikoa:

```{figure} faseplot.PNG
---
height: 300px
name: faseplot
---
Sistema txikietako fase-trantsizioen ereduztapen sinple honek agerian uzten du $N<40$ kasuetako bi kurbetan $A$ eta $B$ egoeren baterako existentziak presio-tarte handia hartzen duela. Era berean, $N=200$ kurbak jada {numref}`{number}a irudiaren <faseirudi>` tankera aurkezten du.
```
Errepara bekio {numref}`{number} irudiari <faseplot>`. Ohartu gaitezen grafikoa ezkerrerantz 90$^\circ$ biratuz gero, helize-haril adibideko {numref}`{number} irudiko <hc_phase>` kurba-sortarekin bat etorriko dela. Hori dela eta, bi adibide horiek bateragarriak dira. Bestela esanda, sendotasun handiagoz baiezta dezakegu helize-haril katean ere bi egoeren arteko fase-trantsizioa gauzatzen dela limite makroskopikoan.






(cryst_melt)=
#### Klastoaren fusioa

Bigarren adibide honetan, klasto esferiko baten fusio-tenperaturan sistemaren beraren tamainak duen eragina aztertuko dugu. Beraz, _bi egoeren hurbilketari_ segituz, $A$ egoera solidoa ($S$) eta $B$ egoera likidoa $(L)$ ditugu. Sistema txikien Gibbs-en energia askeak gai __lineal__ makroskopikoa $(\propto N)$ ez ezik, __gainazal-efektuei__ $(\propto N^{2/3})$ zein __errotazioari__ $(\propto \ln N)$ dagozkion ekarpen txikiak ere biltzen ditu, hau da,

$$
F(T,p,N) := N\widehat{\mu} = Nf(T,p) + N^{2/3}a(T,p) + \ln N \; b(T) \; .
$$ (fklasto)


Gauzak horrela, multzoan makroskopikoki behatuko diren bi egoeren _baterako existentziaren gunean_ ardaztuko dugu azterketa. Bertako tenperatura eta presioa $T_{\infty}$ eta $p_{\infty}$ izendatuko ditugu. Zehazki, oreka-egoera horretan, sistemaren tamainak tenperaturari sorrarazten dizkion desbideraketak kalkulatuko ditugu, presioa konstante mantenduz. Bada, {numref}`{number} ataleko <fase1order>` azalpenei jarraikiz, gune horretan $\Delta \widehat{\mu} = \widehat{\mu}_ {L} - \widehat{\mu}_{S} = 0$ beteko da. Baldintza hori eta {eq}`fklasto` ekuazioa erabiliz, honako hauxe izango dugu:

$$
\Delta \widehat{\mu}(T,p_{\infty},N) = \Delta f(T,p_{\infty}) + N^{-1/3}\Delta a(T,p_{\infty}) + \frac{\ln N}{N}\Delta b(T) = 0 \; .
$$ (muhatklasto)

Bertan $T$ aldagaia agerrarazteko, $\Delta f$ eta $\Delta a$ funtzioen $T=T_{\infty}$ puntuaren inguruko Taylorren hurbilketa idatzi, eta lehenengo gai ez-nulua ez beste guztiak baztertuko ditugu:

$$
\Delta f(T,p_{\infty}) \approx \left(\frac{\partial \Delta f}{\partial T}\right)_ {T_{\infty}}\left(T-T_{\infty}\right) = -\Delta \mathrm{s}_ {\infty}(T-T_{\infty})
$$
$$
\Delta a(T,p_{\infty}) \approx \Delta a(T_{\infty},p_{\infty}) \; .
$$

```{admonition} Oharra
 Baterako existentziaren gunean bi egoeren $f_{S}(T,p)$ eta $f_{L}(T,p)$ gai makroskopikoak bat datoz. Izan ere, limite termodinamikoan horixe da behatzen duguna: fase batetik besterako bat-bateko jauzia. Bertan azaltzen diren desbideraketak ekarpen txikien ondoriozkoak dira soilik. Hori dela eta, $\Delta f(T_{\infty},p_{\infty}) = 0$ betetzen dela onartu behar dugu.

```

Adierazpenok {eq}`muhatklasto` ekuazioan sartuz, honakoa da tenperaturak beteko duen ekuazioa:

$$
\boxed{T = T_{\infty} + N^{-1/3}\frac{\Delta a (T_{\infty},p_{\infty})}{\Delta \mathrm{s}_ {\infty}} + \frac{\ln N}{N}\frac{\Delta b(T_{\infty})}{\Delta \mathrm{s}_{\infty}}} \; .
$$ (t_ez_int)

Agerikoa da limite makroskopikoan behatuko den tenperaturari gehitu dizkiogun ekarpen txikiek izaera estentsiboa dutela.



Kapitulu honetan zehar aztertu ditugun fase-trantsizioekin loturiko iruzkinek biziki indartu dute {numref}`{number} azpiatalean <tpn_azter>` aurresandakoa. Batik bat, __$\widehat{\mu}$ potentzial kimiko integralaren__ berezko izaera finkatzeko lagungarriak izan zaizkigu. Hain zuzen, ikusi dugu berori azpisistema osoek pairatzen dituzten aldaketen adierazlea dela ({eq}`fracnanb` ekuazioa); eta, hartara, sistema txiki horiez osatutako __multzoaren propietateei__ erasaten diela. Aitzitik, __$\mu$ potentzial kimiko diferentzialak sistema txiki soilei__ eragiten dieten banakako molekulen aldakuntzak hartzen ditu aintzakotzat. Nanotermodinamikak zorrozki bereizten ditu bi efektu horiek.
