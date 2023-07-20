(osagarri)=
## Adibide osagarriak

(mupt_sphagg)=
### Agregatu esferikoa

Jarraian aurkeztuko dugun analisiak {numref}`{number} azpiataleko <mupt_linagg>` adibidearen tankera du. Oraingoan, aitzitik, unitate-osatzaileen biraketa barik, gainazal- eta kurbadura-efektuen eraginari erreparatuko diogu. Horiek horrela, aztergai izango dugun sistema $N$ monomeroz osaturiko agregatu esferiko konprimaezina da; hartara, askatasun-gradu mekanikoa ez dugu aintzat hartuko; beraz, azterketa $(T,N)$ ingurune-aldagaien bidez jarriko dugu abian. Agregatu linealaren kasuan bezalaxe, unitateei $j(T)$ partizio-funtzio intrintsekoa esleituko diegu. Horrez gain, $a(T)N^{2/3}$ gainazaleko energia askearen ekarpena kontuan izango dugu ($a>0$). Aipatzekoa da $a(T)$ magnitudea $\gamma$ gainazal-tentsioarekiko proportzionala dela. Berebat, formulazioa osatze aldera, gainazal esferikoaren kurbaduraren ondoriozko gainazal-tentsioaren aldakuntza ere hartuko dugu aintzat. Hark $b(T)N^{1/3}$ ekarpena gaineratuko du ($b>0$). Hill-en liburuan {cite}`hill` zenbaitetan ageri da adibide hau. Bada, esan beharrekoa da horietan guztietan kurbaduraren eragina baztertu egiten dela. Guk, azterketa honetan, gainontzeko ekarpenekiko zuzenketa txikitzat joko dugu, $b \rightarrow 0^{+}$ hartuz. Hori onartzeak nabarmenki arinduko du $\Upsilon (T,\mu)$ partizio-funtzioa kalkulatzeko bidea.

Lehenbizi, $Q(T,N)$ partizio-funtzio kanonikoa eraikiko dugu, hurbilketarik gabe.

$$
Q(T,N) = j(T)^N\;\exp\left[{\frac{-a(T)N^{2/3}}{k_{\mathrm{B}}T}}\right]\exp\left[{\frac{-b(T)N^{1/3}}{k_{\mathrm{B}}T}}\right]
$$ (qagg_sph)

Bertatik, $Q=e^{-\widehat{\mu}N/k_{\mathrm{B}}T}$ erlazioa gogora ekarriz, potentzial kimiko diferentziala eta integrala eskuratuko ditugu, baita banatze-potentziala ere:

$$
\left.\begin{array}{l}
\widehat{\mu}=-k_{\mathrm{B}}T\ln j + N^{-1/3}\;a(T) + N^{-2/3}\;b(T)\\\\
\mu=-k_{\mathrm{B}}T\ln j +\frac{2}{3} N^{-1/3}\;a(T) + \frac{1}{3} N^{-2/3}\;b(T)
\end{array}\right\}\underset{(N \rightarrow \infty)}{\boldsymbol{\longrightarrow}} \; \mu^{(0)}(T) = -k_{\mathrm{B}}T\ln j \; ,
$$ (sph_agg_mu)

$$
\mathcal{E} = N\left(\widehat{\mu}-\mu\right) = \frac{1}{3}N^{2/3}a(T) + \frac{2}{3}N^{1/3}b(T) \; .
$$ (sph_epsilon_c)

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
$$ (s_sph_agg_tn)

$$
\bar{E}(T,N) = \widehat{\mu}N + TS = Nk_{\mathrm{B}}T^2\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} + N^{2/3}\left(a -T\frac{\mathrm{d}a}{\mathrm{d}T}\right) + N^{1/3}\left(b -T\frac{\mathrm{d}b}{\mathrm{d}T}\right) \; .
$$(bar_e_tn_sph)

Orain __multzo nanokanonikora__ eramango dugu azterketa. Definizioaren adierazpena {eq}`excess_mu` ekuazio-bikotearen bidez berridatziko dugu, hain zuzen, $\widehat{\mu}^{(x)}$ eta $\mu^{(x)}$ gaiak agerrarazteko.

$$
\Upsilon(T,\mu) = \sum_{N=0}^{\infty}e^{-\widehat{\mu}N/k_{\mathrm{B}}T}e^{{\mu}N/k_{\mathrm{B}}T} = \sum_{N=0}^{\infty}e^{-\widehat{\mu}^{(x)}N/k_{\mathrm{B}}T}e^{{\mu^{(x)}}N/k_{\mathrm{B}}T}
$$ (upsilon_sph)


