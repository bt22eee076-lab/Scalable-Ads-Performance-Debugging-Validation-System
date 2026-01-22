import sqlite3

conn = sqlite3.connect("ads_debugger.db")
cursor = conn.cursor()

print("\n--- HIGH Severity Issues ---")
for row in cursor.execute("""
    SELECT campaign_id, issue
    FROM ad_issues
    WHERE severity = 'HIGH'
"""):
    print(row)

print("\n--- Issue Count by Severity ---")
for row in cursor.execute("""
    SELECT severity, COUNT(*)
    FROM ad_issues
    GROUP BY severity
"""):
    print(row)

conn.close()
