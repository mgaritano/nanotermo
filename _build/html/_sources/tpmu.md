(tpmu)=
## **6**. Multzo nanokanonikoa: $(T,p,\mu)$ ingurune-aldagaiak

Azken-aurreko kapitulu honetan teoriaren alor esanguratsuenari ekingo diogu. Demagun esku artean dugun sistema $N$ monomeroz osaturiko polimero agregatua dela, eta berori $T$ tenperaturan eta $p$ presiopean dagoela. Bada, molekulen arteko lotze-indarrak aski sendoak ez balira, luzaroan $N$ molekulen kopuruak ez lirauke finko, fluktuazioak jasango bailituzke. Hori dela eta, sistemari $\mu$ potentzial-kimikoa esleitu beharko genioke hirugarren ingurune-aldagaitzat; alegia, azterketa $(T,p,\mu)$ aldagaidun azpisistemak biltzen dituen multzo  nanokanonikoaren bitartez burutu beharko genuke baitezpada.

Alabaina, har dezagun gogoan [1](sarrera). atalean aipaturikoa: maila makroskopikoan ez dugu horrelako multzoa definitzerik izango, sistemaren hiru aldagai intentsiboetatik soilik bi izan baitaitezke aske (Gibbs-Duhem erlazioa). Horren harira, sistema txikiek $\mathcal{E}$ banatze-potentzialak ezaugarritzen duen askatasun-gradu berezia dutela onartu dugu. Hala, orain sistemaren tamainak aldagai intentsiboei erasango die. Horrek ahalbidetzen du, hain zuzen, multzo nanokanonikoaren eraikuntza. Hala ere, askatasun-gradu hori ez da nolanahikoa. Izan ere, sistema handitu ahala, funtzio termodinamikoetako ekarpen makroskopikoen gailentasunak berori desagerrarazi egingo dute.

```{admonition} Oharra
Hill-ek bere liburuan _multzo orokortu_ izena erabiltzen du.

```

Ildo horretatik, [6.2](mupt_linagg) eta [6.3](mupt_gi) adibideetako sistemei askatasun-gradu guztiak abiarazteak sorrarazten dituen ekarpen finituak kalkulatu, eta beroriek __entropian__ duten eraginari erreparatuko diogu, ondorio esanahitsuak erdietsiz. Berebat, limite makroskopikoan lortzen diren emaitzak gainontzeko multzo estatistikoenekin bateragarriak direnentz egiaztatuko dugu. Baina, lehenik, azterketarako beharrezkoa izango zaigun tresneria aurkeztuko dugu laburki.

(mupt_azter)=
### **6.1** Multzoaren azterketa

Aipatzekoa da multzo honi dagozkion adierazpen gehienak [3.1](hillteo) atalean eraiki ditugula, berori baita, hain zuzen, Hill-en teoriari heltzeko abiapuntu aproposa. Bada, {eq}`h_g_d` ekuazioa berridatziz, $S$ entropia, $\bar{V}$ bolumena eta $\bar{N}$ partikula-kopuruaren erlazioetara iritsiko gara:

$$
 \mathrm{d}\mathcal{E}(T,p,\mu) = \left(\frac{\partial \mathcal{E}}{\partial T}\right)_ {p,\mu}\mathrm{d}T +\left(\frac{\partial \mathcal{E}}{\partial p}\right)_ {T,\mu}\mathrm{d}p + \left(\frac{\partial \mathcal{E}}{\partial \mu}\right)_{T,p}\mathrm{d}\mu \; .
 $$ (depsilonnew)

 Jarraian, Fisika Estatistikoarekin lotura ezartze aldera, $\Upsilon(T,p,\mu)$ hizkiaren bidez adieraziko dugun __partizio-funtzio nanokanonikoaren__ eta multzoaren izaeraren isla den banatze-potentzialaren arteko erlazioa idatziko dugu:

$$
  \mathcal{E}(T,p,\mu) := -k_{\mathrm{B}}T\ln \Upsilon \; .
$$ (epspf)

Partizio-funtzio orokortua gainontzekoei kasuan kasuko Legendreren transformazioak aplikatuz kalkulatuko dugu. Esate baterako, multzo isotermo-isobarotik abiatuz,

