DROP TABLE IF EXISTS articles;
CREATE TABLE articles (
  id SERIAL,
  article TEXT,
  created_date INTEGER,
  UNIQUE(created_date)
);

-- DROP TABLE IF EXISTS access_log;
-- CREATE TABLE access_log (
--   id SERIAL,
--   path VARCHAR(255),
--   ip_address VARCHAR(20),
--   user_agent TEXT,
--   referer TEXT,
--   access_time INTEGER
-- );
