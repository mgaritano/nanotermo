(elek_mag)=
## Sistema elektrikoak eta magnetikoak

___*Atala osatzen ari naiz...___

(ising)=
### Ising-en eredua


Adibide honetan aztergai izango dugun spin magnetikoz osaturiko sistemak ere abagune egokia eskainiko digu tamaina finituko efektuekin aritzeko. Hain zuzen, Nanotermodinamikaren tresneria sistema magnetikoetara eramanez, {numref}`{number} irudiko <ising_arrows>` ereduaren benetako oreka termikoa bilatzea dugu erronka, hura multzo estatistiko mikrokanonikoan, kanonikoan eta, azkenik, nanokanonikoan aztertuz; batik bat, entropiak multzoz multzo duen bilakaerari erreparatuko diogu.

(ising_arrows)=
```{figure} ising_geziak.png
---
width: 650px
name: ising_geziak
---
  Ising-en dimentsio bakarreko katea $N$ spinez osatuta dago. Beroriek $+\mathbf{u}_z$ eta $-\mathbf{u}_z$ noranzkoetan lerrokatu daitezke soilik. Garapenak errazteko, lehen auzokoen arteko $\pm J$ ez beste elkarrekintza-energiak baztertu egingo ditugu ({numref}`{number} irudia <ising_1>`).
```

Ising-en sistemaren osagaietako bakoitzek barne-energiari bi ekarpen sorrarazten dizkiote: alde batetik, bi spinen arteko lerrokatze magnetikoaren araberako $\pm J$ delakoa; bestetik, berorietako bakoitzari $\mathbf{m}$ momentu magnetikoa esleituko bagenio, $\mathbf{B}$ kanpo-eremu magnetikoaren ondoriozko $-\mathbf{m}\cdot\mathbf{B}$ elkarrekintza ere izango genuke.

Aipatu beharrekoa da efektu biak batera aztertzea ez dela kontu erraza. Izan ere, partizio-funtzio kanonikoa eraikitzerakoan, _transferentzia-matrizearen_ metodora jo beharko dugu. Gainera, bertatik eskuratutako adierazpen luzeak ez dira erabilerrazak. Bada, horren ordez, analisia bi zatitian burutuko dugu, bakoitza bere aldetik. Lehenik, {numref}`{number} atalean <b0jnot0>`, lehen auzokoen arteko $\pm J$ lerrokatze-elkarrekintza emango dugu soilik aintzakotzat. Ondoren, {numref}`{number} atalean <j0bnot0>` zatian, aurkakoa egingo dugu: sistemari $\mathbf{B}$ kanpo-eremua ezarriko diogu, eta spinek elkar ikusten ez dutela onartuko dugu $(J=0)$.



(b0jnot0)=
#### Ising-en katea, $J$ elkarrekintza-energiaren eraginpean

Errepara diezaiogun {numref}`{number} irudiari <ising_1>`.

(ising_1)=
```{figure} ising_j.png
---
width: 650px
name: ising_j
---
  Ising-en spinek lerrokatze magnetikoa hobesten dutela onartuko dugu; alegia, konfigurazio horrek energia magnetikoa minimizatu egingo du. Hartara, noranzko bereko bi lehen auzokok $-J$ elkarrekintza-energia hautemango dute; aurkako noranzkoak erakutsiko balituzte, aldiz, lotze-energia $+J$ litzateke.
```

Arestian azaldutako hurbilketari jarraikiz, demagun sistema $N+1$ spin magnetikoz osatuta dagoela; hartara, orotara $N$ lotura izango ditu (azken kontu hori argitzeko, behatu goiko irudia). Haietatik $n_+$ aurkako noranzkodun spinen arteko loturak dira $(+J)$, eta, beraz, $N-n_+$ noranzko beredun spinen artekoak $(-J)$. Esaterako, {numref}`{number} irudiaren <ising_1>` kasuan, $N=10$ eta $n_+ = 7$. Hori dela eta, __multzo mikrokanonikoan__ $N$ eta $n_+$ aldagaiak finko dituen sistemaren barne-energia honela idaztea daukagu:

