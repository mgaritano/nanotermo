(tpn)=
## Multzo isotermo-isobaroa: $(T,p,N)$ ingurune-aldagaiak

Kapitulu honen fisikari heldu baino lehen, honako honi erreparatu behar diogu: {numref}`{number}. atalean <tpmu>` ikusiko dugunez, multzo nanokanonikorako $(T,p,\mu)$ trantsizioa $Q(T,V,N)$ partizio-funtzio kanonikotik abiatzen dugu normalean, Legendreren transformazioen laguntzaz. Kontua da tarteko multzotzat makrokanonikoa $(T,V,\mu)$ hautatuz gero, zenbaitetan bidea malkartsua gertatuko zaigula. Bada, bolumenean barreneko integrala barik $N$ partikula-kopuruan zeharreko batukaria kalkulatzeak lana arinduko digu.
Hala, ibilbide hori multzo isotermo-isobaroan $(T,p,N)$ barrena burutzea mesedegarria izango zaigu oso. Bestetik, ingurune-aldagai horien bidez $T$ eta $p$ finkatzen dituen ingurune batean makromolekula edo koloide konprimaezin eta hedagarria ezaugarritu daiteke. Ildo horretatik, {numref}`{number}. azpiatalean <helix_coil>` lan honetako lehenbiziko adibide garrantzitsuari helduko diogu, hurbilketa bereziekin bada ere.

Horiek horrela, multzo honetara arreta bideratzea merezi du.

(tpn_azter)=
### Multzo estatistikoaren azterketa

Kontrol-aldagaitzat $(T,p,N)$ dituzten sistema txikiek $\overline{E}=E_{t}/\mathscr{N}$, $\overline{V}=V_{t}/\mathscr{N}$ eta $N=N_{t}/\mathscr{N}$ aldagai estentsiboak izango dituzte.

##### Ariketa

Aurreko esaldian aipatutakoa aintzat hartuz, eta {numref}`{number}. ataleko <hillsec>` azalpenei segituz, eraiki honako adierazpenak:

$(a)$ Hill-Gibbsen ekuazioa multzo isotermo-isobaroan, eta $X(T,p,N)$ aldaki-energia. Emaitzak azaldu.

```{dropdown} __Erantzuna__
$$
\mathrm{d}E_{t}(S_{t},V_{t},N,\mathscr{N}) = T\mathrm{d}S_{t} - p\mathrm{d}V_{t} + \mu \mathscr{N}\mathrm{d}N + (\mathscr{E}+\mu N)\mathrm{d}\mathscr{N}
$$ (dEttpn)
$$
X(T,p,N) = \mathscr{E} + \mu N := \left(\frac{\partial E_{t}}{\partial \mathscr{N}}\right)_{S_{t},V_{t},N} := \widehat{\mu}N \; .
$$ (xtpn)
```

```{dropdown} __Azalpenak__
Kasu honetan, $N$ ingurune-aldagaia agerrarazi behar dugu ekuazioan, $\mathrm{d}N_{t} = \mathscr{N}\mathrm{d}N + N\mathrm{d}\mathscr{N}$ erabiliz, zeinak, agerikoa den legez, $N_{t}$ magnitudeak aldaezin irautea eragotziko duen. Era berean, aldaki-energia multzo honen izaeraren isla da. Hala, aldaki bat txertatzean, guztizko bolumena zein energia birbanatu egingo dira, sistema txikiei aldagaiok askatasun osoz eraldatu baitiezazkiekegu. Aitzitik, $N$ partikula-kopuruak aldaezin iraun behar duenez sistema guztietan, multzoaren barne-energiak ekarpen kimikoa ere jasango luke, bere ikuspuntutik kanpotik $N$ partikuladun sorta berri bat gehitzen arituko gintzaizkioke eta. Aipaturiko ekarpen kimikoa multzoaren mailako $\widehat{\mu}$ potentziala txertatuz ereduztatu beharrean gaude; izan ere, hark ez du aurkeztuko azpisistemei esleitutako $\mu$ potentzialaren jokamoldea, tamaina finituko efektuen ondoriozko bereizketa tarteko.
```

$(b)$ Sistema txikien Gibbsen ekuazioa eta barne-energiaren adierazpena.
```{dropdown} __Erantzuna__
$$
\mathrm{d}\overline{E} = T\mathrm{d}S - p\mathrm{d}\overline{V} + \mu \mathrm{d}N
$$ (detpn)
$$
\overline{E} = TS - p\overline{V} + \widehat{\mu}N
$$ (etpn)
```
$(c)$ Gibbsen energia askea, $F(T,p,N)$. Hortik abiatuta, idatzi magnitude integrala eta diferentziala erlazionatzen dituen adierazpena.

