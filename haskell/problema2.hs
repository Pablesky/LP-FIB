myLength :: [Int] -> Int
myLength [] = 0
myLength (x:xs) = 1 + myLength xs

myMaximum :: [Int] -> Int
myMaximum (primer : resta)
  |resta == [] || primer > y = primer
  |otherwise = y
  where y = myMaximum resta

average :: [Int] -> Float
average lista = fromIntegral(sum(lista)) / fromIntegral(length(lista))

buildPalindrome :: [Int] -> [Int]
buildPalindrome lista = reverse(lista) ++ lista

remove :: [Int] -> [Int] -> [Int]
remove [] _ = []
remove (x:xs) d
  |elem x d = remove xs d
  |otherwise = x : remove xs d

flatten :: [[Int]] -> [Int]
flatten [] = []
flatten (x:xs) = x ++ flatten(xs)

oddsNevens :: [Int] -> ([Int],[Int])
oddsNevens [] = ([], [])
oddsNevens (x:xs)
  |even x = (a, x : b)
  |otherwise = (x : a, b)
  where
    (a, b) = oddsNevens xs

primeDivisors :: Int -> [Int]
primeDivisors 1 = []
primeDivisors x = reverse (primeDivisorsRec x x)

primeDivisorsRec :: Int -> Int -> [Int]
primeDivisorsRec _ 0 = []
primeDivisorsRec x y
  |mod x y == 0 && isPrime y = y:primeDivisorsRec x (y - 1)
  |otherwise = primeDivisorsRec x (y - 1)

isPrime :: Int -> Bool
isPrime n
  |n < 2 = False
  |otherwise = isPrimeRec n (n - 1)

isPrimeRec :: Int -> Int -> Bool
isPrimeRec x p
  |p == 1 = True
  |mod x p == 0 = False
  |otherwise = isPrimeRec x (p - 1)
