(tpn)=
## 4

## Multzo isotermo-isobaroa: $(T,p,N)$ ingurune-aldagaiak

Kapitulu honen fisikari heldu baino lehen, honako honi erreparatu behar diogu: \ref{nano}. atalean ikusiko dugunez, multzo nanokanonikorako $(T,p,\mu)$ trantsizioa $Q(T,V,N)$ partizio-funtzio kanonikotik abiatzen dugu normalean, Legendreren transformazioen laguntzaz. Kontua da tarteko multzotzat makrokanonikoa $(T,V,\mu)$ hautatuz gero, zenbaitetan bidea malkartsua gertatuko zaigula. Bada, bolumenean barreneko integrala barik $N$ partikula-kopuruan zeharreko batukaria kalkulatzeak lana arinduko digu.
Hala, ibilbide hori multzo isotermo-isobaroan $(T,p,N)$ barrena burutzea mesedegarria izango zaigu oso. Bestetik, ingurune-aldagai horien bidez $T$ eta $p$ finkatzen dituen ingurune batean makromolekula edo koloide konprimaezin eta hedagarria ezaugarritu daiteke. Ildo horretatik, \ref{npt_ex} azpiatalean lan honetako lehenbiziko adibideari helduko diogu, hurbilketa bereziekin bada ere.

Horiek horrela, multzo estatistiko honi azterketa sakonagoa eskaintzea merezi du.

###  4.1 Multzoaren azterketa

Kontrol-aldagaitzat $(T,p,N)$ dituzten sistema txikiek $\bar{E}=E_{t}/\mathcal{N}$, $\bar{V}=V_{t}/\mathcal{N}$ eta $N=N_{t}/\mathcal{N}$ aldagai estentsiboak izango dituzte.

####  Ariketa

Aurreko esaldian aipatutakoa aintzat hartuz, eta [](hillsec). ataleko azalpenei segituz, eraiki honako adierazpenak:

$(a)$ Multzo isotermo-isobaroaren Gibbs-en ekuazioa eta $X(T,p,N)$ aldaki-energia. Emaitzak azaldu.

```{dropdown} __Erantzuna__
```{math}
\mathrm{d}E_{t}(S_{t},V,N_{t},\mathcal{N}) = T\mathrm{d}S_{t} - p\mathrm{d}V_{t} + \mu \mathcal{N}\mathrm{d}N + (\mathcal{E}+\mu N)\mathrm{d}\mathcal{N}\;
\\
\\
X(T,p,N) = \mathcal{E} + \mu N := \left(\frac{\partial E_{t}}{\partial \mathcal{N}}\right)_{S_{t},V_{t},N} := \widehat{\mu}N \; .

```

```{dropdown} __Azalpenak__
Kasu honetan, $N$ ingurune-aldagaia agerrarazi behar dugu ekuazioan, $\mathrm{d}N_{t} = \mathcal{N}\mathrm{d}N + N\mathrm{d}\mathcal{N}$ erabiliz. Berorrek $N_{t}$ magnitudeak aldaezin irautea galarazten du. Aldaki-energia multzo honen izaeraren isla da. Hala, aldaki bat txertatzean, guztizko bolumena zein energia birbanatu egingo dira, sistema txikiei aldagaiok askatasun osoz eraldatu baitiezazkiekegu. Aitzitik, $N$ partikula-kopuruak aldaezin iraun behar duenez sistema orotan, multzoaren barne-energiak ekarpen kimikoa ere jasango luke, bere ikuspuntutik kanpotik $N$ partikuladun sorta berri bat gehitzen genbilzkioke eta. Aipaturiko ekarpen kimikoa $\widehat{\mu}$ potentzialaren bidez ereduztatu behar dugu, ez baitauka azpisistemei esleitutako $\mu$ potentzialaren esanahi bera.
```

$(b)$ Sistema txikien Gibbs-en ekuazioa eta barne-energiaren adierazpena.
```{dropdown} __Erantzuna__
```{math}
\mathrm{d}\bar{E} = T\mathrm{d}S - p\mathrm{d}\bar{V} + \mu \mathrm{d}N
\\
\\
\bar{E} = TS - p\bar{V} + \widehat{\mu}N
```
$(c)$ Gibbs-en energia askea ($F(T,p,N)$). Hortik abiatuta, idatzi magnitude integrala eta diferentziala erlazionatzen dituen adierazpena. 

```{dropdown} __Erantzuna__
```{math}
F(T,p,N) := \bar{E} - TS + p\bar{V} = \widehat{\mu}N
\\
\\
\mathrm{d}F(T,p,N) = -S\mathrm{d}T + \bar{V}\mathrm{d}p + \mu\mathrm{d}N \;
\\
\\
\boxed {\mu := \left[\frac{\partial(\widehat{\mu}N)}{\partial N}\right]_{T, p} = \widehat{\mu} + N\left(\frac{\partial \widehat{\mu}}{\partial N}\right)_{T,p} \quad ; \quad \mathcal{E} =  (\widehat{\mu} - \mu)N}

```
