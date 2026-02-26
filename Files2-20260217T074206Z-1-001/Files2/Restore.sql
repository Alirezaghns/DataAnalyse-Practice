USE [master]
RESTORE DATABASE [Northwind_Test] FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\FULL\Northwind_9_25_2025_9_41.bak' WITH  FILE = 1, 
MOVE N'Northwind' TO N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Northwind_Test.mdf',
MOVE N'Northwind_log' TO N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\Northwind_Test_log.ldf',  NORECOVERY,  NOUNLOAD,  STATS = 5
RESTORE DATABASE [Northwind_Test] FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\Diff\Northwind_Diff_0954' WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 5
RESTORE LOG [Northwind_Test] FROM  DISK = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\Tran\Northwind_1001.trn' WITH  FILE = 1,  NOUNLOAD,  STATS = 5

GO


