DROP TABLE IF EXISTS practice221;

CREATE TABLE practice221 (
    day TEXT,
    language TEXT
);

INSERT INTO practice221 VALUES
('Monday', 'Python'),
('Tuesday', 'SQL'),
('Wednesday', 'Python'),
('Thursday', 'SQL'),
('Friday', 'Excel'),
('Saturday', 'Python');

SELECT DISTINCT language
FROM practice221
ORDER BY language;