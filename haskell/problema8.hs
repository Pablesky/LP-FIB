myMap :: (a -> b) -> [a] -> [b]
myMap func lista = [func x | x <- lista]

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter func lista = [x | x <- lista, func x]

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith func lista1 lista2 = [func x y | (x, y) <- zip lista1 lista2]

thingify :: [Int] -> [Int] -> [(Int, Int)]
thingify dividendo divisor = [(x, y) | x <- dividendo, y <- divisor, mod x y == 0]

factors :: Int -> [Int]
factors n = [x | x <- [1..n], mod n x == 0]
