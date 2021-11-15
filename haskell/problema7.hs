countIf :: (Int -> Bool) -> [Int] -> Int
countIf _ [] = 0
countIf func (x:xs)
  |func x = 1 + countIf func xs
  |otherwise = countIf func xs

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam _ [] = []
pam lista (f:fs) = map f lista : pam lista fs

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
--pam2 lista funciones = [map (flip ($) x) funciones | x <- lista]
pam2 lista funciones = [map ($ x) funciones | x <- lista]

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl funcbool func valor lista = foldl func valor [x | x <- lista, funcbool x]

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert _ [] a = [a]
insert funcbool (x:xs) valor
  |funcbool valor x = valor:x:xs
  |otherwise = x:insert funcbool xs valor

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort _ [] = []
insertionSort funcbool lista = foldl (insert funcbool) [] lista
