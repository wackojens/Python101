import JC_stockbeheerFunct

lijst1 = []
lijst2 = []
lijst3 = []

bestellingen = [
['P016235',14,'CA100'],
['P016231',93,'CB23'],
['PD235',2,'PR14'],
['P016231',13,'CB48'],
['PD235',5,'PR01'],
['P016235',62,'CA101'],
['PD235',1,'DIR1'],
['P016231',42,'CB21']
]

voorraad = {
'P016235':[25,20,100,0,'LEV01',14],
'P016231':[243,100,500,0,'LEV25',5],
'PD235':[3,4,20,0,'LEV156',14]
}

JC_stockbeheerFunct.getProducts(bestellingen, voorraad, lijst1, lijst2, lijst3)

JC_stockbeheerFunct.printList1(lijst1)
JC_stockbeheerFunct.printList2(lijst2)
JC_stockbeheerFunct.printList3(lijst3)