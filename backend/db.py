import sqlite3

def init_db():
    conn = sqlite3.connect("scan_history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS history (url TEXT, result TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def insert_scan(url, result, date):
    conn = sqlite3.connect("scan_history.db")
    c = conn.cursor()
    c.execute("INSERT INTO history VALUES (?, ?, ?)", (url, result, date))
    conn.commit()
    conn.close()

def get_all_scans():
    conn = sqlite3.connect("scan_history.db")
    c = conn.cursor()
    c.execute("SELECT * FROM history")
    rows = c.fetchall()
    conn.close()
    return rows