```{dropdown} __Erantzuna__
$$
F(T,p,N) := \overline{E} - TS + p\overline{V} = \widehat{\mu}N
$$ (ftpn)
$$
\mathrm{d}F(T,p,N) = \mathrm{d}(\widehat{\mu}N) = -S\mathrm{d}T + \overline{V}\mathrm{d}p + \mu\mathrm{d}N \;
$$ (dftpn)
$$
\boxed {\mu := \left[\frac{\partial(\widehat{\mu}N)}{\partial N}\right]_{T, p} = \widehat{\mu} + N\left(\frac{\partial \widehat{\mu}}{\partial N}\right)_{T,p}}
$$ (mumuhat)
```

**----------------------------------------------------**


Gaineko {eq}`ftpn` ekuazioan sistema txikiaren Gibbsen energia askearen eta __potentzial kimiko integralaren__ arteko erlazioa agertzen da: $F := \widehat{\mu}N$. Azken horrek, $\mu$ __potentzial kimiko diferentzialarekin__ batera, banatze-potentziala finkatzen du: $\mathscr{E} =  (\widehat{\mu} - \mu)N$ ({eq}`xtpn` ekuazioa). Bada, horren bidez $\mathrm{d}\widehat{\mu}$ potentzialaren espresioa idatziko dugu:

$$
\boxed{\mathrm{d}\widehat{\mu} = -\frac{S}{N}\mathrm{d}T + \frac{\overline{V}}{N}\mathrm{d}p - \frac{\mathscr{E}}{N^2}\mathrm{d}N}
$$ (dmuhat)

Ildo horri segituz, interesgarria litzateke $\mathrm{d}\mu$ potentzialari ere tankerako adierazpen bat esleitzea. Horretarako, Maxwellen erlazioak lortu behar ditugu, deribatuen trukatze-propietateak erabiliz:

$$
\left(\frac{\partial \mu}{\partial T}\right)_{p, N} := \frac{\partial}{\partial T}\left(\frac{\partial F}{\partial N}\right)_{T, p} =  \frac{\partial}{\partial N}\left(\frac{\partial F}{\partial T}\right)_{p, N} := -\left(\frac{\partial S}{\partial N}\right)_{T, p}  \; ,
$$ (dmuhatdT)

$$
\left(\frac{\partial \mu}{\partial p}\right)_{T, N} := \frac{\partial}{\partial p}\left(\frac{\partial F}{\partial N}\right)_{T, p} =  \frac{\partial}{\partial N}\left(\frac{\partial F}{\partial p}\right)_{T, N} := \left(\frac{\partial \overline{V}}{\partial N}\right)_{T, p} \; .
$$ (dmuhatdp)

Horiekin batera, banatze-potentzialaren adierazpena eta {eq}`dmuhat` ekuazioko azkeneko gaia baliatuko ditugu

$$
\left(\frac{\partial \mu}{\partial N}\right)_{T, p} = \left(\frac{\partial \widehat{\mu}}{\partial N}\right)_{T, p} - \left[\frac{\partial (\mathscr{E}/N)}{\partial N}\right]_{T,p} = - \frac{1}{N}\left(\frac{\partial \mathscr{E}}{\partial N}\right)_{T,p} 
$$

berdintza erdiesteko. Horrenbestez,

$$
\boxed{\mathrm{d}\mu = -\left(\frac{\partial S}{\partial N}\right)_{T,p}\mathrm{d}T + \left(\frac{\partial \overline{V}}{\partial N}\right)_{T,p}\mathrm{d}p - \frac{1}{N}\left(\frac{\partial \mathscr{E}}{\partial N}\right)_{T,p}\mathrm{d}N} \; .
$$ (dmu)

Ikus daitekeen legez, {eq}`dmuhat` eta {eq}`dmu` ekuazioek bi potentzial kimikoen izaera integrala eta diferentziala azaleratu dituzte, hurrenez hurren. Berebat, aldagai estentsiboek $N$ aldagaiarekiko azaltzen duten ez-linealtasunaren erakusle dira. Halaber, {eq}`dmu` ekuazioko azkenengo gaia $\left(\partial \mu/\partial N\right)_{T,p}\mathrm{d}N$ dugu, zeina ez baita nulua. Horrek $\mu$ potentzial kimikoak orokorki jokaera ez-intentsiboa duela diosku, hau da, $\mu = \mu(T,p,N)$ erlazioari darraikiola. Eskualde makroskopikoan bi adierazpenok bat etorriko dira, hain zuzen, {eq}`gibbs-duhem` erlazioarekin (Gibbs-Duhem). Era berean, {eq}`dftpn` ekuazioaren laguntzaz, Hill-Gibbs-Duhem erlazioa lortzea daukagu:

$$
\mathrm{d}\left[\left(\widehat{\mu}-\mu\right)N\right] = \mathrm{d}\mathscr{E} = -S\mathrm{d}T+\overline{V}\mathrm{d}p-N\mathrm{d}\mu \; .
$$ (depsilontpn)

