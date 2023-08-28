(tpmu)=
## Multzo nanokanonikoa: $(T,p,\mu)$ ingurune-aldagaiak

Azken-aurreko kapitulu honetan teoriaren alor esanguratsuenari ekingo diogu. Demagun esku artean dugun sistema $N$ monomeroz osaturiko polimero agregatua dela, eta berori $T$ tenperaturan eta $p$ presiopean dagoela. Bada, molekulen arteko lotze-indarrak aski sendoak ez balira, luzaroan $N$ molekulen kopuruak ez luke finko iraungo, fluktuazioak jasango bailituzke. Hori dela eta, sistemari $\mu$ potentzial-kimikoa esleitu beharko genioke hirugarren ingurune-aldagaitzat; alegia, azterketa $(T,p,\mu)$ aldagaidun azpisistemak biltzen dituen multzo  nanokanonikoaren bitartez burutu beharko genuke baitezpada.

Alabaina, har dezagun gogoan {numref}`{number}. atalburuan <nanointro>` aipaturikoa: maila makroskopikoan ez dugu horrelako multzoa definitzerik izango, sistemaren hiru aldagai intentsiboetatik soilik bi izan baitaitezke aske (Gibbs-Duhem erlazioa). Horren harira, sistema txikiek $\mathscr{E}$ banatze-potentzialak ezaugarritzen duen askatasun-gradu berezia dutela onartu dugu. Hala, orain sistemaren tamainak aldagai intentsiboei erasango die. Horrek ahalbidetzen du, hain zuzen, multzo nanokanonikoaren eraikuntza. Hala ere, askatasun-gradu hori ez da nolanahikoa. Izan ere, sistema handitu ahala, funtzio termodinamikoetako ekarpen makroskopikoen gailentasunak berori desagerrarazi egingo dute.

```{admonition} Oharra
Hill-ek bere liburuan _multzo orokortu_ izena erabiltzen du ("_generalized ensemble_"), _multzo nanokanoniko_ beharrean.

```

Ildo horretatik, {numref}`{number} <mupt_linagg>` eta {numref}`{number} <mupt_gi>` adibideetako sistemei askatasun-gradu guztiak abiarazteak sorrarazten dituen ekarpen finituak kalkulatu, eta beroriek __entropian__ duten eraginari erreparatuko diogu, ondorio esanahitsuak erdietsiz. Berebat, limite makroskopikoan lortzen diren emaitzak gainontzeko multzo estatistikoenekin bateragarriak direnentz egiaztatuko dugu. Baina, lehenik, azterketarako beharrezkoa izango zaigun tresneria aurkeztuko dugu laburki.

(mupt_azter)=
### Multzoaren azterketa

Aipatzekoa da multzo honi dagozkion adierazpen gehienak {numref}`{number} azpiatalean <hillteo>` eraiki ditugula, berori baita, hain zuzen, Hill-en teoriari heltzeko abiapuntu aproposa. Bada, {eq}`h_g_d` ekuazioa berridatziz, $S$ entropia, $\bar{V}$ bolumena eta $\bar{N}$ partikula-kopuruaren erlazioetara iritsiko gara:

$$
 \mathrm{d}\mathscr{E}(T,p,\mu) = \left(\frac{\partial \mathscr{E}}{\partial T}\right)_ {p,\mu}\mathrm{d}T +\left(\frac{\partial \mathscr{E}}{\partial p}\right)_ {T,\mu}\mathrm{d}p + \left(\frac{\partial \mathscr{E}}{\partial \mu}\right)_{T,p}\mathrm{d}\mu \; .
 $$ (depsilonnew)

 Jarraian, Fisika Estatistikoarekin lotura ezartze aldera, $\Upsilon(T,p,\mu)$ hizkiaren bidez adieraziko dugun __partizio-funtzio nanokanonikoaren__ eta multzoaren izaeraren isla den banatze-potentzialaren arteko erlazioa idatziko dugu:

$$
  \mathscr{E}(T,p,\mu) := -k_{\mathrm{B}}T\ln \Upsilon \; .
$$ (epspf)

Partizio-funtzio orokortua gainontzekoei kasuan kasuko Legendreren transformazioak aplikatuz kalkulatuko dugu. Esate baterako, multzo isotermo-isobarotik abiatuz,

