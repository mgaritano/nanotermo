(tpmu)=
## **6**. Multzo nanokanonikoa: $(T,p,\mu)$ ingurune-aldagaiak

Azken-aurreko kapitulu honetan teoriaren alor esanguratsuenari ekingo diogu. Demagun esku artean dugun sistema $N$ monomeroz osaturiko polimero agregatua dela, eta berori $T$ tenperaturan eta $p$ presiopean dagoela. Bada, molekulen arteko lotze-indarrak aski sendoak ez balira, luzaroan $N$ molekulen kopuruak ez luke finko iraungo, fluktuazioak jasango bailituzke. Hori dela eta, sistemari $\mu$ potentzial-kimikoa esleitu beharko genioke hirugarren ingurune-aldagaitzat; alegia, azterketa $(T,p,\mu)$ aldagaidun azpisistemak biltzen dituen multzo  nanokanonikoaren bitartez burutu beharko genuke baitezpada.

Alabaina, har dezagun gogoan [1](sarrera). atalean aipaturikoa: maila makroskopikoan ez dugu horrelako multzoa definitzerik izango, sistemaren hiru aldagai intentsiboetatik soilik bi izan baitaitezke aske (Gibbs-Duhem erlazioa). Horren harira, sistema txikiek $\mathcal{E}$ banatze-potentzialak ezaugarritzen duen askatasun-gradu berezia dutela onartu dugu. Hala, orain sistemaren tamainak aldagai intentsiboei erasango die. Horrek ahalbidetzen du, hain zuzen, multzo nanokanonikoaren eraikuntza. Hala ere, askatasun-gradu hori ez da nolanahikoa. Izan ere, sistema handitu ahala, funtzio termodinamikoetako ekarpen makroskopikoen gailentasunak berori desagerrarazi egingo dute.

```{admonition} Oharra
Hill-ek bere liburuan _multzo orokortu_ izena erabiltzen du ("_generalized ensemble_"), _multzo nanokanoniko_ beharrean.

```

Ildo horretatik, [6.2](mupt_linagg) eta [6.3](mupt_gi) adibideetako sistemei askatasun-gradu guztiak abiarazteak sorrarazten dituen ekarpen finituak kalkulatu, eta beroriek __entropian__ duten eraginari erreparatuko diogu, ondorio esanahitsuak erdietsiz. Berebat, limite makroskopikoan lortzen diren emaitzak gainontzeko multzo estatistikoenekin bateragarriak direnentz egiaztatuko dugu. Baina, lehenik, azterketarako beharrezkoa izango zaigun tresneria aurkeztuko dugu laburki.

(mupt_azter)=
### **6.1** Multzoaren azterketa

Aipatzekoa da multzo honi dagozkion adierazpen gehienak [3.1](hillteo) atalean eraiki ditugula, berori baita, hain zuzen, Hill-en teoriari heltzeko abiapuntu aproposa. Bada, {eq}`h_g_d` ekuazioa berridatziz, $S$ entropia, $\bar{V}$ bolumena eta $\bar{N}$ partikula-kopuruaren erlazioetara iritsiko gara:

$$
 \mathrm{d}\mathcal{E}(T,p,\mu) = \left(\frac{\partial \mathcal{E}}{\partial T}\right)_ {p,\mu}\mathrm{d}T +\left(\frac{\partial \mathcal{E}}{\partial p}\right)_ {T,\mu}\mathrm{d}p + \left(\frac{\partial \mathcal{E}}{\partial \mu}\right)_{T,p}\mathrm{d}\mu \; .
 $$ (depsilonnew)

 Jarraian, Fisika Estatistikoarekin lotura ezartze aldera, $\Upsilon(T,p,\mu)$ hizkiaren bidez adieraziko dugun __partizio-funtzio nanokanonikoaren__ eta multzoaren izaeraren isla den banatze-potentzialaren arteko erlazioa idatziko dugu:

$$
  \mathcal{E}(T,p,\mu) := -k_{\mathrm{B}}T\ln \Upsilon \; .
$$ (epspf)

Partizio-funtzio orokortua gainontzekoei kasuan kasuko Legendreren transformazioak aplikatuz kalkulatuko dugu. Esate baterako, multzo isotermo-isobarotik abiatuz,

$$
\Upsilon(T,p,\mu) := \sum_{E,V,N}\Omega(E,V,N)e^{-E/k_{\mathrm{B}}T}e^{-pV/k_{\mathrm{B}}T}e^{\mu N/k_{\mathrm{B}}T} \equiv \sum_{N}\Delta(T,p,N)e^{\mu N/k_{\mathrm{B}}T} \; .
$$ (upsilon_def)

(mupt_linagg)=
### **6.2** Adibidea: Agregatu lineala

Adibide honetako sistema txikia [10](agg). irudian azaltzen da. Multzo makroskopikoa sistema bereizgarriz osaturiko gas diluitua dela onartuko dugu. Horrela, aldakien arteko elkarrekintzak baztergarritzat joko dira, eta askatasun-gradu mekanikoa ez da aintzat hartuko.

```{figure} aggregate.PNG
---
height: 225px
name: agg
---
Agregatu lineala $N$ monomeroz osaturiko $Nm$ masadun eta $Na$ luzeradun hagaxka luzea da. Barne-higidurarekin lotutako $j(T)$ partizio-funtzioa dute unitateek; eta lehen auzokoen arteko elkarrekintza-energia $\epsilon$ da, negatiboa ($N-1$ ekarpen). Berebat, zentrutik igarotzen den ardatzarekiko biratu dezake hagaxkak. Inertzia-momentua $I = \frac{1}{12}N^{3}ma^{2}$ da.
```