Kontuan izan dezagun {eq}`upsilon_sph` ekuazioan $\mu^{(x)}$ positiboa izateak seriearen dibergentzia lekarkeela, $N$ handietarako $e^{{\mu^{(x)}}N/k_{\mathrm{B}}T}$ esponentziala gailenduko bailitzateke. Beraz, $\mu^{(x)} \leq 0$ inposatu beharko dugu konbergentzia bermatzeko (ekar dezagun gogora $a$ eta $b$ positiboak direla, eta, ondorioz, $\widehat{\mu}^{(x)}$ ere bai). Izan ere, ondoren ikusiko dugunez, $\mu^{(x)} > 0$ edo $\mu > \mu^{(0)}(T)$ izatearen ondoriozko dibergentziak $\bar{N} = \infty$ ekarriko du. Nabarmentzekoa da ezen kasu honetan $\mu$ aldagaia ez dela arestian kalkulatutako {eq}`sph_agg_mu` ekuazioan ageri dena, sistemari egokitutako konstantea baizik. Bada, segidan azalduko dugunez, konbergentzia bermatze aldera $\mu \rightarrow \mu^{(0)}$ baldintza inposatu beharko dugu. Aurrera egin baino lehen, komenigarria da honako notazio hau sartzea:

$$
\delta(T,\mu) = \frac{-\mu^{(x)}}{k_{\mathrm{B}}T} = \frac{\mu^{(0)}-\mu}{k_{\mathrm{B}}T} \quad , \quad \alpha(T) = \frac{a(T)}{k_{\mathrm{B}}T} \quad , \quad \beta(T) = \frac{b(T)}{k_{\mathrm{B}}T} \; .
$$

Gauzak horrela, kalkuluei ekin aurretik, bada argitu beharreko beste hainbat kontu. Izan ere, aurreko paragrafoko azalpenei jarraituz, aztergai dugun agregatuaren tamaina zentzuzkoa izan dadin, $\delta \rightarrow 0^{+}$ limitera jo beharko dugu, hark mantenduko baikaitu dibergentziatik urrun. Bestalde, $aN^{2/3}$ gainazal energia askea errealista izango da soilik $N$ aski handietarako (adibidez, $N>20$). Hori dela eta, {eq}`upsilon_sph` ekuazioan, $N$ aldagaiarekiko batukariaren ordez, integrala kalkulatuko dugu. Aipatzekoa da eredu hau $N$ txikietarako desegokia izanagatik, $\bar{N}$ handi samarra denean errorea ez dela hain esanahitsua izango. Bukatzeko, arestian kurbadura-efektuen inguruan esandakoaren harira, $\beta \rightarrow 0^{+}$ limitea erabiltzea ere zilegi zaigu. Azaldutako hori guztia jarraian datorren partizio-funtzioaren adierazpen moldatuan islatuko dugu:

$$
\Upsilon (T,\mu) \approx \int_0^\infty \mathrm{d}N\;\left[1-\delta(T,\mu) N\right] \; e^{-\alpha(T) N^{2/3}}\left[1-\beta(T) N^{1/3}\right] \; .
$$ (upsilon_sph_int)

```{dropdown} __Oharra__
Atal honetan zehar azalduko diren integralen kalkuluak arras luzeak eta konplexuak dira. Esaterako, {eq}`upsilon_sph_int` ekuazioan ageri denak hiru aldagai-aldaketa egitea eskatzen du. Inork kalkuluei ekiteko ausardia balu, jakin beza integral ez-mugatu horren soluzioa honako hau dela:

$$
 \dfrac{\mathrm{e}^{-{\alpha}N^\frac{2}{3}}\cdot\left(\left(45\sqrt{{\pi}}\,{\alpha}^3{\beta}{\delta}+12\sqrt{{\pi}}\,{\alpha}^5\right)\operatorname{erf}\left(\sqrt{{\alpha}}\sqrt[3]{N}\right)\,\mathrm{e}^{{\alpha}N^\frac{2}{3}}-24{\alpha}^\frac{11}{2}{\beta}{\delta}N^\frac{5}{3}+24{\alpha}^\frac{11}{2}{\delta}N^\frac{4}{3}-60{\alpha}^\frac{9}{2}{\beta}{\delta}N+\left(48{\alpha}^\frac{9}{2}{\delta}+24{\alpha}^\frac{11}{2}{\beta}\right)N^\frac{2}{3}+\left(-90{\alpha}^\frac{7}{2}{\beta}{\delta}-24{\alpha}^\frac{11}{2}\right)\sqrt[3]{N}+48{\alpha}^\frac{7}{2}{\delta}+24{\alpha}^\frac{9}{2}{\beta}\right)}{16{\alpha}^\frac{13}{2}}
$$


Guk, jakina, sistemaren azterketa nanotermodinamikoa burutzea dugunez xedea, ez gara inondik inora horrelako sasiarteetan sartuko.

```


Integral mugatuaren emaitza honako hau da:

$$
\Upsilon (T,\mu) = \frac{\pi^{1/2}\left(45\delta\beta+12\alpha^2\right)}{16\alpha^{7/2}} - \frac{3\beta}{2\alpha^2} - \frac{3\delta}{\alpha^3} \; \underset{(\delta \rightarrow 0^{+})}{\boldsymbol{\longrightarrow}} \; \frac{3\pi^{1/2}}{4\alpha^{3/2}} - \frac{3\beta}{2\alpha^2}
$$ (upsilon_sph_good)

