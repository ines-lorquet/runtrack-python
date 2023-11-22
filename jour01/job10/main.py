#Programme financier
init_investissement=100
taux=0.03
gain_annuel=init_investissement * taux
print(gain_annuel,"€")

init_investissement+=gain_annuel
init_investissement+=5000
taux+= taux * 0.02
gain_annuel=init_investissement * taux
print(gain_annuel,"€")

init_investissement-=0.10
taux-= taux*0.01
gain_annuel=init_investissement * taux
print(init_investissement,"€")
print(gain_annuel)