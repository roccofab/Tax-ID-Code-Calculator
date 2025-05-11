import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Tax_code import (
    calculateSurname,
    calculateName,
    add_data_gender,
    calculate_cadastral_code,
    calculate_control_code,
)

def test_calculateSurname():
    assert calculateSurname("Rosi") == "RSO"
    assert calculateSurname("Rossi") == "RSS"
    assert calculateSurname("Fo") == "FOX"
    assert calculateSurname("Li") == "LIX"
    assert calculateSurname("A") == "AXX"

def test_calculateName():
    assert calculateName("Rosi") == "RSO"
    assert calculateName("Rossi") == "RSS"
    assert calculateName("Marco") == "MRC"
    assert calculateName("Giovanni") == "GNN"
    assert calculateName("Gian") == "GNI"
    assert calculateName("Fo") == "FOX"
    assert calculateName("Li") == "LIX"
    assert calculateName("A") == "AXX"

def test_add_data_gender():
    assert add_data_gender("12-05-1990", "M") == "90E12"
    assert add_data_gender("12-05-1990", "F") == "90E52"
    assert add_data_gender("20-10-2010", "M") == "10R20"
    assert add_data_gender("9-11-2000", "F") == "00S49"
    
def test_calculate_cadastral_code():
    filename = os.path.join(os.path.dirname(__file__), "gi_comuni.csv")
    assert calculate_cadastral_code(filename, "Roma") == "H501"
    assert calculate_cadastral_code(filename, "Milano") == "F205"
    assert calculate_cadastral_code(filename, "Torino") == "L219"
    assert calculate_cadastral_code(filename, "Napoli") == "F839"
    assert calculate_cadastral_code(filename, "Firenze") == "D612"
    assert calculate_cadastral_code(filename, "Monte Compatri") == "F477"
    assert calculate_cadastral_code(filename, "Castel Gandolfo") == "C116"
    assert calculate_cadastral_code(filename, "NonExistentCity") == "Municipality not found"
    