Lehenbizi, sistema __multzo kanonikoan__ aztertuko dugu. Biraketari dagokion partizio-funtzioa

$$
Q_{\mathrm{rot}}(T,N) := \frac{4\pi^2}{h^2}I(N)k_{\mathrm{B}}T = \alpha(T)N^3
$$ (qrot)
daukagu.

```{admonition} Oharra
Ikus {cite}`pathria` liburuko 6. kapituluko 11. oin-oharra. Aurrerantzean, $\alpha(T) = \frac{\pi^2ma^2}{3h^2}k_{\mathrm{B}}T$ erabiliko dugu.
```

Unitateen ekarpen intrintsekoarekin zein berorien arteko elkarrekintzekin batera bilduz biraketaren eragina, partizio-funtzio kanonikoa eraikiko dugu. Hala, adierazpenak laburtze aldera $c = \alpha e^{\epsilon/k_{\mathrm{B}}T}$ definituz,

$$
\boxed{Q(T,N) := j(T)^{N} \cdot Q_{\mathrm{rot}}(T,N) \cdot e^{-(N-1)\epsilon/k_{\mathrm{B}}T} = c\;N^3j(T)^N\;e^{-N\epsilon/k_{\mathrm{B}}T}} \quad (N\geq1)\; .
$$ (qagg)

Ohartu gaitezen $N=0$ denean ez dela ez biraketarik ez, are gutxiago, elkarrekintza-energiarik egongo. Hori dela eta, partizio-funtzio intrintsekotik $Q(T,0)=j(T)^0=1$ izango dugu.

####  Ariketa

$(a)$ Kalkulatu $\widehat{\mu}$ eta $\mu$ potentzial kimikoak, baita berorien $N\rightarrow \infty$ limitea ere.

```{dropdown} __Erantzuna__

Partizio-funtzio kanonikoa erabiliz ({eq}`qagg` ekuazioa), eta $N\widehat{\mu} = -k_{\mathrm{B}}T\ln Q(T,N)$ betetzen dela gogora ekarriz,

$$
\left.\begin{array}{l}
\widehat{\mu}=-k_{\mathrm{B}}T\ln j + \frac{N-1}{N} \epsilon - \frac{\ln(\alpha N^3)}{N}k_{\mathrm{B}}T \\\\
\mu=-k_{\mathrm{B}}T\ln j + \epsilon -\frac{3}{N}k_{\mathrm{B}} T
\end{array}\right\}\underset{(N \rightarrow \infty)}{\boldsymbol{\longrightarrow}} \; \mu^{(0)} = -k_{\mathrm{B}}T\ln j + \epsilon
$$ (muagg)

```

$(b)$ Eraiki $S(T,N)/k_{\mathrm{B}}$ adierazpena. Aztertu limite makroskopikoan zer gertatzen den.

```{dropdown} __Erantzuna__

$$
\frac{S(T,N)}{k_{\mathrm{B}}} := -\frac{1}{k_{\mathrm{B}}}\left(\frac{\partial N\widehat{\mu}}{\partial T}\right)_{N} = N\ln j + NT\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} + \{1 + \ln\left(\alpha N^3\right) \}
$$ (stnagg)

Giltzen artean ageri diren ekarpenak biraketari dagozkio, eta tamaina finitukoak dira, limite termodinamikoan aurreko bi gai linealek baitaukate gailentasuna. Badirudi, hortaz, sistema makroskopikoak ez duela biraketaren eragina hautemango, ez eta unitateen arteko $\epsilon$ elkarrekintza ere.
```



Horiek horrela, askatasun-gradu kimikoa abiarazi, eta __multzo nanokanonikora__ igaroko gara. Hala, adierazpenetan $ x  =  je^{\left(\mu-\epsilon\right)/k_{\mathrm{B}}T}$ erlazioa sartuz, eta {eq}`upsilon_def` definizioan {eq}`qagg` ekuazioa txertatuz,

$$
\boxed{\Upsilon(T,\mu) = 1 + c\sum_{N=1}^{\infty}  N^{3}\;x^N = 1 +  c \left[\frac{6x^2}{(x-1)^4} + \frac{x}{(x-1)^2}\right]}\; , \; \vert x \vert < 1 \; ,
$$ (upsilontn)
izango dugu partizio-funtzio orokortua.

```{dropdown} __Seriearen garapena__

Abiatu gaitezen dagoeneko ezaguna dugun honako serie geometriko honetatik:

$$
\sum_{N=1}^{\infty}x^N = \frac{1}{1-x} \; , \; \vert x \vert < 1 \; .
$$

Jarraian, bi aldeen $x$-rekiko deribatuak kalkulatzeaz bat, $x$-rekin biderkatuko ditugu.

$$
\sum_{N=1}^{\infty}Nx^N = \frac{x}{(x-1)^2}
$$

Prozedura berbera segituz, $\sum_{N=1}^{\infty}N^2x^N$ kalkulatu, eta, jarraian, beharrezkoa zaigun $\sum_{N=1}^{\infty}N^3x^N$ berdintza eraikiko dugu:

$$
\sum_{N=1}^{\infty}N^3x^N = \frac{6x^2}{(x-1)^4} + \frac{x}{(x-1)^2} \; .
$$

```

