(ising)=
## **8**. Ising-en eredua

_*Adibidea osatzen ari naiz..._

Adibide honetan aztergai izango dugun spin magnetikoz osaturiko sistemak ere abagune egokia eskainiko digu tamaina finituko efektuak aztertzeko. Hain zuzen, Nanotermodinamikaren tresneriaren bitartez,  [17](ising_arrows). irudiko ereduaren benetako oreka termikoa bilatzea dugu erronka.

(ising_arrows)=
```{figure} ising_geziak.png
---
height: 200px
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
height: 200px
name: ising_j
---
  Ising-en spinek lerrokatze magnetikoa hobesten dutela onartuko dugu; alegia, konfigurazio horrek energia magnetikoa minimizatu egingo du. Hartara, noranzko bereko bi lehen auzokok $-J$ elkarrekintza-energia hautemango dute; aurkako noranzkoak erakutsiko balituzte, aldiz, lotze-energia $+J$ litzateke.
```

Arestian azaldutako hurbilketari jarraikiz, demagun sistema $N+1$ spin magnetikoz osatuta dagoela; hartara, orotara $N$ lotura izango ditu (azken kontu hori argitzeko, behatu goiko irudia). Haietatik $n_J$ aurkako noranzkodun spinen arteko loturak dira $(+J)$, eta, beraz, $N-n_J$ noranzko beredun spinen artekoak $(-J)$. Esaterako, [18](ising_1). irudiaren kasuan, $N=10$ eta $n_J = 7$. Hori dela eta, __multzo mikrokanonikoan__ $N$ eta $n_J$ aldagaiak finko dituen sistemaren energia honela idaztea daukagu:

$$
  E_J = n_J J - (N-n_J)J = -(N-2n_J)J \; .
$$ (e_j)

Hurrengo pausoa, guztizko energiaren adierazpen horrekin bateragarriak diren mikroegoeren kopurua kalkulatzea da; hots, zenbat eratan sailka ditzakegun $N$ loturak $n_J$ energia altuko eta $N-n_J$ energia baxuko loturetan. Horretarako, oharteman dezagun [18](ising_1). irudiko gezi guztiak alderanzteak ez liokeela {eq}`e_j` adierazpenari eragingo, $n_J$ magnitudea aldaezin mantenduko bailitzateke; alegia, mikroegoera bakoitza bi aldiz zenbatu beharra daukagu. Gauzak horrela,

$$
\Omega(n_J,N) = 2\cdot \frac{N!}{n_J!\;(N-n_J)!} \;\;\;\; .
$$ (omega_nj)

Segidan, entropiaren ekuazioa idatziko dugu, Stirlingen $\ln(n!)$ serieko aurreneko hiru gaiak ez beste guztiak baztertuz:

$$
\boxed{\frac{S(n_J,N)}{k_\mathrm{B}} = N\ln N - n_J\ln n_J - (N-n_J)\ln(N-n_J) - \frac{1}{2}\ln\left[\frac{\pi}{2}n_J\left(1-\frac{n_J}{N}\right)\right]} \; .
$$




(j0bnot0)=
### **8.2** Spin askeak kanpo-eremuaren eraginpean ($J= 0$, $\mathbf{B}\neq\mathbf{0}$)
