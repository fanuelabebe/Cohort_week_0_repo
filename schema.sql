-- -- Create a table called 'users'
CREATE TABLE users (
    id VARCHAR(255) PRIMARY KEY,
    user_name TEXT,
    real_name TEXT,
    is_admin BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table called 'reactions'
CREATE TABLE reactions (
    reaction_id SERIAL PRIMARY KEY,
    reaction_count INTEGER NOT NULL,
    reaction_users_count VARCHAR(255) NOT NULL,  
    user_id VARCHAR(255) REFERENCES users(id),
    channel TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