$$
\Upsilon(T,p,\mu) := \sum_{E,V,N}\Omega(E,V,N)e^{-E/k_{\mathrm{B}}T}e^{-pV/k_{\mathrm{B}}T}e^{\mu N/k_{\mathrm{B}}T} \equiv \sum_{N}\Delta(T,p,N)e^{\mu N/k_{\mathrm{B}}T} \; .
$$ (upsilon_def)

(mupt_linagg)=
### **6.2** Adibidea: Agregatu lineala

Adibide honetako sistema txikia [10](agg). irudian azaltzen da. Multzo makroskopikoa sistema bereizgarriz osaturiko gas diluitua dela onartuko dugu. Horrela, aldakien arteko elkarrekintzak baztergarritzat joko dira, eta askatasun-gradu mekanikoa ez da aintzat hartuko.

```{figure} aggregate.PNG
---
height: 225px
name: agg
---
Agregatu lineala $N$ monomeroz osaturiko $Nm$ masadun eta $Na$ luzeradun hagaxka luzea da. Barne-higidurarekin lotutako $j(T)$ partizio-funtzioa dute unitateek; eta lehen auzokoen arteko elkarrekintza-energia $\epsilon$ da, negatiboa ($N-1$ ekarpen). Berebat, zentrutik igarotzen den ardatzarekiko biratu dezake hagaxkak. Inertzia-momentua $I = \frac{1}{12}N^{3}ma^{2}$ da.
```

Lehenbizi, sistema __multzo kanonikoan__ aztertuko dugu. Biraketari dagokion partizio-funtzioa

$$
Q_{\mathrm{rot}}(T,N) := \frac{4\pi^2}{h^2}I(N)k_{\mathrm{B}}T = \alpha(T)N^3
$$
daukagu.

```{admonition} Oharra
Ikus {cite}`pathria` liburuko 6. kapituluko 11. oin-oharra. Aurrerantzean, $\alpha(T) = \frac{\pi^2ma^2}{3h^2}k_{\mathrm{B}}T$ erabiliko dugu.
```

Unitateen ekarpen intrintsekoarekin zein berorien arteko elkarrekintzekin batera bilduz biraketaren eragina, partizio-funtzio kanonikoa eraikiko dugu. Hala, adierazpenak laburtze aldera $c = \alpha e^{\epsilon/k_{\mathrm{B}}T}$ definituz,

$$
\boxed{Q(T,N) := j(T)^{N} \cdot Q_{\mathrm{rot}}(T,N) \cdot e^{-(N-1)\epsilon/k_{\mathrm{B}}T} = c\;N^3j(T)^N\;e^{-N\epsilon/k_{\mathrm{B}}T}} \quad (N\geq1)\; .
$$ (qagg)

Ohartu gaitezen $N=0$ denean ez dela ez biraketarik ez, are gutxiago, elkarrekintza-energiarik egongo. Hori dela eta, partizio-funtzio intrintsekotik $Q(T,0)=j(T)^0=1$ izango dugu.

####  Ariketa

$(a)$ Kalkulatu $\widehat{\mu}$ eta $\mu$ potentzial kimikoak, baita berorien $N\rightarrow \infty$ limitea ere.

```{dropdown} __Erantzuna__

Partizio-funtzio kanonikoa erabiliz ({eq}`qagg` ekuazioa), eta $N\widehat{\mu} = -k_{\mathrm{B}}T\ln Q(T,N)$ betetzen dela gogora ekarriz,

$$
\left.\begin{array}{l}
\widehat{\mu}=-k_{\mathrm{B}}T\ln j + \frac{N-1}{N} \epsilon - \frac{\ln(\alpha N^3)}{N}k_{\mathrm{B}}T \\\\
\mu=-k_{\mathrm{B}}T\ln j + \epsilon -\frac{3}{N}k_{\mathrm{B}} T
\end{array}\right\}\underset{(N \rightarrow \infty)}{\boldsymbol{\longrightarrow}} \; \mu^{(0)} = -k_{\mathrm{B}}T\ln j + \epsilon
$$ (muagg)

```

$(b)$ Eraiki $S(T,N)/k_{\mathrm{B}}$ adierazpena. Aztertu limite makroskopikoan zer gertatzen den.

