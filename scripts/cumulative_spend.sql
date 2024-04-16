SELECT account_id, SUM(abs(transaction_amount)) AS total_spent
FROM transactions
where
    date(transaction_date) >= date({date}, 'start of month') 
    and
    date(transaction_date) < date({date}, 'start of month', '+1 month', '-1 day') 
GROUP BY account_id
HAVING total_spent > 500