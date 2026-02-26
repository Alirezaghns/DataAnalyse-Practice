--Backup AND Restore
--1.Full                  Friday 10:00 AM
--2.Differential          EveryDay 03:00 AM
--3.Transaction			  Every 1 hour

--09:42 Sheytanat



--Disaster Scenario
 --Tuesday 10:52 AM
 -- How Many Minutes Data Lost Happend?
 -- Which Backups in used?


 --ANSWER:
 --Full: Friday 10:00 AM
 --DIFF: 
 --      Diff Tue
 --------------------------- 03:00 AM Tuesday
 --Tran: Tue 04:00 AM
 --      Tue 05:00 AM
 --      Tue 06:00 AM
 --      Tue 07:00 AM
  --      Tue 08:00 AM
   --      Tue 09:00 AM
    --      Tue 10:00 AM

--------------------------- 10:00 AM Tuesday

--52 Dataloss