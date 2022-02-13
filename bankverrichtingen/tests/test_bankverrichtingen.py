import pytest
from bankverrichtingen.classes_rekeningen import *
from bankverrichtingen.class_persoon import Persoon





# Testpersoon om als input te gebruiken voor de tests
@pytest.fixture
def testPersoon():
    '''Returns a Persoon instance with following input(Jens, Coomans, 00.00.00-000.00)'''
    return Persoon('Jens', 'Coomans', '00.00.00-000.00')





# testen input class persoon
def test_persoon_setting_initial_values(testPersoon):
    assert testPersoon.voornaam == "Jens"
    assert testPersoon.achternaam == "Coomans"
    assert testPersoon.rijksregisternummer == "00.00.00-000.00"

def test_persoon_no_value():
    with pytest.raises(Exception):
        persoon = Persoon()

@pytest.mark.parametrize("vNaam, aNaam, rrnum", [(1,"2","00.00.00-000.00"), ("1",2,"00.00.00-000.00"), ("1","2",3)])
def test_values_not_string(vNaam,aNaam,rrnum):
    with pytest.raises(TypeError):
        persoon = Persoon(vNaam,aNaam,rrnum)

@pytest.mark.parametrize("vNaam, aNaam, rrnum", [("1","2","3"), ("1","2","12.34.567-89.10"), ("1","2","ab.cd.ef-ghi.jk")])
def test_rijksregisternummer_wrong_format(vNaam,aNaam,rrnum):
    with pytest.raises(ValueError):
        persoon = Persoon(vNaam,aNaam,rrnum)





# Test rekening om als input te gebruiken voor de tests
@pytest.fixture
def testRekening(testPersoon):
    '''Returns a rekening instance with 091-0122401-16 as rekeningnummer, balance of 0 and testPersoon(fixture) as persoon'''
    return Rekening("091-0122401-16", testPersoon)

# Test zichtrekening om als input te gebruiken voor de tests
@pytest.fixture
def testZichtrekening(testPersoon):
    '''Returns a zichtrekening instance with 091-0122401-16 as rekeningnummer, balance of 0 and testPersoon(fixture) as persoon'''
    return Zichtrekening("091-0122401-16", testPersoon)

# Test spaarrekening om als input te gebruiken voor de tests
@pytest.fixture
def testSpaarrekening(testPersoon):
    '''Returns a spaarrekening instance with 091-0122401-16 as rekeningnummer, balance of 0 and testPersoon(fixture) as persoon'''
    return Spaarrekening("091-0122401-16", testPersoon)





# testen methodes superclass rekening
def test_rekening_setting_initial_values(testRekening, testPersoon):
    assert testRekening.rekeningnummer == "091-0122401-16"
    assert testRekening.persoon.achternaam == testPersoon.achternaam

def test_rekening_no_value():
    with pytest.raises(Exception):
        rekening = Rekening()

def test_rekeningOverzicht(testRekening):
    assert testRekening.rekeningOverzicht()

@pytest.mark.parametrize("rnum", [("1"), ("0000-0000-0000"), ("abc-defghij-kl")])
def test_controleInput_rekeningnummer_value(rnum, testPersoon):
    with pytest.raises(ValueError):
        rekening = Rekening(rnum, testPersoon)

def test_controleInput_type(testPersoon):
    with pytest.raises(TypeError):
        rekening = Rekening(000-0000000-00, testPersoon)
    with pytest.raises(TypeError):
        rekening = Rekening("091-0122401-16", "Jens Coomans")

def test_controleRekeningnummer(testPersoon):
    with pytest.raises(InvalidRekeningnummer):
        rekening = Rekening("123-4567890-99", testPersoon)





# testen methodes subclass zichtrekening
def test_overschrijven_zichtrekening(testZichtrekening, testSpaarrekening):
    testZichtrekening.overschrijven(testSpaarrekening, 30)
    assert testZichtrekening.geld == -30
    assert testSpaarrekening.geld == 30

def test_overschrijven_zichtrekening_no_value(testZichtrekening):
    with pytest.raises(Exception):
        testZichtrekening.overschrijven()

def test_overschrijven_zichtrekening_other_no_rekening(testZichtrekening):
    rekening2 = "000-0000097-97"
    with pytest.raises(TypeError):
        testZichtrekening.overschrijven(rekening2, 30)

def test_overschrijven_zichtrekening_wrong_bedrag(testZichtrekening, testSpaarrekening):
    with pytest.raises(TypeError):
        testZichtrekening.overschrijven(testSpaarrekening, "30")
    with pytest.raises(ValueError):
        testZichtrekening.overschrijven(testSpaarrekening, -30)

def test_overschrijven_zichtrekening_other_wrong_rekening(testZichtrekening):
    persoon = Persoon("Bert", "Vriens", "11.11.11-111.11")
    spaarrekening = Spaarrekening("000-0000097-97", persoon)
    with pytest.raises(ValueError):
        testZichtrekening.overschrijven(spaarrekening, 30)
    with pytest.raises(ValueError):
        testZichtrekening.overschrijven(testZichtrekening, 30)

def test_opvragen(testZichtrekening):
    testZichtrekening.opvragen(30)
    assert testZichtrekening.geld == -30

def test_opvragen_wrong_bedrag(testZichtrekening):
    with pytest.raises(TypeError):
        testZichtrekening.opvragen("30")
    with pytest.raises(ValueError):
        testZichtrekening.opvragen(-30)

def test_storten(testZichtrekening):
    testZichtrekening.storten(30)
    assert testZichtrekening.geld == 30

def test_storten_wrong_bedrag(testZichtrekening):
    with pytest.raises(TypeError):
        testZichtrekening.storten("30")
    with pytest.raises(ValueError):
        testZichtrekening.storten(-30)





# testen methodes subclass spaarrekening
def test_overschrijven_spaarrekening(testZichtrekening, testPersoon):
    spaarrekening = Spaarrekening("000-0000097-97", testPersoon)
    # eerste geld op spaarrekening zetten om het overschrijven te kunnen testen
    testZichtrekening.overschrijven(spaarrekening, 30)
    spaarrekening.overschrijven(testZichtrekening, 20)
    assert spaarrekening.geld == 10

def test_overschrijven_spaarrekening_other_wrong_rekening(testSpaarrekening, testPersoon):
    persoon = Persoon("Bert", "Vriens", "11.11.11-111.11")
    spaarrekening = Spaarrekening("000-0000097-97", testPersoon)
    zichtrekening = Zichtrekening("000-0000097-97", persoon)
    with pytest.raises(TypeError):
        testSpaarrekening.overschrijven(spaarrekening, 30)
    with pytest.raises(ValueError):
        testSpaarrekening.overschrijven(zichtrekening, 30)

def test_overschrijven_spaarrekening_wrong_bedrag(testSpaarrekening, testZichtrekening):
    with pytest.raises(TypeError):
        testSpaarrekening.overschrijven(testZichtrekening, "30")
    with pytest.raises(ValueError):
        testSpaarrekening.overschrijven(testZichtrekening, -30)

def test_overschrijven_spaarrekening_niet_onder_nul(testSpaarrekening, testZichtrekening):
    with pytest.raises(ValueError):
        testSpaarrekening.overschrijven(testZichtrekening, 30)