$$
\Upsilon(T,p,\mu) := \sum_{E,V,N}\Omega(E,V,N)e^{-E/k_{\mathrm{B}}T}e^{-pV/k_{\mathrm{B}}T}e^{\mu N/k_{\mathrm{B}}T} \equiv \sum_{N}\Delta(T,p,N)e^{\mu N/k_{\mathrm{B}}T} \; .
$$ (upsilon_def)

(mupt_linagg)=
### Adibidea: Agregatu lineala

Adibide honetako sistema txikia {numref}`{number} irudian <agg>` azaltzen da. Multzo makroskopikoa sistema bereizgarriz osaturiko gas diluitua dela onartuko dugu. Horrela, aldakien arteko elkarrekintzak baztergarritzat joko dira, eta askatasun-gradu mekanikoa ez da aintzat hartuko.

```{figure} aggregate.PNG
---
height: 225px
name: agg
---
Agregatu lineala $N$ monomeroz osaturiko $Nm$ masadun eta $Na$ luzeradun hagaxka luzea da. Barne-higidurarekin lotutako $j(T)$ partizio-funtzioa dute unitateek; eta lehen auzokoen arteko elkarrekintza-energia $\epsilon$ da, negatiboa ($N-1$ ekarpen). Berebat, zentrutik igarotzen den ardatzarekiko biratu dezake hagaxkak. Inertzia-momentua $I = \frac{1}{12}N^{3}ma^{2}$ da.
```

Lehenbizi, sistema __multzo kanonikoan__ aztertuko dugu. Biraketari dagokion partizio-funtzioa

$$
Q_{\mathrm{bir}}(T,N) := \frac{4\pi^2}{h^2}I(N)k_{\mathrm{B}}T = \xi(T)N^3
$$ (qrot)
daukagu.

```{admonition} Oharra
Ikus {cite}`pathria` liburuko 6. kapituluko 11. oin-oharra. Aurrerantzean, $\xi(T) = \frac{\pi^2ma^2}{3h^2}k_{\mathrm{B}}T$ erabiliko dugu.
```

Unitateen ekarpen intrintsekoarekin zein berorien arteko elkarrekintzekin batera bilduz biraketaren eragina, partizio-funtzio kanonikoa eraikiko dugu. Hala, adierazpenak laburtze aldera $c(T) = \xi(T) e^{\epsilon/k_{\mathrm{B}}T}$ definituz,

$$
\boxed{Q(T,N) := j(T)^{N} \cdot Q_{\mathrm{bir}}(T,N) \cdot e^{-(N-1)\epsilon/k_{\mathrm{B}}T} = c(T)\;N^3j(T)^N\;e^{-N\epsilon/k_{\mathrm{B}}T}} \quad (N\geq1)\; .
$$ (qagg)

Ohartu gaitezen $N=0$ denean ez dela ez biraketarik ez, are gutxiago, elkarrekintza-energiarik egongo. Hori dela eta, partizio-funtzio intrintsekotik $Q(T,0)=j(T)^0=1$ izango dugu.

#####  Ariketa

$(a)$ Kalkulatu $\widehat{\mu}$ eta $\mu$ potentzial kimikoak, baita berorien $N\rightarrow \infty$ limitea ere.

```{dropdown} __Erantzuna__

Partizio-funtzio kanonikoa erabiliz ({eq}`qagg` ekuazioa), eta $N\widehat{\mu} = -k_{\mathrm{B}}T\ln Q(T,N)$ betetzen dela gogora ekarriz,

$$
\left.\begin{array}{l}
\widehat{\mu}=-k_{\mathrm{B}}T\ln j + \frac{N-1}{N} \epsilon - \frac{\ln(\xi N^3)}{N}k_{\mathrm{B}}T \\\\
\mu=-k_{\mathrm{B}}T\ln j + \epsilon -\frac{3}{N}k_{\mathrm{B}} T
\end{array}\right\}\underset{(N \rightarrow \infty)}{\boldsymbol{\longrightarrow}} \; \mu^{(0)} = -k_{\mathrm{B}}T\ln j + \epsilon
$$ (muagg)

```

$(b)$ Eraiki $S(T,N)/k_{\mathrm{B}}$ adierazpena. Aztertu limite makroskopikoan zer gertatzen den.

