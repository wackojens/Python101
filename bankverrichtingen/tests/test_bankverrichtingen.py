import pytest
from bankverrichtingen.class_rekening import *
from bankverrichtingen.class_zichtrekening import *
from bankverrichtingen.class_spaarrekening import *
from bankverrichtingen.class_persoon import *



# testen input class persoon
def test_voornaam_string_only():
    with pytest.raises(TypeError):
        ()

def test_achternaam():
    pass

def test_rijksregisternummer():
    pass



# Testpersoon om als input te gebruiken voor de rekeningen te testen
@pytest.fixture
def testPersoon():
    '''Returns a Persoon instance with following input(Jens,Coomans, 00.00.00-000.00)'''
    return Persoon('Jens', 'Coomans', '00.00.00-000.00')



# testen methodes superclass rekening
def test_rekeningOverzicht():
    pass

def test_controleRekeningnummer():
    pass

def test_overschrijven():
    pass



# testen methodes subclass zichtrekening
def test_overschrijven_zichtrekening():
    pass

def test_opvragen():
    pass

def test_storten():
    pass



# testen methodes subclass spaarrekening
def test_overschrijven_spaarrekening():
    pass

def test_onderNul():
    pass
