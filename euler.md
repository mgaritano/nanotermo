(euler)=
## _A Eulerren ekuazioa_

Matematikan, $k$ ordenako funtzio homogeneo batek honako adierazpen hau betetzen du:

$$
f(\lambda x_{1},...,\lambda x_{n}) = \lambda^{k}f(x_{1},...,x_{n}), \; \; \forall x_{1},...,x_{n} \; \textrm{eta} \; \lambda \neq 0 \; .
$$ (f_def)

Callen liburuari jarraituz {cite}`callen`, sistema makroskopiko baten oinarrizko ekuazioak **lehen ordenako** funtzio homogeneoak dira. Horrek adierazpenak oso modu baliagarrian idaztea posible egiten du, _Eulerren forman_, alegia. Azalpena trinkotze aldera, demagun barne-energia soilik entropiaren eta bolumenaren funtzioa dela. Kasu horretan, $\lambda$ zeinahi hartuta, eta $k = 1$,

$$
E(\lambda S, \lambda V) = \lambda E(S, V)
$$ (e_euler)

litzateke aipaturiko forma. Ekuazio hori deribatuz gero,

$$
\frac{\partial E(\lambda S, \lambda V)}{\partial (\lambda S)}\frac{\partial(\lambda S)}{\partial \lambda} + \frac{\partial E(\lambda S, \lambda V)}{\partial (\lambda V)}\frac{\partial(\lambda V)}{\partial \lambda} = E(S,V)
$$ (euler_2)

genuke. Bereziki, $\lambda = 1$ hartuz,

$$
 \frac{\partial E(S,  V)}{\partial S}S + \frac{\partial E(S, V)}{\partial V}V = E(S,V) \; .
$$ (euler_3)

 Edo, $S$ eta $V$ aldagaien konjokatuak txertatuz,

 $$
 \boxed{E(S, V) = TS - pV} \; .
 $$ (euler_4)

 Presioak eta tenperaturak, bestalde, zero ordenakoak direnez,

 $$
 f(\lambda S, \lambda V) = \lambda^{0}f(S, V) = f(S, V)
 $$ (euler_5)

 beteko dute, hau da, intentsiboak dira.
