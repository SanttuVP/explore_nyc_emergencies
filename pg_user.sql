-- Step 1: Connect to the PostgreSQL database with a user that has administrative privileges.

-- Step 2: Create a new user with limited permissions.
CREATE USER ro_user WITH PASSWORD 'your_password';

-- Step 3: Grant SELECT privileges on the "incidence" table to the new user.
GRANT SELECT ON TABLE incidents TO ro_user;