Hala eta guztiz ere, egokiagoa generitzoke kontrolpean ditugun $(T,p,N)$ ingurune-aldagaiek gaineko ekuazioan ageri den $(T,p,\mu)$ sorta ordezkatzeari. Horretarako, bertan {eq}`dmu` adierazpena sartuko dugu, honako berridazketa adierazgarri hau burutu ahal izateko:

$$
\boxed{\mathrm{d}\mathscr{E} = -\left[S-N\left(\frac{\partial S}{\partial N}\right)_{T,p}\right]\mathrm{d}T+\left[\overline{V}-N\left(\frac{\partial \overline{V}}{\partial N}\right)_{T,p}\right]\mathrm{d}p + \left(\frac{\partial \mathscr{E}}{\partial N}\right)_{T,p} \mathrm{d}N} \; .
$$ (depsilontpn2)

Aurrera egin aurretik, lagungarria gerta daiteke oraindaino lortutako adierazpenetan ekarpen _txikiak_ antzematea: esate baterako, $\widehat{\mu}$ eta $\mu$ bezalako gai intentsiboen tamainarekiko deribatuak (gainontzeko aldagai intentsiboak konstante mantenduta) limite termodinamikoan arbuiagarriak dira. Hari beretik, aldagai estentsiboek izaera homogeneoa berreskuratuko dute; alegia, tamainarekin lotutako ekarpen lineala gailenduko da. Adibidez, 

$$
\lim_{N\rightarrow \infty} \left(\frac{\partial \overline{V}}{\partial N}\right)_{T,p} = \frac{\overline{V}}{N} \; ,
$$ (barV_mak)

$$
\lim_{N\rightarrow \infty} \left[\frac{\partial (\widehat{\mu}N)}{\partial N}\right]_{T,p} = \frac{\widehat{\mu}N}{N} \quad \Rightarrow \quad \mu = \widehat{\mu} \; .
$$ (mu_mak)

Nabaria da, hortaz, {eq}`depsilontpn2` ekuazioko gai guztiak _txikiak_ direla, eta soilik eskualde nanotermodinamikoan esanguratsuak. Esandakoan areago sakonduz, azter dezagun honako magnitude intentsibo hauetan tamainak ($N$ aldagaiak, egiazki) zer-nolako eragina duen: $S/N$, $\overline{V}/N$, $N/\overline{V}$. Gaineko ekuaziotik erraz asko lor daitezke ondorengo adierazpen hauek:

$$
\left[\frac{\partial \left(S/N\right)}{\partial N}\right]_{T,p} = \frac {1}{N^2}\left(\frac{\partial \mathscr{E}}{\partial T}\right)_{p,N} \, ,
$$ (dsdntp)

$$
\left[\frac{\partial (\overline{V}/N)}{\partial N}\right]_{T,p} = - \frac {1}{N^2}\left(\frac{\partial \mathscr{E}}{\partial p}\right)_{T,N} \; ,
$$ (dvdntp)

$$
\left[\frac{\partial (N/\overline{V})}{\partial N}\right]_{T,p} =  \frac {1}{\overline{V}^2}\left(\frac{\partial \mathscr{E}}{\partial p}\right)_{T,N} \; .
$$ (dndvtp)

Nabarmendu beharrekoa da ezen Termodinamika Klasikoaren bitartez ez dugula goiko berdintzetara iristerik izango. Bestela esanda, Nanotermodinamikak tamaina finituko efektuak azaleratzeaz batera, limite termodinamikotik haratago eramango gaituzten erlazioez hornituko gaitu. Bada, frogapen gisara, hurrengo {numref}`{number} adibidean <helix_coil>`, {eq}`dvdntp` ekuazioaren bi aldeak kalkulatu, eta bat datozela egiaztatuko dugu.

$$
\\
$$

Amaitzeko, beste ekuazio-bikote bat lortuko dugu, oraingoan ere jarraian datorkigun adibideari begira. Bada, entalpia $H(S,p,N) := F(T,p,N) + TS := \widehat{\mu}N + TS$ dela aintzat hartuz,

$$
\widehat{\mu} =\frac{H}{N} - T\frac{S}{N} \; ,
$$ (muhat_H)

eta,

$$
\mu := \left(\frac{\partial F}{\partial N}\right)_{T,p} = \left(\frac{\partial H}{\partial N}\right)_{T,p} - T\left(\frac{\partial S}{\partial N}\right)_{T,p} \; .
$$ (mu_H)

Bertatik honakoa lor daiteke:

$$
 \left(\frac{\partial \widehat{\mu}/T}{\partial T}\right)_{p,N} = -\frac{1}{T^2}\frac{H}{N} \quad \pmb{\neq} \quad \left(\frac{\partial \mu/T}{\partial T}\right)_{p,N} = -\frac{1}{T^2}\left(\frac{\partial H}{\partial N}\right)_{T,p} \; .
$$ (mu_muhat_h)