Bertatik, eta {eq}`epspf` berdintza erabiliz,

$$
\mathcal{E}(T,\mu) = -k_{\mathrm{B}}T\ln \left\{1 + c\left[\frac{6x^2}{(x-1)^4} + \frac{x}{(x-1)^2}\right]\right\} \;
$$ (epsagg)
da banatze-potentziala.

Kontuan izan beharrekoa da, {eq}`muagg` ekuazioko $\mu^{(0)}$ potentzialari erreparatuz, $x = e^{({\mu} - \mu^{(0)})/k_{\mathrm{B}}T}$ berridaztea daukagula. Hortaz, limite makroskopikoan $x\rightarrow 1$ beteko da. Azter dezagun, bada, batez besteko partikula-kopuruan $x$ magnitudeak duen eragina.

$$
\bar{N} := -\left(\frac{\partial \mathcal{E}}{\partial \mu}\right)_{T} = c \; x \; P(0)\left[\frac{12 x(x-1)-24 x^{2}}{(x-1)^{5}}-\frac{x+1}{(x-1)^{3}}\right]
$$ (barnagg)

Espero bezala, $\bar{N}(x\rightarrow 1) \rightarrow \infty$ betetzen da. Entropiaren adierazpen berria eraiki, eta {eq}`barnagg` ekuazioaren laguntzaz trinkotuko dugu:

$$
\frac{S(T,\mu)}{k_{\mathrm{B}}} := -\frac{1}{k_{\mathrm{B}}} \left(\frac{\partial \mathcal{E}}{\partial T}\right)_ {\mu}  = \bar{N}\ln j + \bar{N}T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T}
$$
$$ + \left\{ - \bar{N}\ln x - \ln P(0) + cP(0)\left[1-\frac{\epsilon}{k_{\mathrm{B}} T}\right]\left[\frac{6 x^{2}}{(x-1)^{4}}+\frac{x}{(x-1)^{2}}\right] \right\}
$$(stmuagg)

Ohartu gaitezen aurreko bi ekuazioetan azaltzen den $P(0)$ funtzioa sistemak $N$ unitate izateko probabilitateak betetzen duen adierazpenetik erauzi dugula, alegia,

$$
P(N) := \frac{Q(T,N)e^{N\mu/k_{\mathrm{B}}T}}{\Upsilon}
$$(probagg)
ekuaziotik. Halaber, $Q(T,0) = 1$ denez, $P(0) = 1/\Upsilon$ beteko da.

Adibidearen mamiari helduz, erka ditzagun {eq}`stnagg` eta {eq}`stmuagg` ekuazioak. Lehenengo bi gaiek tankera bera aurkezten dutela dirudi. Alabaina, ernai ibili behar dugu, adierazpen batean $N$ ageri baita; eta, bestean, ordea, batez besteko $\bar{N}$. Itsumustuan aritu barik, eraiki dezagun $P(N)$ magnitudearen adierazpen grafikoa:

```{figure} pn_plot.PNG
---
height: 300px
name: pn_plot
---
Sistema txikien eskualdean ($x \ll 1$), maximo zolia du $N=\bar{N}$ puntuan probabilitate-banaketak, {eq}`barnagg` ekuazioaren bidez egiazta daitekeenez. Aitzitik, sistema handitu ahala, maximoaren kokapena lausotu egingo da, eta ez da $\mathrm{max}[P(N)] = P(\bar{N})$ beteko.
```

Orain bai, [11](pn_plot). irudiko oharrei atxikiz, zilegi zaigu {eq}`stnagg` eta {eq}`stmuagg` ekuazioetako lehen bi gaiak bat datozela baieztatzea. Hori argituta, berrar dezagun lehengo haria. So egin diezaiegun giltzen artean dagertzan tamaina finituko ekarpenei. Bada, multzo kanonikoko {eq}`stnagg` ekuazioaren kasuan, soilik biraketari dagokion askatasun-graduaren ondoriozkoak dira ekarpenok. Aitzitik, multzo nanokanonikoko {eq}`stmuagg` adierazpenean gai gehiago agertzen dira, guztiak positiboak. Izan ere, errotazioaz bestalde, $N$ partikula-kopuruaren inguruko fluktuazioek entropia areago handituko dute!

```{admonition} Oharrak
Oharteman bedi {eq}`stmuagg` ekuazioan $\epsilon < 0$ eta $x,P(0)<1$ betetzen dela. Bestalde, Hill-ek {cite}`hill` liburuko adibidean biraketa ez du aintzat hartzen. Hala, entropiarako gehikuntza fluktuazioekin lotzen du zuzenean, kasu horretan honakoa betetzen baita: $S-S^{(0)} = -k_{\mathrm{B}}\sum_{N}P(N)\ln P(N)\;$.
```

Azpiko kutxak adibide honetako ondorio nagusiak laburbiltzen ditu: (a) sistema erabat askean gertatzen den entropiaren handiagotzea, eta, (b) Nanotermodinamikaren eta Termodinamikaren arteko bateragarritasuna.

$$
\boxed{\begin{gathered}
    (a) \quad S(T,\mu) > S(T,N) \\
    \\
   (b) \quad  \frac{S(T,\mu)}{\bar{N}k_{\mathrm{B}}}\equiv \frac{S(T,N)}{Nk_{\mathrm{B}}} = \frac{\mathrm{s}^{(0)}}{k_{\mathrm{B}}} = \ln j + T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} \quad (\bar{N},N\rightarrow\infty)
