with cte AS
(
SELECT
  account_id,
  strftime('%Y-%m', transaction_date) AS month_yt,
  avg(ABS(transaction_amount)) as avg_monthly_transaction_amount
FROM
  transactions
WHERE
  transaction_date < date('{date}')
group by 1,2
), moving_avg_cte as (

SELECT
  account_id,
  month_yt,
  avg_monthly_transaction_amount,
  AVG(avg_monthly_transaction_amount) OVER (
    PARTITION BY account_id
    ORDER BY month_yt
    ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING
  ) AS moving_avg_monthly_transaction_amount
FROM cte
)
select 
  account_id,
  month_yt,
  avg_monthly_transaction_amount,
  moving_avg_monthly_transaction_amount,
  (avg_monthly_transaction_amount - moving_avg_monthly_transaction_amount) / moving_avg_monthly_transaction_amount * 100 AS pct_change
from 
moving_avg_cte
WHERE
  ABS((avg_monthly_transaction_amount - moving_avg_monthly_transaction_amount) / moving_avg_monthly_transaction_amount) > 0.70  -- Adjust this value for different thresholds