Hurrengo azpiataleko _helize-haril_ kateari dagozkion $\widehat{\mu}$ eta $\mu$ potentzial-bikotea kalkulatutakoan, kasu zehatz horretan {eq}`mu_muhat_h` erlazioak bereizten dituzten ekarpen finituen itxura behatuko dugu.


(helix_coil)=
### Adibidea: Helize-Haril trantsizioa

Esku artean dugun sistema {numref}`{number}. irudiko <heco>` irudiko dimentsio bakarreko soka da. Berori, hurrenez hurren, $l_{H}$ eta $l_{C}$ luzerako $n_{H}$ helize- eta $n_{C} = N - n_{H}$ haril-unitatez osatuta dago. Bestalde, bero-iturri batekin ukipen termikoan dagoela onartuko dugu, eta $N$ aldaezin mantenduko dela. Azterketa termodinamikoa $(T,f,N)$ aldagai-sortaren bitartez gauzatuko dugu, $f$ indarraren konjugatu estentsiboa $\overline{l}$, katearen batez besteko luzera, hartuta.

```{figure} helix-coil.PNG
---
height: 200px
name: heco
---
  “Helize-haril” kateak $l_H$ luzeradun $n_{H}$ helize-unitate eta $l_C$ luzeradun $n_{C} = N - n_{H}$ haril-unitate dauka ($l_C > l_H$). Mutur banatan $f$ indarra eragingo diogu. Guztizko unitate-kopuruari dagokionez, $N\rightarrow \infty$ hurbilketa asintotikora jotzen ez badugu, katean sistema txikien berezitasunak azaleratuko dira.
```

Demagun orain haril-unitateak $(C)$ soilik muturretan koka daitezkeela. Irudiko kasuan, hortaz, aukera hauek genituzke eskura: $C\;H\;H\;H\;C$ ; $C\;C\;H\;H\;H$ ; $H\;H\;H\;C\;C$. Orokortuz, baldintza horrek sistemari $g(n_{H}) = N-n_{H}+1$ endekapena sorraraziko lioke. Jakina, $H$-unitaterik ez balego, $g=1$ izango genuke, sistemak bakarrik $C$-unitateak edukiko lituzke eta. $C$- eta $H$-unitateen partizio-funtzio kanonikoak $q_{H}(T)$ eta $q_{C}(T)$ izendatuko ditugu. Beraz, kate osora zabalduz, $Q(T,l,N)=q_{C}^{n_{C}}q_{H}^{n_{H}}$ genuke. Horiek horrela, $\Delta(T,f,N)$ partizio-funtzioa eraikiko dugu:

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

Hurrengo pausoa, {eq}`d_short` ekuaziotik abiatuz sistemaren (Nano)Termodinamika ondorioztatzea da. Gibbsen energia askea $F(T,f,N) := -k_{\mathrm{B}}T\ln\Delta$ dugu.

##### Ariketa

$(a)$ Kalkulatu $\widehat{\mu}$ eta $\mu$ potentzial kimikoak, $F(T,f,N)$ adierazpenaren laguntzaz. Behin potentzialok erdietsiz gero, eraiki banatze-potentziala, eta aztertu sistemaren tamainaren arabera azaltzen duen portaera, $r = 0,5 \; ;  \; r = 0,98$ eta $r=1,05$ balioak erabiliz.

```{dropdown} __Erantzuna__
$$
\widehat{\mu} := \frac{F}{N} = -k_{\mathrm{B}}T\left[\ln r_{C} + \frac{1}{N}\ln(1+r^N)\right]
$$ (muhathelix)

$$
\mu := \left(\frac{\partial F}{\partial N}\right)_{T,f} = -k_{\mathrm{B}}T\left[\ln r_{C} + \frac{r^N\ln r}{1 + r^N}\right]
$$ (muhelix)

$$
\mathscr{E} = (\widehat{\mu}-\mu)N = -k_{\mathrm{B}}T\left[\ln(1+r^N) - N\frac{r^N\ln r}{1 + r^N}\right]
$$ (epsilonhelix)

```{figure} epsilon_tfn.PNG
---
height: 300px
name: epsilon_tfn
---
  Ekarpen finituen bilakaera banatze-potentzialaren indarraren baitan dago. Tamaina handitu ahala, berori ahulduz doa, eta sistemak eremu makroskopikorantz jotzen du. Era berean, $r$ erlazioak eskualde nanotermodinamikoaren hedaduran eragin zuzena dauka. Fase-trantsizioaren puntura gerturatu ahala $(r \rightarrow 1)$ geroz eta tarte zabalagoa hartuko du, eta $\mathscr{E}\rightarrow\mathscr{E}_{0} = -k_{\mathrm{B}}T \ln 2$ konstanterantz gerturatuko da.
```


$(b)$ Lehengo ataleko potentzial kimikoetatik abiatuz, lortu {eq}`mu_muhat_h` ekuazio-bikotea zein berorren limite makroskopikoa (aintzat eduki $r<1$ edo $r>1$ izatearen eragina). Aztertu, berebat, espresio biak desberdintzen dituzten ekarpenak, eta erlazionatu banatze-potentzialarekin.


```{dropdown} __Erantzuna__

