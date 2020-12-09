CREATE DATABASE inventory;
CREATE USER inventoryuser WITH PASSWORD 'inventory';
GRANT ALL PRIVILEGES ON DATABASE books TO inventoryuser;