$$
  E(n_+, N) = n_+ J - (N-n_+)J = -(N-2n_+)J \; .
$$ (e_j)

Hurrengo pausoa, guztizko energiaren adierazpen horrekin bateragarriak diren mikroegoeren kopurua kalkulatzea da; hots, zenbat eratan sailka ditzakegun $N$ loturak $n_+$ energia altuko eta $N-n_+$ energia baxuko loturetan. Horretarako, oharteman dezagun {numref}`{number} irudiko <ising_1>` gezi guztiak alderanzteak ez liokeela {eq}`e_j` adierazpenari eragingo, $n_+$ magnitudea aldaezin mantenduko bailitzateke; alegia, mikroegoera bakoitza bi aldiz zenbatu beharra daukagu. Gauzak horrela,

$$
\Omega(n_+,N) = 2\cdot \frac{N!}{n_+!\;(N-n_+)!} \;\;\;\; .
$$ (omega_nj)

Segidan, entropiaren ekuazioa idatziko dugu, Stirlingen $\ln(n!)$ serieko aurreneko hiru gaiak ez beste guztiak baztertuz:

$$
\boxed{\frac{S(n_+,N)}{k_\mathrm{B}} = N\ln N - n_+\ln n_+ - (N-n_+)\ln(N-n_+) - \frac{1}{2}\ln\left[\frac{\pi}{2}n_+\left(1-\frac{n_+}{N}\right)\right]} \; .
$$ (s_ising_micro)

Gaineko {eq}`s_ising_micro` ekuazioak dioskunaren arabera, entropiak maximora joko du $n_+$ loturen kopuruaren erdia den kasuan, eta, hartara, sistemak magnetizazioa galtzean $(E = 0)$, hau da:

$$
S(n_+, N)_ {\text{max}} = S(N/2, N) = Nk_\mathrm{B}\ln 2 - \frac{1}{2}k_\mathrm{B}\ln\left(\frac{\pi}{8}N\right) \; .
$$ (s_max_micro)


Aurrerago, askatasun-graduak abiaraziz goazen heinean, azkenengo bi adierazpen horiek birkalkulatuko ditugu, emaitzen arteko erkaketak egite aldera.

__Multzo kanonikora__ igaroko gara orain. Horretarako, $E(n_+)$ energia batukarian dagokion mikroegoeren sortarekin sartuz, eta Boltzmannen faktorea aintzat hartuz, partizio funtzioa eraikiko dugu:

$$
Q(T, N) = \sum_{n_+ = 0}^{N}\Omega(n_+,N)\;e^{-E(n_+, N)/k_\mathrm{B}T}
$$

Goiko {eq}`e_j` eta {eq}`omega_nj` adierazpenak ordezkatuz, eta ekuazioak moldatuz, hona iritsiko gara:

$$
Q(T, N) = 2 \sum_{n_+ = 0}^{N} \frac{N!}{n_+!\;(N-n_+)!}\left(e^{- J/k_\mathrm{B}T}\right)^{n_+}\left(e^{ J/k_\mathrm{B}T}\right)^{N-n_+} = 2\left(e^{- J/k_\mathrm{B}T} + e^{ J/k_\mathrm{B}T}\right)^N \; .
$$ (q_ising)

```{admonition} Oharra
Azkenengo ekuazioa eraikitzeko, binomioaren identitatea erabili dugu:

$$
(x+y)^N = \sum_{k=0}^{N} \frac{N!}{k!\;(N-k)!}\; x^k\; y^{N-k}
$$
```
Bertatik, hasteko, sistemaren barne energiaren batez bestekoa kalkulatuko dugu, honako berdintza honi jarraituz:

$$
\bar{E} = \frac{\sum_{n_+ = 0}^{N}E(n_+,N) \; \Omega(n_+,N) \;e^{-E(n_+,N)/k_\mathrm{B}T}}{\sum_{n_+ = 0}^{N}\Omega(n_+,N)\;e^{-E(n_+, N)/k_\mathrm{B}T}} = k_{\mathrm{B}}T^2\frac{\partial}{\partial T}\ln Q \; .
$$ (bar_E_def)