Hortik, hasteko, batez besteko $\bar{N}$ magnitudea eskuratuko dugu. Horretarako, oharteman dezagun $\delta(T,\mu)$ magnitudearekiko deribatu beharra daukagula. Beraz, {eq}`upsilon_sph_good` ekuazioko ezkerraldeari erreparatu beharko diogu; alegia

$$
 \bar{N} := -\left(\frac{\partial \mathcal{E}}{\partial\mu}\right)_T = \left(\frac{\partial\ln\Upsilon}{\partial\frac{\mu}{k_{\mathrm{B}}T}}\right)_T = \left(\frac{\partial\ln\Upsilon}{\partial\delta}\right)_{\alpha,\beta}\left(\frac{\partial\delta}{\partial\frac{\mu}{k_{\mathrm{B}}T}}\right)_T = \frac{1}{\Upsilon}\left(\frac{3}{\alpha^3}-\frac{45\pi^{1/2}\beta}{16\alpha^{7/2}}\right)\; .
$$ (bar_n_sph)

Aipagarria da ezen $\mu \rightarrow \mu^{(0)}(T)$ limitean dihardugunez, $\bar{N}$ tenperaturaren menpeko funtzioa dela bakarrik. Era berean, entropiaren eta barne-energiaren adierazpenak idazte aldera baliagarriak izango zaizkigu $\overline{N^{2/3}}$ eta $\overline{N^{1/3}}$ batez bestekoak ere idaztea. Hortaz, $P(N)$ probabilitate-funtzioa erabili beharko dugu, hain zuzen:

$$
P(N) = \frac{e^{-\alpha N^{2/3}}e^{-\beta N^{1/3}}}{\Upsilon}\approx \frac{e^{-\alpha N^{2/3}}\left(1-\beta N^{1/3}\right)}{\Upsilon} \; .
$$ (p_n_sph)

Horiek horrela, emaitza hauetara ailegatuko gara:

$$
\overline{N^{2/3}} = \int_0^{\infty}\mathrm{d}NP(N)\;N^{2/3} = \frac{1}{\Upsilon}\left(\frac{9\pi^{1/2}}{8\alpha^{5/2}}-\frac{3\beta}{\alpha^3}\right) \; ,
$$ (bar_n23_sph)

$$
\overline{N^{1/3}} = \int_0^{\infty}\mathrm{d}NP(N)\;N^{1/3} = \frac{1}{\Upsilon}\left(\frac{3}{2\alpha^2}-\frac{9\pi^{1/2}\beta}{8\alpha^{5/2}}\right) \; .
$$ (bar_n13_sph)

Behin ekuaziook lortuz gero, barne-energiaren batez bestekoaren adierazpena berehalakoa da, haren definizioari jarraitzen badiogu. Errepara bekio {eq}`bar_e_tmu_sph_def` ekuazioari.

$$
\bar{E}(T,\mu) =\frac{\sum_E\sum_N\Omega(E,N)\;e^{-E/k_{\mathrm{B}}T}e^{\mu N/k_{\mathrm{B}}T}}{\Upsilon(T,\mu)} = \frac{\sum_N \bar{E}(T,N)\;Q(T,N)\;e^{\mu N/k_{\mathrm{B}}T}}{\Upsilon(T,\mu)}
$$ (bar_e_tmu_sph_def)

Lehenik, $E(S,N)$ energian barreneko batez bestekoa kalkulatu behar dugu, multzo mikrokanonikoko azterketari dagokion $\Omega(E,N)$ funtzioa erabiliz. Bertatik eskuratuko dugu $\bar{E}(T,N)$ adierazpena. Bada, haren $N$ magnitudean zeharreko batez bestekoak itzuliko digu $\bar{E}(T,\mu)$ magnitudea. Hala, {eq}`bar_e_tn_sph` ekuazioko $N$, $N^{2/3}$ eta $N^{1/3}$ funtzioak  {eq}`bar_e_tmu_sph_def` ekuazioaren eskuinaldeko seriean ordezkatuz, haien batez bestekoak lortuko ditugu; hartara, barne-energiaren batez bestekoaren adierazpen eraldatua

$$
\bar{E}(T,\mu) = \bar{N}k_{\mathrm{B}}T^2\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} + \overline{N^{2/3}}\left(a -T\frac{\mathrm{d}a}{\mathrm{d}T}\right) + \overline{N^{1/3}}\left(b -T\frac{\mathrm{d}b}{\mathrm{d}T}\right)
$$ (bar_e_tmu_sph)

izango da. Beste behin, {eq}`bar_e_tn_sph` eta {eq}`bar_e_tmu_sph` bikoteak aditzera ematen duenez, kasuan kasuko ingurune-aldagaiek sistema txikien propietateei erasaten diete; izan ere, $N=\bar{N}$ aukeratzen badugu ere, barne-energiaren bi adierazpenak ez dira bat etorriko, $N^{2/3}$ eta $N^{1/3}$ magnitudeen inguruko fluktuazioak tarteko. Hain zuzen, $\bar{N}^{2/3}\neq \overline{N^{2/3}}$ eta $\bar{N}^{1/3}\neq \overline{N^{1/3}}$ betetzen da.

Banatze-potentziala {eq}`bar_n_sph` ekuazioaren laguntzaz trinkotuko dugu:

