import numpy as np
import pandas as pd
import colorama as clr
def tarpas(x):
    print(f'{clr.Fore.YELLOW}{x}')
clr.init(autoreset=True)
tarpas ('Turime knygų aprašymus ir jų vietinę informaciją bibliotekoje. Reikia atlikti įvairius veiksmus')
knyga1 = ['Don Kichotas', 'M. de Cervantes', 1612, 500000000]
knyga2 = ['Pasakojimas apie miestus', 'Ch. Dickenson', 1859, 200000000]
knyga3 = ['Mažasis princas', 'A. de Saint-Exuperi', 1943, 140000000]
knyga4 = ['Sapnas raudoname kambaryje', 'C.Xueqin', 1754, 100000000]
knyga5 = ['Alchemikas', 'P. Coelh', 1988, 150000000]
biblioteka1 = ['Don Kichotas', 124578, 'A', 54]
biblioteka2 = ['Pasakojimas apie miestus', 164875, 'B', 1057]
biblioteka3 = ['Mažasis princas', 136845, 'C', 400]
biblioteka4 = ['Sapnas raudoname kambaryje', 354789, 'C', 1198]
biblioteka5 = ['Alchemikas', 354126, 'A', 451]

tarpas(' Sukuriamos matricos iš duotos tarpusavyje susietos informacijos')
knygos = (pd.DataFrame(np.array([knyga1, knyga2, knyga3, knyga4, knyga5]),
       [1, 2, 3, 4, 5],
       ['Knygos pavadinimas', 'Autorius', 'Metai', 'Tiražas']))
biblioteka = (pd.DataFrame(np.array([biblioteka1, biblioteka2, biblioteka3, biblioteka4, biblioteka5]),
       [1, 2, 3, 4, 5],
       ['Knygos pavadinimas', 'Reg. Nr.', 'Skyrius', 'Kiek kartų išduotas']))
print(f''' {clr.Fore.GREEN}Bibliotekoje naudojamos knygos
{knygos}

''')
print(f''' {clr.Fore.BLUE}Informacija apie bibliotekoje esamas knygas
{biblioteka}

''')

tarpas(' Numetami duomenų rodymo ekrane apribojimai')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

tarpas(' Apjungiame duotas matricas į vieną bendros informacijos matricą')
bendra_informacija = knygos.merge(biblioteka, on=['Knygos pavadinimas', 'Knygos pavadinimas'])
print(bendra_informacija)

tarpas (' Patikrinama kuri knyga yra skaitomiausia bibliotekoje. Pradžioje pakeičiame stulpelio turinį į numeric, atrenkame maksimalią ir minimalią reikšmes.')
biblioteka['Kiek kartų išduotas'] = pd.to_numeric(biblioteka['Kiek kartų išduotas'])
skaitomiausia_knyga = biblioteka[biblioteka['Kiek kartų išduotas'] == biblioteka['Kiek kartų išduotas'].max()][['Knygos pavadinimas', 'Kiek kartų išduotas']]
pamirsta_knyga = biblioteka[biblioteka['Kiek kartų išduotas'] == biblioteka['Kiek kartų išduotas'].min()][['Knygos pavadinimas', 'Kiek kartų išduotas']]
print(f'''
Labiausiai skaitoma knyga
{skaitomiausia_knyga}

Pamiršta knyga
{pamirsta_knyga}
''')

tarpas('Atrinkimas pirmo trejetuko pagal tiražą')
bendra_informacija['Tiražas'].astype('int64')
bendra_informacija = bendra_informacija.sort_values(by='Tiražas',ascending=False)
print(bendra_informacija[['Knygos pavadinimas', 'Tiražas']].head(3))

tarpas('Autorių, kurie rašė 19 amžiūje, atrinkimas')
autoriai = knygos[(knygos['Metai'].astype('int64') >1799)&(knygos['Metai'].astype('int64') <1900)]
print(autoriai[['Autorius', 'Knygos pavadinimas', 'Metai']])

tarpas('Knygos nurašymas. Knygos yra siunčiamos stovio įvertinimui, kai jas perskaito 1000 kartų. \nTam yra sukuriamas nauja matrica, į kurią talpinamos knygos peržiūrai')
knygos_ivertinimas = biblioteka[biblioteka['Kiek kartų išduotas']>1000][["Knygos pavadinimas", 'Skyrius', 'Reg. Nr.', 'Kiek kartų išduotas']]
print(knygos_ivertinimas)
tarpas("Pridedame naują stulpelį 'Apžiūros rezultatas'. Galimos reikšmės : 'Buklė gera', 'Nurašyti', 'Tikrinama' uždedama automatiškai" )
listas = []
for i in range(len(knygos_ivertinimas)):
    listas.append('Tikrinama')
knygos_ivertinimas['Apžiūros rezultatas'] =listas
print(knygos_ivertinimas)

tarpas('Knygos nurašymas. Apžiūrėjus knygą, keičiama Apžiūros rezultato reikšmė')
knygos_ivertinimas.loc[knygos_ivertinimas['Reg. Nr.']=='354789','Apžiūros rezultatas'] =  'Nurašyti'
print(knygos_ivertinimas)
knygos1 = knygos.drop(knygos_ivertinimas.loc[knygos_ivertinimas['Apžiūros rezultatas']== 'Nurašyti'].index)
bibliotekos1 = biblioteka.drop(knygos_ivertinimas.loc[knygos_ivertinimas['Apžiūros rezultatas']== 'Nurašyti'].index)
print(knygos1)
print(bibliotekos1)
tarpas('Bibliotekos knygų populiarumo analizė')
bibliotekos = pd.DataFrame({})
bibliotekos['Knygos pavadinimas'] = biblioteka['Knygos pavadinimas']
bibliotekos['Išduota kartų'] = biblioteka['Kiek kartų išduotas']
bibliotekos['Knygos populiarumas'] =pd.cut(biblioteka['Kiek kartų išduotas'], bins = 3, labels = ['Retas', 'Vidutinis', 'Aukštas'])
print(bibliotekos)

