(app)=
## Gas ideala eta adsorbatzaile esferiko txikia

Atal berezi honetan, Python programazio-lengoaia erabiliz, {cite}`ads` artikuluko emaitzak errepikatu eta aztertuko ditugu.

### Sistemaren azterketa

```{figure} adsorbent.png
---
height: 350px
name: adsorbent
---
Zentrutik $r$ distantziara dagoen gas-partikula askeak $a$ erradioko adsorbatzailearen eragina hautemango du, $U(a,r)$ elkarrekintza-energia dela medio. Hala, xurgatutako partikulek $R$ erradioko geruza osatuko dute. Bada, orekako $U_{S}=U(a,R)$ potentzialak esferaren $\Omega$ azaleraren menpekotasuna izango du, ez ordea $T$ tenperaturarena edo $\mu$ potentzial kimikoarena.

```

Xurgatutako partikulen geruza izango da aurrerantzean aztergai izango dugun sistema termodinamikoa. Berorren azalera $\Omega$ da, eta $T$ tenperaturan dagoen bero-iturri batekin ukipenean dago. Era berean, xurgatutako partikulek iturri kimikoa osatzen dutela onartuko dugu. Beraz, sistemaren inguruneko aldagai-sorta $(T,\Omega,\mu)$ da. Adsorbatzailea bera  kanpo-eragiletzat hartuko dugu. Bada, {numref}`{number} irudiko <adsorbent>` azalpenei segituz eta Hillen teorian oinarrituz ({numref}`{number} azpiatala <hillteo>`), $\mathscr{N}$ aldakiz osatutako multzo makrokanonikoa eraikiko dugu. Bere aldagaiak, hortaz, $S_{t}=\mathscr{N}S$, $\Omega_{t}=\mathscr{N}\Omega$ eta $N_{t}=\mathscr{N}\bar{N}$ dira. Horien bidez, dagokion ekuazioa lortuko dugu:

$$
\mathrm{d}E_{t}(S_{t},\Omega,N_{t},\mathscr{N}) = T\mathrm{d}S_{t} + \gamma\mathscr{N}\mathrm{d}\Omega + \mu \mathrm{d}N_{t} + \left(\mathscr{E}+ \gamma\Omega\right)\mathrm{d}\mathscr{N} ,
$$ (adseq)
non $\gamma$ __gainazal-tentsio diferentziala__ den, hau da, $\Omega$ aldagaiaren konjokatua, limite makroskopikoan intentsiboa. Berebat, $\widehat{\gamma}$ __gainazal-tentsio integralaren__ bitartez aldaki-energia eta banatze-potentziala definituko ditugu:

$$
X(T,\Omega,\mu) = \mathscr{E} + \gamma\Omega  := \left(\frac{\partial E_{t}}{\partial \mathscr{N}}\right)_{S_{t},\Omega,N_{t}} := \widehat{\gamma}\Omega \; .
$$(adsx)

Sistema txikietara igaroz, barne-energiak honakoa beteko du, aldagaien ez-homogeneotasuna agerian utziz.

$$
\mathrm{d}\bar{E} = T\mathrm{d}S + \gamma\mathrm{d}\Omega + \mu \mathrm{d}\bar{N}
$$ (adsde)
$$
\bar{E} = TS + \widehat{\gamma}\Omega + \mu \bar{N}
$$ (adse)

Ekuazio-bikotetik Hill-Gibbs-Duhem erlaziora helduko gara.

$$
\mathrm{d}(\widehat{\gamma}\Omega) = -S\mathrm{d}T + \gamma \mathrm{d}\Omega - \bar{N} \mathrm{d}\mu
$$ (adshgd)

Hortik gainazal-tentsioen arteko erlazioa finkatuko dugu (makroskopikoki bat datoz).

$$
\gamma := \left[\frac{\partial(\widehat{\gamma}\Omega)}{\partial \Omega}\right]_ {T, \mu} = \widehat{\gamma} + \Omega\left(\frac{\partial \widehat{\gamma}}{\partial \Omega}\right)_{T,\mu} \; .
$$ (adsgandghat)


Segidan, Fisika Estatistikora igaroko gara. Xurgatutako geruzaren partizio-funtzio kanonikoak bi ekarpen bilduko ditu: $\Omega$ gainazalera mugatutako gas idealari dagokiona, eta orekako $U_{S}$ elkarrekintza-energiaren eragina aintzat hartzen duena. Horiek horrela,

$$
Q(T,\Omega,N) = \frac{\Omega^N}{N!\Lambda^{2N}}\cdot e^{-NU_{S}/k_{\mathrm{B}}T} \; .
$$ (adsq)

