(nanointro)=
## 2

## Nanotermodinamikara sarrera

Mekanika estatistikoak esku artean dugun sistemaren fisika bere osagai mikroskopikoen dinamikaren bidez deskribatzea du erronkatzat; horretarako, sistemaren aldakiz (edo kopiaz) osaturiko multzo estatistikoez baliatzen da.  Aldaki-kopurua oso handia bada, denboran geldikortasuna eta oreka estatistikoa bermatzen dira, azterketa termodinamikoa abian jartzeko ezinbesteko baldintzak, egiazki. Berebat, jakin dakigunez, kanpotik ezarritako askatasun-baldintzen arabera, multzoari berari izaera jakina eman diezaiokegu.

```{figure} multzoak.png
---
height: 500px
name: multzo
---
  Multzo mikrokanonikoa, kanonikoa eta makrokanonikoa hagitz ezagunak dira, eta termodinamikan zabalki erabiliak. Nanonakonikoa, ordea, lehen begiratuan arrotza gerta lekiguke.
```

Lehenbizi, azpisistema erabat isolatuz osaturiko multzo __mikrokanonikoa__ dugu. Bertan, sistemaren aldakiek ez dute elkar ikusten, hots, horietako bakoitzean aldagai estentsibo guztiek ($E$ barne-energiak, $V$ bolumenak eta $N$ partikula-kopuruak) finko diraute. Gauzak horrela, sistema aztertzeko abiapuntua makroskopikoki behatuko den _makroegoeraren_ baliokideak diren _mikroegoeren_ kopurua, $\Omega(E,V,N)$, _zenbatzea_ da. Jarraian, Boltzmann-en ekuazioak, $k_{\mathrm{B}}$ Boltzmann-en konstantearen bidez, entropia itzuliko digu: $S(E,V,N) := k_{\mathrm{B}} \ln \Omega$.

```{admonition} Oharra
 Hainbat ekuaziotan ageriko den $:=$ ikurrak bi adierazpen definizioz bat datozela esan nahi du.
```
Azpisistemen arteko energia-trukaketa baimenduz gero, multzo __kanonikora__ egingo dugu jauzi. Tenperatura kontrolpean izango dugu, eta baimendutako $E_{i}$ energia bakoitzarekin bateragarriak diren mikroegoeren sorta dagokion pisuarekin batukarian txertatuz, partizio-funtzio kanonikoa kalkulatzera helduko gara: $Q(T,V,N) := \sum_{E_{i}} \Omega(E_{i},V,N) e^{-E_{i}/k_{\mathrm{B}}T}\;$. Aipatutako pisua Boltzmann-en faktoreak finkatuko du, hain zuzen, sistema $E_{i}$ energiadun egoeran egoteko probabilitatea adieraziz. Horrek Helmholtz-en energia askea (bero-iturri batekin ukipen termikoan dagoen sistema isotermoaren lan erabilgarria) kalkulatzera garamatza: $A(T,V,N) := -k_{\mathrm{B}}T\ln Q\;$.

```{admonition} Oharra
__Argibide garrantzitsua__: Lan guztian zehar Hill-ek bere liburuan erabiltzen duen antzinako edo ezohiko notazioari eutsiko diogu. Hala, potentzial termodinamikoak hizki hauen bidez izendatuko ditugu: Barne-energia $\rightarrow E$ ; Helmholtz-en energia askea $\rightarrow A$ ; Entalpia $\rightarrow H$ ; Gibbs-en energia askea $\rightarrow F$. Eraldaketa horiek ez biezaiote irakurleari nahasmena sorraraz.
```

Azkenik, aldakiei elkarren artean energia ez ezik, materia ere trukatzea onartuko balitzaie, multzo are askeagoa erdietsiko genuke, \underline{makrokanonikoa}, alegia (\ref{multzo}\textcolor{blue}{c}). Askatasun-gradu kimikoari dagokion Legendreren transformazioa aplikatuz, partizio-funtzio makrokanonikoa eraikiko dugu: $\Xi (T, V, \mu) := \sum_{N_{i}} Q(T,V,N_{i})e^{\mu N_{i}/k_{\mathrm{B}}T}$, eta, hortik, multzo horren egoera-funtzioa den gran-potentziala:  $\Psi (T,V,\mu) = -k_{\mathrm{B}}T\ln \Xi$.

