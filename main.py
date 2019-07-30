from utilities.parseweb import ParseWeb

web = ParseWeb("https://www.jutarnji.hr/vijesti/hrvatska/sibenska-policija-otkrila-detalje-o-piromanki-iz-hac-a-prije-odlaska-na-posao-kupila-je-kocke-za-potpalu-i-podmetnula-pozar-zapalila-je-dvije-kutije/9179915/")
web.parse_jutarnji()
print(web.title)
print(web.text)


