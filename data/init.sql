DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
  id SERIAL,
  article TEXT,
  created_date INTEGER,
  UNIQUE(created_date)
);

ALTER TABLE articles ADD title TEXT;