$$
\left(\frac{\partial \widehat{\mu}/T}{\partial T}\right)_{f, N} = -k_{\mathrm{B}}\left(\frac{1}{r_{C}}\frac{\partial r_{C}}{\partial T} + \frac{r^{N-1}}{1 + r^{N}}\frac{\partial r}{\partial T}\right) \; ,
$$ (dmuhatT)

$$
\left(\frac{\partial \mu/T}{\partial T}\right)_{f, N} = -k_{\mathrm{B}}\left[\frac{1}{r_{C}}\frac{\partial r_{C}}{\partial T} + N\frac{r^{N-1}}{1 + r^{N}}\left(\frac{1}{N} + \ln r - \frac{r^{N}\ln r}{1 + r^N} \right)\frac{\partial r}{\partial T} \right] \; .
$$ (dmuT)

Limite makroskopikoan,

$$
\left(\frac{\partial \widehat{\mu}/T}{\partial T}\right)_{f, N} = \left(\frac{\partial \mu/T}{\partial T}\right)_{f, N} = \begin{cases}
      -k_{\mathrm{B}}\left( \frac{1}{r_{C}} \frac{\partial r_{C}}{\partial T} + \frac{1}{r} \frac{\partial r}{\partial T} \right) & \text{$r>1$ bada.}\\
      -k_{\mathrm{B}}\frac{1}{r_{C}}\frac{\partial r_{C}}{\partial T}& \text{$r<1$ bada.}
    \end{cases} 
$$ (dmuT_mak)

 Aitzitik, maila mikroskopikotik alde egin gabe,

$$
\frac{1}{k_{\mathrm{B}}\; \partial r/\partial T}\left(\frac{\partial \mathscr{E}/NT}{\partial T}\right)_{f,N} = -N\frac{r^{N-1}}{1+r^N}\ln r \left[1-\frac{r^N}{1+r^N}\right] \; .
$$ (dmuT_epsilon)

```{figure} epsilon_mu_muhat.png
---
height: 300px
name: epsilon_mumuhat
---
  Unitate-kopuruko banatze-potentzialaren adierazpenari ({eq}`dmuT_epsilon` ekuazioa) limite makroskopikorako trantsizio bortitzagoa hauteman dakioke. Hain zuzen ere, {numref}`{number}. irudiaren <epsilon_tfn>` aldean, zilegi zaigu $N=90-100$ zonaldean eremu termodinamikoan gaudela baieztatzea; ondorioz, inguru horretan tamaina finituko efektuek ez dute jada berebiziko eraginik izango $l/N$ bezalako magnitudeen izaera intentsiboan. Azpimarratu beharrekoa da, orobat, ekarpen txiki horien zeinua alderantzikatu egingo dela fase-trantsizioa gauzatutakoan: positiboa $r<1$ eskualdean $(N \rightarrow n_C)$; negatiboa, ordea, $r>1$ eremuan $(N \rightarrow n_H)$.
```


**----------------------------------------------------**

$$
\\
$$

Hari bertsutik, adibide honen esangura handieneko alderdiari helduko diogu, kateak $r$ erlazioarekin duen bilakaera helize-unitateen batez besteko frakzioaren bidez ereduztatuz $(\overline{n} _ {H}/N)$. Orain arte ez bezala, aurrerantzean $n_{H}$ kopuruari marratxoa erantsiko diogu, berorrek zehaztuko baitu, hain zuzen, katearen batez besteko luzera: 

$$
\overline{l}(\overline{n} _ {H}) = (N-\overline{n} _ {H})l_{C} + \overline{n} _ {H}l_{H} \; .
$$ (lbar)

Bada, horretarako, $\overline{n} _ {H}$ itxarotako balioa eskuratu behar dugu, sistemaren partizio-funtziotik abiatuz:

$$
\overline{n}_{H} := \frac{\sum _ {n _{H}} n _{H}Q(T,l(n _ {H}), N)e^{fl(n _{H})/k _{\mathrm{B}}T}}{\sum _ {n _{H}} Q(T,l(n _ {H}), N)e^{fl(n _{H})/k _{\mathrm{B}}T}} \equiv \frac{\sum _ {n _{H}} n _{H}Q(T,l(n _ {H}), N)e^{fl(n _{H})/k _{\mathrm{B}}T}}{\Delta(T,f,N)} \; .
$$ (nhdef)

Gauzak horrela, hasteko {eq}`d` ekuazioko batukaritik $n_{H}=0$ gaia atera, eta $\Delta$ honela berridatziko dugu:

$$
    \Delta = r_{C}^N\left[1+\sum_{n_{H}=1}^{N}\left(N-n_{H}+1\right)r^{n_{H}}\right]\; .
$$ (dnew)