```{dropdown} __Erantzuna__

$$
\frac{S(T,N)}{k_{\mathrm{B}}} := -\frac{1}{k_{\mathrm{B}}}\left(\frac{\partial N\widehat{\mu}}{\partial T}\right)_{N} = N\ln j + NT\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} + \{1 + \ln\left(\xi N^3\right) \}
$$ (stnagg)

Giltzen artean ageri diren ekarpenak biraketari dagozkio, eta tamaina finitukoak dira, limite termodinamikoan aurreko bi gai linealek baitaukate gailentasuna. Badirudi, hortaz, sistema makroskopikoak ez duela biraketaren eragina hautemango, ez eta unitateen arteko $\epsilon$ elkarrekintza ere.
```

**----------------------------------------------------**

Horiek horrela, askatasun-gradu kimikoa abiarazi, eta __multzo nanokanonikora__ igaroko gara. Hala, adierazpenetan $ x(T,\mu)  =  je^{\left(\mu-\epsilon\right)/k_{\mathrm{B}}T}$ erlazioa sartuz, eta {eq}`upsilon_def` definizioan {eq}`qagg` ekuazioa txertatuz,

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
\mathscr{E}(T,\mu) = -k_{\mathrm{B}}T\ln \left\{1 + c\left[\frac{6x^2}{(x-1)^4} + \frac{x}{(x-1)^2}\right]\right\} \;
$$ (epsagg)
da banatze-potentziala.

Kontuan izan beharrekoa da, {eq}`muagg` ekuazioko $\mu^{(0)}$ potentzialari erreparatuz, $x = e^{({\mu} - \mu^{(0)})/k_{\mathrm{B}}T}$ berridaztea daukagula. Hortaz, limite makroskopikoan $x\rightarrow 1$ beteko da. Azter dezagun, bada, batez besteko partikula-kopuruan $x$ magnitudeak duen eragina.

$$
\bar{N} := -\left(\frac{\partial \mathscr{E}}{\partial \mu}\right)_{T} = c \; x \; P(0)\left[\frac{12 x(x-1)-24 x^{2}}{(x-1)^{5}}-\frac{x+1}{(x-1)^{3}}\right]
$$ (barnagg)

Espero bezala, $\bar{N}(x\rightarrow 1) \rightarrow \infty$ betetzen da. Entropiaren adierazpen berria eraiki, eta {eq}`barnagg` ekuazioaren laguntzaz trinkotuko dugu:

