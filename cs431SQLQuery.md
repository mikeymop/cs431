mysql queries 

1. SELECT * FROM Transaction T, Customer C WHERE C.LoginName=T.LoginName GROUP BY C.CName HAVING AVG(T.TotalAmount)>100;
2. SELECT PhotoID FROM Photo WHERE TransID IS NULL;
3. SELECT C.CName FROM Transaction T, Photo P, Customer C, Models M WHERE C.LoginName=T.LoginName AND T.TransID=P.TransID AND P.PhotoID=M.PhotoID AND M.MName='Jasmine G';
4. SELECT P.PName FROM Photographer P, Influences I WHERE P.PName=I.EPName AND P.PBDate=I.EPBDate AND P.PNationality='United States';
5. Select P.PName FROM Photographer P, Photo A, Models M WHERE P.PName=A.PName AND P.PBDate=A.PBDate AND A.PhotoID=M.PhotoID;
6. Select P.TransID from Photo as P INNER JOIN Transaction as T on P.TransID = T.TransID having COUNT(P.TransID > 3)
7. SELECT M.MName FROM Models M, Photographer P, Photo A WHERE M.PhotoID=A.PhotoID AND A.PName=P.PName AND A.PBDate=P.PBDate AND P.PName='Joan Chaser';
8. SELECT P.PName FROM Photographer P, Photo A WHERE P.PNAME=A.PName AND P.PBDate=A.PBDate ORDER BY A.Price DESC;
9. DELETE FROM Photo WHERE PhotoID='12';
10. UPDATE Photo SET PName='Maxwell Smith', PBDate='1967-02-06' WHERE PhotoID='12'; 
11. SELECT SUM(T.TotalAmount) AS "Total Sales" FROM Customer C, Transaction T WHERE C.LoginName=T.LoginName AND C.LoginName='Jo';
12. SELECT SUM(DISTINCT T.TotalAmount) AS "Total Sales", P.PName
    FROM Transaction T, Photo A, Photographer P 
    WHERE T.TransID=A.TransID AND P.PName=A.PName AND P.PBDate=A.PBDate GROUP BY P.PName
13. SELECT SUM(T.TotalAmount) AS "Total Sales Type" FROM Models M, Transaction T, Photo P WHERE M.PhotoID=P.PhotoID AND P.TransID=T.TransID;
14. 



