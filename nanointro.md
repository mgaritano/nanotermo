(nanointro)=
## Nanotermodinamikara sarrera

Mekanika Estatistikoak esku artean dugun sistemaren fisika bere osagai mikroskopikoen dinamikaren bidez deskribatzea du erronkatzat; horretarako, sistemaren aldakiz (edo kopiaz) osaturiko multzo estatistikoez baliatzen da. Aldaki-kopurua oso handia bada, denboran geldikortasuna eta oreka estatistikoa bermatuko dira, azterketa termodinamikoa abian jartzeko ezinbesteko baldintzak, egiazki. Berebat, jakin dakigunez, kanpotik ezarritako askatasun-baldintzen arabera, multzoari berari izaera jakina eman diezaiokegu.

```{figure} multzoak.png
---
height: 500px
name: multzo
---
  Multzo mikrokanonikoa, kanonikoa eta makrokanonikoa hagitz ezagunak dira, eta Termodinamikan zabalki erabiliak. Multzo nanokanonikoa, ordea, lehen begiratuan arrotza gerta lekiguke. Parentesien barnean multzo bakoitzean kontrolpean izango ditugun azpisistemen mailako aldagaiak daude. Azpisistemek noranzko biko gezien ondoan ageri diren magnitude estentsiboak elkartrukatzeko askatasuna dute. Argi dago, beraz, multzo nanokanonikoa dela lauretatik askeena.
```

Lehenbizi, azpisistema erabat isolatuz osaturiko multzo __mikrokanonikoa__ dugu. Bertan, sistemaren aldakiek ez dute elkar ikusten, hots, horietako bakoitzean aldagai estentsibo guztiek ($E$ barne-energiak, $V$ bolumenak eta $N$ partikula-kopuruak) finko diraute. Gauzak horrela, sistema aztertzeko abiapuntua makroskopikoki behatuko den _makroegoeraren_ baliokideak diren _mikroegoeren_ kopurua, $\Omega(E,V,N)$, _zenbatzea_ da. Jarraian, Boltzmannen ekuazioak, $k_{\mathrm{B}}$ Boltzmannen konstantearen bidez, entropia itzuliko digu: $S(E,V,N) := k_{\mathrm{B}} \ln \Omega$.

```{admonition} Oharra
 Hainbat ekuaziotan ageriko den $:=$ ikurrak bi adierazpen definizioz bat datozela esan nahi du.
```
Azpisistemen arteko energia-trukaketa baimenduz gero, multzo __kanonikora__ egingo dugu jauzi. Tenperatura kontrolpean izango dugu, eta baimendutako $E_{i}$ energia bakoitzarekin bateragarriak diren mikroegoeren sorta dagokion pisuarekin batukarian txertatuz, partizio-funtzio kanonikoa kalkulatzera helduko gara: $Q(T,V,N) := \sum_{E_{i}} \Omega(E_{i},V,N) e^{-E_{i}/k_{\mathrm{B}}T}\;$. Aipatutako pisua Boltzmannen faktoreak finkatuko du, hain zuzen, sistema $E_{i}$ energiadun egoeran egoteko probabilitatea adieraziz. Horrek Helmholtzen energia askea (bero-iturri batekin ukipen termikoan dagoen sistema isotermoaren lan erabilgarria) kalkulatzera garamatza: $A(T,V,N) := -k_{\mathrm{B}}T\ln Q\;$.

```{admonition} __Argibide garrantzitsua__
Lan guztian zehar Hillek bere liburuan erabiltzen duen antzinako notazioari eutsiko diogu. Hala, potentzial termodinamikoak hizki hauen bidez izendatuko ditugu: Barne-energia $\rightarrow E$ ; Helmholtzen energia askea $\rightarrow A$ ; Entalpia $\rightarrow H$ ; Gibbsen energia askea $\rightarrow F$. Eraldaketa horiek ez biezaiote nahasmena sorraraz irakurleari.
```

