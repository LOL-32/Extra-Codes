DROP DATABASE IF EXISTS loginpanel;

CREATE  DATABASE loginpanel;

USE loginpanel;


CREATE TABLE loginpanel.login (
	username VARCHAR(200),
	pswd     VARCHAR(200),
	email	 VARCHAR(200),
	phno     VARCHAR(200)

)