$$
\mathcal{E} = -k_{\mathrm{B}}T\ln\left[\frac{1}{\bar{N}}\left(\frac{3}{\alpha^3}-\frac{45\pi^{1/2}\beta}{16\alpha^{7/2}}\right)\right] \; .
$$ (sph_epsilon_nc)

Horixe da $S(T,\mu)$ entropia eraikitzeko behar dugun azkenengo osagaia. Izan ere, sistema txikiari dagokion {eq}`e_small` ekuazioa adibide jakin honetan honela berridatziko dugu: $\bar{E} = TS + \mu^{(0)}N + \mathcal{E}$. Bada, oroitu gaitezen, alde batetik, askatasun-gradu mekanikoaren ekarpena baztertu dugula hasieratik; bestetik, potentzial kimikoaren balioa $\mu^{(0)}$ limitea da. Horrenbestez, ekuaziotik $S$ askatuz,

$$
\boxed{S(T, \mu) =  \bar{N}k_{\mathrm{B}}\left(\ln j + T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T}\right) - \overline{N^{2/3}}\frac{\mathrm{d}a}{\mathrm{d}T} - \overline{N^{1/3}}\frac{\mathrm{d}b}{\mathrm{d}T} + k_{\mathrm{B}}\ln\left[\frac{1}{\bar{N}}\left(\frac{3}{\alpha^3}-\frac{45\pi^{1/2}\beta}{16\alpha^{7/2}}\right)\right] + \overline{N^{2/3}}\frac{a}{T} + \overline{N^{1/3}}\frac{b}{T}}
$$ (s_sph_agg_tmu)

da multzo nanokanonikoak itzuliko digun entropia. So egin diezaiogun hari; eta, aurrez hainbatetan egindakoaren harira, ipin dezagun parez pare {eq}`s_sph_agg_tn` adierazpenarekin.

Bada, $S(T,\mu)$ ekuazioan hiru gai gehigarri azaltzen dira. Agerikoa da azkenengo biek (positiboak) $N^{2/3}$ eta $N^{1/3}$ magnitudeen inguruko fluktuazioen ondoriozko entropiaren gorakadaren erantzuleak direla. Edonola ere, banatze-potentzialarekin lotutako azken-hirugarren gaiak azterketa sakonagoa eskatzen du. Izan ere, logaritmoaren barnean $\bar{N}$ magnitudearekiko alderantzizko funtzioa agertzen da; are gehiago, parentesi artean dagoena positiboa da. Hori dela eta, $\bar{N}$ handitu ahala, ekarpen hori are negatiboagoa bilakatuko da, guztizko entropia jaitsiz. Badirudi efektu hori kurbaduraren ekarpenak aintzat hartzearen ondorio zuzena dela. Edonola ere, gogora dezagun $\alpha \gg \beta$ onartu dugula hasieratik; hortaz, $\beta/\alpha^{7/2} \approx 0$ beteko da. Gauzak horrela, zilegi zaigu, gai horretan, behintzat, kurbadura-efektuak baztertzea. Hala, $\beta \rightarrow 0$ limitea hartuz, {eq}`bar_n_sph` ekuazioa, banatze-potentziala zein harekin lotutako entropiaren gaia berridatziko ditugu:

$$
\bar{N} \approx \frac{4}{\pi^{1/2}\alpha^{3/2}} \; ,
$$ (bar_n_sph_approx)

$$
\mathcal{E} \approx -k_{\mathrm{B}}T\ln\left(\frac{3\pi\bar{N}}{16}\right) \; ,
$$ (sph_epsilon_nc_approx)

$$
k_{\mathrm{B}}\ln\left[\frac{1}{\bar{N}}\left(\frac{3}{\alpha^3}-\frac{45\pi^{1/2}\beta}{16\alpha^{7/2}}\right)\right] \approx k_{\mathrm{B}}\ln\left(\frac{3\pi\bar{N}}{16}\right) > 0 \; .
$$ (approx)

Erabilitako limiteak gai arazotsu horren benetako izaera jarri du agerian; izatez, $N$ partikula-kopuruaren inguruko fluktuazioak hartzen ditu aintzakotzat, entropia handituz.

Aipagarria da ezen $N \gg N^{2/3}, \; N^{1/3}$ eta $\bar{N} \gg \overline{N^{2/3}}, \; \overline{N^{1/3}}, \; \ln \bar{N}$ betetzen den horretan, {eq}`s_sph_agg_tn` zein {eq}`s_sph_agg_tmu` adierazpenak bat datozela {numref}`{number} ataleko <mupt_linagg>` agregatu linealaren kasuari dagozkion emaitzekin, alegia:

$$
\boxed{\begin{gathered}
    (a) \quad S(T,\mu) > S(T,N) \\
    \\
   (b) \quad  \frac{S(T,\mu)}{\bar{N}k_{\mathrm{B}}}\equiv \frac{S(T,N)}{Nk_{\mathrm{B}}} = \frac{\mathrm{s}^{(0)}}{k_{\mathrm{B}}} = \ln j + T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} \quad (\bar{N},N\rightarrow\infty)\\
   \\
   (c) \quad \frac{\bar{E}(T,N)}{N} \equiv \frac{\bar{E}(T,\mu)}{\bar{N}} = \mathrm{e}^{(0)} = k_{\mathrm{B}}T^2\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} \quad (\bar{N},N\rightarrow\infty)
