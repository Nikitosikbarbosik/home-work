Задание 1
import re

def check_license_plate(plate):
    allowed_letters = "АВЕКМНОРСТУХ"
    plate = plate.upper()

    private_car_pattern = r"^([АВЕКМНОРСТУХ])(\d{3})([АВЕКМНОРСТУХ]{2})(\d{2,3})$"
    private_car_match = re.match(private_car_pattern, plate)

    taxi_pattern = r"^([АВЕКМНОРСТУХ]{2})(\d{3})(\d{2,3})$"
    taxi_match = re.match(taxi_pattern, plate)


    if private_car_match:
        letters = private_car_match.group(1,3)
        numbers = private_car_match.group(2,4)
        if all(c in allowed_letters for c in "".join(letters)) and all(c.isdigit() for c in "".join(numbers)):
            return "Частная легковая"
        else: return None


    elif taxi_match:
        letters = taxi_match.group(1)
        numbers = taxi_match.group(2,3)
        if all(c in allowed_letters for c in letters) and all(c.isdigit() for c in "".join(numbers)):
            return "Такси"
        else: return None
    else:
        return None

plates = ["А123ВВ12", "А123ВС123", "А123ВВ123", "XX12345", "АА12312", "АА123123", "Б123СС77"]
for plate in plates:
    result = check_license_plate(plate)
    print(f"Номер {plate}: {result}")

Задание 2
print(len(re.findall(r'\b[a-zA-Zа-яА-Я-]+(?:-[a-zA-Zа-яА-Я-]+)*\b', open('input.txt').read())))

Задание 3
import re
def replace_time(text):
    return re.sub(r"(?:[01]\d|2[0-3]):[0-5]\d(?:[:][0-5]\d)?", "(TBD)", text)
text = "Уважаемый! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю.  Также в 10:30 и 23:59:59"
new_text = replace_time(text)
print(new_text)

Задание 4
import re

def find_abbreviations(text):
    abbreviations = re.findall(r'\b[А-Я]{2,}(?:\s+[А-Я]{2,})*\b', text)
    return " ".join(abbreviations)

text = "Текст документа: ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п.  Еще одна аббревиатура: АО АБВГДЕ."
result = find_abbreviations(text)
print(result) 

