import re

txt = """PayPal (Europe) S.a.r.l. et Cie., S.C.A.
              PP.1250.PP . , Ihr Einkauf bei EREF: 1017732682350 PP.
              1250.PP PAYPAL MREF: 52NJ224X8RGM2 CRED: LU96ZZZ000000"""

regex = "PayPal\s\(Europe\)"

print(re.search(regex, txt))