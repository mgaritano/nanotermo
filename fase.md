(fase)=
## **5**. Sistema txikietako fase-trantsizioak

Aparteko zati honetan, tamaina finituko efektuek bi oreka-egoeren arteko fase-trantsizioaren jokamoldeari dakarzkioten berezitasunen inguruan jardungo dugu.

(itzul)=
###  Itzulgarritasuna eta oreka-baldintzak

Hill-en teoriari segituz, $\mathcal{N}(\rightarrow \infty)$ aldakiz osaturiko multzo makroskopikoa aztertuko dugu. Azpisistemei ez diegu askatasun-gradurik abiaraziko, hau da, erabat isolatuta daude, eta ($E,V,N$) sorta esleituko diegu. Termodinamikaren bigarren legeak dioenez  {cite}`st`, sistemak, lehen oreka-egoeratik bigarreneranzkora bidean, prozesu infinitesimal itzulezinak pairatuko ditu. Beroriek entropiari ekarpen positiboak sorraraziko dizkiote ($\mathrm{d}S_{t}>0$), harik eta oreka berrezartzen den arte ($\mathrm{d}S_{t}=0$). Aurrerantzean jazoko den aldaketa oro itzulgarria izango da, sistemak oreka-egoera berriari eutsiko baitio.

Oro har, prozesu espontaneo bat [6](esp). irudiaren bidez ereduzta daiteke. Hasiera batean, kanpo-oztopo baten eraginpean dago sistema. Ondorioz, egoera kuantiko posible guztietatik soilik batzuk edukiko du eskuragai: $\Omega_{i}(E,V,N)$.
Kanpo-galarazpen hori kenduz gero, sistemaren egoera aldatu egingo da. Hain zuzen, aldakiek aurrez debekatuta egon diren egoeretara ere sarbidea izango dute; hortaz, bukaeran, $\Omega_{f}(E,V,N) > \Omega_{i}(E,V,N)$ izango dugu. Aktibazio-energiaren gutxitzearen edo potentzial baten minimizazioaren bidez gauzatu daiteke prozesu hori.
Hasierako eztabaidaren harira, entropia maximizatzeak energia askea minimizatzea dakar.

```{figure} esp.PNG
---
height: 200px
name: esp
---
  Prozesu espontaneoaren ereduztapena.  Gasak kutxaren ezkerraldetik alde egitea ekiditen du bereizte-hormak. Amaieran ez dago hormarik, eta, horren eraginez, bolumenaren osotasunera hedatu da gasa, era espontaneoan. Hasieratik bukaerara, entropia igo egin da.
```

Entropiak $S_{t} = \mathcal{N}k_{\mathrm{B}}\ln \Omega$ betetzen duenez, prozesu finitu eta espontaneoa amaitutakoan,

$$
\Delta S_{t} = S_{f}^{t} - S_{i}^{t} = \mathcal{N}k_{\mathrm{B}}\ln\left(\frac{\Omega_f}{\Omega_i}\right) > 0 \; .
$$ (sesp)

Termodinamikaren lege garrantzitsuenetariko baten esangura biltzen du ekuazio horrek. Hain zuzen, aurkako prozesua era espontaneoan jazoko balitz, $\Delta S_{t} < 0$ izango genuke, eta bigarren printzipioa hautsiko litzateke. Hala eta guztiz ere, $\mathcal{N} \rightarrow \infty$ onartu dugunez, **multzoan**, alegia, sistema guzti-guztietan,  horrelakorik gertatzeko probabilitatea kasik nulua da, hau da,

$$
 P_{f \rightarrow i}^{t} := \frac{\Omega_{i}}{\Omega_{f}} = \exp\left(-\frac{\Delta S_{t}}{\mathcal{N}k_{\mathrm{B}}}\right) \rightarrow 0 \; .
 $$ (probcont)

 Alabaina, **azpisistemetan**, $\mathcal{N}$ barik $N$ izango genuke, eta, beraz, $ P_{f\rightarrow i}\propto e^{-N}$. Bada, $N$ magnitudeak ez du zertan izan adierazpenaren balioa baztergarri bihurrarazteko bezain handia. Hori dela eta, $N$ oso txikia bada, baliteke sistema txiki jakin batzuetan bigarren printzipioa urratzen duen ($\Delta S < 0$) aurkako prozesua era espontaneoan behatzea! Nolanahi ere, dakargun gogora aldakien propietateak multzotik ondorioztatzean datzala Hill-en teoria. Beraz, hasteko, multzo osoaren entropiaren aldakuntzari erreparatu beharko diogu, eta bertatik sistema txikietara igaro, $\Delta S = \Delta S_{t}/\mathcal{N}$  betetzen dela aintzat hartuz.

 Eztabaida honen harira, [6.4](tpmu) atalean sistema txikiz osatutako multzoaren banatze-prozesua aztertuko dugu. Berebat, $\mathcal{E}$ banatze-potentzialak prozesu horren itzulgarritasunean duen eraginari erreparatuko diogu.