\end{gathered}}
$$

```{admonition} Oharra
Agregatu linealaren adibidean, orain ez bezala, lehen auzoko unitateen arteko $\epsilon$ elkarrekintza-energia kontuan izan genuen. Hori dela eta,  barne-energia $N\left(k_{\mathrm{B}}T^2\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} + \epsilon\right)$ da egiatan.
```

Badirudi, hortaz, limite makroskopikoan agregatua lineala edo esferikoa izateak ez duela inolako eraginik barne-energia eta entropia bezalako funtzio termodinamikoetan. Hain zuzen, sistemaren __formari__ dagozkion ekarpenak azaleratzeko, nanotermodinamikara jo beharko dugu ezinbestean.

#### Ariketa
Ariketa honen helburua orain arte burututako analisi orokorra $b(T) = 0$ limitean aztertzea da. Hala, kurbatura-efektuak erabat baztertuz eta, hartara, $a(T)N^{2/3}$ gainazalaren ekarpena soilik aintzat hartuz, Hill-en liburuko emaitzak berreskuratuko ditugu bidenabar {cite}`hill`.

$(a)$ Dagoeneko kalkulatu dugu banatze-potentzialak baldintza horietan betetzen duen adierazpena ({eq}`sph_epsilon_nc_approx` ekuazioa). Egin gauza bera honako magnitudeekin: $\widehat{\mu},\;\mu,\; S(T,N),\;\bar{E}(T,N),\;\Upsilon(T,\mu),\;\bar{N},\;\bar{E}(T,\mu)$ eta $S(T,\mu)$.

$(b)$ Egiaztatu $(a)$ ataleko entropiaren $S(T,\mu)$ adierazpena haren definiziora joz ere lor daitekeela, alegia:

$$
S(T,\mu) := \frac{\partial}{\partial T}\left(k_{\mathrm{B}}T\ln\Upsilon\right)_\mu \; .
$$ (sph_agg_s_def)

Horretarako, kontuan izan zer-nolakoa den partizio-funtzio orokortuaren $T$ aldagaiarekiko menpekotasuna, hots, $\Upsilon(T,\mu) = \Upsilon(\alpha(T),\delta(T,\mu))$.



(mupt_id_lattice)=
### Kristal-sare idealeko gasa

_*Adibidea osatzen ari naiz..._


Adibide hau {cite}`hill` liburuko atal zenbaitetan lantzen da. Izan ere, sistema berarekin multzo estatistiko mikrokanonikoan, isobaroan, makrokanonikoan eta nanokanonikoan jardungo dugu ({numref}`{number}. irudia <lattice_multzo>`); bereziki, banatze-potentzialaren araberako entropiaren bilakaerari erreparatuko diogu, {numref}`{number} adibidean <mupt_gi>` egin genuen antzera.

Esanak esan, esku artean dugun sistema $B$ gelaxka bereizgarriz osatutako sarea da. Horietatik $N$ gelaxkatan molekulak daude, bakoitzean bat, kristal-sareko gasaren osatzaileak direlarik. Molekulak identikoak eta bereizezinak direla onartuko dugu. Berebat, elkarrekintza-energia eta barne askatasun-gradu oro baztertuko dugu (biraketa, bibrazioa...); hartara, sistemaren energia posible bakarra $E=0$ da. Gauzak horrela, sistemaren energiarako ekarpen mekanikoa eta kimikoa hartuko ditugu soilik aintzakotzat. Lehenengoari esleituko diogun aldagai estentsiboa $B$ magnitudea da; hortaz, energiarako ekarpen mekanikoa $-pB$ izango dugu. Kontuan izan dezagun ezen $B$ adimentsionala denez, haren $p$ aldagai konjokatuaren dimentsioak energiarenak direla. Ekarpen kimikoa, jakina, potentzial kimikoak finkatuko du: $\mu N$.

```{figure} lattice.png
---
height: 600px
name: lattice_multzo
---
Aztergai izango ditugun multzo estatistikoen adierazpen grafikoa. Multzo mikrokanonikoan lau azpisistemek ez dute elkar ikusten, eta, horietako bakoitza $B=25$ eta $N=9$ baldintzekin bateragarria den mikroegoera baten adierazle da. Kontrolpean izango ditugun ingurune-aldagaiak aldatu ahala, azpisistemek gelaxkak edota partikulak elkartrukatzeko askatasuna izango dute. Multzo nanokanonikoan bi askatasun-graduak daude abiarazita.
```

#### **9.2.1** Multzo mikrokanonikoa: $(B,N)$ ingurune-aldagaiak

Horrenbestez, azterketa $(B,N)$ ingurune-aldagaiek finkatuko duten **multzo mikrokanonikoan** abiatuko dugu. Molekulak bereizezinak direnez, mikroegoera-kopurua

