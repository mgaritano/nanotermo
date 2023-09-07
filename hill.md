(hillsec)=
## Sistema Txikien Termodinamika

(hillteo)=
### Hill-en teoria

Sistema txiki baten azterketa burutzeko Hill-ek darabilen abiapuntua sistema horren $\mathscr{N}$ aldakiz osatutako multzoa eraikitzea da. Sistema guztiak baliokideak, bereizgarriak eta askeak dira, hots, ez dago elkarrekintzarik. Bada, aldaki-kopurua oso handia dela onartuz gero $\left(\mathscr{N}\rightarrow \infty\right)$, sistemak nahi bezain txikiak izanik ere,  multzoa bera sistema makroskopikotzat hartzea izango dugu.
Baieztapen horrek egundoko garrantzia du; izan ere,  hori dela eta, Termodinamika Klasikoa erabiliz abiatu gaitezke makrosistema bere osotasunean aztertzeko. Ondoren, sistema txiki bakarraren propietateak multzo osoaren aldagaien aldakiko batez bestekoak kalkulatuz lortuko ditugu. Horretan datza, hain zuzen, Hill-en metodoa.

```{admonition} Oharra
 Hill-en teoriak ere __hipotesi ergodikoari__ eusten dio: propietate baten ibilbide dinamikoan zeharreko denboran batez bestekoa bat dator multzo estatistikoan barrenekoarekin. Bestalde, multzoaren barne-energia, entropia, bolumena eta partikula-kopurua $t$ azpiindizeaz idatziko ditugu.

```

Multzoaren azterketari ekin aurretik, kontuan izan dezagun laugarren askatasun-gradu bat duela abian eta, beraz, bere barne-energiak $E_{t} = E_{t}(S_{t}, V_{t}, N_{t}, \mathscr{N})$ erlazioa betetzen duela. Gauzak horrela, {eq}`gibbs` ekuazioari beste aldagai konjokatu-pare bat erantsi beharko diogu, __Hill-Gibbs ekuazioa__ eraikitzeko:

$$
 \mathrm{d}E_{t} = \left(\frac{\partial E_{t}}{\partial S_{t}}\right)_{V_{t}, N_{t}, \mathscr{N}}\mathrm{d}S_{t} + \left(\frac{\partial E_{t}}{\partial V_{t}}\right)_{S_{t}, N_{t}, \mathscr{N}}\mathrm{d}V_{t} + \left(\frac{\partial E_{t}}{\partial N_{t}}\right)_{S_{t},V_{t}, \mathscr{N}}\mathrm{d}N_{t} + \color{blue}{\left(\frac{\partial E_{t}}{\partial \mathscr{N}}\right)_{S_{t},V_{t}, N_{t}}}\color{red}{\mathrm{d}\mathscr{N}} \; .
$$

Edo, era trinkoan idatziz gero,

$$
\mathrm{d}E_{t}(S_{t}, V_{t}, N_{t}, \mathscr{N}) = T\mathrm{d}S_{t} - p\mathrm{d}V_{t} + \mu \mathrm{d}N_{t} + \color{blue} {\mathscr{E}} \color{red}{\mathrm{d}\mathscr{N}} \; .
$$ (hill-gibbs)

Bi ekuazioek agerian uzten dute banatze-potentzialak betetzen duen adierazpena:

$$
\boxed{\mathscr{E} = \left(\frac{\partial E_{t}}{\partial \mathscr{N}}\right)_{S_{t},V_{t}, N_{t}}} \; .
$$

Berebat, lehengo ataleko multzo nanokanonikoaren gaineko azalpen lausoak argitzeko lagungarriak gerta daitezke. Ikusten denez, $\mathscr{E}$ potentzialak $\mu$ aldagaiaren eitea aurkezten du, eta, nolabait, azpisistemekin lotutako potentzial kimikotzat har liteke {cite}`hill_diff_app`. Aldaki bat gehitzean, $S_{t}, V_{t}$ eta $N_{t}$ aldagaiek konstante jarraituko dute, baina  birbanatu egingo dira. Hori dela eta, multzoaren azpisistemen banatzea aldatzeak sorrarazten duen ekarpen energetikoa adierazten du banatze-potentzialak.
Hurrengo urratsa, {eq}`hill-gibbs` ekuaziotik barne-energiaren adierazpena erdiestea litzateke. Integratuz,

