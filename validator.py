import csv
from db import setup_database, insert_issue

def validate_ads_data(file_path):
    issues = []

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            campaign = row['campaign_id']
            clicks = int(row['clicks'])
            impressions = int(row['impressions'])
            conversions = row['conversions']

            if impressions > 0 and clicks == 0:
                issues.append((campaign, "Impressions but no clicks", "MEDIUM"))

            if clicks > 0 and (conversions == "" or int(conversions) == 0):
                issues.append((campaign, "Clicks but no conversions", "HIGH"))

    return issues


if __name__ == "__main__":
    setup_database()

    results = validate_ads_data("../data/ads_data.csv")

    for campaign, issue, severity in results:
        insert_issue(campaign, issue, severity)
        print(f"[{severity}] {campaign}: {issue}")
