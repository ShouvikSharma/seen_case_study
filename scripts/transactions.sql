select 
customer_id,
account_id,
merchant_name,
transaction_date
from
transactions
where
abs(transaction_amount) > 300
and 
    date('{date}', '-1 day') =  date(transaction_date)