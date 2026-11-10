SELECT COUNT(*) AS skolenu_skaits FROM skoleni;

SELECT ROUND(AVG(atzime), 2) AS videja FROM atzimes;

SELECT MIN(atzime) AS zemaka, MAX(atzime) AS augstaka FROM atzimes;

SELECT COUNT(*) AS bez_epasta FROM skoleni WHERE epasts IS NULL;