$$
\Omega(B,N) = \frac{B!}{N!\;(B-N)!}
$$ (lattice_omega)

da. Entropia kalkulatzeko, Stirlingen {eq}`stirling` serieko lehenengo lau gaiak mantenduko ditugu. Hortaz,

$$
\boxed{\frac{S(B,N)}{k_\mathrm{B}} = \ln\Omega = B\ln B-N\ln N-(B-N)\ln(B-N)-\frac{1}{2}\ln\left[2\pi\frac{(B-N)N}{B}\right] - \frac{1}{12}\left[\frac{1}{N}+\frac{1}{B-N}-\frac{1}{B}\right]} \; .
$$ (lattice_s_mc)


Banatze-potentziala kalkulatzeko, {numref}`{number} ataleko <hillteo>` garapenak hartu behar ditugu aintzat. Hasteko, sistema txikiaren ekuazioa eta Gibbs-en ekuazioa idatziko ditugu:

$$
E = TS-pB+\mu N + \mathcal{E} \; ,
$$ (lattice_E)

$$
\mathrm{d}E = T\mathrm{d}S-p\mathrm{d}B+\mu \mathrm{d}N \; .
$$ (lattice_dE)


Hortaz, aurkeztutako baldintzetan $E=0$ dela gogora ekarriz, {eq}`lattice_E` eta {eq}`lattice_dE` ekuazioak berridatziko ditugu:

$$
S = \frac{p}{T}B - \frac{\mu}{T}N - \frac{\mathcal{E}}{T} \; ,
$$ (lattice_S)

$$
\mathrm{d}S = \frac{p}{T}\mathrm{d}B - \frac{\mu}{T}\mathrm{d}N \; .
$$ (lattice_dS)

Azkenengo adierazpenari jarraikiz eskuratuko ditugu $p$ eta $\mu$ aldagaiak:

$$
p = T\left(\frac{\partial S}{\partial B}\right)_{N} = k_{\mathrm{B}}T\left\{\ln\left(\frac{B}{B-N}\right) - \frac{N}{2B(B-N)} + \frac{1}{12}\left[\frac{1}{(B-N)^2}-\frac{1}{B^2}\right]\right\} \; ,
$$ (lattice_p_mc)

$$
\mu = -T\left(\frac{\partial S}{\partial N}\right)_{B} = k_{\mathrm{B}}T\left\{\ln\left(\frac{N}{B-N}\right) + \frac{B-2N}{2N(B-N)} + \frac{1}{12}\left[\frac{1}{(B-N)^2}+\frac{1}{N^2}\right]\right\} \; .
$$ (lattice_mu_mc)

Horiek horrela, $\mathcal{E} = -TS + pB -\mu N$ adierazpena erabiliz,

$$
\mathcal{E} = -k_{\mathrm{B}}T\left\{\frac{1}{2} + \frac{1}{2}\ln\left[2\pi\frac{(B-N)N}{B}\right]+\frac{1}{6}\left(\frac{1}{N}-\frac{1}{B}+\frac{1}{B-N}\right)\right\} \; .
$$ (lattice_epsilon_mc)


#### Multzo isobaroa: $(\frac{p}{T}, N)$ ingurune-aldagaiak

Abiaraz dezagun orain askatasun-gradu mekanikoa. Horrela, sistemaren azterketa $\left(\frac{p}{T},N\right)$ aldagaien bidez burutuko dugu **multzo isobaroan**. Hasteko, partizio-funtzioa hauxe dugu:

$$
\Delta \left(\frac{p}{T},N\right) = \sum_{\color{red}{B=N}}^{\color{red}{\infty}}\Omega(B,N)e^{-pB/k_{\mathrm{B}}T} = \frac{e^{-pN/k_{\mathrm{B}}T}}{\left(1-e^{-p/k_{\mathrm{B}}T}\right)^{N+1}} = \frac{x^N}{\left(1-x\right)^{N+1}} \; .
$$ (lattice_Delta)

Azkenengo pausoan $x = e^{-p/k_{\mathrm{B}}T}$ aldagaia txertatu dugu. Horrez gain, ohartu gaitezen batukariari ezarritako limiteetan. Hain zuzen askatasun-gradu mekanikoa abian jartzerakoan, $N$ aldagaiak finkatuko du behe-limitea ($B=N$); izan ere, kristal-sareak, gutxienez, gasaren $N$ molekula-osatzaileak barne hartzeko bezainbeste gelaxka izan beharko du.

