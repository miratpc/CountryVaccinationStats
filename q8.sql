WITH country_medians AS (
    SELECT
        country,
        COALESCE(
            PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY daily_vaccinations) 
            OVER (PARTITION BY country),
            0
        ) AS median_vaccinations
    FROM
        country_vaccination_stats
),
updated_table AS (
    SELECT
        cvs.country,
        cvs.date,
        cvs.vaccines,
        COALESCE(cvs.daily_vaccinations, cm.median_vaccinations) AS daily_vaccinations
    FROM
        country_vaccination_stats cvs
    LEFT JOIN
        country_medians cm
    ON
        cvs.country = cm.country
)
-- Uncomment the below line to actually update the table if needed
-- UPDATE country_vaccination_stats
-- SET daily_vaccinations = updated_table.daily_vaccinations
-- FROM updated_table
-- WHERE country_vaccination_stats.country = updated_table.country
-- AND country_vaccination_stats.date = updated_table.date;

SELECT * FROM updated_table;
