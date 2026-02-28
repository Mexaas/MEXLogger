import aiosqlite

db = None

async def init():
    global db
    db = await aiosqlite.connect("userdata.db")
    await db.executescript(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            join_value INTEGER DEFAULT 1
        );

        DROP TABLE IF EXISTS threads;
        CREATE TABLE IF NOT EXISTS threads (
            thread_id INTEGER PRIMARY KEY,
            owner_id INTEGER NOT NULL,
            message_id INTEGER NOT NULL,
            channel_id INTEGER NOT NULL
        );
        """
    )
    await db.commit()

