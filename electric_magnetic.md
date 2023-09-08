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

Aipatu beharrekoa da efektu biak batera aztertzea ez dela kontu erraza. Izan ere, partizio-funtzio kanonikoa eraikitzerakoan, _transferentzia-matrizearen_ metodora jo beharko dugu. Gainera, bertatik eskuratutako adierazpen luzeak ez dira erabilerrazak. Bada, horren ordez, analisia bi zatitian burutuko dugu, bakoitza bere aldetik. Lehenik, {numref}`{number} atalean <b0jnot0>`, lehen auzokoen arteko $\pm J$ lerrokatze-elkarrekintza izango dugu soilik aintzakotzat. Ondoren, {numref}`{number} atalean <j0bnot0>` zatian, aurkakoa egingo dugu: sistemari $\mathbf{B}$ kanpo-eremua ezarriko diogu, eta spinek elkar ikusten ez dutela onartuko dugu $(J=0)$.



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
\overline{E} = \frac{\sum_{n_+ = 0}^{N}E(n_+,N) \; \Omega(n_+,N) \;e^{-E(n_+,N)/k_\mathrm{B}T}}{\sum_{n_+ = 0}^{N}\Omega(n_+,N)\;e^{-E(n_+, N)/k_\mathrm{B}T}} = k_{\mathrm{B}}T^2\frac{\partial}{\partial T}\ln Q \; .
$$ (bar_E_def)

#####  Ariketa

$(a)$ Kalkulatu $\overline{E}$ adierazpena.

```{dropdown} __Erantzuna__

$$
 \overline{E} = -NJ\tanh\frac{J}{k_{\mathrm{B}}T} \; .
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

Multzo kanonikoan entropiak $S(T, N) =\left(\overline{E} - A\right)/T $ betetzen duela gogora ekarriz, hona ailegatuko gara:

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

$(c)$ Banatze-potentzialaren adierazpen horretatik, kalkulatu $S(T,\mu)$ eta $\overline{N}$. Ondoren, birmoldatu entropiaren ekuazioa $S(T,\overline{N}(\mu))$ adierazpenera heltzeko, eta maximizatu berori.

```{dropdown} __Erantzuna__

Hasteko,

$$
S(T,\mu) = -k_\mathrm{B}\ln\left(\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}\right) - \left(\frac{1}{2}\;\frac{\mu}{T}\;e^{-\mu/k_{\mathrm{B}}T} - \frac{J}{T}\;\sinh\frac{J}{k_\mathrm{B}T}\right)\cdot\left(\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}\right)^{-1} \; .
$$(s_tmu_ising)

Spinen kopuruaren batez bestekoa kalkulatzerakoan, adi ibili behar dugu, adierazpenean $\overline{N} + 1$ idatzi behar dugulako, alegia:

$$
\overline{N} + 1 = -\left(\frac{\partial \mathscr{E}}{\partial \mu}\right)_T =\frac{\frac{1}{2} e^{-\mu/k_{\mathrm{B}}T}}{ \frac{1}{2} e^{-\mu/k_{\mathrm{B}}T} -\cosh\frac{J}{k_\mathrm{B}T}} \; .
$$(bar_n_ising)

Horrenbestez, entropiaren adierazpena era honetan berridaztea daukagu:

$$
\boxed{S(T,\overline{N}(\mu)) = \overline{N}\left[ k_{\mathrm{B}}\ln\left(2\;\frac{\overline{N}+1}{\overline{N}}\;\cosh\frac{J}{k_{\mathrm{B}}T}\right) - \frac{J}{T}\;\tanh\frac{J}{k_{\mathrm{B}}T}\right] + k_{\mathrm{B}}\ln\left[2(\overline{N}+1)\right]} \; .
$$ (s_tbarn_ising)

Funtzio horrek ere maximoa du $\frac{J}{k_{\mathrm{B}}T} = 0$ puntuan:

$$
S(T, \overline{N}(\mu))_{\text{max}} = \overline{N}k_{\mathrm{B}}\ln \left(2\frac{\overline{N}+1}{\overline{N}}\right) + k_{\mathrm{B}}\ln\left[2(\overline{N}+1)\right] \; ,
$$ (s_max_nanokano)

zeinaren limite makroskopikoa, berriz ere, $\overline{N}k_{\mathrm{B}}\ln 2$ den.

```

**----------------------------------------------------**

Behin $S(T, n_+)_{\mathrm{max}}$, $S(T, N)_{\mathrm{max}}$ eta $S(T,\overline{N}(\mu))_{\mathrm{max}}$ adierazpenak kalkulatuz gero, adierazgarria litzateke hiruren arteko alderaketa egitea, sistemaren tamainaren araberako bilakaerari erreparatuz:

```{figure} ising_1_s.png
---
height: 350px
name: sn100
---
Lotura-unitateko entropia. Agerikoa da, alde batetik, sistema txikia denean multzo nanokanonikoak entropia handiagoa itzultzen duela. Bestetik, hiru kasuetan $S/N$ magnitudeak ez du izaera intentsiboa eskualde nanotermodinamikoan. Alabaina, limite makroskopikoan, adierazpenek bat egitera joko dute; halaber, intentsibotasuna berreskuratuko da. Kurbak eraikitzeko, {cite}`multiscale` artikuluan aipatzen den $J/k_{\mathrm{B}}T = 1,45$ zenbakia erabili dugu.

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

