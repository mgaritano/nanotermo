(tpn)=
## Multzo isotermo-isobaroa: $(T,p,N)$ ingurune-aldagaiak

Kapitulu honen fisikari heldu baino lehen, honako honi erreparatu behar diogu: {numref}`{number}. atalean <tpmu>` ikusiko dugunez, multzo nanokanonikorako $(T,p,\mu)$ trantsizioa $Q(T,V,N)$ partizio-funtzio kanonikotik abiatzen dugu normalean, Legendreren transformazioen laguntzaz. Kontua da tarteko multzotzat makrokanonikoa $(T,V,\mu)$ hautatuz gero, zenbaitetan bidea malkartsua gertatuko zaigula. Bada, bolumenean barreneko integrala barik $N$ partikula-kopuruan zeharreko batukaria kalkulatzeak lana arinduko digu.
Hala, ibilbide hori multzo isotermo-isobaroan $(T,p,N)$ barrena burutzea mesedegarria izango zaigu oso. Bestetik, ingurune-aldagai horien bidez $T$ eta $p$ finkatzen dituen ingurune batean makromolekula edo koloide konprimaezin eta hedagarria ezaugarritu daiteke. Ildo horretatik, {numref}`{number}. azpiatalean <helix_coil>` lan honetako lehenbiziko adibide garrantzitsuari helduko diogu, hurbilketa bereziekin bada ere.

Horiek horrela, multzo estatistiko honi azterketa sakonagoa eskaintzea merezi du.

(tpn_azter)=
### Multzoaren azterketa

Kontrol-aldagaitzat $(T,p,N)$ dituzten sistema txikiek $\bar{E}=E_{t}/\mathscr{N}$, $\bar{V}=V_{t}/\mathscr{N}$ eta $N=N_{t}/\mathscr{N}$ aldagai estentsiboak izango dituzte.

##### Ariketa

Aurreko esaldian aipatutakoa aintzat hartuz, eta {numref}`{number}. ataleko <hillsec>` azalpenei segituz, eraiki honako adierazpenak:

$(a)$ Multzo isotermo-isobaroaren Gibbs-en ekuazioa eta $X(T,p,N)$ aldaki-energia. Emaitzak azaldu.

```{dropdown} __Erantzuna__
$$
\mathrm{d}E_{t}(S_{t},V_{t},N,\mathscr{N}) = T\mathrm{d}S_{t} - p\mathrm{d}V_{t} + \mu \mathscr{N}\mathrm{d}N + (\mathscr{E}+\mu N)\mathrm{d}\mathscr{N}
$$ (dEttpn)
$$
X(T,p,N) = \mathscr{E} + \mu N := \left(\frac{\partial E_{t}}{\partial \mathscr{N}}\right)_{S_{t},V_{t},N} := \widehat{\mu}N \; .
$$ (xtpn)
```

```{dropdown} __Azalpenak__
Kasu honetan, $N$ ingurune-aldagaia agerrarazi behar dugu ekuazioan, $\mathrm{d}N_{t} = \mathscr{N}\mathrm{d}N + N\mathrm{d}\mathscr{N}$ erabiliz. Berorrek $N_{t}$ magnitudeak aldaezin irautea galarazten du. Aldaki-energia multzo honen izaeraren isla da. Hala, aldaki bat txertatzean, guztizko bolumena zein energia birbanatu egingo dira, sistema txikiei aldagaiok askatasun osoz eraldatu baitiezazkiekegu. Aitzitik, $N$ partikula-kopuruak aldaezin iraun behar duenez sistema orotan, multzoaren barne-energiak ekarpen kimikoa ere jasango luke, bere ikuspuntutik kanpotik $N$ partikuladun sorta berri bat gehitzen arituko gintzaizkioke eta. Aipaturiko ekarpen kimikoa $\widehat{\mu}$ potentzialaren bidez ereduztatu behar dugu, ez baitauka azpisistemei esleitutako $\mu$ potentzialaren esanahi bera.
```

$(b)$ Sistema txikien Gibbs-en ekuazioa eta barne-energiaren adierazpena.
```{dropdown} __Erantzuna__
$$
\mathrm{d}\bar{E} = T\mathrm{d}S - p\mathrm{d}\bar{V} + \mu \mathrm{d}N
$$ (detpn)
$$
\bar{E} = TS - p\bar{V} + \widehat{\mu}N
$$ (etpn)
```
$(c)$ Gibbs-en energia askea ($F(T,p,N)$). Hortik abiatuta, idatzi magnitude integrala eta diferentziala erlazionatzen dituen adierazpena.

