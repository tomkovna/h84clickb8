from utilities.parseweb import ParseWeb

link = "https://www.index.hr/rouge/clanak/ova-navika-moze-razoriti-vasu-vezu/2104571.aspx?fbclid=IwAR1VXKe_n3AT1yrLbuWpJWaauJshP2AVW3q92O3xb41uGENZpZjqvGz_xiE"
# print("Jutarnji")
# web = ParseWeb("https://www.jutarnji.hr/vijesti/hrvatska/sibenska-policija-otkrila-detalje-o-piromanki-iz-hac-a-prije-odlaska-na-posao-kupila-je-kocke-za-potpalu-i-podmetnula-pozar-zapalila-je-dvije-kutije/9179915/")
# web.parse_jutarnji()
# print("Title: ",web.title)
# print("Text: ",web.text)
#
#
# print("Vecernji")
# web = ParseWeb("https://www.vecernji.hr/sport/policija-hitno-morala-na-teren-zbog-dojave-o-bombi-ispod-vozila-slavnih-nogometasa-1335436")
# web.parse_vecernji()
# print("Title: ",web.title)
# print("Text: ",web.text)


print("Index")
web = ParseWeb(link)
web.parse_index()
print("Title: ",web.title)
print("Text: ",web.text)


