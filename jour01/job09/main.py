#programme
nom="Gâteaux aux chocolat"
prix_unitaire=10
quantité_en_stock=1000

print("Saisir la quantité de produits souhaité : ")
choisi=int(input())

print("Nom du produit : ",nom)
print("Prix unitaire du produit : ",prix_unitaire)

prix_unitaire +=prix_unitaire * (10/100)
quantité_en_stock-=choisi

print("Prix unitaire du produit après inflation : ",prix_unitaire)
print("Quantité en stock : ",quantité_en_stock)
print("Les",choisi,nom,"selectionné vont vous coutez : ",choisi * prix_unitaire)