Arestian esandakoari helduz, horiek dira termodinamikako liburuetan azaltzen diren multzo estatistikoak. Egia da, bai, badugula aldaera gehiago definitzerik; esaterako, $(T,p,N)$ ingurune-aldagaiek ezaugarritzen duten multzo isotermo-isobaroa. Aurrerago ikusiko dugunez, multzo horrek berebiziko esangura du sistema txikien termodinamikan. Halaber, osagai bat baino gehiagodun sistemetan zilegi da multzo osmotikoa $(T,p,N_{1},\mu_{2})$ ere erabiltzea.

Baina kontua zera da: oraingoz azaldu zaizkigun multzo estatistiko guztietan aldagai estentsibo bat, gutxienez, inguruneak zehazten du ($E, V$ edota $N$). Are gehiago, __Gibbs-Duhem__ erlazioari jarraituz, badirudi sistema makroskopikoari ezin dakizkiokeela hiru aldagai intentsiboak aldi berean, bakoitza bere kabuz, finkatu. Hori argiroago ikusteko, sistema makroskopiko baten barne-energiaren aldakuntzak betetzen duen __Gibbs-en ekuazioa__ idatziko dugu:

```{math}
:label: gibbs
\mathrm{d}E(S,V,N) = T\mathrm{d}S - p\mathrm{d}V + \mu \mathrm{d}N \; .
```

Integratuz,

```{math}
:label: E
\mathrm{d}E(S,V,N) = TS - pV + \mu N
```
adierazpenera iritsiko gara. Diferentzial totala hartuz,

```{math}
\mathrm{d}E = T\mathrm{d}S + S\mathrm{d}T -p\mathrm{d}V - V\mathrm{d}p + \mu \mathrm{d}N + N \mathrm{d}\mu \; ,
```

eta berori  {eq}`gibbs` ekuazioarekin berdinduz gero, Gibbs-Duhem erlazioa lortuko dugu:

```{math}
:label: gibbs-duhem
\boxed{N\mathrm{d}\mu = -S\mathrm{d}T + V\mathrm{d}p} \; .
```

Gaineko {eq}`gibbs-duhem` ekuazioak aurrez esandakoa berresten du, muga garrantzitsua ezarriz: $\mu$ potentzial kimikoak, $T$ tenperaturak eta $p$ presioak ez dute, hirurek batera, aske izaterik. Horietatik bi aukeratuz gero, hirugarrena berorien funtziopean zehaztuta geratuko da. Bada, orain arte azaldutako ideiak sendotasun handikoak eta urraezinak dela pentsa genezake. Aztergai dugun irudi-sortan badago, alabaina, __aurreko hori inola ere iradokitzen ez duen__, eta oraindik aurkeztu ez dugun multzo estatistikoa.

Arretaz errepara bekio {numref}`%s <multzo>`d irudiari. Osagai bakarreko azpisistemei askatasun-gradu guztiak abiarazi zaizkie, inguruneko aldagai-sortatzat $(T,p,\mu)$ dute eta. Hori dela eta, elkarren artean energia, partikulak eta bolumena truka ditzakete ezein kanpo-galarazpenik gabe!

Aurrekoaren harira, bi arazori aurre egin beharrean gaude. Baina, horretarako, nanotermodinamikan murgiltzen hasi beharko dugu ezinbestean. Kezka-iturriok honakoak dira: alde batetik, argi dago __multzo nanokanonikok__ {eq}`gibbs-duhem` baldintza hausten duela. Beraz, esan berri duguna aintzat hartuz, multzo horren bidez ez dugu sistema makroskopiko bat deskribatzerik izango. Hill-ek horri honela ihardetsiko lioke: $(T,p,\mu)$ sortak soilik __sistema txikiak__ ezaugarritzeko balio du (tamaina finitukoak). Bide horretatik, \ref{hill_t}. zatian azalduko dugu Hill-en arabera zein den, zehazki, sistema bat _txiki_ izatearen esangura, fisikaren nahiz matematikaren ikuspuntutik.