Askatasun-gradu kimikoari dagokion Legendreren transformazioa aplikatuz, partizio-funtzio makrokanonikoa idatziko dugu.

$$
\Xi(T,\Omega,\mu) = \sum_{N=0}^{\infty} \frac{\Omega^N}{N!\Lambda^{2N}} e^{N(\mu -U_{S})/k_{\mathrm{B}}T} = \exp\left[\frac{\Omega}{\Lambda^2}e^{(\mu -U_{S})/k_{\mathrm{B}}T}\right]
$$ (adsxi)

Jarraian, $\Psi(T,\Omega,\mu) := \widehat{\gamma}\Omega := -k_{\mathrm{B}}T\ln\Xi$ dela gogora ekarriz, grafikoen eraikuntzarako erabiliko ditugun adierazpenak honakoak dira.

$$
\boxed{\widehat{\gamma} = -\frac{k_{\mathrm{B}}T}{\Lambda^2}e^{(\mu -U_{S})/k_{\mathrm{B}}T}}
$$ (ghat)

$$
\boxed{\gamma=-\frac{k_{\mathrm{B}} T}{\Lambda^{2}} e^{(\mu -U_{S})/k_{\mathrm{B}}T}\left[1-\frac{ \Omega}{k_{\mathrm{B}}T}\left(\frac{\partial U_{S}}{\partial \Omega}\right)_{T, \mu}\right]}
$$ (g)

```{admonition} Oharra
Gainazal-tentsio diferentziala {eq}`adsgandghat` ekuazioaren laguntzaz lortu dugu.

```

Baina,  lehenbizi adsorbatzailearen eta gas-partikulen arteko elkarrekintza ereduztatu beharrean gaude, hartara $U(a,r)$ eraiki, eta, hortik $U_{S}$ potentzialera iristeko.

### Elkarrekintza-potentziala eta Emaitzak

Adsorbatzailea $\rho$ dentsitateko esfera trinkoa da. Bolumen-elementuak gas-partikula batekin duen elkarrekintza Lennard-Jonesen 12-6 potentzial-ereduarekin ereduztatuko dugu:

$$
u(r) = 4\epsilon\left[\left(\frac{\sigma}{r}\right)^{12} - \left(\frac{\sigma}{r}\right)^{6}\right] \; ,
$$ (lj)
non $\sigma$ eta $\epsilon$ luzera- eta energia-parametroak diren, hurrenez hurren. Berori adsorbatzailearen bolumenean zehar integratuz lortuko dugu $U(a,r)$ potentziala:

$$
U(a, r) =  \int_{\text{V}}\mathrm{d}^{3}\mathbf{r}\;u(r) = \frac{16 \pi \epsilon \rho \sigma^{3}}{3}\left[\frac{\left(15 a^{3} r^{6}+63 a^{5} r^{4}+45 a^{7} r^{2}+5 a^{9}\right) \sigma^{9}}{15\left(r^{2}-a^{2}\right)^{9}}-\frac{a^{3} \sigma^{3}}{\left(r^{2}-a^{2}\right)^{3}}\right] \; .
$$ (uar)

Segidan, {eq}`uar` adierazpena minimizatuko dugu, hartara $a$ eta $R$ erradioen arteko erlazioa ezartzeko, eta, era berean, $U_{S}$ oreka-potentziala erdiesteko.

$$
U_{S} = U(a,r=R) = \mathrm{min}\left[U(a,r)\right]
$$

Amaitzeko, dentsitatea finkatu behar dugu. Artikuluan $\rho = 3/\left[4\pi(\sigma/2)^3\right]$ hartzen da. Gauzak horrela, {numref}`{number} irudiko <plot1>` grafiko-sortan adsorbatzailearen handi-txikiaren araberako {eq}`ghat` eta {eq}`g` ekuazio-parea irudikatuko dugu, baita azalera-unitateko banatze-potentziala ere: $\mathscr{E}/\Omega = \widehat{\gamma} - \gamma \;$.

```{figure} plot1.PNG
---
height: 350px
name: plot1
---
Sistema txikia denean (esaterako, $a/\sigma<40$ eremuan), gainazal-tentsioak nabarmenki estentsiboak dira, eta, horrez gain, bi kurbak argi bereiz daitezke. Dena den, adsorbatzailearen tamainak gora egin ahala, banatze-potentziala indargabetuz doa. Hori dela eta, $\widehat{\gamma}$ eta $\gamma$ kurbek gutxinaka izaera intentsiboa berreskuratu, eta, era berean, bat egitera joko dute. Hala, $a/\sigma = 100$ puntuan sistema jada eskualde makroskopikorako trantsiziora gerturatzen dabil.

```

