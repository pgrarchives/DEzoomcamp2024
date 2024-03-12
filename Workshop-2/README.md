# Workshop 2 - risingWave


## Question 1: 
### Highest average trip time

- Yorkville East, Steinway
```sql
CREATE MATERIALIZED VIEW zone_stats AS
  SELECT 
    pu_zone.Zone as pickup_zone, 
    do_zone.Zone as dropoff_zone, 
    AVG(trip_data.tpep_dropoff_datetime - trip_data.tpep_pickup_datetime) as avg_time,
    MIN(trip_data.tpep_dropoff_datetime - trip_data.tpep_pickup_datetime) as min_time,
    MAX(trip_data.tpep_dropoff_datetime - trip_data.tpep_pickup_datetime) as max_time
  FROM trip_data
  JOIN taxi_zone pu_zone
    ON trip_data.PULocationID = pu_zone.location_id                 
  JOIN taxi_zone do_zone
    ON trip_data.DOLocationID = do_zone.location_id
  WHERE trip_data.PULocationID != trip_data.DOLocationID
  GROUP BY 
    pu_zone.Zone, do_zone.Zone
  ORDER BY 3 DESC;

SELECT * FROM zone_stats
```

## Question 2: 
### Number of trips
- 1
```sql
CREATE MATERIALIZED VIEW zone_stats AS
  SELECT 
    pu_zone.Zone as pickup_zone, 
    do_zone.Zone as dropoff_zone, 
    AVG(trip_data.tpep_dropoff_datetime - trip_data.tpep_pickup_datetime) as avg_time,
    MIN(trip_data.tpep_dropoff_datetime - trip_data.tpep_pickup_datetime) as min_time,
    MAX(trip_data.tpep_dropoff_datetime - trip_data.tpep_pickup_datetime) as max_time
  FROM trip_data
  JOIN taxi_zone pu_zone
    ON trip_data.PULocationID = pu_zone.location_id                 
  JOIN taxi_zone do_zone
    ON trip_data.DOLocationID = do_zone.location_id
  WHERE trip_data.PULocationID != trip_data.DOLocationID
  GROUP BY 
    pu_zone.Zone, do_zone.Zone
  ORDER BY 3 DESC;

SELECT * FROM zone_stats
```

## Question 3:
### Top 3 busiest zones
- LaGuardia Airport, Lincoln Square East, JFK Airport
```sql
CREATE MATERIALIZED VIEW latest_17_hours_pickups AS
  WITH latest_pickup_time AS (
    SELECT MAX(tpep_pickup_datetime) AS latest_pickup_time
    FROM trip_data
  )
  SELECT 
    pu_zone.Zone as pickup_zone, 
    COUNT(1) as count
  FROM trip_data
  JOIN taxi_zone pu_zone
    ON trip_data.PULocationID = pu_zone.location_id
  WHERE tpep_pickup_datetime > (SELECT latest_pickup_time - INTERVAL '17' HOUR FROM latest_pickup_time)
  GROUP BY 
    pu_zone.Zone
  ORDER BY 2 DESC, 1 DESC;

SELECT * FROM latest_17_hours_pickups
```