#####  Ariketa

$(a)$ Kalkulatu $\bar{E}$ adierazpena.

```{dropdown} __Erantzuna__

$$
 \bar{E} = -NJ\tanh\frac{J}{k_{\mathrm{B}}T} \; .
$$ (bar_E)

```

$(b)$ Jarraian, kalkulatu Helmholtz-en energia askea.

```{dropdown} __Erantzuna__

$$
A(T, N) = -Nk_{\mathrm{B}}T\left[\ln\left(2\cosh\frac{J}{k_{\mathrm{B}}T}\right) + \frac{1}{N}\ln 2\right] \; .
$$ (hehlmholtz_ising)

```

$(c)$ Aurreko bi ekuazioez baliatuz, eraiki entropiaren $S(T,N)$ adierazpena. Jarraian, kalkulatu maximoa, eta alderatu emaitza {eq}`s_max_micro` ekuazioarekin.

```{dropdown} __Erantzuna__

Multzo kanonikoan entropiak $S(T, N) =\left(\bar{E} - A\right)/T $ betetzen duela gogora ekarriz, hona ailegatuko gara:

$$
\boxed{S(T,N)
 = N\left[k_{\mathrm{B}}\ln\left(2\cosh\frac{J}{k_{\mathrm{B}}T}\right) - \frac{J}{T}\tanh\frac{J}{k_{\mathrm{B}}T}\right]  + k_{\mathrm{B}}\ln 2} \; .
$$ (s_ising_kan)

Entropiak maximoa du $\frac{J}{k_{\mathrm{B}}T} = 0$ denean. Egoera horretara bi bi kasuk eraman gaitzakete; alde batetik, $J=0$ izateak, hau da, spinek elkar ez ikusteak (elkarrekintzarik ez), eta, bestetik, $T\rightarrow \infty$ limiteak. Horiek horrela, entropia

$$
S(T, N)_{\text{max}} = (N+1)k_{\mathrm{B}}\ln 2
$$ (s_max_kano)

genuke. Agerikoa da limite makroskopikoan $(N\rightarrow \infty)$ adierazpen horrek zein {eq}`s_max_micro` ekuazioak $Nk_{\mathrm{B}}\ln 2$ baliora joko luketela. Alabaina, eskualde nanotermodinamikoan tamaina finituko efektuak baztertuko ez bagenitu, $S(T, N)_{\text{max}}$ gailenduko litzateke $S(n_+, N)_ {\text{max}}$ adierazpenarekiko.

```

**----------------------------------------------------**

Bukatzeko, azterketa __multzo nanokanonikora__ eramango dugu.

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
\mathscr{E}(T,\mu) = k_\mathrm{B}T\ln\left(\frac{1}{2\lambda} -\cosh\frac{J}{k_\mathrm{B}T}\right) \; .
$$(epsilon_ising)



```

$(c)$ Banatze-potentzialaren adierazpen horretatik, kalkulatu $S(T,\mu)$ eta $\bar{N}$. Ondoren, birmoldatu entropiaren ekuazioa $S(T,\bar{N}(\mu))$
adierazpenera heltzeko.

```{dropdown} __Erantzuna__

Hasteko,

$$
S(T,\mu) = -k_\mathrm{B}\ln\left(\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}\right) - \left(\frac{1}{2}\;\frac{\mu}{T}\;e^{-\mu/k_{\mathrm{B}}T} - \frac{J}{T}\;\sinh\frac{J}{k_\mathrm{B}T}\right)\cdot\left(\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}\right)^{-1} \; .
$$(s_tmu_ising)

Spinen kopuruaren batez bestekoa kalkulatzerakoan, adi ibili behar dugu, adierazpenean $\bar{N} + 1$ idatzi behar dugulako, alegia:

$$
\bar{N} + 1 = -\left(\frac{\partial \mathscr{E}}{\partial \mu}\right)_T =\frac{\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T}}{ \frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}} \; .
$$(bar_n_ising)