```{figure} plot2.PNG
---
height: 350px
name: plot2
---
Adsorbaturiko fasearen molekula-unitateko magnitudeek maila makroskopikora trantsizio are bortitzagoa pairatzen dute ($a/\sigma \approx 50$). Halaber, gainazal-tentsio integralak bi dimentsioko gas idealaren legeari segitzen diola ikus daiteke, hots, $-\widehat{\gamma}\Omega = \bar{N}k_{\mathrm{B}}T$.

```

Kurbei egokitutako parametroak argon gasari dagozkio: $\Lambda_{\text{Ar}} = 16,7 \cdot 10^{-12} \; \mathrm{m}$ ; $\sigma_{\text{Ar}} = 3.4 \cdot 10^{-10} \; \mathrm{m}$ ; $\epsilon_{\text{Ar}} = 0,0104 \; \mathrm{eV}$.

Era berean, {numref}`{number} irudiko <plot2>` kurbak eraikitzerakoan, {eq}`adshgd` ekuazioa aintzat hartuz, honako erlazioa erabili dugu.

$$
\bar{n} \equiv \frac{\bar{N}}{\Omega} = - \left(\frac{\partial \widehat{\gamma}}{\partial \mu}\right)_ {T,\Omega} = \frac{1}{\Lambda^2}e^{(\mu -U_{S})/k_{\mathrm{B}}T} \; .
$$ (nadsorb)

Hasteko, aipatu beharrekoa da adsorbatzailearen erradioaren zeroranzko limitean berori partikula puntualtzat jo dugula. Hortaz, {eq}`lj` ekuazioa minimizatuz, kasu horretan $R(a\rightarrow 0) =2^{1/6}\sigma$ erabili dugu.

Bestalde, grafikoetako iruzkinei jarraituz, eta {eq}`adsgandghat` zein {eq}`g` ekuazioei erreparatuz gero, argi dago sistema txikien eskalan $\widehat{\gamma}\Omega$ bezalako funtzio termodinamikoek esferaren $\Omega$ azalerarekiko menpekotasun ez-lineala aurkezten dutela. Horren eraginez, gainazal-tentsioek jokaera ez-intentsiboa daukate, eta, halaber, berorien arteko aldentzea nabarmena da. Edonola ere, limite makroskopikoak linealtasuna berrezarriko du, eta, hartara, $\partial\left(\widehat{\gamma}\Omega\right)/\partial \Omega  = (\widehat{\gamma}\Omega)/\Omega$ berdintza berreskuratuko dugu. Banatze-potentzialak, hain zuzen ere,

$$
\mathscr{E} = \widehat{\gamma}\Omega - \Omega \left[\frac{\partial (\widehat{\gamma}\Omega)}{\partial \Omega}\right]_{T,\mu}
$$ (epsilonads)
adierazpena betetzen duen horretan, izaera linealarekiko desbideraketen gidaritzan dago.

Ildo beretik, sistemari askatasun-gradu mekanikoa abian jartzeaz bat, multzo nanokanonikoari aldaki bat gaineratzeak $(\mathscr{E}<0)$ multzoaren $\Omega_{t}$ guztizko azalera birbanatzea lekarke. Hortaz, $(T,\gamma,\mu)$ ingurne-aldagaidun azpisistemetako $\Omega$ azalera txikiagotu, eta, berorien gainazalen kurbatura areagotu egingo litzateke. Hillen postulatuari segituz, banatze-potentziala litzateke multzoaren barne-energiak hautemango lukeen gainazal-efektuon erantzule eta adierazle soila; alegia,

$$
\mathscr{E}(T,\gamma,\mu) := \left(\frac{\partial E_{t}}{\partial \mathscr{N}}\right)_ {S_{t},\Omega_{t},N_{t}} \; .
$$ (epsilonadsfree)

Azterketari amaiera emateko, aipatu beharrekoa da aplikazio honetan zenbait hurbilketatan oinarritutako adsortzioaren eredu bakuna erabili dugula: alde batetik, gasa idealtzat hartu dugu, eta, bestetik, orekako $U_{S}$ potentziala soilik gainazalarekiko menpekoa dela onartu dugu. Dena dela ere, Sistema Txikien Termodinamikaren kontzeptuak adsortziora era ulergarri eta didaktikoan moldatzeko adibide arras egokia da.