Bada, $q,\vert\mathbf{E}\vert > 0$ hartuz gero, eremu elektrikoak katearen luzera handituko du; bestela esanda, helize-haril fase trantsizioa areagotu egingo da. Gogora dezagun {numref}`{number} adibidean <helix_coil>` haril-unitateak helize-unitateak baino luzeagoak direla onartu genuela $(l_C>l_H)$. Hori dela eta, $\vert\mathbf{E}\vert \rightarrow \infty$ limitean, $\overline{N}_H/N$ magnitudeak zerorantz joko duela aurresan dezakegu.

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
\frac{\overline{N}_H}{N} = \left(\frac{q_H}{q_C}\right)^N\frac{\exp\frac{N\left(l_H-l_C\right)\left(f+q\vert\mathbf{E}\vert\right)}{k_{\mathrm{B}}T}}{1 + \left[\frac{q_H}{q_C}\exp\frac{N\left(l_H-l_C\right)\left(f+q\vert\mathbf{E}\vert\right)}{k_{\mathrm{B}}T}\right]^N}
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

Aurreko $(a)$ atalean erdietsitako $\widehat{\mu}$-ren ekuazioaren laguntzaz,

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

Nabarmendu beharrekoa da, partizio-funtzio kanonikoa eraikitzen aritu garenean, {eq}`agg_e_q_p0` ekuazioaren bidez askatasun-gradu elektrikoa abiatu dugula. Bada, lorturiko emaitza $\mathbf{E}$ eremuaren moduluaren menpekoa da. Hori dela eta, ingurune-aldagaitzat modulua hartzea daukagu, bektorearen beraren ordez; hartara, haren konjokatua $\mathbf{p}$ momentuaren modulua izango da.


Bertatik eraikiko dugu eskatzen zaigun Maxwellen erlazioa:

$$
\left(\frac{\partial \mu}{\partial \vert\mathbf{E}\vert}\right)_{T,N} = \frac{\partial}{\partial \vert\mathbf{E}\vert} \left(\frac{\partial (\widehat{\mu}N)}{\partial N}\right)_{T,\vert\mathbf{E}\vert} \equiv \frac{\partial}{\partial N} \left(\frac{\partial (\widehat{\mu}N)}{\partial \vert\mathbf{E}\vert}\right)_{T,N} = -\left(\frac{\partial \vert\mathbf{p}\vert}{\partial N}\right)_{T,\vert\mathbf{E}\vert} \; .
$$ (agg_elek_maxwell_1)

Orain, $\mu$ potentzial kimikoaren adierazpen zehatzaren beharrean gaude. Hala, {eq}`agg_e_dmuhat` ekuazioaren bitartez,

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

Ariketa honetan ere, aurreko beste zenbaitetan bezalaxe, azterketa pauso bat haratago eramango dugu, **multzo nanokanonikoan** murgilduz. Partizio-funtzio orokortua {eq}`agg_q_tot` partizio-funtziotik abiatuz eraikiko dugu:

$$
\Upsilon(T,\mu,\vert\mathbf{E}\vert) := 1+ \sum_{N=1}^{\infty}Q(T,N,\vert\mathbf{E}\vert)\;e^{\mu N/k_{\mathrm{B}}T} = 1 +c(T)\left[\sum_{N=1}^{\infty}N^3x^N +\frac{y^2}{6}\sum_{N=1}^{\infty}N^5 x^N\right] \; ,
$$ (agg_e_upsilon)

non, oraingoan, $x(T,\mu,\vert\mathbf{E}\vert) = j(T)\exp\left(\frac{-\epsilon + \mu }{k_{\mathrm{B}}T}\right)\exp\left(\frac{\alpha\vert\mathbf{E}\vert^2}{2k_{\mathrm{B}}T}\right)$ ordezkatu dugun.

Azpimarratu beharrekoa da ezen $\sinh(Ny)$ funtzioaren hurbilketara jotzeak biziki erraztuko duela $N$ magnitudean zeharreko batukariaren kalkulua. Izan ere, ohartu gaitezen batukari bietan $N$-ren berreturak agertzen direla. Horrek seriearen garapena {eq}`upsilontn` ekuazioaren osteko argibideei jarraituz burutzea ahalbidetuko du. Gauzak horrela, 

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

Amaitzeko, begien bistakoa da hirugarren lerroa ekarpen elektrikoari dagokiola bere osotasunean. Nabarmentzekoa da, halaber, $\vert\mathbf{E}\vert^2$ osagaia agertzen dela; hortaz, eremu txikiko limitean ekarpen hori baztergarria da funtsean, aurreko bi lerroetako gaiekiko. Nolanahi dela ere, oharteman dezagun ezen, {numref}`{number} atalean <mupt_linagg>` aipatutako $\epsilon \approx -2,3 \cdot k_{\mathrm{B}}T$ hartuko bagenu, ekarpena zeinuz positiboa litzatekeela; alegia, eskualde nanotermodinamikoan askatasun-gradu elektrikoa abian jartzeak entropia igo egingo du.

Jakina, kanpo-eremua kenduko bagenu, aurreko {eq}`stmuagg` ekuazioa berreskuratuko genuke.