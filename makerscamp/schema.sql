DROP TABLE IF EXISTS messages;
DROP TABLE IF EXISTS user_channels;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS channels;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text NOT NULL,
    password text NOT NULL
);

CREATE TABLE channels (
    id SERIAL PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    user_id int4 NOT NULL,
    message text NOT NULL,
    channel_id int4 NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (channel_id) REFERENCES channels (id)
);

CREATE TABLE user_channels (
    id SERIAL PRIMARY KEY,
    user_id int4 NOT NULL,
    channel_id int4 NOT NULL,
    FOREIGN KEY (channel_id) REFERENCES channels (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