```{dropdown} __Erantzuna__
$$
F(T,p,N) := \bar{E} - TS + p\bar{V} = \widehat{\mu}N
$$ (ftpn)
$$
\mathrm{d}F(T,p,N) = -S\mathrm{d}T + \bar{V}\mathrm{d}p + \mu\mathrm{d}N \;
$$ (dftpn)
$$
\boxed {\mu := \left[\frac{\partial(\widehat{\mu}N)}{\partial N}\right]_{T, p} = \widehat{\mu} + N\left(\frac{\partial \widehat{\mu}}{\partial N}\right)_{T,p} \quad ; \quad \mathscr{E} =  (\widehat{\mu} - \mu)N}
$$ (mumuhat)
```

**----------------------------------------------------**


Gaineko {eq}`ftpn` ekuazioan sistema txikiaren Gibbs-en energia askearen eta __potentzial kimiko integralaren__ arteko erlazioa agertzen da: $F := \widehat{\mu}N$. Azken horrek, $\mu$ __potentzial kimiko diferentzialarekin__ batera, banatze-potentziala finkatzen du. Ildo horri segituz, $\widehat{\mu}$ potentzialak ekuazio hau beteko du:

$$
\boxed{\mathrm{d}\widehat{\mu} = -\frac{S}{N}\mathrm{d}T + \frac{\bar{V}}{N}\mathrm{d}p - \frac{\mathscr{E}}{N^2}\mathrm{d}N}
$$ (dmuhat)

Interesgarria litzateke $\mathrm{d}\mu$ potentzialari ere tankerako adierazpen bat esleitzea. Horretarako, Maxwell-en erlazioak lortu behar ditugu, deribatuen trukatze-propietateak erabiliz, adibidez,

$$
\left(\frac{\partial \mu}{\partial T}\right)_{p, N} := \frac{\partial}{\partial T}\left(\frac{\partial F}{\partial N}\right)_{T, p} =  \frac{\partial}{\partial N}\left(\frac{\partial F}{\partial T}\right)_{p, N} := -\left(\frac{\partial S}{\partial N}\right)_{T, p}  \; .
$$

Horrenbestez,

$$
\boxed{\mathrm{d}\mu = -\left(\frac{\partial S}{\partial N}\right)_{T,p}\mathrm{d}T + \left(\frac{\partial \bar{V}}{\partial N}\right)_{T,p}\mathrm{d}p - \frac{1}{N}\left(\frac{\partial \mathscr{E}}{\partial N}\right)_{T,p}\mathrm{d}N} \; .
$$ (dmu)

Ikus daitekeen legez, {eq}`dmuhat` eta {eq}`dmu` ekuazioek bi potentzial kimikoen izaera integrala eta diferentziala azaleratu dituzte, hurrenez hurren. Berebat, aldagai estentsiboek $N$ aldagaiarekiko azaltzen duten ez-linealtasunaren erakusle dira. Halaber, {eq}`dmu` ekuazioko azkenengo gaia $\left(\partial \mu/\partial N\right)_{T,p}\mathrm{d}N$ dugu, zeina ez baita nulua. Horrek $\mu$ potentzial kimikoak orokorki jokaera ez-intentsiboa duela diosku, hau da, $\mu = \mu(T,p,N)$ erlazioari darraikiola. Eskualde makroskopikoan bi adierazpenok bat etorriko dira, hain zuzen, {eq}`gibbs-duhem` erlazioarekin (Gibbs-Duhem).

Jarraian datorkigun adibidean $\widehat{\mu}$ eta $\mu$ potentzial-bikotea kalkulatu, eta kasu zehatz horretan beroriek bereizten dituzten ekarpen finituen itxura behatuko dugu.

(helix_coil)=
### Adibidea: helize-haril trantsizioa

Esku artean dugun sistema {numref}`{number}. irudiko <heco>` irudiko dimentsio bakarreko soka da. Berori, hurrenez hurren, $l_{H}$ eta $l_{C}$ luzerako $n_{H}$ helize- eta $n_{C} = N - n_{H}$ haril-unitatez osatuta dago. Bestalde, bero-iturri batekin ukipen termikoan dagoela onartuko dugu, eta $N$ aldaezin mantenduko dela. Azterketa termodinamikoa $(T,f,N)$ aldagai-sortaren bitartez gauzatuko dugu, $f$ indarraren konjokatu estentsiboa $\bar{l}$, katearen batez besteko luzera, hartuta.