Horrenbestez, entropiaren adierazpena era honetan berridaztea daukagu:

$$
\boxed{S(T,\bar{N}(\mu)) = \bar{N}\left[ k_{\mathrm{B}}\ln\left(2\;\frac{\bar{N}+1}{\bar{N}}\;\cosh\frac{J}{k_{\mathrm{B}}T}\right) - \frac{J}{T}\;\tanh\frac{J}{k_{\mathrm{B}}T}\right] + k_{\mathrm{B}}\ln\left[2(\bar{N}+1)\right]} \; .
$$ (s_tbarn_ising)

```

**----------------------------------------------------**

Behin $S(T, N)$ eta $S(T,\bar{N}(\mu))$ adierazpenak kalkulatuz gero, adierazgarria litzateke bien arteko alderaketa egitea, sistemaren tamainaren araberako bilakaerari erreparatuz:

```{figure} ising_1_s.png
---
height: 350px
name: sn100
---
Lotura-unitateko entropia. Agerikoa da, alde batetik, sistema txikia denean multzo nanokanonikoak entropia handiagoa itzultzen duela. Bestetik, bi kasuetan $S/N$ magnitudeak ez du izaera intentsiboa eskualde nanotermodinamikoan. Alabaina, limite makroskopikoan, bi adierazpenek bat egitera joko dute; halaber, intentsibotasuna berreskuratuko da. Kurbak eraikitzeko, {cite}`multiscale` artikuluan ageri den $J/k_{\mathrm{B}}T = 1,45$ zenbakia erabili dugu.

```


















(j0bnot0)=
#### Spin askeak, $\mathbf{B}$ kanpo-eremuaren eraginpean








(heco_elek)=
### Helize-haril trantsizioa, $\mathbf{E}$ kanpo-eremuaren eraginpean

Sistema elektrikoak aztertzean, aldagai-pare berri batekin arituko gara: $\mathbf{E}$ eremu elektrikoa, eta haren konjokatu estentsiboa den sistemaren momentu dipolar elektrikoa, $\mathbf{p}$. Gauzak horrela, adibide honetan, {numref}`{number} irudiko <heco>` "helize-haril" kate eraldatua izango dugu aztergaitzat ({numref}`{number} irudia <heco_e>`).

```{figure} heco_efield.jpg
---
height: 200px
name: heco_e
---
  “Helize-haril” kateari $\pm q$ kargak erantsi dizkiogu mutur banatan. Hori dela eta, katean barrena $\vert\mathbf{p}\vert = ql$ momentu dipolar elektrikoa azaleratuko da, non $l$ katearen luzera den. Halaber, helize eta haril unitate bakoitzari $\alpha$ polarizabilitatea esleituko diogu. Bada, $\mathbf{E}$ eremu elektrikoa ezarriz gero $(\mathbf{E} \parallel \mathbf{p})$, bi faktore horiek ekarpen energetikoa izango dute, segidan zehaztuko dugun legez.