Bestetik, $(T,p,\mu)$ aldagaiak hirurak batera askeak izan daitezen, eta, horrela, berorien bidez multzo nanokanonikoa zehazteko gai izateko, sistema txiki horri nahitaez beste askatasun-gradu bat gaineratu beharko zaio, lehengoekin batera {eq}`gibbs-duhem` bezalako ekuazio eraldatu bati jarrai diezaion. Bada, berariazko askatasun-gradu hori, hain zuzen ere, Hill-ek txertatu zuen, eta, tamaina finituko efektuen eragina kontuan izanik, aztergai dugun sistemaren aldakiz osatutako multzoak bere barnean dituen _aldaki horien kopurua_ ($\mathcal{N}$) aldatzeko duen gaitasunari dagokio. Bestela esanda, multzo estatistiko txiki batean, gainontzeko aldagai estentsiboak ($S, V, N$) aldaezin mantentzen ditugularik, multzo horren __banatzean eragiteak__ bere barne-energiari erasango dio. Horren ondorioz, Gibbs-en {eq}`gibbs`  ekuazioari beste ekarpen bat gehitu beharko diogu. Azken esaldiak $\mathcal{N}$ magnitudearen konjokatu intentsiboa aurkeztera gakartza nahitaez:  $\mathcal{E}$ hizkiaren bidez adieraziko dugun __banatze-potentziala__.

Multzo nanokanonikoaren fisika estatistikoari dagokion tresneria \ref{nano}. atalean eraikiko dugu. Aitzitik, eztabaida honi hausnarketa kualitatibo baten bidez emango diogu itxiera.

Banatze-potentzialak sistemaren gainazal- eta ertz-efektuak, zein azpisistemen biraketa edota translazioa hartzen ditu aintzakotzat. Sistema txikien kasuan eragileok ezin dira baztergarritzat jo, hori energiaren kontserbazioaren aurka bailihoake, eta, gainera, entropiaren maximizazioa eragotziko bailuke. Halaber, aipaturiko zuzenketek makroskopikoki estentsiboak diren propietateen izaera birdefinituko dute, beti ezingo baitugu onartu $N$ magnitudearekin linealki aldatuko direnik. Zenbaitetan $\propto N^{2/3}$ edo $\propto N^{1/3}$ erlazioak ere kontuan izan beharko dira. Aurrekoarekin batera, berorien aldagai konjokatuek intentsibo izateari utziko diote; esate baterako, arrotza gerta balekiguke ere, sistema txiki baten presioak eta tenperaturak tamainarekiko menpekotasuna dute (\ref{fase1order} atalean adibidea). Horren ondorioz, estentsibotasunari dagokion aldagaien sailkapen-irizpidea beroriek _makroskopikoki_ daukaten izaeran oinarritu beharko dugu aurrerantzean.

Efektu horiek guztiek mundu makroskopikoan behatzen ez den ondorio batera garamatzate: sistema txiki baten funtzio termodinamikoak multzoz multzo aldatu egingo dira, azterketan erabiliko diren ingurune-aldagaien arabera. Esaldi hori arras esanguratsua da. Esaterako, gas idealaren entropia multzo estatistiko egokian kalkulatzeak Gibbs-en paradoxari konponbide berritzailea eman diezaioke {cite}`multiscale` (\ref{mupt_gi} atala). Noski, sistema handituz joango balitz, ekarpen finituak biltzen dituen banatze-potentziala are baztergarriago bilakatuko litzateke. Horrek, mailaz maila, _ohiko_ termodinamikarantz gindekarzke itzulian. Bertan, hain zuzen, barne-energiak $E \gg \mathcal{E}$ beteko luke, baita gainontzeko gai \textit{handiek} ere.

Hori da, erabat esateko, Hill-en teoriaren muina. Hurrengo atalean, berori aurkeztu ez ezik, erlazio termodinamikoei zer-nolako eraldaketak dakarzkien aztertzeari ekingo diogu.

$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$