\end{gathered}}
$$





(mupt_gi)=
### **6.3** Adibidea: Gas ideal klasikoa, multzo nanokanonikoan

Sistema honen bigarren berrazterketaren abiapuntua [4.3](gitpn) ataleko {eq}`dtpn_gi` ekuazioa da.

#### Ariketa
Eraiki honako adierazpen hauek: $\Upsilon(T,p,\mu)$ partizio-funtzioa, $\mathcal{E}$ banatze-potentziala eta $S(T,p,\mu)$ entropia. Jarraian, lortu $\bar{N}$ eta $\bar{V}$ magnitudeak eta berridatzi entropiaren ekuazioa haien baitan, hau da, $S(T,\bar{V},\bar{N})$.
```{dropdown} __Erantzuna__
 $\Delta(T,p,N)$ partizio-funtzioari askatasun-gradu kimikoa abiarazteak dakarren Legendreren transformazioa erantsiz,

$$
\Upsilon(T,p,\mu) = \sum_{N=0}^{\infty} \left(\frac{k_{\mathrm{B}}T\lambda}{p\Lambda^3}\right)^{N} = \frac{1}{1 - k_{\mathrm{B}}T\lambda/(p\Lambda^3)} \; , \; \left| \frac{k_{\mathrm{B}}T\lambda}{p\Lambda^3} \right| < 1
$$ (upsilongi)
izango dugu partizio-funtzio orokortua. Bertan $\lambda = e^{\mu/k_{\mathrm{B}}T}$ ordezkatu dugu. Hortaz,

$$
\mathcal{E}(T,p,\mu) = k_{\mathrm{B}}T \ln\left(1- \frac{k_{\mathrm{B}}T\lambda}{p\Lambda^3}\right) = -k_{\mathrm{B}}T \ln(\bar{N} + 1) < 0 \; .
$$ (epsilontpmugi)

Eskuinaldea {eq}`barnbarvtpmugi` bikotearen laguntzaz berridatzi dugu:

$$
 \bar{N} = \frac{1}{p\Lambda^3/(k_{\mathrm{B}}T\lambda) - 1} \quad , \quad \bar{V} = \frac{\bar{N}k_{\mathrm{B}}T}{p} \; .
$$(barnbarvtpmugi)

Horrela, entropiaren hirugarren adierazpenera iritsiko gara.

$$
\boxed{S(T,p,\mu) =  \bar{N}k_{\mathrm{B}}\left[\ln\left(\frac{\bar{V}}{\Lambda^3}\frac{\bar{N}+1}{\bar{N}^2}\right) + \frac{5}{2}\right] + k_{\mathrm{B}}\ln(\bar{N} + 1)}
$$ (stpmugi)
```
Errepara diezaiogun multzo nanokanonikoak itzulitako entropiaren {eq}`stpmugi` ekuazioari. Halaber, etor bekizkigu gogora multzo kanonikotik eta isotermo-isobarotik eskuratutako {eq}`stvngi` eta {eq}`stpngi` adierazpenak, eta ipin ditzagun hirurak parez pare. Guztietan Sackur-Tetrode adierazpen _estentsiboa_ ($S_{0}$) da gai nagusia. Baina, aurreneko bien aldean, {eq}`stpmugi` ekuazioak bigarren gai _positibo_ bat duela hauteman daiteke, eta, hori dela eta, sistema txikietan berori izango da nagusi ([12](sn100). irudia).

```{figure} sn100.PNG
---
height: 350px
name: sn100
---
Kurbak Ar gasari dagozkio (1 mol). Datuak honakoak dira: $\Lambda = 16,7 \; \mathrm{pm}$ ; $T=273,15 \; \mathrm{K}$ ; $N/V = 2,687\cdot10^{25}\; \mathrm{at/m^3}$. Agerikoa da, askatasun-graduak abiarazi ahala, eskualde nanotermodinamikoan tamaina finituko efektuek entropia handitu ez ezik, $S/Nk_{\mathrm{B}}$ magnitudea estentsibo bihurrarazi dutela.

```

Gainera, {eq}`epsilontpmugi` ekuazioaren eskuinaldeak entropiarako gehikuntza hori banatze-potentzialerako ekarpen _negatibo_ eta _ez-estentsiboaren_ ondoriozkoa dela diosku, alegia,

$$
S(T,p,\mu) = S_{0}(T,p,\mu) - \mathcal{E}(T,p,\mu)/T\;.
$$ (stpmuginew)

Jarraian datorren [6.4](stabeps) atalean $\mathcal{E}<0$ izateak multzoaren barruan aldaki-kopurua handitzea dakarrela ikusiko dugu ([13](gisub). irudia).

```{figure} gibbsparadox.PNG
---
height: 300px
name: gisub
---
Multzo nanokanonikoan __banatzearen areagotzeak bereizgarritasuna indartuko du__. Izan ere, hasiera batean bi aldakietako bakoitzean egon diren partikulak bereiztezinak izan dira, hain zuzen, aldakikide izateagatik. Aitzitik, bukaeran, azpisistemen arteko bereizte-hormek bereizgarri bihurrarazi dituzte. Horren ondorioz, entropiak gora egingo du.

```