```{dropdown} __Seriearen garapena__

Gaineko {eq}`lattice_Delta` ekuazioan ageri den seriea ebazteko prozedura honako hau da:

Lehenengo, batukariaren barneko adierazpena moldatuko dugu dugu, aldagai-aldaketa baten medioz:

$$
 \Delta = \frac{1}{N!}\sum_{{B=N}}^{{\infty}}\frac{B!}{(B-N)!}x^{B} \underset{(M=B-N)}{=} \frac{1}{N!}\sum_{{M=0}}^{{\infty}}\frac{(M+N)!}{N!}x^{M+N}
$$

Jarraian, errepara diezaiogun berdintza honi:

$$
\frac{\mathrm{d}^{N}}{\mathrm{d}x^{N}}\;x^{N+M} = \frac{(M+N)!}{N!}x^{M} \; .
$$

Horren laguntzaz, batukarian ageri dena honela berridatziko dugu:

$$
\frac{1}{N!}\sum_{{M=0}}^{{\infty}}\frac{(M+N)!}{N!}x^{M+N} =   \frac{1}{N!}\;\frac{\mathrm{d}^{N}}{\mathrm{d}x^{N}}\left[x^{N}\sum_{{M=0}}^{{\infty}}x^{M}\right]\underset{\vert x\vert < 1}{=} \frac{1}{N!}\frac{\mathrm{d}^{N}}{\mathrm{d}x^{N}} \left[\frac{x^N}{1-x}\right] = \frac{1}{N!}\left[\frac{N!\; x^N}{(1-x)^{N+1}}\right]
$$

Heldu gara, beraz, helmugara:

$$
\boxed{\Delta = \frac{x^N}{\left(1-x\right)^{N+1}}} \; .
$$


```

Jarraian, $\Delta = e^{-F/k_{\mathrm{B}}T}$ erlaziotik, Gibbs-en energia askea

$$
F\left(\frac{p}{T}, N\right) = N\widehat{\mu} = k_{\mathrm{B}}T\left[-N\ln x + (N+1)\ln(1-x)\right]
$$ (lattice_F)

da. Hari jarraituz, potentzial kimiko integrala eta diferentziala zein banatze-potentziala eskuratuko ditugu:

$$
\widehat{\mu} = k_{\mathrm{B}}T\left[-\ln x + \frac{N+1}{N}\ln(1-x)\right] \; ,
$$ (lattice_muhat_iso)

$$
\mu = k_{\mathrm{B}}T\ln\left(\frac{1-x}{x}\right) \; ,
$$ (lattice_mu_iso)

$$
\mathcal{E} = k_{\mathrm{B}}T\ln\left(1-x\right) \; .
$$ (lattice_epsilon_iso)

Ohartu gaitezen $\mu^{(x)} = 0$ dela; ondorioz, limite makroskopikoan $\widehat{\mu} = \mu^{(0)} \equiv \mu$ izango dugu.


Halaber, gelaxka-kopuruaren batez bestekoa kalkulatuko dugu:

$$
\bar{B} = \frac{\sum_B B \;\Omega(B,N)e^{-pB/k_{\mathrm{B}}T}}{\sum_B \Omega(B,N)e^{-pB/k_{\mathrm{B}}T}} = -k_{\mathrm{B}}T\;\frac{\partial }{\partial p}\ln \Delta = k_{\mathrm{B}}T\frac{\partial(F/ k_{\mathrm{B}}T)}{\partial p} = \frac{N+x}{1-x}
$$ (lattice_bbar)

Adierazpena berrantolatuz, sistemaren egoera-ekuazioa ere idaztea daukagu:

$$
\frac{p}{k_{\mathrm{B}}T} = \ln\left(\frac{1+\bar{B}}{\bar{B}-N}\right) \underset{(\bar{B},\; N \; \rightarrow\; \infty)}{=} -\ln\left(1-\frac{N}{\bar{B}}\right) \; .
$$ (lattice_eq_state)

Bukatzeko, $S\left(\frac{p}{T}, N\right)$ adierazpena eraikiko dugu. Horretarako, idatz dezagun lehenik multzo estatistiko honi dagokion probabilitate-funtzioa:

$$
P(B) = \frac{e^{-pB/ k_{\mathrm{B}}T}}{\Delta}
$$ (lattice_pb)

Horren bitartez, entropiaren definizioari so eginez ({eq}`entropy_def` ekuazioa), eta {eq}`lattice_bbar` ekuazioaren laguntzaz, hona iritsiko gara:

$$
S\left(\frac{p}{T}, N\right) = -k_{\mathrm{B}}\sum_BP(B)\;\ln P(B) = \frac{p\bar{B}}{T} + k_{\mathrm{B}}\ln\Delta = \frac{p\bar{B}}{T} - \frac{\widehat{\mu}N}{T} \; .
$$ (lattice_s_iso_def)

Aurrez lortutako $\bar{B}$ eta $\widehat{\mu}$ magnitudeak ordezkatuz,

$$
\boxed{\frac{S\left(\frac{p}{T}, N\right) }{k_\mathrm{B}} =  (\bar{B}+1)\ln (\bar{B}+1) -(N+1)\ln (N+1)-(\bar{B}-N)\ln(\bar{B}-N)} \; .
$$ (lattice_s_iso)

Lortutako adierazpena erabat zehatza da, alegia, ez dugu Stirling-en hurbilketa erabili. Hori dela eta, sistema nahi bezain txikietarako ere baliozkoa da (baita $N=1$ kasurako ere). Ildo horretatik, interesgarria izan daiteke sistema bera multzo makrokanonikoan aztertzeaz bat, bertan entropiaren $S\left(B, \frac{\mu}{T}\right)$ ekuazioa lortu berri dugun adierazpenarekin erkatzea, batik bat, kasuan kasuko tamaina finituko zuzenketei erreparatuz; izan ere, multzo makrokanonikoa eta isobaroa parekoak dira (_erdiirekiak_), bietan baitago askatasun-gradu bakarra abian.

