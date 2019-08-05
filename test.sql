SELECT * from admin;

INSERT INTO admin(username, password) values ("rosemary", "rosemary");

UPDATE admin
SET password="rose"
where username="rosemary";