(ising)=
## **8**. Ising-en eredua

_*Adibidea osatzen ari naiz..._

Adibide honetan aztergai izango dugun spin magnetikoz osaturiko sistemak ere abagune egokia eskainiko digu tamaina finituko efektuekin aritzeko. Hain zuzen, Nanotermodinamikaren tresneria sistema magnetikoetara eramanez, [17](ising_arrows). irudiko ereduaren benetako oreka termikoa bilatzea dugu erronka, hura multzo estatistiko mikrokanonikoan, kanonikoan eta, azkenik, nanokanonikoan aztertuz; batik bat, entropiak multzoz multzo duen bilakaerari erreparatuko diogu.

(ising_arrows)=
```{figure} ising_geziak.png
---
width: 650px
name: ising_geziak
---
  Ising-en dimentsio bakarreko katea $N$ spinez osatuta dago. Beroriek $+\mathbf{u}_z$ eta $-\mathbf{u}_z$ noranzkoetan lerrokatu daitezke soilik. Garapenak errazteko, lehen auzokoen arteko $\pm J$ ez beste elkarrekintza-energiak baztertu egingo ditugu ([18](ising_1). irudia).
```

Ising-en sistemaren osagaietako bakoitzek barne-energiari bi ekarpen sorrarazten dizkiote: alde batetik, bi spinen arteko lerrokatze magnetikoaren araberako $\pm J$ delakoa; bestetik, berorietako bakoitzari $\mathbf{m}$ momentu magnetikoa esleituko bagenio, $\mathbf{B}$ kanpo-eremu magnetikoaren ondoriozko $-\mathbf{m}\cdot\mathbf{B}$ elkarrekintza ere izango genuke.

Aipatu beharrekoa da efektu biak batera aztertzea ez dela kontu erraza. Izan ere, partizio-funtzio kanonikoa eraikitzerakoan, _transferentzia-matrizearen_ metodora jo beharko dugu. Gainera, bertatik eskuratutako adierazpen luzeak ez dira erabilerrazak. Bada, horren ordez, analisia bi zatitian burutuko dugu, bakoitza bere aldetik. Lehenik, [8.1](b0jnot0) atalean, lehen auzokoen arteko $\pm J$ lerrokatze-elkarrekintza emango dugu soilik aintzakotzat. Ondoren, [8.2](j0bnot0) atalean, aurkakoa egingo dugu: sistemari $\mathbf{B}$ kanpo-eremua ezarriko diogu, eta spinek elkar ikusten ez dutela onartuko dugu ($J=0$).



(b0jnot0)=
### **8.1** Ising-en kate finitua ($J\neq 0$, $\mathbf{B}=\mathbf{0}$)

Errepara diezaiogun [18](ising_1). irudiari.

(ising_1)=
```{figure} ising_j.png
---
width: 650px
name: ising_j
---
  Ising-en spinek lerrokatze magnetikoa hobesten dutela onartuko dugu; alegia, konfigurazio horrek energia magnetikoa minimizatu egingo du. Hartara, noranzko bereko bi lehen auzokok $-J$ elkarrekintza-energia hautemango dute; aurkako noranzkoak erakutsiko balituzte, aldiz, lotze-energia $+J$ litzateke.
```

Arestian azaldutako hurbilketari jarraikiz, demagun sistema $N+1$ spin magnetikoz osatuta dagoela; hartara, orotara $N$ lotura izango ditu (azken kontu hori argitzeko, behatu goiko irudia). Haietatik $n_+$ aurkako noranzkodun spinen arteko loturak dira $(+J)$, eta, beraz, $N-n_+$ noranzko beredun spinen artekoak $(-J)$. Esaterako, [18](ising_1). irudiaren kasuan, $N=10$ eta $n_+ = 7$. Hori dela eta, __multzo mikrokanonikoan__ $N$ eta $n_+$ aldagaiak finko dituen sistemaren barne-energia honela idaztea daukagu:

$$
  E(n_+, N) = n_+ J - (N-n_+)J = -(N-2n_+)J \; .
$$ (e_j)

Hurrengo pausoa, guztizko energiaren adierazpen horrekin bateragarriak diren mikroegoeren kopurua kalkulatzea da; hots, zenbat eratan sailka ditzakegun $N$ loturak $n_+$ energia altuko eta $N-n_+$ energia baxuko loturetan. Horretarako, oharteman dezagun [18](ising_1). irudiko gezi guztiak alderanzteak ez liokeela {eq}`e_j` adierazpenari eragingo, $n_+$ magnitudea aldaezin mantenduko bailitzateke; alegia, mikroegoera bakoitza bi aldiz zenbatu beharra daukagu. Gauzak horrela,

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

####  Ariketa

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
 = Nk_{\mathrm{B}}\left[\ln\left(2\cosh\frac{J}{k_{\mathrm{B}}T}\right) - \frac{J}{T}\tanh\frac{J}{k_{\mathrm{B}}T}\right]  + k_{\mathrm{B}}\ln 2} \; .
$$ (s_ising_kan)

Entropiak maximoa du $\frac{J}{k_{\mathrm{B}}T} = 0$ denean. Egoera horretara bi bi kasuk eraman gaitzakete; alde batetik, $J=0$ izateak, hau da, spinek elkar ez ikusteak (elkarrekintzarik ez), eta, bestetik, $T\rightarrow \infty$ limiteak. Horiek horrela, entropia

$$
S(T, N)_{\text{max}} = (N+1)k_{\mathrm{B}}\ln 2
$$ (s_max_kano)

genuke. Agerikoa da limite makroskopikoan $(N\rightarrow \infty)$ adierazpen horrek zein {eq}`s_max_micro` ekuazioak $Nk_{\mathrm{B}}\ln 2$ baliora joko luketela. Alabaina, eskualde nanotermodinamikoan tamaina finituko efektuak baztertuko ez bagenitu, $S(T, N)_{\text{max}}$ gailenduko litzateke $S(n_+, N)_ {\text{max}}$ adierazpenarekiko.

```

Bukatzeko, azterketa __multzo nanokanonikora__ eramango dugu.

####  Ariketa

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
\Upsilon (T,\mu)= 2\lambda \sum_{N=0}^{\infty}\left[\left(e^{J/k_\mathrm{B}T} + e^{- J/k_\mathrm{B}T}\right)\lambda\right]^N = \left[\frac{1}{2\lambda} -\cosh\left(\frac{J}{k_\mathrm{B}T}\right)\right]^{-1} \; ,
$$ (upsilon_ising_1)

non $\lambda = e^{\mu/k_{\mathrm{B}}T}$ ordezkatu dugun. Bertatik, banatze-potentzialaren adierazpena berehalakoa da:

$$
\mathcal{E}(T,\mu) = k_\mathrm{B}T\ln\left[\frac{1}{2\lambda} -\cosh\left(\frac{J}{k_\mathrm{B}T}\right)\right] \; .
$$(epsilon_ising)



```




















(j0bnot0)=
### **8.2** Spin askeak kanpo-eremuaren eraginpean ($J= 0$, $\mathbf{B}\neq\mathbf{0}$)
