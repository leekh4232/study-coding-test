SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Dog' AND INSTR(UPPER(NAME), 'EL') > 0
ORDER BY NAME ASC;