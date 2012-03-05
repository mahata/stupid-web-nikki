DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
  id SERIAL,
  article TEXT,
  created_date INTEGER,
  UNIQUE(created_date)
);

