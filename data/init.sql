CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  article TEXT,
  created_date INTEGER,
  UNIQUE(created_date)
);

