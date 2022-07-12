(hill)=
## 3

## Sistema Txikien Termodinamika

###  Hill-en teoria

Sistema txiki baten azterketa burutzeko Hill-ek darabilen abiapuntua, sistema horren $\mathcal{N}$ aldakiz osatutako multzoa eraikitzea da. Sistema guztiak baliokideak, bereizgarriak eta askeak dira, hots, ez dago elkarrekintzarik. Bada, aldaki-kopurua oso handia dela onartuz gero ($\mathcal{N}\rightarrow \infty$), sistemak nahi bezain txikiak izanik ere,  multzoa bera sistema makroskopikotzat hartzea izango dugu.
Baieztapen horrek egundoko garrantzia du; izan ere,  hori dela eta, termodinamika klasikoa erabiliz abiatu gaitezke makrosistema bere osotasunean aztertzeko. Ondoren, sistema txiki bakarraren propietateak multzo osoaren aldagaien aldakiko batez bestekoak kalkulatuz lortuko ditugu. Horretan datza, hain zuzen, Hill-en metodoa.

```{admonition} Oharra
 Hill-en teoriak ere __hipotesi ergodikoari__ deutso: propietate baten ibilbide dinamikoan zeharreko denboran batez bestekoa bat dator multzo estatistikoan barrenekoarekin. Bestalde, ultzoaren barne-energia, entropia, bolumena eta partikula-kopurua $t$ azpiindizeaz idatziko ditugu.

```

Multzoaren azterketari ekin aurretik, kontuan izan dezagun laugarren askatasun-gradu bat duela abian eta, beraz, bere barne-energiak $E_{t} = E_{t}(S_{t}, V_{t}, N_{t}, \mathcal{N})$ erlazioa betetzen duela. Gauzak horrela, {eq}`gibbs` ekuazioari beste aldagai konjokatu-pare bat erantsi beharko diogu, __Hill-Gibbs ekuazioa__ eraikitzeko:

```{math}
 \mathrm{d}E_{t} = \left(\frac{\partial E_{t}}{\partial S_{t}}\right)_{V_{t}, N_{t}, \mathcal{N}}\mathrm{d}S_{t} + \left(\frac{\partial E_{t}}{\partial V_{t}}\right)_{S_{t}, N_{t}, \mathcal{N}}\mathrm{d}V_{t} + \left(\frac{\partial E_{t}}{\partial N_{t}}\right)_{S_{t},V_{t}, \mathcal{N}}\mathrm{d}N_{t} + \color{blue}{\left(\frac{\partial E_{t}}{\partial \mathcal{N}}\right)_{S_{t},V_{t}, N_{t}}}\color{red}{\mathrm{d}\mathcal{N}} \; .
```

Edo, era trinkoan idatziz gero,

```{math}
:label: hill-gibbs
\mathrm{d}E_{t}(S_{t}, V_{t}, N_{t}, \mathcal{N}) = T\mathrm{d}S_{t} - p\mathrm{d}V_{t} + \mu \mathrm{d}N_{t} + \color{blue} {\mathcal{E}} \color{red}{\mathrm{d}\mathcal{N}} \; .
```
Bi ekuazioek agerian uzten dute  banatze-potentzialak betetzen duen adierazpena:

```{math}
\boxed{\mathcal{E} = \left(\frac{\partial E_{t}}{\partial \mathcal{N}}\right)_{S_{t},V_{t}, N_{t}}} \; .
```

Berebat, lehengo ataleko multzo nanokanonikoaren inguruko azalpen lausoak argitzeko lagungarriak gerta daitezke. Ikusten denez, $\mathcal{E}$ potentzialak $\mu$ aldagaiaren eitea aurkezten du, eta, nolabait, azpisistemekin lotutako potentzial kimikotzat har liteke {cite}`hill_diff_app`. Aldaki bat gehitutakoan, $S_{t}, V_{t}$ eta $N_{t}$ aldagaiek konstante jarraituko dute, baina  birbanatu egingo dira.
Hurrengo urratsa, {eq}`hill-gibbs` ekuaziotik barne-energiaren adierazpena erdiestea litzateke. Integratuz,

```{math}
 :label: pausoa
\small E_{t} \left(=\int \mathrm{d}E_{t} = T \int \mathrm{d}S_{t} - p \int \mathrm{d}V_{t} + \mu \int \mathrm{d}N_{t} + \mathcal{E} \int \mathrm{d}\mathcal{N}\right) = TS_{t} - pV_{t} + \mu N_{t} + \mathcal{E}\mathcal{N} \; .
```

Azken pausoak berehalakoa dirudien arren, ohartu gaitezen horren atzean funtsezko propietate matematikoa datzala: _Euler-homogeneotasuna_ (ikus \ref{a} eranskina). Hain zuzen, $E_{t}, S_{t}, V_{t}, N_{t}$ eta $\mathcal{N}$ lehen ordenako funtzio Euler-homogeneoak dira $V$ zein $N$ aldagaiekiko. Are gehiago, tenperatura, presioa eta partikula-kopurua aldagai horiekiko zero ordenako funtzioak dira, hots, intentsiboak. Azken bi ezaugarri horiek ahalbidetzen dute, integraletatik $(T, p, \mu,\mathcal{E})$ sorta ateratzeaz bat, lehenengo ekuaziotik bigarrenera igarotzea. Alabaina, sistema txikietan arestiko guztia ez da beteko, segituan ikusiko dugun legez.

