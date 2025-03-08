-- QUESTION
--Given a cards table and transactions table, return sum of total_eur and total_usd for each account number,
--rounded to 2 DP, arranged in asc order base on account_number
--
--INPUT:
--cards:
--id(pkey)  account_number(varchar)
--1         029375028734502
--2         829348273528379
--3         249839879879876
--4         923942362376875
--
--transactions:
--card_id(Fkey id) amount(varchar)
--1                7.46EUR
--1                902.45USD
--1                21.22USD
--2                784.03EUR
--2                29.1EUR
--2                783.09USD
--3                99EUR
--4                34USD
--4                102.30EUR

SELECT
    c.account_number as number,
    ROUND(SUM(CASE WHEN t.amount LIKE '%EUR'
THEN CAST(t.amount AS DECIMAL(10,2)) ELSE 0
END), 2) as total_eur,
    ROUND(SUM(CASE WHEN t.amount LIKE '%USD'
THEN CAST(t.amount AS DECIMAL(10,2)) ELSE 0
END), 2) as total_usd
FROM cards c
LEFT JOIN transactions t
ON c.id = t.card_id
GROUP BY account_number
ORDER BY account_number ASC;
