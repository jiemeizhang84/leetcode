select month, country,
       sum(case when state="approved" then 1 else 0 end) approved_count,
       sum(case when state="approved" then amount else 0 end) approved_amount,
       sum(case when state="chargeback" then 1 else 0 end) chargeback_count,
       sum(case when state="chargeback" then amount else 0 end) chargeback_amount
from
( select left(trans_date, 7) month, country, state, amount
  from transactions
  where state="approved"
  union all
  select left(c.trans_date, 7) month, country, "chargeback" state, amount
  from chargebacks c
  join transactions t
  on c.trans_id = t.id
) tmp
group by month, country
