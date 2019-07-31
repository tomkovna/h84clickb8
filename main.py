from utilities.parseweb import ParseWeb
import utilities.database as db


def add_link_to_database(web):
    conn = db.create_connection("./h84clickb8.db")
    with conn:
        project = (web.title, web.text);
        project_id = db.create_entry(conn, project)
        return project_id


link = "https://www.index.hr/rouge/clanak/ova-navika-moze-razoriti-vasu-vezu/2104571.aspx?fbclid=IwAR1VXKe_n3AT1yrLbuWpJWaauJshP2AVW3q92O3xb41uGENZpZjqvGz_xiE"

print("Index")
web = ParseWeb(link)
web.parse_index()
add_link_to_database(web)