$$
E_{t} \left(=\int \mathrm{d}E_{t} = T \int \mathrm{d}S_{t} - p \int \mathrm{d}V_{t} + \mu \int \mathrm{d}N_{t} + \mathscr{E} \int \mathrm{d}\mathscr{N}\right) = TS_{t} - pV_{t} + \mu N_{t} + \mathscr{E}\mathscr{N} \; .
$$ (pausoa)

Azken pausoak berehalakoa dirudien arren, ohartu gaitezen horren atzean funtsezko propietate matematikoa datzala: _Euler-homogeneotasuna_ (ikus [___A___](euler) ___eranskina___). Hain zuzen, $E_{t}, S_{t}, V_{t}, N_{t}$ eta $\mathscr{N}$ lehen ordenako funtzio Euler-homogeneoak dira $V$ zein $N$ aldagaiekiko. Are gehiago, tenperatura, presioa eta potentzial kimikoa aldagai horiekiko zero ordenako funtzioak dira, hots, intentsiboak. Azken bi ezaugarri horiek ahalbidetzen dute, integraletatik $(T, p, \mu,\mathscr{E})$ sorta ateratzeaz bat, lehenengo ekuaziotik bigarrenera igarotzea. Alabaina, sistema txikietan arestiko guztia ez da beteko, segituan ikusiko dugun legez.

Lehengo hariari ekinez, sistema txiki baten ezaugarriak ondorioztatzea da helburua, beroriek multzo osoaren funtzioen aldaki-kopuruarekiko batez bestekoak bailiran adieraziz. Beraz, $\overline{E} \equiv E_{t}/\mathscr{N}$; $S \equiv S_{t}/\mathscr{N}$; $\overline{V} \equiv V_{t}/\mathscr{N}$; $\overline{N} \equiv N_{t}/\mathscr{N}$ definituz, multzoaren azpisistema bakarrak ekuazio honi segituko lioke:

$$
\boxed{\overline{E} = TS - p\overline{V} + \mu \overline{N} + \mathscr{E}} \; .
$$ (e_small)

Jarraian, {eq}`e_small` ekuazioa zein aurkeztu berri ditugun propietateak {eq}`hill-gibbs` adierazpenean ordezkatuz,

$$
\mathscr{N}\mathrm{d}\overline{E} + (TS-p\overline{V}+\mu \overline{N} + \mathscr{E})\mathrm{d}\mathscr{N} = T \mathrm{d}(\mathscr{N}S) - p \mathrm{d}(\mathscr{N}\overline{V}) + \mu \mathrm{d}(\mathscr{N}\overline{N}) + \mathscr{E}\mathrm{d}\mathscr{N} \; .
$$

Eragiketak eginez gero, sistema txikiaren Gibbs-en ekuaziora helduko gara:

$$
\mathrm{d}\overline{E} = T\mathrm{d}S - p\mathrm{d}\overline{V} + \mu \mathrm{d}\overline{N} \; .
$$ (gibbs_small)

Orain, {eq}`e_small` ekuazioaren diferentzial osoa hartu eta {eq}`gibbs_small` adierazpenarekin berdinduko dugu, horrela __Hill-Gibbs-Duhem__ ekuazioa lortzeko:

$$
\boxed{\mathrm{d}\mathscr{E}(T,p,\mu) = -S\mathrm{d}T + \overline{V}\mathrm{d}p - \overline{N}\mathrm{d}\mu}\; .
$$ (h_g_d)

