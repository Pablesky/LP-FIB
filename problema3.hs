insert :: [Int] -> Int -> [Int]
insert [] x = [x]
insert (n:lista) num
  |n < num = n:(insert lista num)
  |otherwise = num:n:lista

isort :: [Int] -> [Int]
isort [] = []
isort x = isortRec x []

isortRec :: [Int] -> [Int] -> [Int]
isortRec [] res = res
isortRec (x:xs) res = isortRec xs nueva
  where
    nueva = insert res x

-------------------------------------------------------------

remove :: [Int] -> Int -> [Int]
remove [] _ = []
remove (x:xs) num
  |x == num = xs
  |otherwise = x:(remove xs num)

ssort :: [Int] -> [Int]
ssort [] = []
ssort lista = ssortRec lista []

ssortRec :: [Int] -> [Int] -> [Int]
ssortRec [] res = res
ssortRec lista res = ssortRec nlista nres
  where
    nres = maximum(lista):res
    nlista = remove lista (maximum lista)

-------------------------------------------------------------

merge :: [Int] -> [Int] -> [Int]
merge [] lista = lista
merge lista [] = lista
merge (numero1:lista1) (numero2:lista2)
  |numero1 < numero2 = numero1 : (merge lista1 (numero2:lista2))
  |otherwise = numero2 : (merge (numero1:lista1) lista2)

msort :: [Int] -> [Int]
msort [] = []
msort [x] = [x]
msort l = merge (msort izquierda) (msort derecha)
  where
    (izquierda, derecha) = (take n l, drop n l)
    n = div (length l) 2

--------------------------------------------------------------

qsort :: [Int] -> [Int]
qsort []     = []
qsort (p:xs) = (qsort menors) ++ [p] ++ (qsort majors)
    where
        menors = [x | x <- xs, x <  p]
        majors = [x | x <- xs, x >= p]

-----------------------------------------------------------------

genQsort :: Ord a => [a] -> [a]
genQsort []     = []
genQsort (p:xs) = (genQsort menors) ++ [p] ++ (genQsort majors)
    where
        menors = [x | x <- xs, x <  p]
        majors = [x | x <- xs, x >= p]
