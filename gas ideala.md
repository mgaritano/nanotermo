(gitvn)=
## **_C_** _Gas ideal klasikoa, multzo kanonikoan_

Aztergai dugun sistema $V$ bolumenean dagoen eta $N$ partikula monoatomiko aske eta bereizezinek osatzen duten gasa da. Baldintza horiek nabarmen arinduko digute lana, aintzakotzat hartu beharreko energiarako ekarpena zinetikoa besterik ez baita izango: $H(q,p) = \sum_{i=1}^N \frac{p_{i}^2}{2m_{i}}$.

Azterketa fase-espazioan abiatu dugu;  partikula bakarraren posizio- eta momentu-koordenatuak $(q_{i},p_{i})$ dira. Bada, egoera kuantiko baten eta fase-espazioko bolumen-elementu baten arteko erlazioa $\mathrm{d}^{3N}q\;\mathrm{d}^{3N}p/(N!h^{3N})$ denez, partizio-funtzioa eraikiko dugu, {cite}`pathria` liburuari jarraituz eta $\Lambda = h/\sqrt{2\pi mk_{\mathrm{B}}T}$ uhin-luzera termikoa dugula gogora ekarriz.

$$
Q(T, V, N)=\frac{1}{N ! h^{3 N}} \int \prod_{i=1}^{N} \mathrm{d}^{3} q_{i} \; \mathrm{d}^{3} p_{i} \; \exp\left({-\frac{1}{k_{\mathrm{B}}T} \frac{ p_{i}^2}{2 m}}\right)  = \frac{V^N}{N!\Lambda^{3N}}\; .
$$ (qtvngi)

Hala, Helmholtzen energia askea idatziko dugu.

$$
A(T,V,N) = k_{\mathrm{B}}T\left(N\ln\frac{\Lambda^3}{V} + \ln N!\right)
$$ (atvngi)

Aurrera egin aurretik, jabetu gaitezen adierazpenean $N!$ ageri zaigula. Limite termodinamikoan $\ln N! \sim N\ln N - N$ hurbilketa badarabilgu ere, Nanotermodinamikan haratago joan beharrean gaude. Horretarako, lehenbizi Stirlingen seriea idatziko dugu.

$$
\small \ln N! = N \ln N-N+ \ln \sqrt{2 \pi N}+\frac{1}{12 N}-\frac{1}{360 N^{3}}+\frac{1}{1260 N^{5}}-\frac{1}{1680 N^{7}}+\cdots
$$ (stirling)

Kontua da $N$ txikia denean, {eq}`stirling` ekuazioko eskuinaldeko lehen bi gaiez bestalde, hirugarrena eta laugarrena ere kontuan izan beharko ditugula, gutxienez. Hartutako erabakia entropian islatuko dugu:

$$
\boxed{ S(T,V,N) = N k_{\mathrm{B}} \left[\ln \left(\frac{V}{\Lambda^{3} N}\right)+\frac{5}{2}\right]- k_{\mathrm{B}}\left[ \ln \sqrt{2 \pi N} + \frac{1}{12N}\right]} \; .
$$ (stvngi)

Horrela, azken bi ekarpen _txikiek_ entropia txikituko dutela ohartuko gara, eta batik bat eskualde nanotermodinamikoan izango dute eragina. Bide batez, banatze-potentzialari ere erreparatuko diogu. $A(T,V,N)$ energiari Legendreren bi transformazio aplikatuz, $\mathscr{E}(T,p,\mu) = A +pV - \mu_{N} N$ dugu. Alde batetik, gas idealak $pV=Nk_{\mathrm{B}}T$ betetzen du. Bestetik, $\mu_{N}$ delakoa diferentzia-ekuazio baten bidez definituko dugu: $ \mu_{N} = A_{N+1}-A_{N}$. Sistema oso txikien kasuan berori ekuazio diferentziala baino aproposagoa da.

```{admonition} Oharra
Hillen liburuan azaltzen denez {cite}`hill`, $N$ aldagai diskretutzat hartu behar da $N< \mathcal{O}(50)$ denean.

```
Era berean, Taylorren hurbilketa erabiliko dugu ($N+1 \rightarrow N$). Ondorioz,

$$
\mu_{N} = -k_{\mathrm{B}}T\ln\left(\frac{1}{N+1}\frac{V}{\Lambda^3}\right) \approx -k_{\mathrm{B}}T\left[\ln\left(\frac{V}{\Lambda^3 N}\right) - \frac{1}{N} + \frac{1}{2N^2}\right] \; .
$$

Behin potentzial kimikoa finkatuz gero, banatze-potentziala eraikitzeko gai izango gara:

$$
\mathscr{E} (T,V,N) \approx k_{\mathrm{B}}T\left[\ln\left(\frac{\sqrt{2\pi N}}{e}\right) + \frac{7}{12N}\right] > 0 \; .
$$ (epsilon_tvn)

Askatasun-graduak abiarazi ahala, banatze-potentzialak jasotzen dituen tamaina finituko ekarpenok ez dira bere horretan mantenduko (aldera bitez {eq}`epsilon_tvn` ekuazioa eta {numref}`{number}. <tpn>` eta {numref}`{number}. <tpmu>` ataletako {eq}`gi_epsilon_tpn` zein {eq}`epsilontpmugi` adierazpenak). Azken esaldi horrek Nanotermodinamikaren berariazko ondorio batera garamatza: ekuazio termodinamikoak azterketan erabiliko diren multzo estatistikoekin batera aldatu egingo dira.
