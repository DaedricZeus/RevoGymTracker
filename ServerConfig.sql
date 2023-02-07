-- Creating the schema
CREATE SCHEMA fact;

-- Creating the tables
CREATE TABLE [fact].[MembershipNums] (
	TimeOfQuery		DATETIME	NOT NULL,
	GymName			VARCHAR(64)	NOT NULL,
	MemberCount		INT			NOT NULL
);