```bash
psql -h localhost -p 5432 -U postgres exercises
```

```sql
CREATE DATABASE greenhub
```

```sql
\c greenhub
```

```sql
CREATE USER api_user WITH PASSWORD 'api_user_password';
```

```sql
ALTER USER api_user CREATEDB;
```

```sql
ALTER ROLE api_user SUPERUSER;
```

```sql
exit
```

```bash
psql -h localhost -p 5432 -U api_user greenhub
```

```sql
CREATE SCHEMA greenhub_trx;
```

```sql
CREATE TABLE greenhub_trx.users (
    phone_num INTEGER      PRIMARY KEY,
    name      VARCHAR(100) NOT NULL,
    email     VARCHAR(100) NOT NULL,
    password  VARCHAR(100) NOT NULL
);
```

```sql
CREATE TABLE greenhub_trx.transfers (
    id          SERIAL         ,
    description VARCHAR(100)   NOT NULL,
    amount      DECIMAL(10, 2) NOT NULL,
    date        TIMESTAMP      NOT NULL,
    user_id     INTEGER        REFERENCES greenhub_trx.users(phone_num),
    status      INTEGER        CHECK (status IN (0, 1, 2, 3, 4))
)PARTITION BY RANGE (date);
```

```sql
CREATE TABLE greenhub_trx.collections (
    id          SERIAL         ,
    description VARCHAR(100)   NOT NULL,
    amount      INTEGER        NOT NULL,
    date        TIMESTAMP      NOT NULL,
    user_id     INTEGER        REFERENCES greenhub_trx.users(phone_num),
    status      INTEGER        CHECK (status IN (0, 1, 2, 3, 4))
)PARTITION BY RANGE (date);
```

# Now to seed the tables with about 10 values each, run the following commands:

```sql
INSERT INTO greenhub_trx.users (phone_num, name, email, password) VALUES (1234567890, 'John Doe', 'johndoes@gmail.com', 'password');
```
