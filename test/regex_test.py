import re

txt = """2021Vorgang Wert
                      4.624,58 H
03.01. 03.01. Basislastschrift                                                     15,00 S
              FitX Deutschland GmbH
              XREF 788-727874-713003 FitX Deutschland versch. Rechnu
              ngen EREF: 788-727874-713003 MREF: 727874-1 CRED: DE48
              ZZZ00000858428
03.01. 03.01. Dauerauftragsgutschr                                                          125,00 H
              Frank und Monika Zenz
              Unterst�tzung"""

regex = "\d\d\.\d\d.\s\d\d\.\d\d"

results = re.split(regex, txt)
print(results)


print(re.search(regex, "hiho"))
print(re.search(regex, txt))

dic={"hi": "ho",
    "ha": 3}

print(dic.keys())
print(dic["hi"])