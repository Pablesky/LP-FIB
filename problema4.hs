eql :: [Int] -> [Int] -> Bool
eql lista1 lista2
    |length lista1 /= length lista2  = False
    |otherwise = and (zipWith (==) lista1 lista2)

prod :: [Int] -> Int
prod lista = foldl (*) 1 lista

prodOfEvens :: [Int] -> Int
--prodOfEvens lista = prod (filter even lista)
prodOfEvens lista = foldr (*) 1 (filter even lista)

powersOf2 :: [Int]
powersOf2 = iterate (*2) 1

scalarProduct :: [Float] -> [Float] -> Float
scalarProduct lista1 lista2 = foldr (+) 0 (zipWith (*) lista1 lista2)