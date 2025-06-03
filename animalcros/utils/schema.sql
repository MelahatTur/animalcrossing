-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);


-- Collectables (master list)
CREATE TABLE IF NOT EXISTS collectables (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    image TEXT,
    type TEXT CHECK (type IN ('fish', 'insect', 'seaCreature')),
    price INTEGER,
    description TEXT
);

-- Availability
CREATE TABLE IF NOT EXISTS availability (
    id SERIAL PRIMARY KEY,
    collectable_id INTEGER REFERENCES collectables(id) ON DELETE CASCADE,
    month TEXT CHECK (month IN (
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    )),
    hemisphere TEXT CHECK (hemisphere IN ('NH', 'SH')),
    time_of_day TEXT
);

-- Collections (user-collected items)
CREATE TABLE IF NOT EXISTS collections (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    collectable_id INTEGER REFERENCES collectables(id) ON DELETE CASCADE,
    UNIQUE (user_id, collectable_id)
);