$$
\frac{S(T,\mu)}{k_{\mathrm{B}}} := -\frac{1}{k_{\mathrm{B}}} \left(\frac{\partial \mathscr{E}}{\partial T}\right)_ {\mu}  = \bar{N}\ln j + \bar{N}T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T}
$$
$$ + \left\{ - \bar{N}\ln x - \ln P(0) + cP(0)\left(1-\frac{\epsilon}{k_{\mathrm{B}} T}\right)\frac{x(x^{2}+4x+1)}{(x-1)^{4}}\right\}
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
Sistema txikien eskualdean $(x \ll 1)$, maximo zolia du $N=\bar{N}$ puntuan probabilitate-banaketak, {eq}`barnagg` ekuazioaren bidez egiazta daitekeenez. Aitzitik, sistema handitu ahala, maximoaren kokapena lausotu egingo da, eta ez da $\mathrm{max}[P(N)] = P(\bar{N})$ beteko.
```

Orain bai, {numref}`{number} irudiko <pn_plot>` oharrei atxikiz, zilegi zaigu {eq}`stnagg` eta {eq}`stmuagg` ekuazioetako lehen bi gaiak bat datozela baieztatzea. Hori argituta, berrar dezagun lehengo haria. So egin diezaiegun giltzen artean dagertzan tamaina finituko ekarpenei. Bada, multzo kanonikoko {eq}`stnagg` ekuazioaren kasuan, soilik biraketari dagokion askatasun-graduaren ondoriozkoak dira ekarpenok. Aitzitik, multzo nanokanonikoko {eq}`stmuagg` adierazpenean gai gehiago agertzen dira, guztiak positiboak. Izan ere, biraketaz bestalde, $N$ partikula-kopuruaren inguruko fluktuazioek entropia areago handituko dute!

```{admonition} Oharra
Oharteman bedi {eq}`stmuagg` ekuazioan $x < 1$ eta $P(0) \leq 1$ betetzen dela. Berebat, ohiko agregatu lineal batean, $c = 0.1$ izan ohi da {cite}`hill`. Hortaz, $\epsilon < 0$ dugu. 
```

Azpiko kutxak adibide honetako ondorio nagusiak laburbiltzen ditu: $(a)$ sistema erabat askean gertatzen den entropiaren handiagotzea, eta, $(b)$ Nanotermodinamikaren eta Termodinamikaren arteko bateragarritasuna.

$$
\boxed{\begin{gathered}
    (a) \quad S(T,\mu) > S(T,N) \\
    \\
   (b) \quad  \frac{S(T,\mu)}{\bar{N}k_{\mathrm{B}}}\equiv \frac{S(T,N)}{Nk_{\mathrm{B}}} = \frac{\mathrm{s}^{(0)}}{k_{\mathrm{B}}} = \ln j + T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} \quad (\bar{N},N\rightarrow\infty)
\end{gathered}}
$$


##### Ariketa

Hill-ek {cite}`hill` liburuko adibidean biraketa ez du aintzat hartzen. Hala, entropiarako gehikuntza fluktuazioekin lotzen du zuzenean, kasu horretan honakoa betetzen baita: 

$$
S-S^{(0)} \equiv S^{(x)} = -k_{\mathrm{B}}\sum_{N}P(N)\ln P(N)\;
$$ (agg_sx)

Ariketa honen helburua, egiazki, {eq}`agg_sx` ekuaziora iristea da. Biraketaren eragina baztertu egingo dugunez, {eq}`qagg` partizio-funtzio kanonikoa honela laburtuko dugu:

$$
Q(T,N) = c(T)j(T)^N\;e^{-N\epsilon/k_{\mathrm{B}}T} \quad (N\geq1)\; ,
$$ (agg_q_summ)

non $c(T) = e^{\epsilon/k_{\mathrm{B}}T}$, eta, noski, $Q(T,0) = 1$ diren. 

Horiek horrela, ariketa honetan dugun eginbeharra honako hau da: 

$(a)$ Abiapuntutzat {eq}`agg_q_summ` partizio-funtzioa erabiliz, birkalkulatu {eq}`muagg` ekuaziotik {eq}`probagg` ekuaziora bitarteko magnitudeak, alegia:

$$
\widehat{\mu}, \; \mu, \; \mu^{(0)}, \; S(T,N), \; \Upsilon(T,\mu), \; \mathscr{E}(T,\mu), \; \bar{N}, \; P(N) \; \text{eta} \; S(T,\mu) \; .
$$

Bukatzeko, lortu $S^{(0)}$ limite makroskopikoa. 

$(b)$ Egiaztatu {eq}`agg_sx` berdintza betetzen dela.


(mupt_gi)=
### Adibidea: Gas ideal klasikoa, multzo nanokanonikoan

Sistema honen bigarren berrazterketaren abiapuntua {numref}`{number} adibideko <gitpn>` {eq}`dtpn_gi` ekuazioa da.

##### Ariketa
Eraiki honako adierazpen hauek: $\Upsilon(T,p,\mu)$ partizio-funtzioa, $\mathscr{E}$ banatze-potentziala eta $S(T,p,\mu)$ entropia. Jarraian, lortu $\bar{N}$ eta $\bar{V}$ magnitudeak eta berridatzi entropiaren ekuazioa haien baitan, hau da, $S(T,\bar{V},\bar{N})$.
```{dropdown} __Erantzuna__
 $\Delta(T,p,N)$ partizio-funtzioari askatasun-gradu kimikoa abiarazteak dakarren Legendreren transformazioa erantsiz,

$$
\Upsilon(T,p,\mu) = \sum_{N=0}^{\infty} \left(\frac{k_{\mathrm{B}}T\lambda}{p\Lambda^3}\right)^{N} = \frac{1}{1 - k_{\mathrm{B}}T\lambda/(p\Lambda^3)} \; , \; \left| \frac{k_{\mathrm{B}}T\lambda}{p\Lambda^3} \right| < 1
$$ (upsilongi)
izango dugu partizio-funtzio orokortua. Bertan $\lambda = e^{\mu/k_{\mathrm{B}}T}$ ordezkatu dugu. Hortaz,