```

Bada, $q,\vert\mathbf{E}\vert > 0$ hartuz gero, eremu elektrikoak katearen luzera handituko du; bestela esanda, helize-haril fase trantsizioa areagotu egingo da. Gogora dezagun {numref}`{number} adibidean <helix_coil>` haril-unitateak helize-unitateak baino luzeagoak direla onartu genuela $(l_C>l_H)$. Hori dela eta, $\vert\mathbf{E}\vert \rightarrow \infty$ limitean, $\bar{n}_H/N$ magnitudeak zerorantz joko duela aurresan dezakegu.

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
Q(T,l,N,\vert\mathbf{E}\vert) = Q(T,l,N)\exp\left(\frac{lq\vert\mathbf{E}\vert}{k_{\mathrm{B}}T}\right)\exp\left(\frac{N\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right) \; .
$$ (heco_e_q)


Hori aintzat hartuz, multzo isotermo-isobarora igaroko gara:

$$
\Delta(T,f,N,\vert\mathbf{E}\vert) = \sum_{l}Q(T,l,N,\vert\mathbf{E}\vert)\;e^{fl/k_{\mathrm{B}}T} = \exp\left(\frac{N\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right)\sum_{l}Q(T,l,N)\;e^{(q\vert\mathbf{E}\vert+f)l/k_{\mathrm{B}}T} \; ,
$$ (heco_e_delta)

edo,

$$
\Delta(T,f,N,\vert\mathbf{E}\vert) = \exp\left(\frac{N\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right) \Delta(T,f + q\vert\mathbf{E}\vert,N) \; .
$$ (heco_e_delta_2)

Bada, {numref}`{number} adibidean <helix_coil>` erabilitako hurbilketari eutsiz gero (unitate guztiak $H$ egoeran edo unitate guztiak $C$ egoeran), bertan eraikitako $\Delta$ partizio-funtzioaren adierazpenak bere horretan jarraituko du, hots,

$$
\Delta(T,f,N,\vert\mathbf{E}\vert) = \exp\left(\frac{N\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right) \; r_C^N\left(1+r^N\right) \; .
$$ (heco_e_delta_3)

Alabaina, $r_C$, $r_H$ eta $r$ magnitudeak moldatu beharko ditugu:

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

Ohartu gaitezen, $\alpha$ polarizabilitatearen energiarako ekarpena $N$-rekiko lineala denez, banatze-potentzialaren adierazpena ez dela aldatu ({eq}`epsilonhelix` ekuazioa).

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

Goiko {eq}`heco_e_delta_3` partizio-funtzioaren bidez kalkuluak egindakoan, {eq}`heco_e_pbar` ekuazioko kortxeteen arteko adierazpena lortuko dugu.

```
**----------------------------------------------------**

Berrazterketa labur honi buru emateko, arestian aipatutako kontuari helduko diogu. Helize-unitateen batez besteko frakzioaren {eq}`fraction_N` ekuazioan $r$ magnitudearen definizio berria ordezkatuz,

$$
\frac{\bar{n}_H}{N} = \left(\frac{q_H}{q_C}\right)^N\frac{\exp\frac{N\left(l_H-l_C\right)\left(f+q\vert\mathbf{E}\vert\right)}{k_{\mathrm{B}}T}}{1 + \left[\frac{q_H}{q_C}\exp\frac{N\left(l_H-l_C\right)\left(f+q\vert\mathbf{E}\vert\right)}{k_{\mathrm{B}}T}\right]^N}
$$ (heco_e_nbar)

izango dugu. Agerikoa da, $l_H-l_C<0$ betetzen denez, helize-unitateen frakzioak modu esponentzialean joko duela zerorantz, $\mathbf{E}$ eremu elektrikoaren modulua handiagotzen dugun neurrian. Ondorioz, haril-unitateen frakzioak gora egingo du, eta, aurreko arrazoinamendua dela bide, katearen batez besteko luzerak ere bai.

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

Esanak esan, orain ere $Q(T,N,\vert\mathbf{E}\vert)$ partizio-funtzio kanonikoa eraikitzeari ekin behar diogu. Horretarako, alde batetik, {numref}`{number} irudia <agg_e>` atalean aurkeztutako ekarpenak hartuko ditugu gogoan: monomeroen $j(T)$ partizio-funtzio intrintsekoa, agregatuaren biraketa eta lehen auzokoen arteko elkarrekintza biltzen dituen {eq}`qagg` ekuazioa:

$$
Q_0(T,N) = c(T)\;N^3j(T)^N\;e^{-N\epsilon/k_{\mathrm{B}}T} \quad (N\geq 1) \; .
$$ (agg_e_q0)

Bestetik, ekarpen elektrikoa kalkulatu behar dugu. Agregatuak orotara $N$ unitate dituela aintzat hartuz, $\alpha$ polarizabilitatearen ondoriozko partizio-funtziorako ekarpena aurreko ataleko berbera da, alegia, {eq}`u_alpha_heco` ekuaziotik eskuratu duguna. Aitzitik, unitateko $\mathbf{p_0}$ momentu intrintsekoa eta $\mathbf{E}$ kanpo-eremua ez direnez paraleloak, hari datxekion gaiaren kalkulua ez da jada tribiala. Izan ere, orain 

