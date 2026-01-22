import sqlite3

DB_NAME = "ads_debugger.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ad_issues (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            campaign_id TEXT,
            issue TEXT,
            severity TEXT
        )
    """)

    conn.commit()
    conn.close()


def insert_issue(campaign_id, issue, severity):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO ad_issues (campaign_id, issue, severity)
        VALUES (?, ?, ?)
    """, (campaign_id, issue, severity))

    conn.commit()
    conn.close()