$$
\mathscr{E}(T,p,\mu) = k_{\mathrm{B}}T \ln\left(1- \frac{k_{\mathrm{B}}T\lambda}{p\Lambda^3}\right) = -k_{\mathrm{B}}T \ln(\bar{N} + 1) < 0 \; .
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
**----------------------------------------------------**

Errepara diezaiogun multzo nanokanonikoak itzulitako entropiaren {eq}`stpmugi` ekuazioari. Halaber, etor bekizkigu gogora multzo kanonikotik eta isotermo-isobarotik eskuratutako {eq}`stvngi` eta {eq}`stpngi` adierazpenak, eta ipin ditzagun hirurak parez pare ({numref}`{number} taula <taula_s_gi>` eta {numref}`{number} irudia <sn100>`). Guztietan Sackur-Tetrode adierazpen _estentsiboa_ $(S_{0})$ da gai nagusia. Baina, aurreneko bien aldean, {eq}`stpmugi` ekuazioak bigarren gai _positibo_ bat duela hauteman daiteke, eta, hori dela eta, sistema txikietan berori izango da nagusi.

```{list-table} Gas idealaren banatze-potentziala eta entropia, multzoz multzo.
:header-rows: 1
:name: taula_s_gi

* - Aldagaiak
  - Banatze-potentziala
  - Entropia
* - $\left(T, V,N\right)$
  - $\frac{\mathscr{E}}{k_{\mathrm{B}}T} \approx \ln\left(\frac{\sqrt{2\pi N}}{e}\right) + \frac{7}{12N} > 0$
  - $\frac{S}{k_\mathrm{B}} \approx N \left[\ln \left(\frac{V}{\Lambda^{3} N}\right)+\frac{5}{2}\right]-  \ln \sqrt{2 \pi N} - \frac{1}{12N}$
* - $\left(T,p,N\right)$
  - $\mathscr{E} = 0$
  - $\frac{S}{k_{\mathrm{B}}} =  N\left[\ln\left(\frac{\bar{V}}{\Lambda^3N}\right) + \frac{5}{2}\right]$
* - $\left(T,V,\mu\right)$
  - $\mathscr{E} = 0$
  - $\frac{S}{k_{\mathrm{B}}} =  \bar{N}\left[\ln\left(\frac{V}{\Lambda^3 \bar{N}}\right) + \frac{5}{2}\right]$
* - $\left(T,p,\mu\right)$
  - $\frac{\mathscr{E}}{k_{\mathrm{B}}T} = - \ln(\bar{N} + 1) < 0$
  - $\frac{S}{k_{\mathrm{B}}} = \bar{N}\left[\ln\left(\frac{\bar{V}}{\Lambda^3}\frac{\bar{N}+1}{\bar{N}^2}\right) + \frac{5}{2}\right] + \ln(\bar{N} + 1)$

```

```{figure} sn100.PNG
---
height: 350px
name: sn100
---
Kurbak Ar gasari dagozkio (1 mol). Datuak honakoak dira: $\Lambda = 16,7 \; \mathrm{pm}$ ; $T=273,15 \; \mathrm{K}$ ; $N/V = 2,687\cdot10^{25}\; \mathrm{at/m^3}$. Agerikoa da, askatasun-graduak abiarazi ahala, eskualde nanotermodinamikoan tamaina finituko efektuek entropia handitu ez ezik, $S/Nk_{\mathrm{B}}$ magnitudea estentsibo bihurrarazi dutela.

```

Gainera, {eq}`epsilontpmugi` ekuazioaren eskuinaldeak entropiarako gehikuntza hori banatze-potentzialerako ekarpen _negatibo_ eta _ez-estentsiboaren_ ondoriozkoa dela diosku, alegia,

$$
S(T,p,\mu) = S_{0}(T,p,\mu) - \mathscr{E}(T,p,\mu)/T\;.
$$ (stpmuginew)

Jarraian datorren {numref}`{number} atalean <stabeps>` $\mathscr{E}<0$ izateak multzoaren barruan aldaki-kopurua handitzea dakarrela ikusiko dugu ({numref}`{number}. irudia <gisub>`).

```{figure} gibbsparadox.PNG
---
height: 300px
name: gisub
---
Multzo nanokanonikoan __banatzearen areagotzeak bereizgarritasuna indartuko du__. Izan ere, hasiera batean bi aldakietako bakoitzean egon diren partikulak bereizezinak izan dira, hain zuzen, aldakikide izateagatik. Aitzitik, bukaeran, azpisistemen arteko bereizte-hormek bereizgarri bihurrarazi dituzte. Horren ondorioz, entropiak gora egingo du.

```