Irudia eta {eq}`stpmugi` ekuazioa kontuan hartuz, multzoaren banatzearen ondoriozko ekarpenek entropiaren aldakuntza handituko dute, honako hau beteko baita: $\Delta S = k_{\mathrm{B}}\ln(\bar{N}+1)$. Banatzeari dagokion orekan, $\bar{N} \rightarrow 0$ eta, hortik, $\Delta S_{\text{oreka}}=0$. Baina, partikulako entropia hazi egingo da: $\lim_{\bar{N} \rightarrow 0}\Delta S/\bar{N} = 1$.

Aipatu beharrekoa da gaineko [13](gisub). irudiari lotutako azalpenak arras garrantzitsuak direla, multzo nanokanonikoari berebiziko esangura ematen baitiote. Esate baterako, demagun bi multzo makroskopikok gas berbera daukatela, eta tartean bereizte-horma bat ipini dugula. Horma  kenduz gero, bi multzoek bat egingo dute. Bada, Termodinamikatik abiatuz hau esango genuke: gasak bereizterik ez dagoenez, prozesuak itzulgarria beharko du izan, eta horrek $\Delta S = 0$ izatea dakar. Alabaina, izatez, bide horretatik jarraituz gero, __Gibbs-en paradoxarekin__ egingo dugu topo, entropiak egiatan aldakuntza positiboa jasango du eta. Horri aurre egiteko, partikulen bereiztezintasuna inposatuko dugu, eta, badirudi Gibbs-en $1/N!$ _ad hoc_ faktoreak arazoa konpontzen duela...

Aitzitik, Termodinamikak dioenaz haratago joan, eta, Nanotermodinamikan oinarritutako arrazoinamenduari jarraituko bagenio, honakoa ondorioztatuko genuke: bi sistemak elkartzeaz bat, multzoak banatzeari ekingo dio, partikulen bereizgarritasuna areagotuz. Hori dela eta, gasak berdinak diren arren, eskualde nanotermodinamikoan beroriek era __itzulezinean__ _nahasiko_ dira, eta multzoak nahasketa hori aldakien entropiaren gorakadan islatuko du, berori maximizatuz. Horrela, multzo nanokanonikoaren banatzea handituz, sistema txikietan Gibbs-en paradoxa saihestuko dugu bidenabar {cite}`nanointro, multiscale`.

Soluzio berritzailearen atzean dautzan tamaina finituko efektuak $\mathcal{E}$ potentzialaren gidaritzapean daude. Teoriari dagokion azkenengo atala berorri eskainiko diogu osorik, banatzeari dagokion orekan duen paperean sakonduz.


(mupt_sphagg)=
### **6.4** Adibidea: Agregatu esferikoa

_*Adibidea osatzen ari naiz..._

Jarraian aurkeztuko dugun analisiak [6.3](mupt_linagg) ataleko adibidearen tankera du. Oraingoan, aitzitik, unitate osatzaileen biraketa barik, gainazal- eta kurbatura-efektuen eraginari erreparatuko diogu. Horiek horrela, aztergai izango dugun sistema $N$ monomeroz osaturiko agregatu esferiko konprimaezina da; hartara, askatasun-gradu mekanikoa ez dugu aintzat hartuko; beraz, azterketa $(T,N)$ ingurune-aldagaien bidez jarriko dugu abian. Agregatu linealaren kasuan bezalaxe, unitateei $j(T)$ partizio-funtzio intrintsekoa esleituko diegu. Horrez gain, $a(T)N^{2/3}$ gainazaleko energia askearen ekarpena kontuan izango dugu ($a>0$). Aipatzekoa da $a(T)$ magnitudea $\gamma$ gainazal-tentsioarekiko proportzionala dela. Berebat, formulazioa osatze aldera, gainazal esferikoaren kurbaturaren ondoriozko gainazal-tentsioaren aldakuntza ere hartuko dugu aintzat. Hark $b(T)N^{1/3}$ ekarpena gaineratuko du ($b>0$). Hill-en liburuan ({cite}`hill`) zenbaitetan ageri da adibide hau. Bada, esan beharrekoa da horietan guztietan kurbaturaren eragina baztertu egiten dela. Guk, azterketa honetan, gainontzeko ekarpenekiko zuzenketa txikitzat joko dugu, $a\gg b$ hartuz. Hori onartzeak nabarmenki arinduko du $\Upsilon (T,\mu)$ partizio-funtzioa kalkulatzeko bidea.

Lehenbizi, $Q(T,N)$ partizio-funtzio kanonikoa eraikiko dugu, hurbilketarik gabe.

$$
Q(T,N) = j(T)^N\;\exp\left[{\frac{-a(T)N^{2/3}}{k_{\mathrm{B}}T}}\right]\exp\left[{\frac{-b(T)N^{1/3}}{k_{\mathrm{B}}T}}\right]
$$ (qagg_sph)

Bertatik, $Q=e^{-\widehat{\mu}N/k_{\mathrm{B}}T}$ erlazioa gogora ekarriz, poentzial kimiko diferentziala eta integrala eskuratuko ditugu, baita banatze-potentziala ere:

$$
\left.\begin{array}{l}
\widehat{\mu}=-k_{\mathrm{B}}T\ln j + N^{-1/3}\;a(T) + N^{-2/3}\;b(T)\\\\
\mu=-k_{\mathrm{B}}T\ln j +\frac{2}{3} N^{-1/3}\;a(T) + \frac{1}{3} N^{-2/3}\;b(T)
\end{array}\right\}\underset{(N \rightarrow \infty)}{\boldsymbol{\longrightarrow}} \; \mu^{(0)}(T) = -k_{\mathrm{B}}T\ln j \; ,
$$ (sph_agg_mu)

$$
\mathcal{E} = N\left(\widehat{\mu}-\mu\right) = \frac{1}{3}N^{2/3}a(T) + \frac{2}{3}N^{1/3}b(T) \; .
$$ (sph_epsilon)

Horiekin batera, honako bi magnitudeak idatziko ditugu, gerora erabilgarriak gertatuko zaizkigu eta:

$$
\left.\begin{array}{l}
\widehat{\mu}^{(x)} = \widehat{\mu} - \mu^{(0)} = N^{-1/3}\;a(T) + N^{-2/3}\;b(T)\\\\
\mu^{(x)} = \mu - \mu^{(0)} = \frac{2}{3}N^{-1/3}\;a(T) + \frac{1}{3}N^{-2/3}\;b(T)
\end{array}\right\}
$$ (excess_mu)

```{admonition} Oharra
Hill-ek $\widehat{\mu}^{(x)}$ eta $\mu^{(x)}$ magnitudeei gehiegizko termino deritze (_excess terms_). Hurrenez hurren, $\widehat{\mu}$ eta $\mu$ potentzial kimikoen tamaina finituko efektuen adierazle dira.
```

Aurreko ekuazioetatik entropia eta barne-energiaren batez bestekoa kalkulatuko ditugu, ondoren $S(T,\mu)$ eta $\bar{E}(T, \mu)$ adierazpenekin alderaketak egin ahal izateko:

$$
\boxed{S(T,N) = -\left(\frac{\partial N\widehat{\mu}}{\partial T}\right)_{N} = Nk_{\mathrm{B}}\left(\ln j + T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T}\right) - N^{2/3}\frac{\mathrm{d}a}{\mathrm{d}T} - N^{1/3}\frac{\mathrm{d}b}{\mathrm{d}T}} \; ,
$$ (s_sph_agg)

$$
\bar{E}(T,N) = \widehat{\mu}N + TS = Nk_{\mathrm{B}}T^2\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} + N^{2/3}\left(a -T\frac{\mathrm{d}a}{\mathrm{d}T}\right) + N^{1/3}\left(b -T\frac{\mathrm{d}b}{\mathrm{d}T}\right) \; .
$$

Orain __multzo nanokanonikora__ eramango dugu azterketa. Definizioaren adierazpena {eq}`excess_mu` ekuazio-bikotearen bidez berridatziko dugu, hain zuzen, $\widehat{\mu}^{(x)}$ eta $\mu^{(x)}$ gaiak agerrarazteko.

$$
\Upsilon(T,\mu) = \sum_{N=0}^{\infty}e^{-\widehat{\mu}N/k_{\mathrm{B}}T}e^{{\mu}N/k_{\mathrm{B}}T} = \sum_{N=0}^{\infty}e^{-\widehat{\mu}^{(x)}N/k_{\mathrm{B}}T}e^{{\mu^{(x)}}N/k_{\mathrm{B}}T}
$$ (upsilon_sph)


Kontuan izan dezagun {eq}`upsilon_sph` ekuazioan $\mu^{(x)}$ positiboa izateak seriearen dibergentzia lekarkeela, $N$ handietarako $e^{{\mu^{(x)}}N/k_{\mathrm{B}}T}$ esponentziala gailenduko bailitzateke. Beraz, $\mu^{(x)} \leq 0$ inposatu beharko dugu konbergentzia bermatzeko (ekar dezagun gogora $a$ eta $b$ positiboak direla, eta, ondorioz, $\widehat{\mu}^{(x)}$ ere bai). Izan ere, ondoren ikusiko dugunez, $\mu^{(x)} > 0$ edo $\mu > \mu^{(0)}(T)$ izatearen ondoriozko dibergentziak $\bar{N} = \infty$ ekarriko du. Aurrera egin baino lehen, komenigarria da honako notazio hau sartzea:

$$
\delta(T,\mu) = \frac{-\mu^{(x)}}{k_{\mathrm{B}}T} = \frac{\mu^{(0)}-\mu}{k_{\mathrm{B}}T} \quad , \quad \alpha(T) = \frac{a(T)}{k_{\mathrm{B}}T} \quad , \quad \beta(T) = \frac{b(T)}{k_{\mathrm{B}}T} \; .
$$

Gauzak horrela, kalkuluei ekin aurretik, bada argitu beharreko beste hainbat kontu. Izan ere, aurreko paragrafoko azalpenei jarraituz, aztergai dugun agregatuaren tamaina zentzuzkoa izan dadin, $\delta \rightarrow 0^{+}$ limitera jo beharko dugu, hark mantenduko baikaitu dibergentziatik urrun. Bestalde, $aN^{2/3}$ gainazal energia askea errealista izango da soilik $N$ aski handietarako (adibidez, $N>20$). Hori dela eta, {eq}`upsilon_sph` ekuazioan, $N$ aldagaiarekiko batukariaren ordez, integrala kalkulatuko dugu. Aipatzekoa da eredu hau $N$ txikietarako desegokia izanagatik, $\bar{N}$ handi samarra denean errorea ez dela hain esanahitsua izango. Bukatzeko, arestian kurbatura-efektuen inguruan esandakoaren harira, $\beta \rightarrow 0$ limitea erabiltzea ere zilegi zaigu. Azaldutako hori guztia jarraian datorren partizio-funtzioaren adierazpen moldatuan islatuko dugu:

$$
\Upsilon (T,\mu) \approx \int_0^\infty \mathrm{d}N\;\left[1-\delta(T,\mu) N\right] \; e^{-\alpha(T) N^{2/3}}\left[1-\beta(T) N^{1/3}\right] \; .
$$ (upsilon_sph_int)

```{dropdown} __Oharra__
Atal honetan zehar azalduko diren integralen kalkuluak arras luzeak eta konplexuak dira. Esaterako, {eq}`upsilon_sph_int` ekuazioan ageri denak hiru aldagai-aldaketa egitea eskatzen du. Inork kalkuluei ekiteko ausardia balu, jakin beza integral mugatu horren soluzioa honako hau dela:

$$
 \dfrac{\mathrm{e}^{-{\alpha}N^\frac{2}{3}}\cdot\left(\left(45\sqrt{{\pi}}\,{\alpha}^3{\beta}{\delta}+12\sqrt{{\pi}}\,{\alpha}^5\right)\operatorname{erf}\left(\sqrt{{\alpha}}\sqrt[3]{N}\right)\,\mathrm{e}^{{\alpha}N^\frac{2}{3}}-24{\alpha}^\frac{11}{2}{\beta}{\delta}N^\frac{5}{3}+24{\alpha}^\frac{11}{2}{\delta}N^\frac{4}{3}-60{\alpha}^\frac{9}{2}{\beta}{\delta}N+\left(48{\alpha}^\frac{9}{2}{\delta}+24{\alpha}^\frac{11}{2}{\beta}\right)N^\frac{2}{3}+\left(-90{\alpha}^\frac{7}{2}{\beta}{\delta}-24{\alpha}^\frac{11}{2}\right)\sqrt[3]{N}+48{\alpha}^\frac{7}{2}{\delta}+24{\alpha}^\frac{9}{2}{\beta}\right)}{16{\alpha}^\frac{13}{2}}
$$


Guk, jakina, sistemaren azterketa nanotermodinamikoa burutzea dugunez xedea, ez gara inondik inora horrelako sasiarteetan sartuko.

```

Integral mugatuaren emaitza honako hau dugu:

$$
\Upsilon (T,\mu) = \frac{\pi^{1/2}\left(45\delta\beta+12\alpha^2\right)}{16\alpha^{7/2}} - \frac{3\beta}{2\alpha^2} - \frac{3\delta}{\alpha^3}
$$


(stabeps)=
### **6.5** Banatze-potentziala eta egonkortasuna

Hasteko, dakargun gogora $\mathcal{E}$ potentzialaren definizioa: multzoaren aldaki-kopuruan eragiteak berorren guztizko energiari dakarkion ekarpena, gainontzeko kasuan kasuko ingurune-aldagaiak konstante mantenduz, hau da,

$$
\mathcal{E} := \left(\frac{\partial E_{t}}{\partial \mathcal{N}}\right)_ {S_{t},V_{t}, N_{t}} \equiv \left(\frac{\partial A_{t}}{\partial \mathcal{N}}\right)_ {T,V_{t}, N_{t}} \equiv \left(\frac{\partial F_{t}}{\partial \mathcal{N}}\right)_ {T,p, N_ {t}} \; .
$$ (epsilonnewdef)

Bestela esanda, multzo nanokanonikoaren kasuan, aldaki berri bat sorrarazteko multzoari berari egin beharreko lana da.

Horren harira, atal honetan denboran batez besteko $\bar{\mathcal{N}}$ aldaki-kopuruak jasango dituen aldakuntzen izaera espontaneoa izango dugu hizpide. Multzoko azpisistemak erabat askeak direla onartuko dugu, baina, gutxienez partikula bat izan beharko dute ($N \geq 1$). Era berean, multzoko inguruneko aldagai-sorta $(T,p,N_{t})$ izango dugu, non $N_{t}=\bar{\mathcal{N}}\bar{N}$ den.

Bada, prozesu espontaneoan zehar orekaranzko bidean, minimorantz joko du $F_{t}(T,p,N_{t})$ energia askeak, eta, beraz, $\mathrm{d}F_{t}<0$. Prozesuak dirauela multzoa isolatuta mantentzen bada, $\bar{\mathcal{N}}$ ez beste aldagai guztiek bere horretan iraungo dute. Hori dela eta, {eq}`epsilonnewdef` ekuazioaren eskuinaldetik,

$$
\mathrm{d}F_{t}=\mathcal{E}\mathrm{d}\bar{\mathcal{N}}<0\; .
$$ (dft)

Adierazpen horrek honakoa iradokitzen du: banatze-potentziala positiboa denean, aldaki-kopuruak behera egingo du, eta, negatiboa denean, aldiz, multzoaren banatzea areagotuko da, aldaki txikiagoak sorraraziz (oroitu gaitezen [13](gisub). irudiaz). Era berean, orekara heldutakoan, energia minimoan egongo denez,

$$
\left(\frac{\partial^2 F_{t}}{\partial \bar{\mathcal{N}}^2}\right)_{T,p, N_{t}} = \left(\frac{\partial \mathcal{E}}{\partial \bar{\mathcal{N}}}\right)_{T,p, N_{t}} > 0 \; .
$$ (d2f)

