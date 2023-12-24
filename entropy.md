(entropy)=
## _B Entropiaren esangura_

Eranskin honen helburua entropiaren izaera gainerako aldagai estentsiboena ez bezalakoa dela ikusaraztea da
{cite}`hill, entropy`. Horretarako, sarreran aurkeztutako Boltzmannen adierazpenetik abiatuko gara: $S = k_{\mathrm{B}}\ln\Omega$. Bada, demagun $\mathscr{N}$ sistemaz osaturiko multzoa dugula. Beroriek $n$ egoera kuantikotan banatuko ditugu. Horietako bakoitzean $\mathscr{N} _ {i}$ sistema egongo da, eta $\sum_{i=1}^{n} \mathscr{N}_ {i} = \mathscr{N}$. Era berean, $p_{i} = \mathscr{N}_{i}/\mathscr{N}$ definituko dugu, hots, partikula bat $i$ egoeran egoteko probabilitatea. Aldaki guztiak baliokideak, askeak eta bereizgarriak direnez,

$$
\Omega = \frac{\mathscr{N} !}{\mathscr{N} _ {1}!\cdot ... \cdot \mathscr{N}_{n}!}
$$ (omega_ent)

idaztea zilegi da. Aldaki-kopuruak $\mathscr{N}\rightarrow\infty$ betetzen duela onartuz, Stirlingen hurbilketa erabiltzea daukagu: $\ln \mathscr{N}! \approx \mathscr{N}\ln\mathscr{N} - \mathscr{N}$. Beraz,

$$
\ln\Omega \approx \mathscr{N}\ln\mathscr{N} - \sum_{i=1}^{n}\mathscr{N} _ {i}\ln\mathscr{N}_{i} \; .
$$ (ln_omega_ent)

Eragiketak eginez gero, guztizko entropia era honetan berridatziko dugu:

$$
 S_{t} = -\mathscr{N}k_{\mathrm{B}}\sum_{i=1}^{n}\frac{\mathscr{N}_ {i}}{\mathscr{N}}\ln \left(\frac{\mathscr{N}_ {i}}{\mathscr{N}}\right) = \mathscr{N}\left(-k_{\mathrm{B}}\sum_{i=1}^{n}p_{i}\ln p_{i}\right) = \mathscr{N}S \; .
 $$ (entropy_def)

 Lortu berri dugun ekuaziotik bi ondorio nagusi atera daiteke: aldakien $S$ magnitudea _batukorra_ da (estentsiboa), ez haatik propietate mekaniko baten batez bestekoa. Hain zuzen, egoera kuantiko bakarrari ezin dakioke entropia jakina egokitu, berori sistema txiki guztietan zeharreko probabilitate-banaketaren baitan dago eta.

 Ekuazioak berak aditzera ematen duenez, makroegoerarekin bateragarriak diren mikroegoeren kopurua altua balitz, probabilitate-banaketa nahikoa uniformea litzateke, hots, mikroegoera jakin baten (edo batzuen) eskuragarritasuna ez litzateke gainontzekoenekiko gailenduko. Hala, $p_{i}$ guztiak arras txikiak lirateke eta, hortaz, berorien logaritmoak moduluz izugarriak, baina zero azpitik, entropiaren igoera indartuz. Aitzitik, bakarrik egoera gutxi batzuk baldin baleude baimenduta, $S_{t}$ guztizko entropiak behera legike $(p_{i}\rightarrow 1)$, sistemaren ordena estatistikoa eta, funtsean, aurresangarritasuna, areagotuz.

 Esandakoa aintzat hartuz, azpisistema bakoitzak batez besteko $\overline{S}$ balio baten inguruko entropia jakin bat duela iradokitzea ez dator bat magnitude honen izaerarekin.