Erlazio horrek matematikoki erakustera ematen du {numref}`{number}. zatian <nanointro>` esaten aritu garena, agerikoa baita banatze-potentzialak askatasun-gradu bat abiaraziko duela. Hartara, zilegi izango zaigu, $(T, p, \mu)$ aldagai-sorta $\mathscr{E}(T,p,\mu)$ potentzialaren baitan finkatzeaz bat, multzo nanokanonikoa eraikitzea. Berorren bidez sistema txikiaren propietateei xehetasun handiagoz hurreratuko gatzaizkie.
Bestalde, {eq}`gibbs_small` adierazpenaren itxurak hasieran aurkeztu dugun {eq}`gibbs` ekuazio berera heldu garela pentsaraz liezaguke. Baina adi egon behar dugu, bertako aldagaien ez-homogeneotasunak ez baitu baimentzen {eq}`pausoa` espresioan parentesi artean agertzen dena burutzea; horren adierazle da {eq}`e_small` ekuazioan azaltzen den $\mathscr{E}$ gaia. Jakina, banatze-potentziala baztergarria balitz, $S, \overline{V}$ eta $\overline{N}$ aldagaiek zein berorien konjokatuek izaera homogeneoa berreskuratuko lukete. Horrek multzo nanokanonikoa suntsituko luke, ekuazioak maila makroskopikora eramango bailituzke: {eq}`e_small` $\rightarrow$ {eq}`E`, {eq}`gibbs_small` $\rightarrow$ {eq}`gibbs` eta {eq}`h_g_d` $\rightarrow$ {eq}`gibbs-duhem`.


Ikusten dugunez, Termodinamikaren ohiko ekuazioen eraldaketen bidez, aurrez kualitatiboki aipatutako kontzeptuei azalpen mardulagoak eta landuagoak eman dizkiegu. Horrek sailkapen-irizpide zorrotza eraikitzea ahalbidetzen du: _Sistema bat txikia da, baldin eta bere banatze-potentziala finitua eta bazterrezina bada_.


Aurrera egin baino lehen, sistema txikiaren entropiaren inguruko ohartarazpena egin beharrean gaude. Izan ere, dagoeneko hainbatetan aipatu dugu sistema bakarraren propietateak multzoaren aldakiko batez besteko balioak direla. Hala, $\overline{E}, S, \overline{V}$ eta $\overline{N}$ aurkeztu ditugu. Lauretatik guztiek marratxoa daramate soinean, $S = S_{t}/\mathscr{N}$ aldagaiak izan ezik. Bada, argi gelditu bedi ezen aurrekoa ez dela oharkabeko akatsa izan, horren atzean entropiaren esangura baitago (ikus [**_B_**](entropy) ___eranskina___).

Atal honi amaiera emateko, multzo estatistiko jakinek sistema txikiaren banatze-potentzialari nola eragiten dioten aztertzen hasiko gara. Horrek bide emango die jarraian datozen atalei, eta bertan agertzen diren adibide azpimarragarriei. Halaber, aurreko zatiko kontzeptu garrantzitsuenean murgiltzen hasiko gara: funtzio termodinamikoek ingurune-aldagaien araberako zuzenketak pairatzen dituzte.

(replica_e)=
### Hill-Gibbs ekuazioaren orokorpena eta aldaki-energia

Orain arte, sistema txiki baten banatzeari dagokion askatasun-graduaren eragina aztertzerakoan, aldaki bat sartzean multzoaren propietate estentsibo guztiak $(S_{t}, V_{t}, N_{t})$ aldaezin mantendu ditugu.
Horrela, banatze-potentziala definitu dugu: aldaki-kopuruan eragiteak soilik, _eta ez beste ezerk_, multzo osoaren energiari dakarkion aldakuntza. Hala ere, kontura gaitezen ezen multzoaren aldagaien birbanatzeak sistema txiki soilaren propietateei zuzenean erasaten diela,  $E, V$ eta $N$ finko mantentzea galarazten baitu. Ondorioz, sistema txikiei $(T, p, \mu)$ aldagaiak esleitu behar izan dizkiegu nahitaez.

Jakina, beti ez dugu aldagai horietara sarbidea izango. Horrek arestiko eztabaida orokortzera gakartza ezinbestean. Preseski, $(A, B, C,...)$ ingurune-aldagaien aurrean $\mathscr{E}(T, p, \mu)$ banatze-potentzialaren orokorpena definitu beharrean gaude. Hura $X(A, B, C...)$ hizkiaren bidez izendatuko dugun, eta kasuan kasuko inguruneari egokituko zaion __aldaki-energia__ da. Noski, multzo nanokanonikoaren kasuan $X(T,p,\mu) = \mathscr{E}(T, p, \mu)$ genuke, baina, oro har, ez da hori beteko.