Hala, {eq}`nhdef` definizioari jarraituz,

$$
\overline{n}_{H} := \frac{r_{C}^N\left[0+\sum_{n_{H}=1}^{N}n_{H}\left(N-n_{H}+1\right)r^{n_{H}}\right]}{\Delta} = r\frac{\partial}{\partial r}\ln \Delta \; .
$$ (nbar)

`````{admonition} Iradokizuna
:class: tip
Egiaztatu {eq}`nbar` ekuazioaren bi aldeak bat datozela.
`````

Bada, {eq}`nbar` ekuazioan {eq}`d_short` adierazpena ordezkatuz gero, azkenean ere! iritsiko gara helmugara:

$$
\boxed{\frac{\overline{n} _ {H}}{N} = \frac{r}{N}\frac{\partial}{\partial r}\ln\left[r_{C}^N(1 + r^N)\right] = \frac{r^N}{1+r^N}}\; .
$$(fraction_N)


Errepara diezaiogun orain ekuazio horren adierazpen grafikoari:

```{figure} hc_phase.PNG
---
height: 350px
name: hc_phase
---
  Helize-unitateen batez besteko frakzioaren kurbek eite bitxia eta susmagarria dute. Izan ere, badirudi intentsibotasuna ez dela dirudien bezain kontzeptu tinkoa.
```

Lortutako emaitzak direla eta, berehalako geldialdia egin beharrean gaude, ezinbestean.

Hurrera gakizkion, **arreta handiz**, {numref}`{number}. irudiko <hc_phase>` kurba-sortari. Izatez, Termodinamikaren ikuspuntutik, batez besteko frakzioak izaera INTENTSIBOA beharko luke izan, zero ordenako funtzio Euler-homogeneo orok bezalaxe. Baina $N$ aldatu ahala, $\overline{n}_{H}/N$ kurbaren formak ez dirau bere horretan!! Horrek, argi eta garbi, aztergai dugun magnitudeak tamainarekiko menpekotasuna duela iradokitzen du, hots, ESTENTSIBOA dela. Preseski, sistema txikia denean $(N=2)$, tamaina laukoiztean, helize-unitateen frakzioak aldaketa bortitza pairatu du, ez ordea $N=40$tik $N=200$erakoa bezain gogorra. Berezitasun horiek {numref}`{number}. irudiak <epsilon_tfn>` islatzen duen banatze-potentzialaren bilakaeraren ondorio dira.

Ondorioz, $N=200$ inguruan $\overline{n}_{H}/N$ren jokaera intentsiboa berrezarri dela esan liteke, arestian aipatutako bat-bateko helize-haril fase-trantsizioa igarri dakioke eta. Nolanahi ere, sailkapen zorrotzari atxikiz, soilik $N\rightarrow \infty$ limiteak deuseztatuko ditu erabat tamaina finituko efektuak, maila makroskopikora jauzi egitea ahalbidetuz. Osterantzean, helize-haril katea sistema txikia da.

$$
\\
$$

Esanak esan, fase-trantsizioen gaian murgildutakoan ({numref}`{number}. atalean <fase>`) izango dugu {numref}`{number}. irudira <hc_phase>` bihurtzeko beta egokia. Horrekin hasi aurretik, alabaina, {numref}`{number}. atalaren <tpn_azter>` amaiera aldeko haria berrartuko dugu une batez.

(helix_ariketa_2)=
#### Ariketa
Ariketa osagarri honen xedea, {eq}`dsdntp` eta {eq}`dvdntp` berdintzak "helize-haril" ereduan aztertzean datza. 

$(a)$ Eraiki $S(T,f,N)$ entropiaren adierazpena, eta egiaztatu {eq}`dsdntp` erlazioa betetzen dela.

```{dropdown} __Erantzuna__

Bada, $S(T,f,N) := \frac{\partial}{\partial T}\left(k_{\mathrm{B}}T \ln \Delta\right)$ definiziora joz, eta arestiko {eq}`d_short` partizio-funtzioa bertan sartuz,

$$
S(T,f,N) = k_{\mathrm{B}}\left[N \ln r_C + \ln\left(1 + r^N\right)\right] + Nk_{\mathrm{B}}T\left\{\frac{\mathrm{d}\ln q_C}{\mathrm{d} T} - \frac{fl_C}{k_{\mathrm{B}}T^2} + \frac{r^N}{1 + r^N}\left[-\frac{\mathrm{d}\ln q_C}{\mathrm{d} T} + \frac{\mathrm{d}\ln q_H}{\mathrm{d} T} - \frac{f\left(l_H - l_C\right)}{k_{\mathrm{B}}T^2}\right]\right\} \; .
$$ (stfn)

Adierazpen horrekin zein aurrez kalkulatu dugun {eq}`epsilonhelix` banatze-potentzialarekin eragiketak burutuz gero, {eq}`dsdntp` ekuazoaren alde biak bat datozela ikusiko dugu:

$$
\left[\frac{\partial \left(S/N\right)}{\partial N}\right]_{T,p} = \frac{1}{N}k_{\mathrm{B}}\left[\frac{r^N\ln r}{1 + r^N} - \frac{1}{N}\ln\left(1 + r^N\right)\right] + k_{\mathrm{B}}T \frac{r^N \ln r}{\left(1 + r^N\right)^2}\left[-\frac{\mathrm{d}\ln q_C}{\mathrm{d} T} + \frac{\mathrm{d}\ln q_H}{\mathrm{d} T} - \frac{f\left(l_H - l_C\right)}{k_{\mathrm{B}}T^2}\right] = \frac {1}{N^2}\left(\frac{\partial \mathscr{E}}{\partial T}\right)_{p,N}
$$ (heco_equality_0)

Gaineko adierazpenari behako bat emanez gero, gai guztiak tamaina finitukoak direla ohartuko gara, eta, beraz, $N \rightarrow \infty$ limitean baztergarriak. Hartara, partikulako entropia $(S/N)$ intentsibo bilakatuko da. 


```

