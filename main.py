from utilities.parseweb import ParseWeb


print("Jutarnji")
web = ParseWeb("https://www.jutarnji.hr/vijesti/hrvatska/sibenska-policija-otkrila-detalje-o-piromanki-iz-hac-a-prije-odlaska-na-posao-kupila-je-kocke-za-potpalu-i-podmetnula-pozar-zapalila-je-dvije-kutije/9179915/")
web.parse_jutarnji()
print("Title: ",web.title)
print("Text: ",web.text)


print("Vecernji")
web = ParseWeb("https://www.vecernji.hr/sport/policija-hitno-morala-na-teren-zbog-dojave-o-bombi-ispod-vozila-slavnih-nogometasa-1335436")
web.parse_vecernji()
print("Title: ",web.title)
print("Text: ",web.text)


print("Index")
web = ParseWeb("https://www.index.hr/vijesti/clanak/inspekcija-ne-zna-tko-je-to-zabetonirao-obalu-ispred-vile-medjugorske-vidjelice/2105065.aspx")
web.parse_index()
print("Title: ",web.title)
print("Text: ",web.text)