```{figure} helix-coil.PNG
---
height: 200px
name: heco
---
  “Helize-haril” kateak helize-unitateak ($H$) eta haril-unitateak ($C$) dauzka. Mutur banatan $f$  indarra eragingo diogu. Guztizko unitate-kopuruari dagokionez, $N\rightarrow \infty$ hurbilketa asintotikora jotzen ez badugu, katean sistema txikien berezitasunak azaleratuko dira. Oroz gain, beroriek makroskopikoki intentsiboak diren aldagaiei nabarmenki erasango diete.
```

Demagun orain haril-unitateak ($C$) soilik muturretan koka daitezkeela. Irudiko kasuan, hortaz, aukera hauek genituzke eskura: $C\;H\;H\;H\;C$ ; $C\;C\;H\;H\;H$ ; $H\;H\;H\;C\;C$. Orokortuz, baldintza horrek sistemari $g(n_{H}) = N-n_{H}+1$ endekapena sorraraziko lioke. Jakina, $H$-unitaterik ez balego, $g=1$ izango genuke, sistemak bakarrik $C$-unitateak edukiko lituzke eta. $C$- eta $H$-unitateen partizio-funtzio kanonikoak $q_{H}(T)$ eta $q_{C}(T)$ izendatuko ditugu. Beraz, kate osora zabalduz, $Q(T,l,N)=q_{C}^{n_{C}}q_{H}^{n_{H}}$ genuke. Horiek horrela, $\Delta(T,f,N)$ partizio-funtzioa eraikiko dugu:

$$
\Delta := \sum_{l} Q(T,l,N)e^{fl/k_{\mathrm{B}}T}
     = \sum_{n_{H}=0}^{N} g(n_{H})q_{C}^{N-n_{H}}q_{H}^{n_{H}}e^{\left[\left(N-n_{H}\right)l_{C} + n_{H}l_{H}\right]f/k_{\mathrm{B}}T} \; .
$$ (d)

Batukariaren kalkulua saihesteko, eta, batez ere, bertatik eratortzen diren magnitudeen adierazpenak laburbiltzeko, hurbilketa nahiko gordina erabiliko dugu: unitate guztiak soilik $H$ egoeran edo soilik $C$ egoeran egon daitezke. Irudiko adibidean, esaterako, $H\;H\;H\;H\;H$ eta $C\;C\;C\;C\;C$ sortak izan ahalko genituzke. Horrela, bada, batukaritik $n_{H}=0$ eta $n_{H}=N$ gaiak erauziz, eta gai bakoitzaren endekapena aintzakotzat hartuz, hona iritsiko gara:

$$
\Delta = q_{C}^Ne^{Nl_{C}f/k_{\mathrm{B}}T} + q_{H}^Ne^{Nl_{H}f/k_{\mathrm{B}}T} = r_{C}^N(1 + r^N)\; .
$$ (d_short)

Ekuazioa $r_{C,H}(T,f) = q_{C,H}(T)\exp(fl_{C,H}/k_{\mathrm{B}}T)$ eta $r=r_{H}/r_{C}$ txertatuz trinkotu dugu. Aipatzekoa da {eq}`d_short` partizio-funtzioak adierazten duen eredu sinplifikatua ez-errealista izanagatik, adibide didaktiko honen xedeari ez diola eragingo.

Ezer baino lehen, azter dezagun partizio-funtzioaren $N\rightarrow \infty$ limitea:

$$
\Delta(T,f,N) =
    \begin{cases}
      r_{C}^N & \text{$r<1$ bada.}\Rightarrow N = n_{C} \\
      r_{H}^N & \text{$r>1$ bada.}\Rightarrow N = n_{H}
    \end{cases}  
$$

Hortik agerikoa da $r=1$ denean, katean bat-bateko helize-haril **fase-trantsizioa** gertatuko dela (limite termodinamikoan).

Hurrengo pausoa, {eq}`d_short` ekuaziotik abiatuz, sistemaren termodinamika ondorioztatzea da. Gibbs-en energia askea $F(T,f,N) := -k_{\mathrm{B}}T\ln\Delta$ dugu.

##### Ariketa

$(a)$ Kalkulatu $\widehat{\mu}$ eta $\mu$ potentzial kimikoak, $F(T,f,N)$ adierazpenaren laguntzaz.

```{dropdown} __Erantzuna__
$$
\widehat{\mu} := \frac{F}{N} = -k_{\mathrm{B}}T\left[\ln r_{C} + \frac{1}{N}\ln(1+r^N)\right]
$$ (muhathelix)
$$
\mu := \left(\frac{\partial F}{\partial N}\right)_{T,f} = -k_{\mathrm{B}}T\left[\ln r_{C} + \frac{r^N\ln r}{1 + r^N}\right]
$$ (muhelix)
```

