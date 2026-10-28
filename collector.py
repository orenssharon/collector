import json
from datetime import datetime

def fetch_domain_deals():
    # כאן תהיה הלוגיקה לשאיבת דומיינים (למשל מ-Sedo / Afternic API או RSS)
    return [
        {
            "id": "dom_1",
            "platform": "Sedo",
            "type": "דומיין נישה (AI Tools)",
            "metrics": "DA 34 / 4K ביקורים",
            "price": "$120",
            "potential": "$1,200+",
            "category": "domain",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "link": "https://sedo.com"
        }
    ]

def fetch_saas_deals():
    # כאן תהיה הלוגיקה לשאיבת מיקרו-SaaS (למשל מ-Flippa / Acquire)
    return [
        {
            "id": "saas_1",
            "platform": "Flippa",
            "type": "מיקרו-SaaS (כלי PDF)",
            "metrics": "הכנסה $150/חודש",
            "price": "$450",
            "potential": "$3,000+",
            "category": "saas",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "link": "https://flippa.com"
        }
    ]

def fetch_github_deals():
    # כאן תהיה הלוגיקה לשאיבת פרויקטי קוד פתוח למכירה / GitHub Sponsors / Repos
    return [
        {
            "id": "gh_1",
            "platform": "GitHub / BuiltWith",
            "type": "בוט אוטומציה לטלגרם",
            "metrics": "1.2k Stars / פעיל",
            "price": "$200",
            "potential": "$1,500+",
            "category": "code",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "link": "https://github.com"
        }
    ]

def main():
    print("🚀 מתחיל איסוף נתונים בזמן אמת...")
    
    all_deals = []
    all_deals.extend(fetch_domain_deals())
    all_deals.extend(fetch_saas_deals())
    all_deals.extend(fetch_github_deals())

    # שמירה לקובץ JSON שישמש את האתר שלך
    output_data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_deals": len(all_deals),
        "deals": all_deals
    }

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

    print(f"✅ הקובץ עודכן בהצלחה! נמצאו {len(all_deals)} הזדמנויות.")

if __name__ == "__main__":
    main()
