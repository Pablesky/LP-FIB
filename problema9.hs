ones :: [Integer]
ones = 1:ones

nats :: [Integer]
nats = iterate (+1) 0

nats2 :: [Integer]
nats2 = iterate (+1) 2

nats1 :: [Integer]
nats1 = iterate (+1) 1

ints :: [Integer]
ints = 0:concatMap(\x -> [x, -x]) (iterate (+1) 1)

triangulars :: [Integer]
triangulars = tail $ scanl (+) 0 nats

factorials :: [Integer]
factorials = scanl (*) 1 (tail nats)

fibs :: [Integer]
fibs = 0:1:zipWith (+) fibs (tail fibs)

primes :: [Integer]
primes = garbell nats2
    where
        garbell (p : xs) = p : garbell [x | x <- xs, x `mod` p /= 0]

hammings :: [Integer]
hammings = 1 : fusio3 (map (*2) hammings) (map (*3) hammings) (map (*5) hammings)

fusio3 :: [Integer] -> [Integer] -> [Integer] -> [Integer]
fusio3 xs ys zs = fusio2 (fusio2 xs ys) zs

fusio2 :: [Integer] -> [Integer] -> [Integer]
fusio2 (x:xs) (y:ys)
  |x < y = x : fusio2 xs (y:ys)
  |x > y = y : fusio2 (x:xs) ys
  |otherwise = fusio2 (x:xs) ys

lookNsay :: [Integer]
lookNsay = iterate count 1

count :: Integer -> Integer
count a = read $ next $ show a

next :: [Char] -> [Char]
next [] = []
next lista = (show n) ++ [primero] ++ next resta
  where
    primero = head lista
    n = length $ takeWhile (== primero) lista
    resta = dropWhile (== primero) lista

tartaglia :: [[Integer]]
tartaglia = (iterate (operador) [1])

operador :: [Integer] -> [Integer]
operador lista = zipWith (+) ([0]++lista) (lista ++ [0cd ])
