-- Creating the schemas
CREATE SCHEMA dim;

CREATE SCHEMA fact;

-- Creating the tables
CREATE TABLE [dim].[GymIDs] (
	GymID		INT				IDENTITY(1,1)	NOT NULL,
	GymName		VARCHAR(64)		NOT NULL
);

CREATE TABLE [fact].[MembershipNums] (
	TimeOfQuery		DATETIME	NOT NULL,
	GymName			INT			NOT NULL,
	MemberCount		INT			NOT NULL
);

-- Adding gyms into the dim table
INSERT INTO [dim].[GymIDs] (
	[GymName]
)
VALUES(
	"belmont"
);