$(b)$ Bigarren ekuazioari helduko diogu orain. Ezer baino lehen, ohartu gaitezen ezen dimentsio bakarreko katea dugula aztergaitzat; ondorioz, ekarpen mekanikoa $f$ indarraren eta berorren konjugatua den $\overline{l}$ luzeraren bitartez azaleratu dugu. Hori dela eta, lehendabizi, ekuazioa bera egokitu eta berridatzi beharra daukagu. Bada, pausoz pauso ekingo diogu eginbeharrari.

Idatzi sistema txikiaren Gibbs-en ekuazioa. Hortik abiatuz, berreraiki {eq}`depsilontpn2` ekuazioa, $(T,f,N)$ ingurune-aldagaien baitan. Bertatik, erauzi {eq}`dvdntp` ekuazioaren adierazpen baliokidea. Hori guztia egin aurretik, hausnartu ekarpen mekanikoak eramango duen zeinuaren gainean; positiboa ala negatiboa beharko luke izan?

```{dropdown} __Erantzuna__

Adibidearen hasieran dugun {numref}`{number}. irudiarekin <heco>` lotutako azalpenei atxikiz, kateari bi muturretan kanporanzko $f$ indarra eragingo bagenio $(f>0)$, haren luzerak $\Delta l$ ekarpen positiboa jasoko luke; alegia, sistemari $f \Delta l$ lana egiten arituko gintzaizkioke, zeinak barne-energia igoko lukeen. Nabarmendu beharrekoa da, ezen, ohiko sistema hidrostatikoari dagokionez, ekarpen mekanikoaren portaera oso bestelakoa dela. Har dezagun, esate baterako, tanga batean $p$ presiopean dagoen gasa $(p>0)$. Bada, gasa hedatzen hasiko balitz, sistemak berak lana egingo lioke inguruneari. Hortaz, $\Delta V$ bolumen-aldakuntza positiboak sistemaren barne-energiari $-p\Delta V$ galera lekarkioke egiatan. Aitzitik, $p$ presioak gasa konprimatzeko bezainbesteko ahalmena baleuka, $\Delta V < 0$ genuke; hartara, hitzarmen horri jarraikiz, konprimatze-prozesuak sistemari lana eragingo lioke, barne-energia handituz.

Aurkeztutako arrazoinamendua dela bide, "helize-haril" sistema txikiaren Gibbsen ekuazioa hauxe izango dugu:

$$
\mathrm{d}\overline{E} = T\mathrm{d}S + f\mathrm{d}\overline{l} + \mu\mathrm{d}N \; .
$$ (heco_gibbs)

Legendreren bi transformazio aplikatuz, Gibssen energia askeak eta banatze-potentzialak, hurrenez hurren,

$$
\mathrm{d}F(T,f,N) = -S\mathrm{d}T - \overline{l}\mathrm{d}f +\mu\mathrm{d}N
$$ (heco_gibss_aske)

eta

$$
\mathrm{d}\mathscr{E} = -S\mathrm{d}T - \overline{l}\mathrm{d}f - N\mathrm{d}\mu
$$ (heco_depsilon)

erlazioei eutsiko diete. Jarraian, {numref}`{number}. atalean <tpn_azter>` segitutako prozedura errepikatuz, {eq}`heco_depsilon` ekuazioa berridatziko dugu:

$$
\mathrm{d}\mathscr{E} = -\left[S-N\left(\frac{\partial S}{\partial N}\right)_{T,f}\right]\mathrm{d}T+\left[\overline{l}-N\left(\frac{\partial \overline{l}}{\partial N}\right)_{T,f}\right]\mathrm{d}f + \left(\frac{\partial \mathscr{E}}{\partial N}\right)_{T,f} \mathrm{d}N \; .
$$ (heco_depsilon_1)

Errepara diezaiogun orain {eq}`dvdntp` ekuazioari eta daramagun berori $(T,f,N)$ ingurune-aldagaietara. Aurreko {eq}`heco_depsilon_1` ekuazioaren laguntzaz, 

$$
\left[\frac{\partial (\overline{l}/N)}{\partial N}\right]_{T,f} =  \frac {1}{N^2}\left(\frac{\partial \mathscr{E}}{\partial f}\right)_{T,N} 
$$ (heco_equality)

adierazpena beteko dela ohartuko gara. 

```


