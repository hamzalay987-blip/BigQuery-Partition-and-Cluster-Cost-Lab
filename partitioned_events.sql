-- Change `your_project.your_dataset` before running in BigQuery.
CREATE TABLE `your_project.your_dataset.events` (
  event_id STRING, event_date DATE, customer_id STRING, event_type STRING
)
PARTITION BY event_date
CLUSTER BY customer_id;
SELECT event_type, COUNT(*) AS events
FROM `your_project.your_dataset.events`
WHERE event_date = DATE '2026-01-02'
GROUP BY event_type;
