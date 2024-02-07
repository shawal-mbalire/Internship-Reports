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