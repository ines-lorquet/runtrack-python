#Programme financier
init_investissement=1000
rendement=0.02
gain_annuel=init_investissement * rendement
print(gain_annuel,"€")

init_investissement+=gain_annuel
init_investissement+=5000
rendement+= 0.02
gain_annuel=init_investissement * rendement
print(gain_annuel,"€")

init_investissement-=0.10
rendement-=0.01
gain_annuel=init_investissement * rendement
print(init_investissement,"€")
print(gain_annuel)