Azkenik, aldakiei elkarren artean energia ez ezik, materia ere trukatzea onartuko balitzaie, multzo are askeagoa erdietsiko genuke, __makrokanonikoa__, alegia. Askatasun-gradu kimikoari dagokion Legendreren transformazioa aplikatuz, partizio-funtzio makrokanonikoa eraikiko dugu: $\Xi (T, V, \mu) := \sum_{N_{i}} Q(T,V,N_{i})e^{\mu N_{i}/k_{\mathrm{B}}T}$, eta, hortik, multzo horren egoera-funtzioa den gran-potentziala:  $\Psi (T,V,\mu) = -k_{\mathrm{B}}T\ln \Xi$.

Arestian esandakoari helduz, horiek dira Termodinamikako liburuetan azaltzen diren multzo estatistikoak. Egia da, bai, badugula aldaera gehiago definitzea; esaterako, $(T,p,N)$ ingurune-aldagaiek ezaugarritzen duten multzo isotermo-isobaroa. Aurrerago ikusiko dugunez, multzo horrek berebiziko esangura du sistema txikien analisian. Halaber, osagai bat baino gehiagodun sistemetan zilegi da multzo osmotikoa $(T,p,N_{1},\mu_{2})$ ere erabiltzea.

Baina nabarmendu beharreko kontua ondorengoa da: oraingoz azaldu zaizkigun multzo estatistiko guztietan aldagai estentsibo bat, gutxienez, inguruneak zehazten du $(E, V$ edota $N)$. Are gehiago, __Gibbs-Duhem__ erlazioari jarraituz, badirudi sistema makroskopikoari ezin dakizkiokeela hiru aldagai intentsiboak aldi berean, bakoitza bere kabuz, finkatu. Hori argiroago ikusteko, sistema makroskopiko baten barne-energiaren aldakuntzak betetzen duen __Gibbsen ekuazioa__ idatziko dugu:

$$
\mathrm{d}E(S,V,N) = T\mathrm{d}S - p\mathrm{d}V + \mu \mathrm{d}N \; .
$$ (gibbs)

Integratuz,

$$
E(S,V,N) = TS - pV + \mu N
$$ (E)
adierazpenera iritsiko gara. Diferentzial totala hartuz,

$$
\mathrm{d}E = T\mathrm{d}S + S\mathrm{d}T -p\mathrm{d}V - V\mathrm{d}p + \mu \mathrm{d}N + N \mathrm{d}\mu \; ,
$$

eta, hura {eq}`gibbs` ekuazioarekin berdinduz gero, Gibbs-Duhem erlazioa lortuko dugu:

$$
\boxed{N\mathrm{d}\mu = -S\mathrm{d}T + V\mathrm{d}p} \; .
$$ (gibbs-duhem)

Gaineko {eq}`gibbs-duhem` ekuazioak aurrez esandakoa berresten du, muga garrantzitsua ezarriz: $\mu$ potentzial kimikoak, $T$ tenperaturak eta $p$ presioak ez dute, hirurek batera, aske izaterik. Horietatik bi aukeratuz gero, hirugarrena haien funtziopean zehaztuta geratuko da $[T(p,\mu),\; p(T,\mu)$ edo $\mu (p,T)]$. Bada, orain arte azaldutako ideiak sendotasun handikoak eta urraezinak dela pentsa genezake. Aztergai dugun irudi-sortan badago, alabaina, ___aurreko hori inola ere iradokitzen ez duen___, eta oraindik aurkeztu ez dugun multzo estatistikoa.

Arretaz errepara bekio {numref}`{number}d irudiari <multzo>`. Osagai bakarreko azpisistemei askatasun-gradu guztiak abiarazi zaizkie, inguruneko aldagai-sortatzat $(T,p,\mu)$ dute eta. Hori dela eta, elkarren artean energia, partikulak eta bolumena truka ditzakete ezein kanpo-galarazpenik gabe!

Aurrekoaren harira, bi arazori aurre egin beharrean gaude. Baina, horretarako, Nanotermodinamikan murgiltzen hasi beharko dugu ezinbestean. Kezka-iturriok honakoak dira: alde batetik, argi dago __multzo nanokanonikoak__ {eq}`gibbs-duhem` baldintza hausten duela. Beraz, esan berri duguna aintzat hartuz, multzo horren bidez ez dugu sistema makroskopiko bat deskribatzerik izango. Hillek horri honela ihardetsiko lioke: $(T,p,\mu)$ sortak soilik __sistema txikiak__ ezaugarritzeko balio du (tamaina finitukoak). Bide horretatik, {numref}`{number} zatian <hillteo>` sakonago azalduko dugu Hillen arabera zein den, zehazki, sistema bat _txiki_ izatearen esangura, Fisikaren nahiz Matematikaren ikuspuntutik.

