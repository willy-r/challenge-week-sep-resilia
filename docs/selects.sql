-- Busca todos os estudantes
SELECT * FROM resilia_students
  ORDER BY id;

-- Busca estudades agrupados por faixa etária
SELECT COUNT(*) AS count FROM resilia_students
  WHERE CASE
    WHEN age >= 18 AND age <= 21 THEN 'De 18 a 21 anos'
    WHEN age >= 22 AND age <= 25 THEN 'De 22 a 25 anos'
    WHEN age >= 26 AND age <= 29 THEN 'De 26 a 29 anos'
    WHEN age >= 30 AND age <= 33 THEN 'De 30 a 33 anos'
    ELSE 'Acima de 33 anos'
  END AS age_cases
GROUP BY age_cases, count;
