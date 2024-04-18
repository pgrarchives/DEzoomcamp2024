##1)Frequency Analysis
#1.1) Frequency of noise complaints over time: 
SELECT
  FORMAT_DATE('%Y-%m', PARSE_DATE('%Y-%m-%d', open_date)) AS month_year,
  COUNT(case_no) AS total_complaints
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  month_year
ORDER BY
  month_year;
#1.2) Frequency of complaints by type of noise
SELECT
  sub_type,
  COUNT(case_no) AS total_complaints
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  sub_type
ORDER BY
  total_complaints DESC;

##2) Geographical Analysis
#2.1)Highest number of noise complaints by zip code:
SELECT
  address_zipcode,
  COUNT(case_no) AS total_complaints
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  address_zipcode
ORDER BY
  total_complaints DESC;

#2.2)Correlation between type of noise complaints and zip codes:
SELECT
  address_zipcode,
  sub_type,
  COUNT(case_no) AS total_complaints
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  address_zipcode, sub_type
ORDER BY
  address_zipcode, total_complaints DESC;

##3)Resolution Time Analysis
#3.1) Average time to resolve noise complaints by complaint type:
SELECT
  sub_type,
  AVG(DATE_DIFF(PARSE_DATE('%Y-%m-%d', close_date), PARSE_DATE('%Y-%m-%d', open_date), DAY)) AS avg_resolution_days
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  sub_type
ORDER BY
  avg_resolution_days;

#3.2)Differences in resolution times based on geographical area:
SELECT
  address_zipcode,
  AVG(DATE_DIFF(PARSE_DATE('%Y-%m-%d', close_date), PARSE_DATE('%Y-%m-%d', open_date), DAY)) AS avg_resolution_days
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  address_zipcode
ORDER BY
  avg_resolution_days;
##4)Type and Severity Analysis
#4.1) Most common types of noise complaints:
SELECT
  sub_type,
  COUNT(case_no) AS total_complaints
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  sub_type
ORDER BY
  total_complaints DESC;
#4.2) Prevalence of industrial/commercial vs residential noise complaints:
SELECT
  CASE
    WHEN sub_type LIKE 'Residential%' THEN 'Residential'
    WHEN sub_type LIKE 'Industrial/commercial%' THEN 'Industrial/commercial'
  END AS complaint_category,
  COUNT(case_no) AS total_complaints
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  complaint_category
ORDER BY
  total_complaints DESC;

##5)Yearly Comparisons
#5.1)Change in noise complaints over the years:
SELECT
  case_year,
  COUNT(case_no) AS total_complaints
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  case_year
ORDER BY
  case_year;

#5.2)Trends in specific types of noise complaints over the years:
SELECT
  case_year,
  sub_type,
  COUNT(case_no) AS total_complaints
FROM
  `adta5240grp.noise_complaints.transformed_data`
GROUP BY
  case_year, sub_type
ORDER BY
  case_year, total_complaints DESC;