Irudia eta {eq}`stpmugi` ekuazioa kontuan hartuz, multzoaren banatzearen ondoriozko ekarpenek entropiaren aldakuntza handituko dute, honako hau beteko baita: $\Delta S = k_{\mathrm{B}}\ln(\bar{N}+1)$. Banatzeari dagokion orekan, $\bar{N} \rightarrow 0$ eta, hortik, $\Delta S_{\text{oreka}}=0$. Baina, partikulako entropia hazi egingo da: $\lim_{\bar{N} \rightarrow 0}\Delta S/\bar{N} = 1$.

Aipatu beharrekoa da gaineko {numref}`{number} irudiari <gisub>` lotutako azalpenak arras garrantzitsuak direla, multzo nanokanonikoari berebiziko esangura ematen baitiote. Esate baterako, demagun bi multzo makroskopikok gas berbera daukatela, eta tartean bereizte-horma bat ipini dugula. Horma  kenduz gero, bi multzoek bat egingo dute. Bada, Termodinamikatik abiatuz hau esango genuke: gasak bereizterik ez dagoenez, prozesuak itzulgarria beharko du izan, eta horrek $\Delta S = 0$ izatea dakar. Alabaina, izatez, bide horretatik jarraituz gero, __Gibbs-en paradoxarekin__ egingo dugu topo, entropiak egiatan aldakuntza positiboa jasango du eta. Horri aurre egiteko, partikulen bereizezintasuna inposatuko dugu, eta, badirudi Gibbs-en $1/N!$ _ad hoc_ faktoreak arazoa konpontzen duela...

Aitzitik, Termodinamikak dioenaz haratago joan, eta, Nanotermodinamikan oinarritutako arrazoinamenduari jarraituko bagenio, honakoa ondorioztatuko genuke: bi sistemak elkartzeaz bat, multzoak banatzeari ekingo dio, partikulen bereizgarritasuna areagotuz. Hori dela eta, gasak berdinak diren arren, eskualde nanotermodinamikoan beroriek era __itzulezinean__ _nahasiko_ dira, eta multzoak nahasketa hori aldakien entropiaren gorakadan islatuko du, berori maximizatuz. Horrela, multzo nanokanonikoaren banatzea handituz, sistema txikietan Gibbs-en paradoxa saihestuko dugu bidenabar {cite}`nanointro, multiscale`.

Soluzio berritzailearen atzean dautzan tamaina finituko efektuak $\mathscr{E}$ potentzialaren gidaritzapean daude. Teoriari dagokion azkenengo atala berorri eskainiko diogu osorik, banatzeari dagokion orekan duen paperean sakonduz.

##### Ariketa : Gas ideala, multzo makrokanonikoan $\left(T,V,\mu\right)$

Kalkulatu {numref}`{number} taulako <taula_s_gi>` hirugarren lerroko emaitzak.

```{dropdown} __Erantzuna__

Hasteko, partizio-funtzio makrokanonikoa

$$
\Xi (T,V,\mu) = \sum_{N=0}^{\infty}\; Q(T,V,N)\;e^{\mu N/k_{\mathrm{B}}T} = \sum_{N=0}^{\infty}\;\frac{1}{N!}\left(\frac{V\lambda}{\Lambda^3}\right)^N = e^{V\lambda/\Lambda^3} := e^{\widehat{p}V/k_{\mathrm{B}}T}
$$ (gi_xi)

da. Hortik, $\widehat{p}$ presio integrala eta $p$ presio diferentziala bat datozela ohartuko gara; izan ere,

$$
\widehat{p}V = -\frac{k_{\mathrm{B}}T  \lambda}{\Lambda^3}V
$$ (gi_widehatp_v)

adierazpena lehen ordenako funtzio Euler homogeneoa da. Horren ondorioz, $\mathscr{E} = 0$ dugu. Bestalde,

$$
\bar{N} = \left[\frac{\partial \left(\widehat{p}V\right)}{\partial \mu}\right]_{T,V} = \frac{\lambda V}{\Lambda^3} \; ,
$$ (gi_barn_makro)

eta, berori {eq}`gi_widehatp_v` ekuazioan ordezkatuz, entropia lortuko dugu:

$$
\boxed{S(T,V,\mu) = \left[\frac{\partial \left(\widehat{p}V\right)}{\partial T}\right]_{V,\mu} = \bar{N}k_{\mathrm{B}}\left[\ln\left(\frac{V}{\Lambda^3 \bar{N}}\right) + \frac{5}{2}\right]} \; .
$$ (gi_s_makro)

```

