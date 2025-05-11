"""
The fiscal code is a 16-character string calculated based on the following fields:
    - Last Name
    - First Name
    - Gender
    - Date of Birth
    - Place of Birth
-The last name occupies 3 alphabetic characters: 3 consonants of the last name are taken in their order of appearance. 
    If the last name has fewer than 3 consonants, vowels are also taken in their order of appearance. 
    The vowels must always be placed after the consonants. 
    If the last name has fewer than 3 letters, the code is completed with an X.
    Example: Rosi --> RSO
    Example: Fo --> FOX
    
-The first name occupies 3 alphabetic characters: if the first name has more than 3 consonants, 
    the first, third, and fourth consonants are taken. 
    If the first name has only 3 consonants, all 3 are taken in their order of appearance. 
    If the first name does not have enough consonants, vowels are also taken and placed after the consonants. 
    If the first name has fewer than 3 letters, the code is completed with an X.
     
- Date of birth and gender occupy 5 characters of the fiscal code in total: 
    the year of birth occupies 2 characters, the month of birth occupies 1 character, 
    and the day of birth occupies 2 characters (if the day is between 1 and 9, a 0 is added as the first digit). 
    If the person is female, 40 is added to the day of birth, so for females, 
     the days of birth will range from 41 to 71 instead of 1 to 31. 
    For the month of birth, a dictionary is used to associate a letter from the month's name 
    with the month's name according to a predefined table.
      
- Municipality and State of birth occupy 4 alphanumeric characters of the fiscal code: 
    For municipalities, the cadastral code is used. 
    In the file gi_comuni.csv, each row contains all the information about a specific municipality in the format:
         TO;001001;Agliè;Agliè;;NO;A074;45,3634669;7,7686057;13,2851;201
    It is necessary to open the file in read mode, calculate the list for each row, 
    and split each element of the read row using the ';' character. 
    Compare the content of the list at index 2 (containing the municipality's name in the row converted to uppercase) 
    with the user's municipality name (also converted to uppercase). 
    If they match, return the element of the list at index 5 (municipality cadastral code), 
    converted to uppercase and with empty spaces removed. Otherwise, return "Municipality not found."
    
- Starting from the 15 alphanumeric characters derived from the last name, first name, date of birth, gender, 
  municipality, and state, the control internal number is calculated:
    The characters in odd positions correspond to specific values from a predefined table(odd_positions dictionary). 
    The characters in even positions correspond to specific values from another predefined table(even_positions dictionary). 
    The values obtained from the odd and even tables are summed and divided by 26. 
    The remainder of the division is converted into an identification code according to a predefined remainder table 
    that associates each number with a specific character.
    Therefore, it is necessary to declare 3 dictionaries: even, odd, and control_value.
"""

vowels = "aeiouAEIOU"

months = {'01': 'A', '02':'B', '03':'C', '04':'D',
        '05':'E', '06':'H', '07':'L', '08':'M',
        '09':'P','10':'R', '11':'S', '12':'T'}

even_positions = {'0':1, '1':0, '2':5, '3':7, '4':9,'5':13,
                  '6':15,'7':17,'8':19,'9':21,'A':1,'B':0,
                  'C':5,'D':7,'E':9,'F':13,'G':15,'H':17,
                  'I':19,'J':21,'K':2,'L':4,'M':18,'N':20,
                  'O':11,'P':3,'Q':6,'R':8,'S':12,'T':14,
                  'U':16,'V':10,'W':22,'X':25,'Y':24,'Z':23}

odd_positions = {'0':1,'1':0,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
                 '8':8,'9':9,'A':0,'B':1,'C':2,'D':3,
                 'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,
                 'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,
                 'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

control_value = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F', 6:'G', 7:'H',8:'I',9:'J',10:'K',
                  11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',
                  21:'V',22:'W',23:'X',24:'Y',25:'Z'}

filename = "C:\\Users\\lenovo\\Desktop\\python_tutorial\\Programmazione_Strutturata\\Stringhe\\gi_comuni.csv"

def calculateSurname(surname):
    cons = []
    vow = []
    for i in surname:
        if i in vowels:
            vow.append(i)
        else:
            cons.append(i)
    characters = cons + vow + ['X'] * 2  #the order of the characters is important, first consonants then vowels and finally two characters 'X'
    fullCode = "".join(characters)
    codSurname = fullCode[:3]  # take the first 3 characters of the full string that contains cons,vows and two characters 'X'
    return codSurname.upper()

def calculateName(name):
    cons = []
    vow = []
    for i in name:
        if i in vowels:
            vow.append(i)
        else:
            cons.append(i)
            
    if len(cons) > 3:
        # if the name has more than 3 consonants, take the first, third and fourth consonants
        cons = [cons[0], cons[2], cons[3]]
    elif len(cons) < 3:
        # if the name has less than 3 consonants, take the vowels
        while len(cons) < 3 and vow:
            cons.append(vow.pop(0))
        # If still less than 3, pad with 'X'
        while len(cons) < 3:
            cons.append('X')
        
    
    codName = "".join(cons[:3])  # take the first 3 characters of the full string that contains cons,vows and two characters 'X'
    return codName.upper()

def add_data_gender(data,gender):
    data_parts = data.split('-')
    year = data_parts[2][2:]  # take the last two digits of the year
    month = months[data_parts[1]]  # get the month letter from the dictionary months
    if gender.upper() != 'M':
        day = str(int(data_parts[0]) + 40)  # if the gender is 'F' add the value 40 to the day
    else:
        day = data_parts[0]
    return year + month + day

def calculate_cadastral_code(filename,comune):
    """
    Read the codici_comuni.csv file and split rows with the character ';'.
    The content of the raws at index 2 is the municipality name and the content of the raws at index 5
        is the cadastral code of the municaplity.
    Compare the name of the municipality in the raws with the name of the municipality passed as argument of the method
        and if they match, it returns the element of the row at index 6 (cadastral code) else "Municaplity not found".

    Args:
        filename (.csv): _path to the csv file containing the details of municipalities.
        comune (str): name of the municipality of the user.

    Returns:
        str: the cadastral code of the municipality if found, else "Municipality not found".
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:  
            for line in file:
                fields = line.rstrip().split(';') #split any line with the character ';'
                if len(fields) >= 7:
                    #replace characters "" around the municipality name with '' 
                    municipality_csv = fields[2].replace('"', '').strip().upper()
                    if municipality_csv == comune.upper().strip():  #compare the name of the municipality in the csv with the name of the municipality passed as argument and converted to uppercase with whitespaces removed
                        return fields[6].upper().strip()  # returns cadastral code
            return "Municipality not found"
    except FileNotFoundError:
        print("The file doesn't exists.")
        return None
    except UnicodeDecodeError as e:
        print(f"Decoding error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
def calculate_control_code(codFsc):
    """
    calculate the control code from the partial tax code obtained by name-surname-birth date-gender-cadastral code
       and add it to the tax_code.

    Args:
        codFsc (str): the partial tax code obtained by name-surname-birth date-gender-cadastral code.

    Returns:
        control code: the value found in the dictionary control_value 
    """
    i = 0
    a = 0
    b = 0
    even = list()
    odd = list()
    while i < len(codFsc):
        if i % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
        i += 1
    for x in odd:
        a += odd_positions[codFsc[x].upper()]  #search the element at the index x in the dictionary odd_positions make it upper and add it to a
        
    for y in even:
        b += even_positions[codFsc[y].upper()]   #search the element at the index y in the dictionary even_positions make it upper and add it to b
    return control_value[((a + b) % 26)].upper()   # return the value found in the dictionary control_value 