Esandakoa argitze aldera, lehenik, lehengo azterketa multzo makrokanonikora eramango dugu, hau da, sistema txikien aldagaiak $(T,V,\mu)$ izango dira. Gauzak horrela, $E_{t} = \mathscr{N}\overline{E}$, $S_{t} = \mathscr{N}S$, $V_{t} = \mathscr{N}V$ eta $N_{t} = \mathscr{N}\overline{N}$ izango ditugu. Aipatzekoa da $V$ bolumenak ez daramala marratxoa, kasu honetan ez baita batez besteko magnitudea. Jarraian, {eq}`hill-gibbs` berridatziko dugu, oraingoan, ordea, $V$ agerraraziz $(\mathrm{d}V_{t} = \mathscr{N}\mathrm{d}V + V\mathrm{d}\mathscr{N})$:


$$
\mathrm{d}E_{t}(S_{t},V,N_{t},\mathscr{N}) = T\mathrm{d}S_{t} - p\mathscr{N}\mathrm{d}V + \mu \mathrm{d}N_{t} + (\mathscr{E}-pV)\mathrm{d}\mathscr{N} \; .
$$ (degc)

Hortik aipaturiko aldaki-energia definituko dugu:

$$
X(T,V,\mu) = \mathscr{E}-pV := \left(\frac{\partial E_{t}}{\partial \mathscr{N}}\right)_{S_{t},V,N_{t}} := -\widehat{p}\;V\;.
$$ (xgc)

Esanak esan, {eq}`xgc` ekuazioari so eginez gero, $X(T,V,\mu)$ ingurune honetan $\mathscr{E}$ baino aldagai are aproposagoa dela ikusiko dugu, hark baitarama multzo makrokanonikoaren berezko izaera. Hain zuzen, aldaki bat sartzean, multzo osoaren $V_{t}$ bolumena aldatu egingo da, horrek bermatuko baitu sistema txiki bakoitzaren $V$ bolumenak aldaezin irautea. Beraz, multzo zehatz horretako aldaki-energia multzoak hautemango duen, eta $\widehat{p}$ presioak ereduztatuko duen lan mekanikotzat har daiteke: $-\widehat{p}\;V$. Jakina, $p\neq \widehat{p}$, presio bien energiarako ekarpenek ez dutelako esangura bera: lehenengoarena sistema txikiei dagokie, eta bigarrenarena multzo osora hedatzen da. Ondorioz, efektu finituak direla eta, sistema txikien kasuan adierazpen desberdinak izango dituzte, eta bakarrik eskualde termodinamikoan etorriko dira bat.

Segidan, {eq}`xgc` ekuazioa erabiliz, eta lehengo ataleko prozedura jarraituz, espresio hauetara iritsiko gara:

$$
\overline{E} = TS - \widehat{p}\;V + \mu \overline{N} \; ,
$$ (e_small_gc)

$$
\mathrm{d}\overline{E} = T\mathrm{d}S - p\mathrm{d}V + \mu \mathrm{d}\overline{N} \; .
$$ (dE_small_gc)

Horiek agerian uzten dute, $p$ eta $\widehat{p}$ presioen arteko desberdintza dela eta, $\overline{E}$ ez dela funtzio Euler-homogeneoa. Jarraian, Legendreren bi transformazio aplikatuz,

$$
\mathrm{d}(-\widehat{p}\;V) := \mathrm{d}\Psi(T,V,\mu) = -S\mathrm{d}T - p\mathrm{d}V - \overline{N}\mathrm{d}\mu \; .
$$ (pot_gc)

Bertatik, hitzez azaldutakoa laburbildu ez ezik, beharrezkoa duen adierazgarritasuna emango dioten adierazpenak erdietsiko ditugu:

$$
\boxed {-\widehat{p} := \frac{-\widehat{p}\;V}{V} \quad \pmb{\neq} \quad -p := \left[\frac{\partial(-\widehat{p}\;V)}{\partial V}\right]_{T,\mu} \quad ; \quad \mathscr{E} = - (\widehat{p} - p)V} \; .
$$ (gc_summ)

Hala, $\widehat{p}$ __presio integral__ eta $p$ __presio diferentzial__ izendatuko ditugu. Biak bereizten dituzten ez-linealtasunaren ondoriozko ekarpen _txikiak_ banatze-potentzialak biltzen ditu.