(stabeps)=
### Banatze-potentziala eta egonkortasuna

Hasteko, dakargun gogora $\mathscr{E}$ potentzialaren definizioa: multzoaren aldaki-kopuruan eragiteak berorren guztizko energiari dakarkion ekarpena, gainontzeko kasuan kasuko ingurune-aldagaiak konstante mantenduz, hau da, 

$$
\mathscr{E} := \left(\frac{\partial E_{t}}{\partial \mathscr{N}}\right)_ {S_{t},V_{t}, N_{t}} \equiv \left(\frac{\partial A_{t}}{\partial \mathscr{N}}\right)_ {T,V_{t}, N_{t}} \equiv \left(\frac{\partial F_{t}}{\partial \mathscr{N}}\right)_ {T,p, N_ {t}} \; .
$$ (epsilonnewdef)

Bestela esanda, multzo nanokanonikoaren kasuan, aldaki berri bat sorrarazteko multzoari berari egin beharreko lana da.

Horren harira, atal honetan denboran batez besteko $\bar{\mathscr{N}}$ aldaki-kopuruak jasango dituen aldakuntzen izaera espontaneoa izango dugu hizpide. Multzoko azpisistemak erabat askeak direla onartuko dugu, baina, gutxienez partikula bat izan beharko dute $(N \geq 1)$. Era berean, multzoko inguruneko aldagai-sorta $(T,p,N_{t})$ izango dugu, non $N_{t}=\bar{\mathscr{N}}\bar{N}$ den.

Bada, prozesu espontaneoan zehar orekaranzko bidean, minimorantz joko du $F_{t}(T,p,N_{t})$ energia askeak, eta, beraz, $\mathrm{d}F_{t}<0$. Prozesuak dirauela multzoa isolatuta mantentzen bada, $\bar{\mathscr{N}}$ ez beste aldagai guztiek bere horretan iraungo dute. Hori dela eta, {eq}`epsilonnewdef` ekuazioaren eskuinaldetik,

$$
\mathrm{d}F_{t}=\mathscr{E}\mathrm{d}\bar{\mathscr{N}}<0\; .
$$ (dft)

Adierazpen horrek honakoa iradokitzen du: banatze-potentziala positiboa denean, aldaki-kopuruak behera egingo du, eta, negatiboa denean, aldiz, multzoaren banatzea areagotuko da, aldaki txikiagoak sorraraziz (oroitu gaitezen {numref}`{number} irudiaz <gisub>`). Era berean, orekara heldutakoan, energia minimoan egongo denez,

$$
\left(\frac{\partial^2 F_{t}}{\partial \bar{\mathscr{N}}^2}\right)_{T,p, N_{t}} = \left(\frac{\partial \mathscr{E}}{\partial \bar{\mathscr{N}}}\right)_{T,p, N_{t}} > 0 \; .
$$ (d2f)

Bertatik agerikoa da $\mathrm{d}\mathscr{E}$ eta $\mathrm{d}\bar{\mathscr{N}}$ zeinu berekoak direla. Horrez gain, {eq}`dft`  ekuazioa aintzat hartuz, $\mathscr{E}\cdot\mathrm{d}\mathscr{E}<0$ beteko da. Ondorio esanahitsu hori {numref}`{number} adibidean <mupt_gi>` jorratutako azalpenak osatzeko lagungarria izango zaigu: $\mathscr{E}$ eta $\mathrm{d}\mathscr{E}$ aurkako zeinudunak direnez, $\bar{\mathscr{N}}$ aldatuz doan neurrian, $\mathscr{E}$ potentzialak zerorantz joko du, harik eta orekara heldu arte. __Banatzeari dagokion oreka-egoera__ batek $\mathscr{E} = 0$ baldintza bete beharko du.