$(b)$ Eraiki banatze-potentziala, eta aztertu sistemaren tamainaren arabera azaltzen duen portaera, $r = 0,5 \; ;  \; r = 0,98$ eta $r=1,05$ balioak erabiliz.

```{dropdown} __Erantzuna__
$$
\mathscr{E} = (\widehat{\mu}-\mu)N = -k_{\mathrm{B}}T\left[\ln(1+r^N) - N\frac{r^N\ln r}{1 + r^N}\right]
$$ (epsilonhelix)

```{figure} epsilon_tfn.PNG
---
height: 300px
name: epsilon_tfn
---
  Ekarpen finituen bilakaera banatze-potentzialaren indarraren baitan dago. Tamaina handitu ahala, berori ahulduz doa, eta sistemak eremu makroskopikorantz jotzen du. Era berean, $r$ erlazioak eskualde nanotermodinamikoaren hedaduran eragin zuzena dauka. Fase-trantsizioaren puntura gerturatu ahala ($r\rightarrow1$) geroz eta tarte zabalagoa hartuko du, eta $\mathscr{E}\rightarrow\mathscr{E}_{0} = -k_{\mathrm{B}}T \ln 2$ konstanterantz gerturatuko da.
```

**----------------------------------------------------**

Hari bertsutik, adibide honen esangura handieneko alderdiari helduko diogu, kateak $r$ erlazioarekin duen bilakaera helize-unitateen batez besteko frakzioaren bidez ereduztatuz ($\bar{n} _ {H}/N $). Orain arte ez bezala, aurrerantzean $n_{H}$ kopuruari marratxoa erantsiko diogu, berorrek zehaztuko baitu, hain zuzen, katearen batez besteko luzera: $\bar{l}(\bar{n} _ {H}) = (N-\bar{n} _ {H})l_{C} + \bar{n} _ {H}l_{H}$. Bada, horretarako, $\bar{n} _ {H}$ itxarotako balioa eskuratu behar dugu, sistemaren partizio-funtziotik abiatuz:

$$
\bar{n}_{H} := \frac{\sum _ {n _{H}} n _{H}Q(T,l(n _ {H}), N)e^{fl(n _{H})/k _{\mathrm{B}}T}}{\sum _ {n _{H}} Q(T,l(n _ {H}), N)e^{fl(n _{H})/k _{\mathrm{B}}T}} \equiv \frac{\sum _ {n _{H}} n _{H}Q(T,l(n _ {H}), N)e^{fl(n _{H})/k _{\mathrm{B}}T}}{\Delta(T,f,N)}
$$ (nhdef)

Gauzak horrela, hasteko {eq}`d` ekuazioko batukaritik $n_{H}=0$ gaia atera, eta $\Delta$ honela berridatziko dugu:

$$
    \Delta = r_{C}^N\left[1+\sum_{n_{H}=1}^{N}\left(N-n_{H}+1\right)r^{n_{H}}\right]\; .
$$ (dnew)

Hala, {eq}`nhdef` definizioari jarraituz,

$$
\bar{n}_{H} := \frac{r_{C}^N\left[0+\sum_{n_{H}=1}^{N}n_{H}\left(N-n_{H}+1\right)r^{n_{H}}\right]}{\Delta} = r\frac{\partial}{\partial r}\ln \Delta \; .
$$ (nbar)

`````{admonition} Iradokizuna
:class: tip
Nahi izanez gero, egiaztatu aurreko ekuazioaren bi aldeak bat datozela.
`````

Bada, {eq}`nbar` ekuazioan {eq}`d_short` adierazpena ordezkatuz gero, azkenean ere! iritsiko gara helmugara:

$$
\boxed{\frac{\bar{n} _ {H}}{N} = \frac{r}{N}\frac{\partial}{\partial r}\ln\left[r_{C}^N(1 + r^N)\right] = \frac{r^N}{1+r^N}}\; .
$$(fraction_N)


Errepara diezaiogun orain ekuazio horren adierazpen grafikoari:

```{figure} hc_phase.PNG
---
height: 300px
name: hc_phase
---
  Helize-unitateen batez besteko frakzioaren kurbek eite bitxia eta susmagarria dute. Izan ere, badirudi intentsibotasuna ez dela dirudien bezain kontzeptu tinkoa.