#### Multzo makrokanonikoa: $(B, \frac{\mu}{T})$ ingurune-aldagaiak

Abiaraz dezagun soilk askatasun-gradu kimikoa, partizio-funtzio makrokanonikoa eraikitzeko:

$$
\Xi\left(B,\frac{\mu}{T}\right) = \sum_{\color{red}{N=0}}^{\color{red}{B}}\;\Omega(B,N)\;e^{\mu N/k_{\mathrm{B}}T} = \sum_{N=0}^B \frac{B!}{N!(B-N)!}\;\lambda^N = (1+\lambda)^B \; ,
$$ (lattice_xi)

non, aurreko batean bezala, $\lambda = e^{\mu/k_{\mathrm{B}}T}$ ordezkatu dugun. Batukariaren kalkuluari dagokionez, irakurleari lagungarria gerta dakioke {eq}`q_ising` ekuazioari darraion oharra.

Orain, {numref}`{number} ataleko <replica_e>` argibideak aintzat hartuz, $\widehat{p}$ magnitude integralak $\Xi = e^{\widehat{p}B/k_{\mathrm{B}}T}$ berdintza beteko duela onartuko dugu, hark finkatuko baitu multzo estatistikoaren mailako ekarpen mekanikoa. Horiek horrela, {eq}`lattice_xi` ekuazioa behatuz, $p$ aldagai diferentziala eta integrala bat datozela ohartuko gara, alegia:

$$
p =\left[\frac{\partial (\widehat{p}B)}{\partial B}\right]_{\frac{\mu}{T}} = k_{\mathrm{B}}T\ln \left(1+\lambda\right) = \widehat{p}
$$ (lattice_p_phat)


Hortaz, banatze-potentzialak bi aldagaiak bereizten dituzten ekarpenak biltzen dituenez,

$$
\mathcal{E} = -(\widehat{p}-p)B = 0
$$ (lattice_epsilon_gc)

daukagu. Batez besteko partikula-kopuruari dagokionez,

$$
\bar{N} = \left[\frac{\partial (\widehat{p}B)}{\partial \mu}\right]_{T,B} = \frac{B\lambda}{1+\lambda} \; .
$$ (lattice_nbar)

Ondorioz,

$$
\widehat{p} = p = -k_{\mathrm{B}}T\ln\left(1-\frac{\bar{N}}{B}\right) \; .
$$ (lattice_p_phat_new)

Lor dezagun orain entropiaren adierazpena.


##### Ariketa

Idatzi multzo estatistiko jakin honi dagokion probabilitate-banaketaren adierazpena. Horren bitartez, idatzi entropiak bete beharko duen ekuazioa. Azkenik moldatu adierazpena, $B$ eta $\bar{N}$ aldagaien baitan ager dadin.

```{dropdown} __Erantzuna__

$$
P(N) = \frac{e^{\mu N/k_{\mathrm{B}}T}}{\Xi}
$$ (lattice_pn)

Gauzak horrela, entropiak $N$ magnitudearen inguruko fluktuazioak hartuko ditu aintzakotzat, hau da,

$$
S = -k_{\mathrm{B}}\sum_N P(N)\ln P(N) = k_{\mathrm{B}}\ln\Xi -\frac{\mu\bar{N}} {T}  = \frac{\widehat{p}B} {T} - \frac{\mu\bar{N}} {T}
$$ (lattice_s_gc_def)

Adierazpena {eq}`lattice_nbar` zein {eq}`lattice_p_phat_new` ekuazioen bidez moldatu behar dugu.

```

Ariketan erdietsitako berdintza garatuz,

$$
\boxed{\frac{S\left(B,\frac{\mu}{T}\right) }{k_\mathrm{B}} =  B\ln B -(B-\bar{N})\ln (B-\bar{N})-\bar{N}\ln\bar{N}} \; .
$$ (lattice_s_gc)

Entropiaren {eq}`lattice_s_gc` ekuazioa ere erabat zehatza da. Berebat, nabarmentzekoa da limite makroskopikora joz gero, adierazpen horrek bere horretan jarraituko duela, alegia, kasu honetan multzo makrokanonikoak ez dio inolako tamaina finituko zuzenketarik erantsi. Horren adierazle garbia da aurrez lortutako banatze-potentzial hertsiki nulua ({eq}`lattice_epsilon_gc` ekuazioa).

Halaber, {eq}`lattice_s_iso` ekuazioaren alderatuz, eta $\bar{B}=B$ zein $\bar{N}=N$ onartuz, entropiak behera egin duela hauteman daiteke. Zuzenketak, hala ere, oso txikiak dira, alegia, $N$ eta $B$ aldagaiekiko $\mathcal{O}(1)$ ordenakoak.


Azken txanpa multzo erabat askean sistemaren berrazterketari ekitean datza.



#### Multzo nanokanonikoa: $(\frac{p}{T}, \frac{\mu}{T})$ ingurune-aldagaiak
