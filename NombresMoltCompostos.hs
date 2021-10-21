divisors :: Int -> [Int]
divisors n = filter func [1..n]
  where
    func :: Int -> Bool
    func x = mod n x == 0

nbDivisors :: Int -> Int
nbDivisors = length . divisors

moltCompost :: Int -> Bool
--moltCompost 1 = True
moltCompost n = and [nbDivisors x < nbDivisors n | x <- [1..(n-1)]]
--moltCompost n = [x | x <- [1..(n-1)], nbDivisors x < nbDivisors n]