```

Lortutako emaitzak direla eta, berehalako geldialdia egin beharrean gaude, ezinbestean.

Hurrera gakizkion, **arreta handiz**, {numref}`{number}. irudiko <hc_phase>` kurba-sortari. Izatez, Termodinamikaren ikuspuntutik, batez besteko frakzioak izaera INTENTSIBOA beharko luke izan, zero ordenako funtzio Euler-homogeneo orok bezalaxe. Baina $N$ aldatu ahala, $\bar{n}_{H}/N$ kurbaren formak ez dirau bere horretan!! Horrek, argi eta garbi, aztergai dugun magnitudeak tamainarekiko menpekotasuna duela iradokitzen du, hots, ESTENTSIBOA dela. Preseski, sistema txikia denean ($N=2$), tamaina laukoiztean, helize-unitateen frakzioak aldaketa bortitza pairatu du, ez ordea $N=40$tik $N=200$erakoa bezain gogorra. Berezitasun horiek {numref}`{number}. irudiak <epsilon_tfn>` islatzen duen banatze-potentzialaren bilakaeraren ondorio dira.

Ondorioz, $N=200$ inguruan $\bar{n}_{H}/N$ren jokaera intentsiboa berrezarri dela esan liteke, arestian aipatutako bat-bateko helize-haril fase-trantsizioa igarri dakioke eta. Nolanahi ere, sailkapen zorrotzari atxikiz, soilik $N\rightarrow \infty$ limiteak deuseztatuko ditu erabat tamaina finituko efektuak, maila makroskopikora jauzi egitea ahalbidetuz. Osterantzean, helize-haril katea sistema txikia da.

Fase-trantsizioen gaian murgildutakoan ({numref}`{number}. atalean <fase>`) izango dugu {numref}`{number}. irudira <hc_phase>` bihurtzeko beta egokia.

(gitpn)=
### Adibidea: Gas ideal klasikoa, multzo isotermo-isobaroan

Bigarren sistemaren azterketa [___C___](gitvn) ___eranskineko___ emaitzetatik abiatuko dugu. Hasteko, askatasun-gradu mekanikoa abiarazi, eta multzo kanonikotik isotermo-isobarora igaroko gara. Partizio-funtzio berria eraikitzerakoan, {eq}`qtvngi` ekuazioko zaharrari dagokion Legendreren transformazioa aplikatuko diogu.

$$
\Delta(T,p,N) := \int_{0}^{\infty}\mathrm{d}\left(\frac{pV}{k_{\mathrm{B}}T}\right)\left[\frac{V^N}{N!\Lambda^{3N}}\right]\;e^{-pV/k_{\mathrm{B}}T} = \left(\frac{k_{\mathrm{B}}T}{p\Lambda^3}\right)^N \; .
$$ (dtpn_gi)

```{admonition} Oharra
 $$
 \int_{0}^{\infty}\mathrm{d}x \; x^n e^{-ax} = \Gamma(n+1)a^{-n-1}
 $$
```

Aipatzekoa da jada ez dela $N!$ agertzen. Are gehiago, Gibbs-en energia askea idatziz gero,

$$
F(T,p,N) = Nk_{\mathrm{B}}T\ln\left(\frac{p\Lambda^3}{k_{\mathrm{B}}T}\right) \; ,
$$ (ftpngi)

berorrek uneoro jokaera makroskopikoa erakusten duela ohartuko gara, lehen mailako funtzio Euler-homogeneoa da eta, hots, lineala. Ondorioz, $\widehat{\mu}=\mu$, eta, beraz, $\mathscr{E}=0$. Aipatzekoa da multzo kanonikoan $\mathscr{E}>0$ lortu dugula (ikus {eq}`epsilon_tvn` ekuazioa).

Beha dezagun arestiko emaitzok entropian zer-nolako eragina duten:

$$
\boxed{ S(T,p,N) := -\left(\frac{\partial F}{\partial T}\right)_{p,N}=Nk_{\mathrm{B}}\left[\ln\left(\frac{\bar{V}}{\Lambda^3N}\right) + \frac{5}{2}\right]} \; .
$$ (stpngi)

Berori {eq}`stvngi` ekuazioarekin alderatuz (eta $Nk_{\mathrm{B}}T/p = \bar{V}=V$ onartuz), azken gai negatiboak ageri ez direla ohartuko gara, Sackur-Tetrode adierazpena berreskuratu baitugu; alegia, multzo kanonikoaren aldean, askatasun-gradu bat abiarazteak banatze-potentziala desagerrarazi, eta, horrekin batera, entropia handitu egin du!

Aurrerago, {numref}`{number}. atalean <tpmu>`, gas ideala azpisistema erabat askez osaturiko multzo nanokanonikoan berraztertuko dugu. Bertan azalduko diren efektu berriek berebiziko adierazgarritasuna emango diote Nanotermodinamikari.