Lehengo hariari ekinez, sistema txiki baten ezaugarriak ondorioztatzea da helburua, beroriek multzo osoaren funtzioen aldaki-kopuruarekiko batez bestekoak bailiran adieraziz. Beraz, $\bar{E} \equiv E_{t}/\mathcal{N}$; $S \equiv S_{t}/\mathcal{N}$; $\bar{V} \equiv V_{t}/\mathcal{N}$; $\bar{N} \equiv N_{t}/\mathcal{N}$ definituz, multzoaren azpisistema bakarrak ekuazio honi segituko lioke:

```{math}
 :label: e_small
\boxed{\bar{E} = TS - p\bar{V} + \mu \bar{N} + \mathcal{E}} \; .
```

Jarraian, {eq}`e_small` ekuazioa zein aurkeztu berri ditugun propietateak {eq}`hill-gibbs` adierazpenean ordezkatuz,

```{math}
\mathcal{N}\mathrm{d}\bar{E} + (TS-p\bar{V}+\mu \bar{N} + \mathcal{E})\mathrm{d}\mathcal{N} = T \mathrm{d}(\mathcal{N}S) - p \mathrm{d}(\mathcal{N}\bar{V}) + \mu \mathrm{d}(\mathcal{N}\bar{N}) + \mathcal{E}\mathrm{d}\mathcal{N} \; .
```

Eragiketak eginez gero, sistema txikiaren Gibbs-en ekuaziora helduko gara:

```{math}
:label: gibbs_small
\mathrm{d}\bar{E} = T\mathrm{d}S - p\mathrm{d}\bar{V} + \mu \mathrm{d}\bar{N} \; .
```

Orain, {eq}`e_small` ekuazioaren diferentzial osoa hartu eta {eq}`gibbs_small` adierazpenarekin berdinduko dugu, horrela __Hill-Gibbs-Duhem__ ekuazioa lortzeko:

```{math}
:label: h_g_d
\boxed{\mathrm{d}\mathcal{E}(T,p,\mu) = -S\mathrm{d}T + \bar{V}\mathrm{d}p - \bar{N}\mathrm{d}\mu}\; .
```

Erlazio horrek matematikoki erakustera ematen du [](nanointro). zatian esaten aritu garena, agerikoa baita banatze-potentzialak askatasun-gradu bat abiaraziko duela. Hartara, zilegi izango zaigu, $(T, p, \mu)$ aldagai-sorta finkatzeaz bat, multzo nanokanonikoa eraikitzea. Berorren bidez sistema txikiaren propietateei xehetasun handiagoz hurreratuko gatzaizkie.
Bestalde, {eq}`gibbs_small` adierazpenaren itxurak hasieran aurkeztu dugun {eq}`gibbs` ekuazio berera heldu garela pentsaraz liezaguke. Baina adi egon behar dugu, bertako aldagaien ez-homogeneotasunak ez baitu baimentzen {eq}`pausoa` espresioan parentesi artean agertzen dena burutzea; horren adierazle da {eq}`e_small` ekuazioan azaltzen den $\mathcal{E}$ gaia. Jakina, banatze-potentziala baztergarria balitz, $S, \bar{V}$ eta $\bar{N}$ aldagaiek zein berorien konjokatuek izaera homogeneoa berreskuratuko lukete. Horrek multzo nanokanonikoa suntsituko luke, ekuazioak maila makroskopikora baileramazke: {eq}`e_small` $\rightarrow$ {eq}`E`, {eq}`gibbs_small` $\rightarrow$ {eq}`gibbs` eta {eq}`h_g_d` $\rightarrow$ {eq}`gibbs-duhem`.


Ikusten dugunez, termodinamikaren ohiko ekuazioen eraldaketen bidez, aurrez kualitatiboki aipatutako kontzeptuei azalpen mardulagoak eta landuagoak eman dizkiegu. Horrek sailkapen-irizpide zorrotza eraikitzea ahalbidetzen du: _Sistema bat txikia, da baldin eta bere banatze-potentziala finitua eta bazterrezina bada_.


Aurrera egin baino lehen, sistema txikiaren entropiaren inguruko ohartarazpena egin beharrean gaude. Izan ere, dagoeneko hainbatetan aipatu dugu sistema bakarraren propietateak multzoaren aldakiko batez besteko balioak direla. Hala, $\bar{E}, S, \bar{V}$ eta $\bar{N}$ aurkeztu ditugu. Lauretatik guztiek marratxoa daramate soinean, $S = S_{t}/\mathcal{N}$ aldagaiak izan ezik. Bada, argi gelditu bedi ezen aurrekoa ez dela oharkabeko akatsa izan, horren atzean entropiaren esangura baitatza (ikus \ref{b} eranskina).

Atal honi amaiera emateko, multzo estatistiko jakinek sistema txikiaren banatze-potentzialari nola eragiten dioten aztertzen hasiko gara. Horrek bide emango die jarraian datozen \ref{npt}., \ref{fase}. eta \ref{nano}. atalei, eta bertan agertzen diren adibide azpimarragarriei. Halaber, aurreko zatiko kontzeptu garrantzitsuenean murgiltzen hasiko gara: funtzio termodinamikoek ingurune-aldagaien araberako zuzenketak pairatzen dituzte.
