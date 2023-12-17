(elek_mag)=
## Sistema elektrikoak eta magnetikoak

Aurreneko bi atalak aurrez landutako bi sistemaren berrazterketara daude bideratuta, efektu elektrikoak gaineratuko dizkiegularik. Egiazki, lehendabizi {numref}`{number} adibideko <helix_coil>` “helize-haril” sistema itxuraldatuko dugu, alde banatan aurkako zeinudun bi karga erantsiz. Ondoren, {numref}`{number} adibidean <mupt_linagg>` ageri den agregatu linealari helduko diogu, eta unitate-osatzaileetako bakoitza $z$ norabidearekiko ausazko orientaziodun dipolo elektrikotzat hartuko dugu. Kasu bietan, kanpoko eremu elektrikoaren eraginpean ezarriko ditugu sistemak, berorien azterketa termodinamikoa berrabiarazteko.

Hirugarren zatian, Isingen dimentsio bakarreko katea izango dugu hizpide, eta, batik bat, harekin multzo nanokanonikoan arituko gara, 
horri esker lortu ahalko baitugu multzoaren banatzeari dagokion oreka termikoa erdiestea.


(heco_elek)=
### Helize-haril trantsizioa, $\mathbf{E}$ kanpo-eremuaren eraginpean

Sistema elektrikoak aztertzean, aldagai-pare berri batekin arituko gara: $\mathbf{E}$ eremu elektrikoa, eta haren konjugatu estentsiboa den sistemaren momentu dipolar elektrikoa, $\mathbf{p}$. Gauzak horrela, adibide honetan, {numref}`{number} irudiko <heco>` "helize-haril" kate eraldatua izango dugu aztergaitzat ({numref}`{number} irudia <heco_e>`).

```{figure} heco_efield.jpg
---
height: 200px
name: heco_e
---
  “Helize-haril” kateari $\pm q$ kargak gehitu dizkiogu mutur banatan. Hori dela eta, katean barrena $\vert\mathbf{p}\vert = ql$ momentu dipolar elektrikoa azaleratuko da, non $l$ katearen luzera den. Halaber, helize eta haril unitate bakoitzari $\alpha$ polarizabilitatea esleituko diogu. Bada, $\mathbf{E}$ eremu elektrikoa ezarriz gero $(\mathbf{E} \parallel \mathbf{p})$, bi faktore horiek ekarpen energetikoa izango dute, segidan zehaztuko dugun legez.
```

Bada, $q,\vert\mathbf{E}\vert > 0$ hartuz gero, eremu elektrikoak katearen luzera handituko du; bestela esanda, helize-haril fase trantsizioa areagotu egingo da. Gogora dezagun {numref}`{number} adibidean <helix_coil>` haril-unitateak helize-unitateak baino luzeagoak direla onartu genuela $(l_C>l_H)$. Hori dela eta, $\vert\mathbf{E}\vert \rightarrow \infty$ limitean, $\overline{n}_H/N$ magnitudeak zerorantz joko duela aurresan dezakegu.

$$
\\
$$

Sistemaren azterketa termodinamikoari ekinez, multzo kanonikoan eskuragai dugun ingurune-aldagai sorta $(T,l,N,\vert\mathbf{E}\vert)$ da. Beraz, $Q(T,l,N,\vert\mathbf{E}\vert)$ partizio-funtzioa eraikitzeko, {numref}`{number} irudian <heco_e>` azaltzen diren faktore gehigarriek barne-energiarako izango duten ekarpena idatzi behar dugu, alegia,

$$
U_{p} = - \mathbf{p}\cdot \mathbf{E} = -lq\vert\mathbf{E}\vert 
$$ (u_p_heco)

eta

$$
U_{\alpha} = N\left(-\int_0^{\vert\mathbf{E}\vert} \mathrm{d}\vert\mathbf{E}\vert^{\prime} \; \alpha\vert\mathbf{E}\vert^{\prime} \right) = -\frac{1}{2}N\alpha \vert\mathbf{E}\vert^2 \; .
$$ (u_alpha_heco)


Beraz, jatorrizko adibideko $Q(T,l,N)$ adierazpenetik abiatuz, partizio-funtzio berria honako hau izango da:

$$
Q(T,l,N,\vert\mathbf{E}\vert) = Q(T,l,N)\cdot Q_p\cdot Q_{\alpha} = Q(T,l,N)\exp\left(\frac{lq\vert\mathbf{E}\vert}{k_{\mathrm{B}}T}\right)\exp\left(\frac{N\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right) \; .
$$ (heco_e_q)


Hori aintzat hartuz, multzo isotermo-isobarora igaroko gara:

$$
\Delta(T,f,N,\vert\mathbf{E}\vert) = \sum_{l}Q(T,l,N,\vert\mathbf{E}\vert)\;e^{fl/k_{\mathrm{B}}T} = \exp\left(\frac{N\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right)\sum_{l}Q(T,l,N)\;e^{(q\vert\mathbf{E}\vert+f)l/k_{\mathrm{B}}T} \; ,
$$ (heco_e_delta)

edo,

$$
\Delta(T,f,N,\vert\mathbf{E}\vert) = \exp\left(\frac{N\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right) \Delta(T,f + q\vert\mathbf{E}\vert,N) \; .
$$ (heco_e_delta_2)

Bada, {numref}`{number} adibidean <helix_coil>` erabilitako hurbilketari eutsiz gero (unitate guztiak $H$ egoeran edo unitate guztiak $C$ egoeran), {eq}`heco_e_delta_2` adierazpeneko $\Delta(T,f + q\vert\mathbf{E}\vert,N)$ gaia bat etorriko da {eq}`d_short` ekuazioko partizio-funtzioarekin, alegia,

$$
\Delta(T,f,N,\vert\mathbf{E}\vert) = \exp\left(\frac{N\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right) \; r_C^N\left(1+r^N\right) \; .
$$ (heco_e_delta_3)

Hori bai, $r_C$, $r_H$ eta $r$ magnitudeak moldatu beharko ditugu:

$$
r_{C,H} = q_{C,H}\exp\left(l_{C,H}\frac{f+q\vert\mathbf{E}\vert}{k_{\mathrm{B}}T}\right) \quad , \quad r = \frac{r_H}{r_C} \; .
$$


Gaineko {eq}`heco_e_delta_3` ekuaziotik eskuratuko ditugu $\widehat{\mu}$ eta $\mu$ potentzial kimikoak:

$$
\widehat{\mu} = -\frac{1}{2}\alpha \vert\mathbf{E}\vert^2 - k_{\mathrm{B}}T\left[\ln r_{C} + \frac{1}{N}\ln\left(1+r^N\right)\right] \; ,
$$ (heco_e_muhat)

$$
\mu = - \frac{1}{2}\alpha \vert\mathbf{E}\vert^2 - k_{\mathrm{B}}T\left[\ln r_{C} + \frac{r^N\ln r}{1 + r^N}\right] \; .
$$ (heco_e_mu)

Ohartu gaitezen, $\alpha$ polarizabilitatearen energiarako ekarpena $N$rekiko lineala denez, banatze-potentzialaren adierazpena ez dela aldatu ({eq}`epsilonhelix` ekuazioa).

Berebat, interesgarria da sistemaren batez besteko momentu dipolarra ere kalkulatzea:

$$
\overline{\vert\mathbf{p}\vert} := k_{\mathrm{B}}T\left(\frac{\ln\Delta}{\partial \vert\mathbf{E}\vert}\right)_{T,f,N} = N\alpha\vert\mathbf{E}\vert + q\left[Nl_C+\frac{r^{N+1}\ln r}{1+r^N}\left(l_H-l_C\right)\right] = N\alpha\vert\mathbf{E}\vert + q\bar{l} \, .
$$ (heco_e_pbar)

##### Ariketa
Egiaztatu {eq}`heco_e_pbar` ekuazioaren bi aldeak bat datozela,  $\bar{l}$ katearen batez besteko luzeraren adierazpena eraikiz.

```{dropdown} __Erantzuna__

Definizioaren arabera,

$$
\bar{l} := k_{\mathrm{B}}T\left(\frac{\ln\Delta}{\partial f}\right)_{T,N, \vert\mathbf{E}\vert} \; .
$$ (heco_e_lbar)

Goiko {eq}`heco_e_delta_3` partizio-funtzioaren medioz kalkuluak egindakoan, {eq}`heco_e_pbar` ekuazioko kortxeteen arteko adierazpena lortuko dugu.

```
**----------------------------------------------------**

Berrazterketa labur honi buru emateko, arestian aipatutako kontuari helduko diogu. Helize-unitateen batez besteko frakzioaren {eq}`fraction_N` ekuazioan $r$ magnitudearen definizio berria ordezkatuz,

$$
\frac{\overline{n}_H}{N} = \frac{\left[\frac{q_H}{q_C}\exp\frac{\left(l_H-l_C\right)\left(f+q\vert\mathbf{E}\vert\right)}{k_{\mathrm{B}}T}\right]^N}{1 + \left[\frac{q_H}{q_C}\exp\frac{\left(l_H-l_C\right)\left(f+q\vert\mathbf{E}\vert\right)}{k_{\mathrm{B}}T}\right]^N}
$$ (heco_e_nbar)

izango dugu. Agerikoa da, $l_H-l_C<0$ betetzen denez, helize-unitateen frakzioak modu esponentzialean joko duela zerorantz, $\mathbf{E}$ eremu elektrikoaren modulua handiagotzen dugun neurrian haril-fasea areagotuko da-eta. Ondorioz, haril-unitateen frakzioak gora egingo du, eta, aurreko arrazoinamendua dela bide, katearen batez besteko luzerak ere bai, katean zeharreko momentu dipolarra indartuz.

(agg_elek)=
### Agregatu lineala, $\mathbf{E}$ kanpo-eremuaren eraginpean

Azter dezagun azpian dugun {numref}`{number} irudia <agg_e>`.

```{figure} aggregate_efield.jpg
---
height: 225px
name: agg_e
---
Agregatu lineala ere zertxobait moldatuko dugu. Alde batetik, {numref}`{number} irudian <heco_e>` bezala, unitateek $\alpha$ polarizabilitatea dute. Alabaina, oraingoan berorietako bakoitza dipolo elektrikotzat hartuko dugu, $\mathbf{p_0}$ momentua duelarik; orobat, $\mathbf{p_0}$ bektoreak eta katea zeharkatzen duen ardatzak $\theta$ angelua osatuko dute. Horiek horrela, kanpotik $\mathbf{E}$ eremua jartzeak sorrarazten dituen ekarpenak aztertuko ditugu jarraian.
```

Esanak esan, orain ere $Q(T,N,\vert\mathbf{E}\vert)$ partizio-funtzio kanonikoa eraikitzeari ekin behar diogu. Horretarako, alde batetik, {numref}`{number} adibidean <mupt_linagg>` aurkeztutako ekarpenak hartuko ditugu gogoan: monomeroen $j(T)$ partizio-funtzio intrintsekoa, agregatuaren biraketa eta lehen auzokoen arteko elkarrekintza biltzen dituen {eq}`qagg` ekuazioa:

$$
Q_0(T,N) = c(T)\;N^3j(T)^N\;e^{-N\epsilon/k_{\mathrm{B}}T} \quad (N\geq 1) \; .
$$ (agg_e_q0)

Bestetik, ekarpen elektrikoa kalkulatu behar dugu, {numref}`{number} irudiari <agg_e>` so eginez. Agregatuak orotara $N$ unitate dituela aintzat hartuz, $\alpha$ polarizabilitatearen ondoriozko partizio-funtziorako ekarpena aurreko ataleko {eq}`u_alpha_heco` ekuaziotik eratorritako $Q_{\alpha}$ da. Aitzitik, unitateko $\mathbf{p_0}$ momentu intrintsekoa eta $\mathbf{E}$ kanpo-eremua ez direnez paraleloak, haiekin lotutako bigarren $Q_{p}$ gaiaren kalkulua ez da jada berehalakoa. Izan ere, orain 

$$
 U_{p_0}(\theta) = -Np_0\vert\mathbf{E}\vert \cos \theta
$$ (agg_e_u_p0)

dugu. 

Kontua da $\mathbf{p_0}$ bektorearen orientazioa hartu behar dugula aintzakotzat. Kanpo-eremurik jarri ezean, bektore horren edozein orientaziok probabilitate bera izango luke $(\theta,\varphi)$ koordenatuen espazioan. Hori dela eta, momentuaren orientazioa $\mathrm{d}\theta\;\mathrm{d}\varphi$ tartean aurkitzeko probabilitatea $\sin\theta\;\mathrm{d}\theta\;\mathrm{d}\varphi$ angelu solido diferentzialarekiko proportzionala da. Alabaina, kanpo-eremua ezarriz gero, $U_{p_0}(\theta)$ elkarrekintza-energia tarteko, orientazio jakin batzuk hobetsiko dira beste batzuen aldean. Hitzez esandakoa jarraian datorren partizio-funtzio normalizatuan islatuko dugu, hain zuzen, angelu solido diferentzialean zehar integratuz:

$$
 Q_{p_0} = \frac{\int_0^{2\pi}\mathrm{d}\varphi\int_0^{\pi}\mathrm{d}\theta\;\sin \theta \; e^{-U_{p_0}(\theta)/k_\mathrm{B}T}}{\int_0^{2\pi}\mathrm{d}\varphi\int_0^{\pi}\mathrm{d}\theta\;\sin \theta} = \frac{1}{2}\int_0^{\pi}\mathrm{d}\theta\;\sin \theta \exp\left(\frac{Np_0\vert\mathbf{E}\vert \cos \theta}{k_\mathrm{B}T}\right) = \frac{\sinh (Ny)}{Ny} \; ,
$$ (agg_e_q_p0)

non $y = p_0\vert\mathbf{E}\vert/(k_\mathrm{B}T)$ den.

$$
\\
$$

Jarraian datozen kalkuluak arintze aldera, _eremu txikiko limitean_ jardungo dugu hemendik aurrera $(\vert\mathbf{E}\vert \ll 1)$. Berebat, kontuan izan dezagun esku artean dugun agregatu lineala sistema _txikia_ dela, alegia, ez dihardugu $N\rightarrow \infty$ limitean; hartara, zilegi zaigu $Ny \ll 1$ hartzea. Beraz, $\sinh (Ny)$ funtzioaren seriea idatziz,


$$
\sinh(Ny) = \sum_{n=0}^{\infty}\frac{(Ny)^{2n+1}}{(2n+1)!} \; ,
$$ (agg_e_sinh)

eta, aurreko arrazoinamenduari atxikiz,

$$
\frac{\sinh(Ny)}{Ny} = 1 + \frac{N^2y^2}{6} + \mathcal{O}\left[(Ny)^4\right]
$$ (agg_e_approx)

hurbilketaz baliatuko gara aurrerantzean. Hori dela eta, partizio-funtzio _elektrikoa_ $Q_1 = Q_{\alpha} \cdot Q_{p_0}$ eran idatziz, eta, sistemaren partizio-funtzioa $Q(T,N,\vert\mathbf{E}\vert) = Q_0(T,N)\cdot Q_1(T,N,\vert\mathbf{E}\vert)$ dela aintzat hartuz,

$$
\boxed{Q(T,N,\vert\mathbf{E}\vert) \approx c(T)\;N^3j(T)^N\exp\left(-\frac{N\epsilon}{k_{\mathrm{B}}T}\right) \exp\left(\frac{N\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T}\right)\left[1 + \frac{1}{6}\left(\frac{Np_0\vert\mathbf{E}\vert}{k_\mathrm{B}T}\right)^2 \right]} \quad (N\geq 1) \; .
$$ (agg_q_tot)

$$
\\
$$

Bada, {eq}`agg_q_tot` ekuaziotik abiatuz, **multzo kanonikoan** aldagai termodinamikoak lortzeari ekingo diogu.

##### Ariketa

$(a)$ Kalkulatu $\widehat{\mu}$ eta $\mu$ potentzial kimikoak, baita $\mu^{(0)}$ limitea ere. Horiekin batera, idatzi banatze-potentzialak beteko duen ekuazioa.

```{dropdown} __Erantzuna__

$$
\left.\begin{array}{l}
\frac{\widehat{\mu}}{k_{\mathrm{B}}T} = -\frac{\ln Q}{N} = -\ln j + \frac{N-1}{N} \frac{\epsilon}{k_{\mathrm{B}}T} - \frac{\ln(\xi N^3)}{N} - \frac{\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T} - \frac{1}{N}\ln\left(1 + \frac{N^2y^2}{6}\right) \\\\
\frac{\mu}{k_{\mathrm{B}}T} = -\ln j + \frac{\epsilon}{k_{\mathrm{B}}T} - \frac{3}{N} - \frac{\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T} - \frac{2Ny^2}{6+N^2y^2}
\end{array}\right\}\underset{(N \rightarrow \infty)}{\boldsymbol{\longrightarrow}} \; \frac{\mu^{(0)}}{k_{\mathrm{B}}T} = -\ln j + \frac{\epsilon}{k_{\mathrm{B}}T} - \frac{\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T} 
$$ (agg_elek_mu)

$$
\frac{\mathscr{E}(T,N)}{k_\mathrm{B}T} = \frac{N(\widehat{\mu}-\mu)}{k_\mathrm{B}T} = -\frac{\epsilon}{k_\mathrm{B}T} + 3  -\ln(\xi N^3) - \ln\left(1+\frac{N^2y^2}{6}\right)  + \frac{2N^2y^2}{6+N^2y^2}
$$ (agg_elek_epsilon_k)

```


$(b)$ Kalkulatu entropiaren $S(T,N,\vert\mathbf{E}\vert)$ adierazpena. Bertatik, eskuratu $S^{(0)}$ ekuazio makroskopikoa zein $S^{(x)}(T,N,\vert\mathbf{E}\vert) = S(T,N,\vert\mathbf{E}\vert) - S^{(0)}$ gai gehigarria.

```{dropdown} __Erantzuna__

Aurreko $(a)$ atalean erdietsitako $\widehat{\mu}$ren ekuazioaren laguntzaz,

$$
 \frac{S(T,N,\vert\mathbf{E}\vert)}{k_\mathrm{B}} := -\frac{1}{k_\mathrm{B}}\left[\frac{\partial (\widehat{\mu}N)}{\partial T}\right]_{N,\vert\mathbf{E}\vert} = N\left(\ln j + T\frac{\mathrm{d}\ln j}{\mathrm{d}T}\right) + \color{red}\left\{ \color{black} \ln(\xi N^3)+1 + \ln\left(1+\frac{N^2y^2}{6}\right) + \frac{2N^2y^2}{6+N^2y^2} \color{red} \right\}\; \color{black} ,
$$ (agg_e_stn)

zeinean,

$$
\frac{S^{(0)}}{k_\mathrm{B}} = N\left(\ln j + T\frac{\mathrm{d}\ln j}{\mathrm{d}T}\right)
$$ (agg_e_s0)

eta

$$
\frac{S^{(x)}(T,N,\vert\mathbf{E}\vert)}{k_\mathrm{B}} = \ln(\xi N^3)+1 + \ln\left(1+\frac{N^2y^2}{6}\right) + \frac{2N^2y^2}{6+N^2y^2}
$$ (agg_e_sx_tn)

ekarpenak bereiz baititzakegu.

Bada, {eq}`agg_e_stn` eta {eq}`agg_elek_epsilon_k` ekuazioak parez pare jarriz gero, argiro hauteman daiteke ezen entropiarako ekarpen ez-lineal positibo gehienak banatze-potentzialaren gai positiboekin lotuta daudela, zeina berearekin. 

```

$(c)$ Eraiki $\overline{\vert\mathbf{p}\vert}$ magnitudea, {eq}`agg_e_approx` ekuazioko hurbilketara **jo barik**. Ondoren, kalkulatu lortutako adierazpenaren hurbilketa, $\mathcal{O}(\vert\mathbf{E}\vert^5)$ magnitude-ordenatik aurreragoko gaiak mespretxatuz.

```{dropdown} __Erantzuna__

Hasteko, $N\widehat{\mu}$ birkalkulatu behar dugu. Hala, baldin eta $\sinh(Ny)$ funtzioa bere horretan bagenerabil,

$$
\frac{N\widehat{\mu}}{k_{\mathrm{B}}T} = -\ln Q = -N\ln j + (N-1) \frac{\epsilon}{k_{\mathrm{B}}T} - \ln(\xi N^3) - \frac{N\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T} - \ln\left[\frac{\sinh (Ny)}{Ny}\right]
$$ (agg_elek_muhatN)

genuke. Bertatik, 

$$
\overline{\vert\mathbf{p}\vert} := -\left[\frac{\partial (\widehat{\mu}N)}{\partial\vert\mathbf{E}\vert}\right]_{T,N} = N\left[\alpha\vert\mathbf{E}\vert + p_0 \coth(Ny) \right] - \frac{k_{\mathrm{B}}T}{\vert\mathbf{E}\vert} \; .
$$ (agg_elek_p0)

Bada, $\coth{Ny}$ funtzioaren Taylorren seriea honako hau da:

$$
\coth(Ny) = \sum_{n=0}^{\infty} \frac{2^{2n}B_{2n}(Ny)^{2n-1}}{(2n)!} = \frac{1}{Ny} + \frac{Ny}{3} - \frac{(Ny)^3}{45} + \mathcal{O}[(Ny)^5] \quad,\quad 0 <\vert Ny\vert < \pi \; ,
$$

non $B_{2n}$ direlakoei Bernoulliren zenbakiak deritzen.

Hortaz, {eq}`agg_elek_p0` ekuazioarekin eragiketak eginez gero,

$$
\overline{\vert\mathbf{p}\vert} = N\alpha\vert\mathbf{E}\vert + \frac{1}{3}\frac{N^2p_0^2\vert\mathbf{E}\vert}{k_{\mathrm{B}}T} - \frac{1}{45}\frac{N^4p_0^4\vert\mathbf{E}\vert^3}{(k_{\mathrm{B}}T)^3} + \mathcal{O}(\vert\mathbf{E}\vert^5) \; .
$$ (agg_e_p_0_1)

```

**----------------------------------------------------**

##### Ariketa gehigarria: Maxwellen erlazioak

$(a)$ Idatzi, lehenik, sistema txikiaren ekuazioak, eta, hortik abiatuz, lortu $\mathrm{d}(\widehat{\mu}N)$ ekuazio diferentziala. Bertatik, eraiki $\left(\frac{\partial \mu}{\partial \vert\mathbf{E}\vert}\right)_{T,N}$ adierazpenari dagokion Maxwellen erlazioa, eta egiaztatu bi adierazpenak bat datozela.

```{dropdown} __Erantzuna__

Sistemaren barne-energiaren jatorrizko aldagaiak estentsiboak dira: entropia, partikula-kopurua eta momentu dipolar elektrikoa. Hori dela eta,

$$
\overline{E}(S,N,\mathbf{p}) = TS+\widehat{\mu}N + \mathbf{E}\cdot\mathbf{p} \; ,
$$ (agg_e_E)

eta,

$$
\mathrm{d}\overline{E}(S,N,\mathbf{p}) = T\mathrm{d}S+\mu\mathrm{d}N + \mathbf{E}\cdot\mathrm{d}\mathbf{p} \; .
$$ (agg_e_gibbs)


Aurreko bi ekuazioen bitartez, 

$$
\mathrm{d}(\widehat{\mu}N)(T,N,\vert\mathbf{E}\vert) = -S\mathrm{d}T+\mu\mathrm{d}N - \vert\mathbf{p}\vert \mathrm{d}\vert\mathbf{E}\vert\; .
$$ (agg_e_dmuhat)

Nabarmendu beharrekoa da, partizio-funtzio kanonikoa eraikitzen aritu garenean, {eq}`agg_e_q_p0` ekuazioaren bidez askatasun-gradu elektrikoa abiatu dugula. Bada, lorturiko emaitza $\mathbf{E}$ eremuaren moduluaren menpekoa da. Hori dela eta, ingurune-aldagaitzat modulua hartzea daukagu, bektorearen beraren ordez; hartara, haren konjugatua $\mathbf{p}$ momentuaren modulua izango da.


Bertatik eraikiko dugu eskatzen zaigun Maxwellen erlazioa:

$$
\left(\frac{\partial \mu}{\partial \vert\mathbf{E}\vert}\right)_{T,N} = \frac{\partial}{\partial \vert\mathbf{E}\vert} \left(\frac{\partial (\widehat{\mu}N)}{\partial N}\right)_{T,\vert\mathbf{E}\vert} \equiv \frac{\partial}{\partial N} \left(\frac{\partial (\widehat{\mu}N)}{\partial \vert\mathbf{E}\vert}\right)_{T,N} = -\left(\frac{\partial \vert\mathbf{p}\vert}{\partial N}\right)_{T,\vert\mathbf{E}\vert} \; .
$$ (agg_elek_maxwell_1)

Orain, $\mu$ potentzial kimikoaren adierazpen zehatzaren beharrean gaude. Hala, {eq}`agg_e_dmuhat` ekuazioaren medioz,

$$
\frac{\mu}{k_{\mathrm{B}}T} = -\ln j + \frac{\epsilon}{k_{\mathrm{B}}T} - \frac{2}{N} - \frac{\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T} - \frac{2Ny^2}{6+N^2y^2} - y\coth(Ny)
$$ (agg_elek_mu_zehatz)

lortuko dugu. Hala, {eq}`agg_elek_p0` eta {eq}`agg_elek_mu_zehatz` ekuazio-bikotearekin arituz,

$$
\left(\frac{\partial \mu}{\partial \vert\mathbf{E}\vert}\right)_{T,N} = -\left(\frac{\partial \vert\mathbf{p}\vert}{\partial N}\right)_{T,\vert\mathbf{E}\vert} = -\alpha \vert\mathbf{E}\vert - p_0\coth(Ny) + Np_0\frac{y}{\sinh^2(Ny)} \; .
$$ (maxwell_1)


```

$(b)$ Egin $(a)$ ataleko gauza berbera $\left(\frac{\partial \overline{\vert\mathbf{p}\vert} }{\partial T}\right)_{\vert\mathbf{E}\vert, N}$ adierazpenarekin.

```{dropdown} __Erantzuna__

Hasteko, $S(T, N, \vert\mathbf{E}\vert)$ entropiaren ekuazio zehatza lortu behar dugu, {eq}`agg_e_dmuhat` espresioari segituz:

$$
\frac{S(T,N,\vert\mathbf{E}\vert)}{k_\mathrm{B}} = N\left(\ln j + T\frac{\mathrm{d}\ln j}{\mathrm{d}T}\right) + \ln(\xi N^3)+ 2 + \ln\left(\frac{\sinh(Ny)}{Ny}\right) -Ny\coth(Ny) \; .
$$ (agg_elek_S_zehatz)

Hala, {eq}`agg_elek_p0` eta {eq}`agg_elek_S_zehatz` ekuazio-bikotearekin jardunez gero,

$$
\left(\frac{\partial \overline{\vert\mathbf{p}\vert} }{\partial T}\right)_{\vert\mathbf{E}\vert, N} = \left(\frac{\partial S}{\partial \vert\mathbf{E}\vert}\right)_{T,N} = -\frac{k_{\mathrm{B}}}{\vert\mathbf{E}\vert} + N^2\frac{p_0}{T}\frac{y}{\sinh^2(Ny)} \; .
$$ (maxwell_2)


```


**----------------------------------------------------**

$$
\\
$$

Ariketa honetan ere, aurreko beste zenbaitetan bezalaxe, azterketa pauso bat haratago eramango dugu, **multzo nanokanonikoan** murgilduz. Partizio-funtzio orokortua {eq}`agg_q_tot` partizio-funtziotik abiatuz eraikiko dugu:

$$
\Upsilon(T,\mu,\vert\mathbf{E}\vert) := 1+ \sum_{N=1}^{\infty}Q(T,N,\vert\mathbf{E}\vert)\;e^{\mu N/k_{\mathrm{B}}T} = 1 +c(T)\left[\sum_{N=1}^{\infty}N^3x^N +\frac{y^2}{6}\sum_{N=1}^{\infty}N^5 x^N\right] \; ,
$$ (agg_e_upsilon)

non, oraingoan, $x(T,\mu,\vert\mathbf{E}\vert) = j(T)\exp\left(\frac{-\epsilon + \mu }{k_{\mathrm{B}}T}\right)\exp\left(\frac{\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right)$ ordezkatu dugun.

Azpimarratu beharrekoa da ezen $\sinh(Ny)$ funtzioaren hurbilketara jotzeak biziki erraztuko duela $N$ magnitudean zeharreko batukariaren kalkulua. Izan ere, ohartu gaitezen batukari bietan $N$ren berreturak agertzen direla. Horrek seriearen garapena {eq}`upsilontn` ekuazioaren osteko argibideei jarraituz burutzea ahalbidetuko du. Gauzak horrela, 

$$
\boxed{\Upsilon = 1 + c(T)\left[\frac{x(x^2+4x+1)}{(x-1)^4} + \frac{y^2}{6}\frac{x^4+26x^3 + 66x^2+26x+1}{(x-1)^6}\right]}\quad, \quad \vert x\vert < 1 \; .
$$ (agg_e_upsilon_1)


Halaber, azpimarratzekoa da ezen, {numref}`{number} adibidean <mupt_linagg>` bezala, $x$ magnitudeak $x = e^{({\mu} - \mu^{(0)})/k_{\mathrm{B}}T}$ erlazioari eusten diola.


`````{admonition} Iradokizuna
:class: tip
Egiaztatu azkenengo esaldian aipatutakoa, {eq}`agg_elek_mu` ekuazio-sortako $\mu$ eta $\mu^{(0)}$ potentzialen adierazpenak eta aurrez definitutako $x(T,\mu,\vert\mathbf{E}\vert) = j(T)\exp\left(\frac{-\epsilon + \mu }{k_{\mathrm{B}}T}\right)\exp\left(\frac{\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right)$ erabiliz.
`````


Esanak esan, betiko lez, {eq}`agg_e_upsilon_1` partizio-funtzioaren bitartez multzo nanokanonikoan magnitude termodinamikoak eraikiko ditugu. Hasteko, ekuazioak laburtzeko, $P(N)$ probabilitate-funtzioa definituko dugu:

$$
P(N) = \frac{Q(T,N,\vert\mathbf{E}\vert)e^{\mu N/k_{\mathrm{B}}T}}{\Upsilon(T,\mu,\vert\mathbf{E}\vert)} \quad \Rightarrow \quad P(0) = \frac{1}{\Upsilon}
$$ (agg_e_pn)

Batez besteko momentu dipolarraren eta entropiaren adierazpenak areago trinkotzeko, arras mesedegarria izango zaigu lehenik $\overline{N}$ unitateen batez bestekoa kalkulatzea:

$$
\overline{N} := k_{\mathrm{B}}T\left(\frac{\partial\ln\Upsilon}{\partial \mu}\right)_{T,\vert\mathbf{E}\vert} = -cxP(0)\left[\frac{x^3+11x^2+11x+1}{(x-1)^5}+\frac{y^2}{6}\frac{x^5+57x^4+302(x^3+x^2)+57x+1}{(x-1)^7}\right]
$$ (agg_elek_nbar)

Bada, ekuazio horri atxikiz, eta eragiketak (kontu handiz) burutuz gero, hona heldu beharko genuke:

$$
\overline{\vert\mathbf{p}\vert}(T,\mu,\vert\mathbf{E}\vert) := k_{\mathrm{B}}T\left(\frac{\partial\ln\Upsilon}{\partial \vert\mathbf{E}\vert}\right)_{T,\mu} = \overline{N}\alpha\vert\mathbf{E}\vert + c(T)P(0)\frac{p_0^2\vert\mathbf{E}\vert}{3k_{\mathrm{B}}T}\frac{x(x^4+26x^3+66x^2+26x+1)}{(x-1)^6} \; ,
$$ (agg_elek_p_bar)

ekuaziora, alde batetik, eta, honako adierazpen adierazgarri honetara, bestetik:

$$
\frac{S(T,\mu,\vert\mathbf{E}\vert)}{k_{\mathrm{B}}} := T\left(\frac{\partial\ln\Upsilon}{\partial T}\right)_{\mu,\vert\mathbf{E}\vert} = \overline{N}\left(\ln j + T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T}\right)
$$
$$
+ \color{red}\left\{ \color{black} - \overline{N}\ln x - \ln P(0) + cP(0)\left(1-\frac{\epsilon}{k_{\mathrm{B}} T}\right)\frac{x(x^{2}+4x+1)}{(x-1)^{4}} \color{red} \right\} 
$$ 
$$
+ \color{red} \left\{ \color{black} cP(0)\left(\frac{p_0\vert\mathbf{E}\vert}{k_{\mathrm{B}} T}\right)^2 \left[\left(1-\frac{\epsilon}{k_{\mathrm{B}} T}\right)\frac{1}{6}-\frac{1}{3}\right]\frac{x(x^4+26x^3+66x^2+26x+1)}{(x-1)^6} \color{red} \right\} \color{black} \; .
$$ (agg_elek_s_nc)


Errepara bekio {eq}`agg_elek_s_nc` ekuazioari, gaiz gai. Bada, lehengoan bezala, $\overline{N}=N$ onartuz gero, aurreneko lerroan $S^{(0)}/k_{\mathrm{B}}$ gaia dugu. Hortik aurrera dagertzan gai guztiak tamaina finitukoak dira. Hala, bigarren lerroan, {eq}`stmuagg` ekuazioan eskuratutako gai gehigarria hauteman dezakegu. Alabaina, ohartu gaitezen adibide honetan definitu dugun $x$ aldagaiak, {numref}`{number} ataleko <mupt_linagg>` $ x(T,\mu)  =  je^{\left(\mu-\epsilon\right)/k_{\mathrm{B}}T}$ delakoaren aldean, $\alpha$ polarizabilitatearen ondoriozko $\exp\left(\frac{\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right)$ ekarpena daramala.

Amaitzeko, begien bistakoa da hirugarren lerroa ekarpen elektrikoari dagokiola bere osotasunean. Nabarmentzekoa da, halaber, $\vert\mathbf{E}\vert^2$ osagaia agertzen dela; hortaz, eremu txikiko limitean ekarpen hori baztergarria da funtsean, aurreko bi lerroetako gaiekiko. Nolanahi dela ere, oharteman dezagun ezen, {numref}`{number} atalean <mupt_linagg>` adierazi dugun $\epsilon \approx -2,3 \cdot k_{\mathrm{B}}T$ hartuko bagenu, ekarpena zeinuz positiboa litzatekeela; alegia, eskualde nanotermodinamikoan askatasun-gradu elektrikoa abian jartzeak entropia igo egingo du.

Jakina, kanpo-eremua kenduko bagenu, jatorrizko {eq}`stmuagg` ekuazioa berreskuratuko genuke.




(ising)=
### Isingen eredua


Adibide honetan aztergai izango dugun spin magnetikoz osaturiko sistemak ere abagune egokia eskainiko digu tamaina finituko efektuekin aritzeko. Hain zuzen, Nanotermodinamikaren tresneria sistema magnetikoetara eramanez, {numref}`{number} irudiko <ising_geziak>` ereduaren benetako oreka termikoa bilatzea dugu erronka, hura multzo estatistiko mikrokanonikoan, kanonikoan eta, azkenik, nanokanonikoan aztertuz; batik bat, entropiak multzoz multzo duen bilakaerari erreparatuko diogu.

(ising_arrows)=
```{figure} ising_geziak.png
---
width: 650px
name: ising_geziak
---
  Isingen dimentsio bakarreko katea $N$ spin bereizezinez osatuta dago. Beroriek $+\mathbf{u}_z$ eta $-\mathbf{u}_z$ noranzkoetan lerrokatu daitezke soilik. Garapenak errazteko, lehen auzokoen arteko $\pm J$ ez beste elkarrekintza-energiak baztertu egingo ditugu ({numref}`{number} irudia <ising_j>`).
```

Isingen sistemaren osagaietako bakoitzek barne-energiari bi ekarpen sorrarazten dizkiote: alde batetik, bi spinen arteko lerrokatze magnetikoaren araberako $\pm J$ delakoa; bestetik, berorietako bakoitzari $\mathbf{m}$ momentu magnetikoa esleituko bagenio, $\mathbf{B}$ kanpo-eremu magnetikoaren ondoriozko $-\mathbf{m}\cdot\mathbf{B}$ elkarrekintza ere izango genuke.

Aipatu beharrekoa da efektu biak batera aztertzea ez dela kontu erraza. Izan ere, partizio-funtzio kanonikoa eraikitzerakoan, _transferentzia-matrizearen_ metodora jo beharko dugu. Gainera, bertatik eskuratutako adierazpen luzeak ez dira erabilerrazak. Bada, horren ordez, analisia bi zatitian burutuko dugu, bakoitza bere aldetik. Lehenik, {numref}`{number} atalean <b0jnot0>`, lehen auzokoen arteko $\pm J$ lerrokatze-elkarrekintza izango dugu soilik aintzakotzat. Ondoren, {numref}`{number} atalean <j0bnot0>`, aurkakoa egingo dugu: sistemari $\mathbf{B}$ kanpo-eremua ezarriko diogu, eta spinek elkar ikusten ez dutela onartuko dugu $(J=0)$.



(b0jnot0)=
#### Isingen katea, $J$ elkarrekintza-energiaren eraginpean

Errepara diezaiogun {numref}`{number} irudiari <ising_j>`.

(ising_j)=
```{figure} ising_j.png
---
width: 650px
---
  Isingen spinek lerrokatze magnetikoa hobesten dutela onartuko dugu; alegia, konfigurazio horrek energia magnetikoa minimizatu egingo du. Hartara, noranzko bereko bi lehen auzokok $-J$ elkarrekintza-energia hautemango dute; aurkako noranzkoak erakutsiko balituzte, aldiz, lotze-energia $+J$ litzateke.
```

Arestian azaldutako hurbilketari jarraikiz, demagun sistema, egiatan, $N+1$ spin magnetikoz osatuta dagoela; hartara, orotara $N$ lotura izango ditu (azken kontu hori argitzeko, behatu goiko irudia). Haietatik $n_+$ aurkako noranzkodun spinen arteko loturak dira $(+J)$, eta, beraz, $N-n_+$ noranzko beredun spinen artekoak $(-J)$. Esaterako, {numref}`{number} irudiaren <ising_j>` kasuan, $N=10$ eta $n_+ = 7$. Hori dela eta, __multzo mikrokanonikoan__ $N$ eta $n_+$ aldagaiak finko dituen sistemaren barne-energia honela idatz dezakegu:

$$
  E(n_+, N) = n_+ J - (N-n_+)J = -(N-2n_+)J 
$$ (e_j)

Hurrengo pausoa, guztizko energiaren adierazpen horrekin bateragarriak diren mikroegoeren kopurua kalkulatzea da; hots, zenbat eratan sailka ditzakegun sistemaren spin osatzaile bereizezinen arteko $N$ loturak $n_+$ energia altuko eta $N-n_+$ energia baxuko sorten artean. Horretarako, oharteman dezagun {numref}`{number} irudiko <ising_j>` gezi guztiak alderantzikatzeak ez liokeela {eq}`e_j` adierazpenari eragingo, $n_+$ magnitudeak bere horretan bailirauke; alegia, mikroegoera bakoitza bi aldiz zenbatu beharra daukagu. Gauzak horrela,

$$
\Omega(n_+,N) = 2\cdot \frac{N!}{n_+!\;(N-n_+)!} \;\;\;\; .
$$ (omega_nj)

Segidan, entropiaren ekuazioa idatziko dugu, Stirlingen $\ln(n!)$ serieko aurreneko hiru gaiak ez beste guztiak baztertuz:

$$
\boxed{\frac{S(n_+,N)}{k_\mathrm{B}} = N\ln N - n_+\ln n_+ - (N-n_+)\ln(N-n_+) - \frac{1}{2}\ln\left[\frac{\pi}{2}n_+\left(1-\frac{n_+}{N}\right)\right]} \; .
$$ (s_ising_micro)

Gaineko {eq}`s_ising_micro` ekuazioak dioskunaren arabera, entropiak maximora joko du $n_+$ loturen kopuruaren erdia den kasuan, eta, hartara, sistemak magnetizazioa galtzean $(E = 0)$, hau da:

$$
S(n_+, N)_ {\text{max}} = S(N/2, N) = Nk_\mathrm{B}\ln 2 - \frac{1}{2}k_\mathrm{B}\ln\left(\frac{\pi}{8}N\right) 
$$ (s_max_micro)


Aurrerago, askatasun-graduak abiaraziz goazen heinean, azkenengo bi adierazpen horiek birkalkulatuko ditugu, emaitzen arteko erkaketak egite aldera.

$$
\\
$$

__Multzo kanonikora__ igaroko gara orain. Horretarako, $E(n_+)$ energia batukarian dagokion mikroegoeren sortarekin sartu, eta Boltzmannen faktorea aintzat hartuz, partizio funtzioa eraikiko dugu:

$$
Q(T, N) = \sum_{n_+ = 0}^{N}\Omega(n_+,N)\;e^{-E(n_+, N)/k_\mathrm{B}T}
$$

Goiko {eq}`e_j` eta {eq}`omega_nj` adierazpenak txertatu, eta, ekuazioak moldatzeaz bat, hona iritsiko gara:

$$
Q(T, N) = 2 \sum_{n_+ = 0}^{N} \frac{N!}{n_+!\;(N-n_+)!}\left(e^{- J/k_\mathrm{B}T}\right)^{n_+}\left(e^{ J/k_\mathrm{B}T}\right)^{N-n_+} = 2\left(e^{- J/k_\mathrm{B}T} + e^{ J/k_\mathrm{B}T}\right)^N 
$$ (q_ising)

```{admonition} Oharra
Azkenengo ekuazioa eraikitzeko, binomioaren identitatea erabili dugu:

$$
(x+y)^N = \sum_{k=0}^{N} \frac{N!}{k!\;(N-k)!}\; x^k\; y^{N-k}
$$
```
Bertatik, hasteko, sistemaren barne energiaren batez bestekoa kalkulatuko dugu, honako berdintza honi jarraituz:

$$
\overline{E} = \frac{\sum_{n_+ = 0}^{N}E(n_+,N) \; \Omega(n_+,N) \;e^{-E(n_+,N)/k_\mathrm{B}T}}{\sum_{n_+ = 0}^{N}\Omega(n_+,N)\;e^{-E(n_+, N)/k_\mathrm{B}T}} = k_{\mathrm{B}}T^2\frac{\partial}{\partial T}\ln Q 
$$ (bar_E_def)

#####  Ariketa

$(a)$ Kalkulatu $\overline{E}$ adierazpena.

```{dropdown} __Erantzuna__

$$
 \overline{E} = -NJ\tanh\frac{J}{k_{\mathrm{B}}T} 
$$ (bar_E)

```

$(b)$ Jarraian, kalkulatu Helmholtzen energia askea.

```{dropdown} __Erantzuna__

$$
A(T, N) = -Nk_{\mathrm{B}}T\left[\ln\left(2\cosh\frac{J}{k_{\mathrm{B}}T}\right) + \frac{1}{N}\ln 2\right] 
$$ (hehlmholtz_ising)

```

$(c)$ Aurreko bi ekuazioez baliatuz, eraiki entropiaren $S(T,N)$ adierazpena. Jarraian, kalkulatu maximoa, eta alderatu emaitza {eq}`s_max_micro` ekuazioarekin.

```{dropdown} __Erantzuna__

Multzo kanonikoan entropiak $S(T, N) =\left(\overline{E} - A\right)/T $ betetzen duela gogora ekarriz, hona ailegatuko gara:

$$
\boxed{S(T,N)
 = N\left[k_{\mathrm{B}}\ln\left(2\cosh\frac{J}{k_{\mathrm{B}}T}\right) - \frac{J}{T}\tanh\frac{J}{k_{\mathrm{B}}T}\right]  + k_{\mathrm{B}}\ln 2} 
$$ (s_ising_kan)

Entropiak maximoa du $\frac{J}{k_{\mathrm{B}}T} = 0$ denean. Egoera horretara honako bi kasu hauetan iritsi gaitezke: alde batetik, $J=0$ izatean, hau da, spinek elkar ez ikustean (elkarrekintzarik ez), eta, bestetik, $T\rightarrow \infty$ limitean. Horiek horrela, entropia

$$
S(T, N)_{\text{max}} = (N+1)k_{\mathrm{B}}\ln 2
$$ (s_max_kano)

genuke. Agerikoa da limite makroskopikoan $(N\rightarrow \infty)$ adierazpen horrek zein {eq}`s_max_micro` ekuazioak $Nk_{\mathrm{B}}\ln 2$ baliora joko luketela. Alabaina, eskualde nanotermodinamikoan tamaina finituko efektuak baztertuko ez bagenitu, $S(T, N)_{\text{max}}$ gailenduko litzateke $S(n_+, N)_ {\text{max}}$ adierazpenaren aurrean.

```

**----------------------------------------------------**

$$
\\
$$

Segidan, azterketa __multzo nanokanonikora__ eramango dugu.

#####  Ariketa

$(a)$ Idatzi $\Upsilon(T,\mu)$ partizio-funtzioaren adierazpena, {eq}`q_ising` ekuaziotik abiatuz. Ez egin kalkulurik.

```{dropdown} __Erantzuna__

Partizio-funtzio orokortua eraikitzerakoan, dakargun gogora sistemak lehen auzoko spinen arteko $N$ lotura dituela esan dugula arestian; hartara, sistemaren spinen kopurua $N+1$ da. Hori dela eta, batukariko Boltzmannen faktorean $N+1$ sartu beharko dugu, eta, beraz,

$$
\Upsilon (T,\mu)= \sum_{N=0}^{\infty} Q(T,N)\; e^{\mu(N+1)/k_\mathrm{B}T}
$$ (upsilon_ising)

ekuaziora helduko gara.

```

$(b)$ Ondoren, kalkulatu $\Upsilon(T,\mu)$ partizio-funtzio nanokanonikoa eta banatze-potentziala.



```{dropdown} __Erantzuna__

Aurreko $(a)$ ataleko espresioa garatuz eta moldatuz,

$$
\Upsilon (T,\mu)= 2\lambda \sum_{N=0}^{\infty}\left[\left(e^{J/k_\mathrm{B}T} + e^{- J/k_\mathrm{B}T}\right)\lambda\right]^N = \left(\frac{1}{2\lambda} -\cosh\frac{J}{k_\mathrm{B}T}\right)^{-1} \; ,
$$ (upsilon_ising_1)

non $\lambda = e^{\mu/k_{\mathrm{B}}T}$ ordezkatu dugun. Bertatik, banatze-potentzialaren adierazpena berehalakoa da:

$$
\mathscr{E}(T,\mu) = k_\mathrm{B}T\ln\left(\frac{1}{2\lambda} -\cosh\frac{J}{k_\mathrm{B}T}\right) 
$$(epsilon_ising)



```

$(c)$ Banatze-potentzialaren adierazpen horretatik, kalkulatu $S(T,\mu)$ eta $\overline{N}$. Ondoren, birmoldatu entropiaren ekuazioa $S(T,\overline{N}(\mu))$ adierazpenera heltzeko, eta maximizatu berori.

```{dropdown} __Erantzuna__

Hasteko,

$$
S(T,\mu) = -k_\mathrm{B}\ln\left(\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}\right) - \left(\frac{1}{2}\;\frac{\mu}{T}\;e^{-\mu/k_{\mathrm{B}}T} - \frac{J}{T}\;\sinh\frac{J}{k_\mathrm{B}T}\right)\cdot\left(\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}\right)^{-1} \; .
$$(s_tmu_ising)

Spinen kopuruaren batez bestekoa kalkulatzerakoan, adi ibili behar dugu, adierazpenean $\overline{N} + 1$ idatzi behar dugulako, alegia,

$$
\overline{N} + 1 = -\left(\frac{\partial \mathscr{E}}{\partial \mu}\right)_T =\frac{\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T}}{ \frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}} \; .
$$(bar_n_ising)

Horrenbestez, entropiaren adierazpena era honetan berridaztea daukagu:

$$
\boxed{S(T,\overline{N}(\mu)) = \overline{N}\left[ k_{\mathrm{B}}\ln\left(2\;\frac{\overline{N}+1}{\overline{N}}\;\cosh\frac{J}{k_{\mathrm{B}}T}\right) - \frac{J}{T}\;\tanh\frac{J}{k_{\mathrm{B}}T}\right] + k_{\mathrm{B}}\ln\left[2(\overline{N}+1)\right]} 
$$ (s_tbarn_ising)

Funtzio horrek ere maximoa du $\frac{J}{k_{\mathrm{B}}T} = 0$ puntuan:

$$
S(T, \overline{N}(\mu))_{\text{max}} = \overline{N}k_{\mathrm{B}}\ln \left(2\frac{\overline{N}+1}{\overline{N}}\right) + k_{\mathrm{B}}\ln\left[2(\overline{N}+1)\right] \; ,
$$ (s_max_nanokano)

zeinaren limite makroskopikoa, berriz ere, $\overline{N}k_{\mathrm{B}}\ln 2$ den.

```

**----------------------------------------------------**

Behin $S(n_+, N)_{\mathrm{max}}$, $S(T, N)_{\mathrm{max}}$ eta $S(T,\overline{N}(\mu))_{\mathrm{max}}$ adierazpenak kalkulatuz gero, adierazgarria litzateke hiruren arteko alderaketa egitea, sistemaren tamainaren araberako bilakaerari erreparatuz:

```{figure} ising_1_s.png
---
height: 350px
name: sn100
---
Lotura-unitateko entropia. Agerikoa da, alde batetik, sistema txikia denean multzo nanokanonikoak entropia handiagoa itzultzen duela. Bestetik, hiru kasuetan $S/N$ magnitudeak ez du izaera intentsiboa eskualde nanotermodinamikoan. Alabaina, limite makroskopikoan, adierazpenek bat egitera joko dute; halaber, intentsibotasuna berreskuratuko da. Kurbak eraikitzeko, {cite}`multiscale` artikuluan adierazten den $J/k_{\mathrm{B}}T = 1,45$ zenbakia erabili dugu.

```


Horrez gain, hainbatetan azpimarratu dugun legez, multzo nanokanonikoaren giltzarri da multzoak berak azpisistemetan banatzeko duen gaitasuna. Ildo horretatik, esku artean dugun sistemaren nanoeskalako oreka termikoa bilatu ahal izango dugu. Hain zuzen ere, banatze-potentzialari erreparatuz, $\mathscr{E}(T,\mu)=0$ ezartzeak bermatuko du azpisistema txikiz osaturiko multzo guztiz irekia banatzeari dagokion oreka-egoerara helduko dela, eragozpenik gabe. Izan ere, orekaranzko bidean $\overline{\mathscr{N}}$ aldaki-kopuruan aldakuntza espontaneoak gauzatuko dira.

Esanak esan, oreka egoeran aldakiko batez besteko partikula-kopurua eta entropia honako hauek ditugu:

$$
\overline{N}_{\mathrm{oreka}} = \cosh \frac{J}{k_{\mathrm{B}}T} \; ,
$$ (ising_nbar_oreka)

eta,

$$
S(T,\overline{N}(\mu))_{\mathrm{oreka}} = \overline{N} k_{\mathrm{B}}\ln\left(2 + 2\cosh\frac{J}{k_{\mathrm{B}}T}\right) - \overline{N}\frac{J}{T}\;\tanh\frac{J}{k_{\mathrm{B}}T} \; .
$$ (ising_s_oreka)

Horiek horrela, oroitu gaitezen {numref}`{number} atalaren <stabeps>` amaieran egindako ohartarazpenaz. Hain zuzen, nabarmendu beharrekoa da {eq}`s_ising_kan` eta {eq}`s_tbarn_ising` ekuazioetako entropien limite makroskopikoa ez datorrela bat {eq}`ising_s_oreka` ekuazioan ageri den adierazpenarekin. Beste hitzez esateko, ezberdintza hori dela bide, agerikoa da multzo nanokanonikoan erdietsitako oreka-egoera, zeinean banatze-potentziala hertsiki nulua den, ez dela inondik inora sistemaren egoera makroskopikoa. Egiazki, {eq}`epsilon_ising` ekuazioa {eq}`bar_n_ising` adierazpenaren laguntzaz berridatziz gero,

$$
\mathscr{E}(T,\mu) = -k_{\mathrm{B}}T \ln\left(\frac{\overline{N}}{\cosh\frac{J}{k_{\mathrm{B}}T}}\right)
$$ (ising_epsilon_1)

berdintzara helduko gara, zeinak argi adierazten baitu ezen, $\overline{N} \rightarrow \infty$ limitean, banatze-potentziala ez dela zerorantz gerturatuko, haren aurrean ekarpen lineal makroskopikoek nagusitasuna berreskuratuko duten arren.




(j0bnot0)=
#### Spin askeak, $\mathbf{B}$ kanpo-eremuaren eraginpean

Sistema beraren berrazterketa honetan, aurreko ataleko prozedura bertsua jarraituko dugu. Dena dela ere, eskuratuko ditugun emaitzek berebiziko adierazgarritasuna dutela ohartuko gara; ororen gainetik, {numref}`{number} adibideko <mupt_gi>` gas idealaren analisian eraikitako adierazpenekiko parekotasun nabaria antzemango diegu. 

Bada, egin diezaiogun so {numref}`{number} irudiari <ising_b>`.

(ising_1)=
```{figure} ising_b.png
---
width: 700px
name: ising_b
---
Eman dezagun $N$ spinak soilik $\mathbf{B} = B \mathbf{u_z}$ kanpoko eremu magnetikoarekin daudela elkarrekintzan. Hortaz, spinei $\mathbf{m} = \pm m \mathbf{u_z}$ momentu magnetikoa esleituz gero, sistemaren barne-energia $E = (N-2n_+)mB$ izango dugu, non $n_+$ eremuaren noranzko berean $(+z)$ lerrokatuta dauden spinen kopurua den.

```

Irudiko azalpenak aintzakotzat hartuz, __multzo mikrokanonikoan__ $E(n_+,N)$ barne-energia finkatuta duen makroegoerarekin bateragarriak diren mikroegoeren kopurua koefiziente binomialak emango digu, beste behin:

$$
\Omega(n_+,N) = \frac{N!}{n_+! (N-n_+)!} \; .
$$ (ising_b_omega)

Stirling-en $\ln N! \approx N\ln N - N + \frac{1}{2}\ln (2\pi N)$ hurbilketara joz gero, entropian soilik gai ez-lineal bakarra mantenduko dugu, zeina $\mathscr{E}(n_+, N)$ banatze-potentzialak zehaztuko duen. Hortaz,

$$
\boxed{\frac{S(n_+,N)}{k_{\mathrm{B}}} \approx N\ln N - n_+ \ln n_+ - (N-n_+)\ln(N-n_+) - \frac{1}{2}\ln\left[2\pi n_+\left(1-\frac{n_+}{N}\right)\right]} \; ,
$$ (ising_b_s_mc)

eta,

$$
\mathscr{E}(n_+, N) \approx \frac{1}{2} k_{\mathrm{B}}T \ln\left[2\pi n_+\left(1-\frac{n_+}{N}\right)\right] > 0 \; , \quad n_+ <N \; .
$$ (ising_b_epsilon_mc)

Aurreko bi ekuazioen bitartez hauteman daitekeen legez, banatze-potentzial positiboak entropiaren beherakada dakar. Hain zuzen, {numref}`{number}. ataleko <stabeps>` azalpenak gogora ekarriz, berorrek multzo mikrokanonikoa azpisistema txikiagoetan banatzea eragozten du, aldaki-kopurua txikituz, eta, horrekin batera, spin osatzaileen bereizezintasuna areagotuz.

$$
\\
$$

Aurrera eginez, azpisistemak ukipen termikoan jarri eta __multzo kanonikora__ egingo dugu jauzi. Horretarako, beste behin onartu behar dugu $n_+$ magnitudea jada ez dela konstante mantenduko. Hala, mikroegoeren sorta bakoitza $E(n_+, N)$ barne-energiaren baitan dagoen $e^{-E(n_+, N)/k_{\mathrm{B}}T}$ Boltzmannen faktorearekin haztatuz, $Q(T, N)$ partizio-funtzioa eraikiko dugu:

$$
Q(T, N) = \sum_{n_+=0}^N \Omega(n_+,N)\;e^{-(N-2n_+)mB/k_{\mathrm{B}}T} = \left[2\cosh\frac{mB}{k_{\mathrm{B}}T}\right]^N 
$$ (ising_b_q)

Bertatik, $A(T,N) = -Nk_{\mathrm{B}}T\ln\left[2\cosh\frac{mB}{k_{\mathrm{B}}T}\right]$ eta $\overline{E} = -NmB\tanh\frac{mB}{k_{\mathrm{B}}T} $, eta, horien bidez,

$$
\boxed{S(T,N)
 = N\left[k_{\mathrm{B}}\ln\left(2\cosh\frac{mB}{k_{\mathrm{B}}T}\right) - \frac{mB}{T}\tanh\frac{mB}{k_{\mathrm{B}}T}\right]} \; .
$$ (ising_b_s_c)

Oraingo honetan, entropiaren gai guztiak $N$ magnitudearekiko linealak dira. Izan ere, {eq}`ising_b_q` ekuazioan mikroegoera guztietan zeharreko batukaria kalkulatzean, faktorialak desagerrarazi egin ditugu. Hori dela eta, goian definitu dugun $A(T, N)$ Helmholtzen energia askearen adierazpena lehen ordenako funtzio Euler-homogeneoa da (erabat zehatza), eta, hartara, $\mathscr{E}(T, N) = 0$ izango dugu.

$$
\\
$$

Azterketari buru emateko, abiarazteko dagoen askatasun-gradu kimikoa martxan ipini, eta, __multzo nanokanonikoan__ entropia berreraikiko dugu. Hala, $x(T,\mu) = 2 \cosh\frac{mB}{k_{\mathrm{B}}T}\;e^{\mu /k_{\mathrm{B}}T}$ ordezkatuz, 

$$
\Upsilon (T,\mu) = \sum_{N=0}^\infty x^N = \frac{1}{1-x} \;, \quad \vert x \vert < 1 
$$ (ising_b_upsilon)

izango dugu partizio funtzio orokortua. Bertatik,

$$
\overline{N} = \frac{x}{1-x} \; ,
$$ (ising_b_nbar)


$$
\mathscr{E}(T,\mu) = k_{\mathrm{B}}T\ln(1-x) = -k_{\mathrm{B}}T\ln\left(\overline{N}+1\right) \; ,
$$ (ising_b_epsilon_tmu)

eta,

$$
\boxed{S(T,\overline{N}(\mu)) = \overline{N}\left[ k_{\mathrm{B}}\ln\left(2\cosh\frac{mB}{k_{\mathrm{B}}T}\right) - \frac{mB}{T}\;\tanh\frac{mB}{k_{\mathrm{B}}T} + \ln\left(\frac{\overline{N}+1}{\overline{N}}\right)\right] + k_{\mathrm{B}}\ln\left(\overline{N}+1\right)} \; .
$$ (ising_b_s_tmu)


Bada, {eq}`ising_b_s_c` ekuazioko $S(T,N)$ adierazpenaren aldean, $\mathscr{E}(T,\mu)$ banatze-potentzial negatiboak entropiari ekarpen positiboa gaineratu dio ($\overline{N}>0$ da eta). Emaitzak ikusita, nabarmena da aztergaitzat dugun elkarrekintzan ez dauden spinek osaturiko sistemaren eta {numref}`{number} atalean <mupt_gi>` aurkeztutako gas idealaren jokamoldeen arteko parekotasuna. Kasu horretan bezalaxe, banatze-potentzial negatibo eta ez-estentsiboaren ekarpenak partikulako entropiaren maximizazioa ahalbidetuko du $\overline{N} \rightarrow 0$ limitean, alegia, multzoaren banatzea areagotuz doan heinean (dakargun gogora {eq}`gi_tpmu_s_n` ekuazioa). Horretarako, jakina, azpisistemek euren tamaina inolako kanpo-galarazpenik gabe aldatzeko gai izan beharko dute. Azken eskakizun hori soilik multzo estatistiko nanokanonikoak beteko du.