Bestetik, $(T,p,\mu)$ aldagaiak hirurak batera askeak izan daitezen, eta, horrela, haien bidez multzo nanokanonikoa zehazteko gai izateko, sistema txiki horri nahitaez _beste askatasun-gradu bat_ gaineratu beharko diogu, lehengoekin batera {eq}`gibbs-duhem` bezalako ekuazio eraldatu bati jarrai diezaion. Bada, berariazko askatasun-gradu hori, hain zuzen ere, Hillek txertatu zuen, eta, tamaina finituko efektuen eragina kontuan izanik, aztergai dugun sistemaren aldakiz osatutako multzoak bere barnean dituen _aldaki horien kopurua_ $(\mathscr{N})$ aldatzeko duen gaitasunari dagokio. Bestela esanda, multzo estatistiko txiki baten gainontzeko aldagai estentsiboak $(S, V, N)$ aldaezin mantentzen ditugularik, multzo horren __banatzean eragiteak__ bere barne-energiari erasango dio. Horren ondorioz, Gibbsen {eq}`gibbs`  ekuazioari beste ekarpen bat gehitu beharko diogu. Azken esaldiak $\mathscr{N}$ magnitudearen konjugatu intentsiboa aurkeztera gakartza nahitaez:  $\mathscr{E}$ hizkiaren bidez adieraziko dugun __BANATZE-POTENTZIALA__.

Multzo nanokanonikoaren Fisika Estatistikoari dagokion tresneria aurrerago eraikiko dugu. Aitzitik, eztabaida honi hausnarketa kualitatibo baten bidez emango diogu itxiera.

Banatze-potentzialak sistemaren gainazal- eta ertz-efektuak, zein azpisistemen biraketa edota translazioa hartzen ditu aintzakotzat. Sistema txikien kasuan eragileok ezin dira baztergarritzat jo, hori energiaren kontserbazioaren aurka bailihoake, eta, gainera, entropiaren maximizazioa eragotziko bailuke. Halaber, aipaturiko zuzenketek _makroskopikoki estentsiboak diren propietateen izaera birdefinituko dute_, beti ezingo baitugu onartu $N$ magnitudearekin linealki aldatuko direnik. Zenbaitetan $\propto N^{2/3}$ edo $\propto N^{1/3}$ erlazioak ere kontuan izan beharko dira. Aurrekoarekin batera, haien _aldagai konjugatuek intentsibo izateari utziko diote_; esate baterako, arrotza gerta balekiguke ere, sistema txiki baten presioak eta tenperaturak tamainarekiko menpekotasuna dute. Horren ondorioz, estentsibotasunari dagokion aldagaien sailkapen-irizpidea _limite makroskopikoan_ daukaten izaeran oinarritu beharko dugu aurrerantzean.

Efektu horiek guztiek mundu makroskopikoan behatzen ez den ondorio batera garamatzate: _sistema txiki baten funtzio termodinamikoak multzoz multzo aldatu egingo dira_, azterketan erabiliko diren ingurune-aldagaiek berariazko zuzenketak erantsiko baitizkiete. Esaldi hori arras esanguratsua da. Esaterako, gas idealaren entropia multzo estatistiko egokian kalkulatzeak Gibbsen paradoxari konponbide berritzailea eman diezaioke {cite}`multiscale`. Noski, sistema handituz joango balitz, ekarpen finituak biltzen dituen banatze-potentziala are baztergarriago bilakatuko litzateke. Horrek, mailaz maila, _ohiko_ Termodinamikarantz gindekarzke itzulian. Bertan, hain zuzen, barne-energiak $E \gg \mathscr{E}$ beteko luke, baita gainontzeko gai _handiek_ ere.

Hori da, erabat esateko, Hillen teoriaren muina. Hurrengo atalean, hura aurkeztu ez ezik, erlazio termodinamikoei zer-nolako eraldaketak dakarzkien aztertzeari ekingo diogu.  
