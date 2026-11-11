-- Run on a fresh database. To reset, DROP TABLE SpectatorSources first.
CREATE DATABASE IF NOT EXISTS SpecSources;
USE SpecSources;

CREATE TABLE SpectatorSources (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO SpectatorSources (name, email) VALUES
    ('Maya Patel', 'maya.patel@example.com'),
    ('Jordan Reyes', 'jordan.reyes@example.com'),
    ('Priya Natarajan', 'priya.natarajan@example.com'),
    ('Sam Okafor', 'sam.okafor@example.com'),
    ('Lena Fischer', 'lena.fischer@example.com');
