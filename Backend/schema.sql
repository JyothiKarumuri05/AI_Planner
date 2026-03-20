-- PRAGMA foreign_keys = ON;

-- CREATE TABLE users (
--     id TEXT PRIMARY KEY,
--     name TEXT NOT NULL,
--     email TEXT UNIQUE NOT NULL,
--     created_at DATETIME DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE travel_requests (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     user_id TEXT NOT NULL,
--     current_city TEXT NOT NULL,
--     destination TEXT NOT NULL,
--     start_date TEXT NOT NULL,
--     end_date TEXT NOT NULL,
--     budget TEXT NOT NULL,
--     group_type TEXT,
--     travel_style TEXT,
--     food_preference TEXT,
--     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
-- );

-- CREATE TABLE travel_plans (
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     user_id TEXT NOT NULL,
--     request_id INTEGER NOT NULL UNIQUE,
--     final_itinerary TEXT NOT NULL,
--     pdf_path TEXT,
--     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
--     FOREIGN KEY (request_id) REFERENCES travel_requests(id) ON DELETE CASCADE
-- );





CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS travel_requests (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    current_city TEXT NOT NULL,
    destination TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL,
    budget TEXT NOT NULL,
    group_type TEXT,
    travel_style TEXT,
    food_preference TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS travel_plans (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL,
    request_id INTEGER UNIQUE NOT NULL,
    final_itinerary TEXT NOT NULL,
    pdf_path TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (request_id) REFERENCES travel_requests(id) ON DELETE CASCADE
);
