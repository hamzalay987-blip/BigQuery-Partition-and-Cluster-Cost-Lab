# Project notes: BigQuery Partition and Cluster Cost Lab

**Business problem:** Analytics queries may scan unnecessary historical partitions when filters are missing.

**Design:** Demonstrate a partition-aware design and calculate a reproducible local approximation of records scanned.

**Interview discussion:** Explain schema assumptions, late data/duplicate behavior, controls, expected tradeoffs, and what would change at enterprise scale.

**Suggested next feature:** Add sample-sized integration tests or a docker-compose service when the implementation is ready.
