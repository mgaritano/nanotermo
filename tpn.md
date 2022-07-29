(tpn)=
## Multzo isotermo-isobaroa: $(T,p,N)$ ingurune-aldagaiak

Kapitulu honen fisikari heldu baino lehen, honako honi erreparatu behar diogu: [](tpmu) atalean ikusiko dugunez, multzo nanokanonikorako $(T,p,\mu)$ trantsizioa $Q(T,V,N)$ partizio-funtzio kanonikotik abiatzen dugu normalean, Legendreren transformazioen laguntzaz. Kontua da tarteko multzotzat makrokanonikoa $(T,V,\mu)$ hautatuz gero, zenbaitetan bidea malkartsua gertatuko zaigula. Bada, bolumenean barreneko integrala barik $N$ partikula-kopuruan zeharreko batukaria kalkulatzeak lana arinduko digu.
Hala, ibilbide hori multzo isotermo-isobaroan $(T,p,N)$ barrena burutzea mesedegarria izango zaigu oso. Bestetik, ingurune-aldagai horien bidez $T$ eta $p$ finkatzen dituen ingurune batean makromolekula edo koloide konprimaezin eta hedagarria ezaugarritu daiteke. Ildo horretatik, [](helix_coil) azpiatalean lan honetako lehenbiziko adibideari helduko diogu, hurbilketa bereziekin bada ere.

Horiek horrela, multzo estatistiko honi azterketa sakonagoa eskaintzea merezi du.

###  Multzoaren azterketa

Kontrol-aldagaitzat $(T,p,N)$ dituzten sistema txikiek $\bar{E}=E_{t}/\mathcal{N}$, $\bar{V}=V_{t}/\mathcal{N}$ eta $N=N_{t}/\mathcal{N}$ aldagai estentsiboak izango dituzte.

####  Ariketa

Aurreko esaldian aipatutakoa aintzat hartuz, eta [](hillsec). ataleko azalpenei segituz, eraiki honako adierazpenak:

$(a)$ Multzo isotermo-isobaroaren Gibbs-en ekuazioa eta $X(T,p,N)$ aldaki-energia. Emaitzak azaldu.

```{dropdown} __Erantzuna__
$$
\mathrm{d}E_{t}(S_{t},V,N_{t},\mathcal{N}) = T\mathrm{d}S_{t} - p\mathrm{d}V_{t} + \mu \mathcal{N}\mathrm{d}N + (\mathcal{E}+\mu N)\mathrm{d}\mathcal{N}
$$
$$
X(T,p,N) = \mathcal{E} + \mu N := \left(\frac{\partial E_{t}}{\partial \mathcal{N}}\right)_{S_{t},V_{t},N} := \widehat{\mu}N \; .
$$
```

```{dropdown} __Azalpenak__
Kasu honetan, $N$ ingurune-aldagaia agerrarazi behar dugu ekuazioan, $\mathrm{d}N_{t} = \mathcal{N}\mathrm{d}N + N\mathrm{d}\mathcal{N}$ erabiliz. Berorrek $N_{t}$ magnitudeak aldaezin irautea galarazten du. Aldaki-energia multzo honen izaeraren isla da. Hala, aldaki bat txertatzean, guztizko bolumena zein energia birbanatu egingo dira, sistema txikiei aldagaiok askatasun osoz eraldatu baitiezazkiekegu. Aitzitik, $N$ partikula-kopuruak aldaezin iraun behar duenez sistema orotan, multzoaren barne-energiak ekarpen kimikoa ere jasango luke, bere ikuspuntutik kanpotik $N$ partikuladun sorta berri bat gehitzen genbilzkioke eta. Aipaturiko ekarpen kimikoa $\widehat{\mu}$ potentzialaren bidez ereduztatu behar dugu, ez baitauka azpisistemei esleitutako $\mu$ potentzialaren esanahi bera.
```

$(b)$ Sistema txikien Gibbs-en ekuazioa eta barne-energiaren adierazpena.
```{dropdown} __Erantzuna__
$$
\mathrm{d}\bar{E} = T\mathrm{d}S - p\mathrm{d}\bar{V} + \mu \mathrm{d}N
$$
$$
\bar{E} = TS - p\bar{V} + \widehat{\mu}N
$$
```
$(c)$ Gibbs-en energia askea ($F(T,p,N)$). Hortik abiatuta, idatzi magnitude integrala eta diferentziala erlazionatzen dituen adierazpena.

```{dropdown} __Erantzuna__
$$
F(T,p,N) := \bar{E} - TS + p\bar{V} = \widehat{\mu}N
$$
$$
\mathrm{d}F(T,p,N) = -S\mathrm{d}T + \bar{V}\mathrm{d}p + \mu\mathrm{d}N \;
$$
$$
\boxed {\mu := \left[\frac{\partial(\widehat{\mu}N)}{\partial N}\right]_{T, p} = \widehat{\mu} + N\left(\frac{\partial \widehat{\mu}}{\partial N}\right)_{T,p} \quad ; \quad \mathcal{E} =  (\widehat{\mu} - \mu)N}
$$
```

Ariketa horretako $(c)$ atalean, sistema txikiaren Gibbs-en energia askearen eta __potentzial kimiko integralaren__ arteko erlazioa erakusten du: $F := \widehat{\mu}N$. Azken horrek, $\mu$ __potentzial kimiko diferentzialarekin__ batera, banatze-potentziala finkatzen du. Ildo horri segituz, $\widehat{\mu}$ potentzialak ekuazio hau beteko du:

$$
\boxed{\mathrm{d}\widehat{\mu} = -\frac{S}{N}\mathrm{d}T + \frac{\bar{V}}{N}\mathrm{d}p - \frac{\mathcal{E}}{N^2}\mathrm{d}N}
$$ (dmuhat)

Interesgarria litzateke $\mathrm{d}\mu$ potentzialari ere tankerako adierazpen bat esleitzea. Horretarako, Maxwell-en erlazioak lortu behar ditugu, deribatuen trukatze-propietateak erabiliz, adibidez,

$$
\left(\frac{\partial \mu}{\partial T}\right)_{p, N} := \frac{\partial}{\partial T}\left(\frac{\partial F}{\partial N}\right)_{T, p} =  \frac{\partial}{\partial N}\left(\frac{\partial F}{\partial T}\right)_{p, N} := -\left(\frac{\partial S}{\partial N}\right)_{T, p}  \; .
$$

Horrenbestez,

$$
\boxed{\mathrm{d}\mu = -\left(\frac{\partial S}{\partial N}\right)_{T,p}\mathrm{d}T + \left(\frac{\partial \bar{V}}{\partial N}\right)_{T,p}\mathrm{d}p - \frac{1}{N}\left(\frac{\partial \mathcal{E}}{\partial N}\right)_{T,p}\mathrm{d}N} \; .
$$ (dmu)

Ikus daitekeen legez, {eq}`dmuhat` eta {eq}`dmu` ekuazioek bi potentzial kimikoen izaera integrala eta diferentziala azaleratu dituzte, hurrenez hurren. Berebat, aldagai estentsiboek $N$ aldagaiarekiko azaltzen duten ez-linealtasunaren erakusle dira. Halaber, {eq}`dmu` ekuazioko azkenengo gaia $\left(\partial \mu/\partial N\right)_{T,p}\mathrm{d}N$ dugu, zeina ez baita nulua. Horrek $\mu$ potentzial kimikoak orokorki jokaera ez-intentsiboa duela diosku, hau da, $\mu = \mu(T,p,N)$ erlazioari darraikiola. Eskualde makroskopikoan bi adierazpenok bat etorriko dira, hain zuzen, {eq}`gibbs-duhem` erlazioarekin (Gibbs-Duhem).

Horiez gain, entalpia $H(S,p,N) := F(T,p,N) + TS := \widehat{\mu}N + TS$ dela aintzat hartuz,

$$
\widehat{\mu} = \frac{H}{N} - T\frac{S}{N} \; ,
$$ (muhat)

eta

$$
\mu := \left(\frac{\partial F}{\partial N}\right)_{T,p} = \left(\frac{\partial H}{\partial N}\right)_{T,p} - T\left(\frac{\partial S}{\partial N}\right)_{T,p} \; .
$$ (mu)

Bertatik honakoa lor daiteke:

$$
\left(\frac{\partial \widehat{\mu}/T}{\partial T}\right)_{p,N} = -\frac{1}{T^2}\frac{H}{N} \quad \pmb{\neq} \quad \left(\frac{\partial \mu/T}{\partial T}\right)_{p,N} = -\frac{1}{T^2}\left(\frac{\partial H}{\partial N}\right)_{T,p} \; .
$$ (h)
Jarraian datorkigun [](helix_coil) adibidean {eq}`h` ekuazio-bikotea kalkulatu, eta kasu zehatz horretan beroriek bereizten dituzten ekarpen finituen eitea behatuko dugu.

(helix_coil)=
###  Adibidea: helize-haril trantsizioa

Esku artean dugun sistema [3](heco). irudiko dimentsio bakarreko soka da. Berori, hurrenez hurren, $l_{H}$ eta $l_{C}$ luzerako $n_{H}$ helize- eta $n_{C} = N - n_{H}$ haril-unitatez osatuta dago. Bestalde, bero-iturri batekin ukipen termikoan dagoela onartuko dugu, eta $N$ aldaezin mantenduko dela. Azterketa termodinamikoa $(T,f,N)$ aldagai-sortaren bitartez gauzatuko dugu, $f$ indarraren konjokatu estentsiboa $\bar{l}$, unitateen batez besteko luzera, hartuta.

(heco)=
```{figure} helix-coil.PNG
---
height: 200px
name: helix-coil
---
  “Helize-haril” kateak helize-unitateak ($H$) eta haril-unitateak ($C$) dauzka. Mutur banatan $f$  indarra eragingo diogu. Guztizko unitate-kopuruari dagokionez, $N\rightarrow \infty$ hurbilketa asintotikoa ez badarabilgu, katean sistema txikien berezitasunak azaleratuko dira. Oroz gain, beroriek makroskopikoki intentsiboak diren aldagaiei nabarmenki erasango diete.
```

Demagun orain haril-unitateak ($C$) soilik muturretan koka daitezkeela. Irudiko kasuan, hortaz, aukera hauek genituzke eskura: $C\;H\;H\;H\;C$ ; $C\;C\;H\;H\;H$ ; $H\;H\;H\;C\;C$. Orokortuz, baldintza horrek sistemari $g(n_{H}) = N-n_{H}+1$ endekapena lekarkioke. Jakina, $H$-unitaterik ez balego, $g=1$ izango genuke, sistemak bakarrik $C$-unitateak baileuzkake. $C$- eta $H$-unitateen partizio-funtzio kanonikoak $q_{H}(T)$ eta $q_{C}(T)$ izendatuko ditugu. Beraz, kate osora zabalduz, $Q(T,l,N)=q_{C}^{n_{C}}q_{H}^{n_{H}}$ genuke. Horiek horrela, $\Delta(T,f,N)$ partizio-funtzioa eraikiko dugu:

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