$(c)$ Egiaztatu $(a)$ atalean lortutako {eq}`heco_equality` berdintza betetzen dela, adibidearen garapenean barrena eraikitako ekuazioak baliatuz.

```{dropdown} __Erantzuna__

Ezkerraldeko adierazpena {eq}`lbar` ekuazioaren bidez kalkulatuko dugu; eskumakoa, ordea, {eq}`epsilonhelix` ekuazioa erabiliz, eta $r(T,f)= r_H(T,f)/r_C(T,f)$ erlazioari so eginez. Eragiketak egiteaz bat, bi aldeak bat datozela ikusiko dugu:

$$
\left[\frac{\partial (\overline{l}/N)}{\partial N}\right]_{T,f} = \frac{r^N \ln r}{\left(1+r^N \right)^2} \left(l_H - l_C\right) = \frac {1}{N^2}\left(\frac{\partial \mathscr{E}}{\partial f}\right)_{T,N} 
$$ (heco_equality_1)

Agerikoa da ezen gaineko {eq}`heco_equality_1` adierazpenak zerorantz joko duela limite makroskopikoan, nola $r < 1$ kasuan hala $r>1$ denean; horrekin batera, $\overline{l}/N$ magnitudeak izaera intentsiboa berreskuratuko du.

```

**----------------------------------------------------**


(gitpn)=
### Adibidea: Gas ideal klasikoa, multzo isotermo-isobaroan

Bigarren sistemaren azterketa [_C eranskineko_](gitvn) emaitzetatik abiatuko dugu. Hasteko, askatasun-gradu mekanikoa abiarazi, eta multzo kanonikotik isotermo-isobarora igaroko gara. Partizio-funtzio berria eraikitzerakoan, {eq}`qtvngi` ekuazioko zaharrari dagokion Legendreren transformazioa aplikatuko diogu.

$$
\Delta(T,p,N) := \int_{0}^{\infty}\mathrm{d}\left(\frac{pV}{k_{\mathrm{B}}T}\right)\left[\frac{V^N}{N!\Lambda^{3N}}\right]\;e^{-pV/k_{\mathrm{B}}T} = \left(\frac{k_{\mathrm{B}}T}{p\Lambda^3}\right)^N \; .
$$ (dtpn_gi)

```{admonition} Oharra
 $$
 \int_{0}^{\infty}\mathrm{d}x \; x^n e^{-ax} = \Gamma(n+1)a^{-n-1}
 $$
```

Aipatzekoa da jada ez dela $N!$ agertzen. Are gehiago, Gibbsen energia askea idatziz gero,

$$
F(T,p,N) = Nk_{\mathrm{B}}T\ln\left(\frac{p\Lambda^3}{k_{\mathrm{B}}T}\right) \; ,
$$ (ftpngi)

berorrek uneoro jokaera makroskopikoa erakusten duela ohartuko gara, lehen mailako funtzio Euler-homogeneoa da eta, hots, lineala. Ondorioz, $\widehat{\mu}=\mu$, eta, beraz, 

$$
\mathscr{E}(T,p,N)=0 \; .
$$ (gi_epsilon_tpn)

Aipatzekoa da multzo kanonikoan $\mathscr{E}(T,V,N)>0$ lortu dugula (ikus {eq}`epsilon_tvn` ekuazioa). Beha dezagun emaitzok entropian zer-nolako eragina duten:

$$
\boxed{S(T,p,N) := -\left(\frac{\partial F}{\partial T}\right)_{p,N}=Nk_{\mathrm{B}}\left[\ln\left(\frac{\overline{V}}{\Lambda^3N}\right) + \frac{5}{2}\right]} \; .
$$ (stpngi)

Berori {eq}`stvngi` ekuazioarekin alderatuz (eta $Nk_{\mathrm{B}}T/p = \overline{V}=V$ onartuz), azken gai negatiboak ageri ez direla ohartuko gara, Sackur-Tetrode adierazpena berreskuratu baitugu; alegia, multzo kanonikoaren aldean, askatasun-gradu bat abiarazteak banatze-potentziala desagerrarazi, eta, horrekin batera, entropia handitu egin du!

$$
\\
$$

Aurrerago, {numref}`{number}. atalean <tpmu>`, gas ideala azpisistema erabat askez osaturiko multzo nanokanonikoan berraztertuko dugu. Bertan azalduko diren efektu berriek berebiziko adierazgarritasuna emango diote Nanotermodinamikari.