$$
 U_{p_0}(\theta) = -Np_0\vert\mathbf{E}\vert \cos \theta
$$ (agg_e_u_p0)

dugu. 

Kontua da $\mathbf{p_0}$ bektorearen orientazioa hartu behar dugula aintzakotzat. Kanpo-eremurik jarri ezean, bektore horren edozein orientaziok probabilitate bera du $(\theta,\varphi)$ koordenatuen espazioan. Hori dela eta, momentuaren orientazioa $\mathrm{d}\theta\;\mathrm{d}\varphi$ tartean aurkitzeko probabilitatea $\sin\theta\;\mathrm{d}\theta\;\mathrm{d}\varphi$ angelu solido diferentzialarekiko proportzionala da. Alabaina, kanpo-eremua ezarriz gero, $U_{p_0}(\theta)$ elkarrekintza-energia tarteko, orientazio jakin batzuk hobetsiko dira beste batzuen aldean. Hitzez esandakoa jarraian datorren partizio-funtzio normalizatuan islatuko dugu, hain zuzen, angelu solido diferentzialean zehar integratuz:

$$
 Q_{p_0} = \frac{\int_0^{2\pi}\mathrm{d}\varphi\int_0^{\pi}\mathrm{d}\theta\;\sin \theta \; e^{-U_{p_0}(\theta)/k_\mathrm{B}T}}{\int_0^{2\pi}\mathrm{d}\varphi\int_0^{\pi}\mathrm{d}\theta\;\sin \theta} = \frac{1}{2}\int_0^{\pi}\mathrm{d}\theta\;\sin \theta \exp\left(\frac{Np_0\vert\mathbf{E}\vert \cos \theta}{k_\mathrm{B}T}\right) = \frac{\sinh (Ny)}{Ny} \; ,
$$ (agg_e_q_p0)

non $y = p_0\vert\mathbf{E}\vert/(k_\mathrm{B}T)$ den.

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

Bada, {eq}`agg_q_tot` ekuaziotik abiatuz, **multzo kanonikoan** aldagai termondinamikoak lortzeari ekingo diogu.

##### Ariketa

$(a)$ Kalkulatu $\widehat{\mu}$ eta $\mu$ potentzial-kimikoak, baita $\mu^{(0)}$ limitea ere. Horiekin batera, idatzi banatze-potentzialak beteko duen ekuazioa.

```{dropdown} __Erantzuna__

$$
\left.\begin{array}{l}
\frac{\widehat{\mu}}{k_{\mathrm{B}}T} = -\frac{\ln Q}{N} = -\ln j + \frac{N-1}{N} \frac{\epsilon}{k_{\mathrm{B}}T} - \frac{\ln(\xi N^3)}{N} - \frac{\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T} - \frac{1}{N}\ln\left(1 + \frac{N^2y^2}{6}\right) \\\\
\frac{\mu}{k_{\mathrm{B}}T} = -\ln j + \frac{\epsilon}{k_{\mathrm{B}}T} - \frac{3}{N} - \frac{\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T} - \frac{2Ny^2}{6+N^2y^2}
\end{array}\right\}\underset{(N \rightarrow \infty)}{\boldsymbol{\longrightarrow}} \; \frac{\mu^{(0)}}{k_{\mathrm{B}}T} = -\ln j + \frac{\epsilon}{k_{\mathrm{B}}T} - \frac{\alpha \vert\mathbf{E}\vert^2}{2k_\mathrm{B}T} 
$$ (muagg)



```


$(b)$ Kalkulatu entropiaren $S(T,N,\vert\mathbf{E}\vert)$ adierazpena.

$(c)$ Kalkulatu $\overline{\vert\mathbf{p}\vert}$ magnitudea, {eq}`agg_e_approx` ekuazioko hurbilketa **erabili barik**.