Esaldi hori dela eta, azken kontu bat argitu beharrean gaude. Berorri heltzeko, gas idealaren adibidea berreskuratuko dugu. Ezer baino lehen, kontuan izan dezagun multzoko sistema txikiei $N\geq1$ baldintza ezarri diegula. Hortaz, {eq}`upsilongi`  ekuaziotik $N=0$ gaia erauzi beharko dugu. Bada, $x=k_{\mathrm{B}}T\lambda/(p\Lambda^3)$ ordezkatuz,

$$
 \Upsilon = \frac{x}{1-x}
$$ (upsilonginew)
izango da partizio-funtzio eraldatua. Bertatik $\mathscr{E}$ eta $\bar{N}$ magnitudeak birkalkulatuko ditugu:

$$
\mathscr{E} = -k_{\mathrm{B}}T\ln\left(\frac{x}{1-x}\right) = -k_{\mathrm{B}}T\ln\left(\bar{N}-1\right) \; ,
$$ (epsginew)

$$
 \bar{N} = \frac{1}{1-x} = 1 + e^{-\mathscr{E}/k_{\mathrm{B}}T} \; .
$$ (barnginew)


Demagun orain $\bar{\mathscr{N}}$ azpisistema-kopuruari eragingo dion prozesu espontaneoa abian jartzen dugula, $T$ eta $p$ konstante mantenduz. Banatzeak dirauela $(\mathrm{d}\bar{\mathscr{N}}<0$ edo $\mathrm{d}\bar{\mathscr{N}}>0)$, entropiak $\Delta S=\pm k_{\mathrm{B}}\ln(\bar{N}/2)$ aldakuntza jasango duela frogatu daiteke.  Orekara ailegatutakoan,

$$
\mathscr{E}_ {\text{oreka}} = 0 \quad \Rightarrow \quad \bar{N}_ {\text{oreka}}=2 \quad \text{eta} \quad \Delta S_{\text{oreka}}=0 \; .
$$

Gogora dezagun lehen, partizio-funtzioan $N=0$ gaia sartzeagatik, $\bar{N}\rightarrow 0$ baldintzak ginderamatzala orekara, zeinak banatzea etengabekoa dela iradoki bailezake. Horren aldean, orain lorturiko emaitzek esangura eta zentzu fisiko handiagoa dute.


Amaitzeko, argitzeko geratu den alderdiari helduko diogu. Aurreko zenbait ataletan esan bezala, limite makroskopikoan $\bar{N}$ aldagaiarekin erlazio lineala betetzen duten ekarpenak biziki gailenduko dira banatze-potentzialarekiko, eta, beraz, $\mathscr{E}$ baztergarri bilakatuko da. Bada, azken esaldi hori iruzurtia gerta lekiguke, arrazoibide okerretik eraman gintzake eta, honakoa pentsaraziz: sistema makroskopikoak $\mathscr{E}\approx 0$ hautemango duenez, _limite makroskopikoa bera oreka-egoeratzat hartzea daukagu_.

Izan ere, horren aurrean erne ibili behar dugu! Esate baterako, gas idealaren kasuan, {eq}`epsginew` ekuazioak $\bar{N}\rightarrow \infty$ limitean

$$
\mathscr{E} = -k_{\mathrm{B}}T\ln \bar{N}
$$ (epslimgi)
adierazpenari segituko dio, eta, ondorioz, moduluz gora egingo du, astiro bada ere. Egia da, bai, beste zenbait kasutan ({numref}`{number} <helix_coil>` zein {numref}`{number}. <app>` ataletako sistemetan, adibidez) eskuratzen diren adierazpenek $\mathscr{E}\rightarrow 0$ betetzen dutela limite makroskopikoan, baina {eq}`epslimgi` ekuazioak argiro diosku oro har ez dela hala gertatuko! Gainera, nabarmendu beharrekoa da banatze-potentzialaren zeroranzko limite horren esanahia ez datorrela bat orekak zorrozki eskatzen duen $\mathscr{E}=0$ baldintzarekin. Hortaz, eskuarki, ez zaigu zilegi izango egoera makroskopikoa oreka-egoera baten baliokidea dela iradokitzea.


Iruzkin argigarri horiekin itxiko dugu Sistema Txikien Termodinamikari dagokion teoriaren zatia. Lanaren azkenengo atalean 1960. hamarkadatik 2021era jauzi egin, eta dagoeneko luzaz jorratu dugun teoriaren aplikazio garrantzitsu batean murgilduko gara.