Bertatik agerikoa da $\mathrm{d}\mathcal{E}$ eta $\mathrm{d}\bar{\mathcal{N}}$ zeinu berekoak direla. Horrez gain, {eq}`dft`  ekuazioa aintzat hartuz, $\mathcal{E}\cdot\mathrm{d}\mathcal{E}<0$ beteko da. Ondorio esanahitsu hori [6.3](mupt_gi) adibideko azalpena osatzeko lagungarria izango zaigu: $\mathcal{E}$ eta $\mathrm{d}\mathcal{E}$ aurkako zeinudunak direnez, $\bar{\mathcal{N}}$ aldatuz doan neurrian, $\mathcal{E}$ potentzialak zerorantz joko du, harik eta orekara heldu arte. __Banatzeari dagokion oreka-egoera__ batek $\mathcal{E} = 0$ baldintza bete beharko du.

Esaldi hori dela eta, azken kontu bat argitu beharrean gaude. Berorri heltzeko, gas idealaren adibidea berreskuratuko dugu. Ezer baino lehen, kontuan izan dezagun multzoko sistema txikiei $N\geq1$ baldintza ezarri diegula. Hortaz, {eq}`upsilongi`  ekuaziotik $N=0$ gaia erauzi beharko dugu. Bada, $x=k_{\mathrm{B}}T\lambda/(p\Lambda^3)$ ordezkatuz,

$$
 \Upsilon = \frac{x}{1-x}
$$ (upsilonginew)
izango da partizio-funtzio eraldatua. Bertatik $\mathcal{E}$ eta $\bar{N}$ magnitudeak birkalkulatuko ditugu:

$$
\mathcal{E} = -k_{\mathrm{B}}T\ln\left(\frac{x}{1-x}\right) = -k_{\mathrm{B}}T\ln\left(\bar{N}-1\right) \; ,
$$ (epsginew)

$$
 \bar{N} = \frac{1}{1-x} = 1 + e^{-\mathcal{E}/k_{\mathrm{B}}T} \; .
$$ (barnginew)


Demagun orain $\bar{\mathcal{N}}$ azpisistema-kopuruari eragingo dion prozesu espontaneoa abian jartzen dugula, $T$ eta $p$ konstante mantenduz. Banatzeak dirauela ($\mathrm{d}\bar{\mathcal{N}}<0$ edo $\mathrm{d}\bar{\mathcal{N}}>0$), entropiak $\Delta S=\pm k_{\mathrm{B}}\ln(\bar{N}/2)$ aldakuntza jasango duela frogatu daiteke.  Orekara ailegatutakoan,

$$
\mathcal{E}_ {\text{oreka}} = 0 \quad \Rightarrow \quad \bar{N}_ {\text{oreka}}=2 \quad \text{eta} \quad \Delta S_{\text{oreka}}=0 \; .
$$

Gogora dezagun lehen, partizio-funtzioan $N=0$ gaia sartzeagatik, $\bar{N}\rightarrow 0$ baldintzak ginderamatzala orekara, zeinak banatzea etengabekoa dela iradoki bailezake. Horren aldean, orain lorturiko emaitzek esangura eta zentzu fisiko handiagoa dute.


Amaitzeko, argitzeko geratu den alderdiari helduko diogu. Aurreko zenbait ataletan esan bezala, limite makroskopikoan $\bar{N}$ aldagaiarekin erlazio lineala betetzen duten ekarpenak biziki gailenduko dira banatze-potentzialarekiko, eta, beraz, $\mathcal{E}$ baztergarri bilakatuko da. Bada, azken esaldi hori iruzurtia gerta lekiguke, arrazoibide okerretik eraman gintzake eta, honakoa pentsaraziz: sistema makroskopikoak $\mathcal{E}\approx 0$ hautemango duenez, _limite makroskopikoa bera oreka-egoeratzat hartzea daukagu_.

Izan ere, horren aurrean erne ibili behar dugu! Esate baterako, gas idealaren kasuan, {eq}`epsginew` ekuazioak $\bar{N}\rightarrow \infty$ limitean

$$
\mathcal{E} = -k_{\mathrm{B}}T\ln \bar{N}
$$ (epslimgi)
adierazpenari segituko dio, eta, ondorioz, moduluz gora egingo du, astiro bada ere. Egia da, bai, beste zenbait kasutan ([4.2](helix_coil) zein [7](app). ataletako sistemetan, adibidez) eskuratzen diren adierazpenek $\mathcal{E}\rightarrow 0$ betetzen dutela limite makroskopikoan, baina {eq}`epslimgi` ekuazioak argiro diosku oro har ez dela hala gertatuko! Gainera, nabarmendu beharrekoa da banatze-potentzialaren zeroranzko limite horren esanahia ez datorrela bat orekak zorrozki eskatzen duen $\mathcal{E}=0$ baldintzarekin. Hortaz, eskuarki, ez zaigu zilegi izango egoera makroskopikoa oreka-egoera baten baliokidea dela iradokitzea.


Iruzkin argigarri horiekin itxiko dugu Sistema Txikien Termodinamikari dagokion teoriaren zatia. Lanaren azkenengo atalean 1960. hamarkadatik 2021era jauzi egin, eta dagoeneko luzaz jorratu dugun teoriaren aplikazio garrantzitsu batean murgilduko gara.
