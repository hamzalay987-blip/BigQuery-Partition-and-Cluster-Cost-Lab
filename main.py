import csv
from collections import Counter

def run(path='data/events.csv',date='2026-01-02'):
    with open(path,newline='') as f: events=list(csv.DictReader(f))
    selected=[e for e in events if e['event_date']==date]
    return {'total_rows':len(events),'partition_rows':len(selected),'rows_avoided':len(events)-len(selected),'customers_in_partition':len({e['customer_id'] for e in selected})}

if __name__ == '__main__':
    import json
    print(json.dumps(run(), indent=2))
