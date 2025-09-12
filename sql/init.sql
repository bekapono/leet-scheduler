-- db

-- tables
---- problems
CREATE TABLE IF NOT EXISTS problems (
    id          INT NOT NULL PRIMARY KEY,
    title       VARCHAR(100),
    difficulty  VARCHAR(20),
    created_on  DATE NOT NULL,
    updated_on  DATE
);
---- scheduler
CREATE TABLE IF NOT EXISTS scheduler (
    id          INT NOT NULL PRIMARY KEY,
    problem_id  INT NOT NULL REFERENCES problems(id),
    due_at      DATE,
    status      VARCHAR(20),
    created_at  DATE NOT NULL,
    updated_at  DATE
);
----   reviews
CREATE TABLE IF NOT EXISTS reviews
(
    id             INT  NOT NULL,
    problem_id     INT  NOT NULL REFERENCES problems (id),
    reviewed_at    DATE NOT NULL,
    results        VARCHAR(20),
    interval_days  INT  NOT NULL,
    next_review_at DATE
);
-- indexes