```{dropdown} __Erantzuna__

$$
\frac{S(T,N)}{k_{\mathrm{B}}} := -\frac{1}{k_{\mathrm{B}}}\left(\frac{\partial N\widehat{\mu}}{\partial T}\right)_{N} = N\ln j + NT\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} + \color{red}\{\color{black}1 + \ln\left(\alpha N^3\right) \color{red}\}
$$ (stnagg)

Giltza gorrien artean ageri diren ekarpenak biraketari dagozkio, eta tamaina finitukoak dira, limite termodinamikoan aurreko bi gai linealek baitaukate gailentasuna. Badirudi, hortaz, sistema makroskopikoak ez duela biraketaren eragina hautemango, ez eta unitateen arteko $\epsilon$ elkarrekintza ere.
```



Horiek horrela, askatasun-gradu kimikoa abiarazi, eta __multzo nanokanonikora__ igaroko gara. Hala, adierazpenetan $ x  =  je^{\left(\mu-\epsilon\right)/k_{\mathrm{B}}T}$ erlazioa sartuz, eta {eq}`upsilon_def` definizioan {eq}`qagg` ekuazioa txertatuz,

$$
\boxed{\Upsilon(T,\mu) = 1 + c\sum_{N=1}^{\infty}  N^{3}\;x^N = 1 +  c \left[\frac{6x^2}{(x-1)^4} + \frac{x}{(x-1)^2}\right]}\; , \; \vert x \vert < 1 \; ,
$$ (upsilontn)
izango dugu partizio-funtzio orokortua.

```{dropdown} __Seriearen garapena__

Abiatu gaitezen dagoeneko ezaguna dugun honako serie geometriko honetatik:

$$
\sum_{N=1}^{\infty}x^N = \frac{1}{1-x} \; , \; \vert x \vert < 1 \; .
$$

Jarraian, bi aldeen $x$-rekiko deribatuak kalkulatzeaz bat, $x$-rekin biderkatuko ditugu.

$$
\sum_{N=1}^{\infty}Nx^N = \frac{x}{(x-1)^2}
$$

Prozedura berbera segituz, $\sum_{N=1}^{\infty}N^2x^N$ kalkulatu, eta, jarraian, beharrezkoa zaigun $\sum_{N=1}^{\infty}N^3x^N$ berdintza eraikiko dugu:

$$
\sum_{N=1}^{\infty}N^3x^N = \frac{6x^2}{(x-1)^4} + \frac{x}{(x-1)^2} \; .
$$

```

Bertatik, eta {eq}`epspf` berdintza erabiliz,

$$
\mathcal{E}(T,\mu) = -k_{\mathrm{B}}T\ln \left\{1 + c\left[\frac{6x^2}{(x-1)^4} + \frac{x}{(x-1)^2}\right]\right\} \;
$$ (epsagg)
da banatze-potentziala.

Kontuan izan beharrekoa da, {eq}`muagg` ekuazioko $\mu^{(0)}$ potentzialari erreparatuz, $x = e^{({\mu} - \mu^{(0)})/k_{\mathrm{B}}T}$ berridaztea daukagula. Hortaz, limite makroskopikoan $x\rightarrow 1$ beteko da. Azter dezagun, bada, batez besteko partikula-kopuruan $x$ magnitudeak duen eragina.

$$
\bar{N} := -\left(\frac{\partial \mathcal{E}}{\partial \mu}\right)_{T} = c \; x \; P(0)\left[\frac{12 x(x-1)-24 x^{2}}{(x-1)^{5}}-\frac{x+1}{(x-1)^{3}}\right]
$$ (barnagg)

Espero bezala, $\bar{N}(x\rightarrow 1) \rightarrow \infty$ betetzen da. Entropiaren adierazpen berria eraiki, eta {eq}`barnagg` ekuazioaren laguntzaz trinkotuko dugu:

$$
\frac{S(T,\mu)}{k_{\mathrm{B}}} := -\frac{1}{k_{\mathrm{B}}} \left(\frac{\partial \mathcal{E}}{\partial T}\right)_ {\mu}  = \bar{N}\ln j + \bar{N}T\frac{1}{j}\frac{\mathrm{d}j}{\mathrm{d}T} + \left\{ - \bar{N}\ln x - \ln P(0) + cP(0)\left[1-\frac{\epsilon}{k_{\mathrm{B}} T}\right]\left[\frac{6 x^{2}}{(x-1)^{4}}+\frac{x}{(x-1)^{2}}\right] \right\}
$$

(mupt_gi)=
### **6.3** Adibidea: Gas ideal klasikoa, multzo nanokanonikoan
