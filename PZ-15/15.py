import sqlite3 as sq
from data_prom import info_prom

with sq.connect('promishlenost.db') as con:
    cur = con.cursor()

    #cur.execute("DROP TABLE IF EXISTS predpriyatia")

    cur.execute("""CREATE TABLE IF NOT EXISTS predpriyatia(
    kod_predpriatia INTEGER PRIMARY KEY AUTOINCREMENT,
    name_predpiatia TEXT NOT NULL,
    fiz_adres TEXT NOT NULL,
    filials INTEGER,
    obsh_chisl_personala INTEGER,
    obsh_stoim_oborud INTEGER,
    v_vipysk_prod INTEGER,
    data_registr INTEGER
    )""")

with sq.connect('promishlenost.db') as con:
 cur = con.cursor()
 cur.executemany("INSERT INTO predpriyatia VALUES (?, ?, ?, ?, ?, ?, ?, ?)", info_prom)

with sq.connect('promishlenost.db') as con:
 cur = con.cursor()
 cur.execute("SELECT * FROM predpriyatia")
 result = cur.fetchall()
 print(result)

with sq.connect('promishlenost.db') as con:
 cur = con.cursor()
 cur.execute("SELECT * FROM predpriyatia WHERE filials < 6 AND obsh_chisl_personala > 40")
 result = cur.fetchall()
 print(result)

with sq.connect('promishlenost.db') as con:
 cur = con.cursor()
 cur.execute("SELECT * FROM predpriyatia WHERE filials IN(3, 6) OR obsh_stoim_oborud > 1000000")
 result = cur.fetchall()
 print(result)

 with sq.connect('promishlenost.db') as con:
  cur = con.cursor()
 cur.execute("UPDATE predpriyatia SET obsh_stoim_oborud = obsh_stoim_oborud + 50000 WHERE filials = 2")
 result = cur.fetchall()
 print(result)

with sq.connect('promishlenost.db') as con:
 cur = con.cursor()
 cur.execute("UPDATE predpriyatia SET v_vipysk_prod = 154000 WHERE name_predpiatia LIKE 'Евросеть'")
 result = cur.fetchall()
 print(result)

with sq.connect('promishlenost.db') as con:
 cur = con.cursor()
 cur.execute("UPDATE predpriyatia SET obsh_chisl_personala = obsh_chisl_personala + 10 WHERE name_predpiatia LIKE 'Р%'")
 result = cur.fetchall()
 print(result)

# with sq.connect('promishlenost.db') as con:
#  cur = con.cursor()
#  cur.execute("DELETE FROM predpriyatia WHERE filials = 5")
# result = cur.fetchall()
# print(result)
#
# with sq.connect('promishlenost.db') as con:
#  cur = con.cursor()
#  cur.execute("DELETE FROM predpriyatia WHERE kod_predpriatia = 9")
# result = cur.fetchall()
# print(result)
#
# with sq.connect('promishlenost.db') as con:
#  cur = con.cursor()
#  cur.execute("DELETE FROM predpriyatia WHERE obsh_chisl_personala > 54")
# result = cur.fetchall()
# print(result)









