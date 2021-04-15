CREATE TABLE photos(
	id TEXT PRIMARY KEY NOT NULL,
	collection TEXT NOT NULL,
	record INT NOT NULL,
	posted_date DATETIME,
	dont_post INT,
	invalid_record INT
);
