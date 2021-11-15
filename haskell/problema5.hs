flatten :: [[Int]] -> [Int]
flatten lista = foldr (++) [] lista

myLength :: String -> Int
myLength [] = 0
myLength palabra = last (zipWith (\x y -> y) palabra (iterate (+1) 1))

myReverse :: [Int] -> [Int]
myReverse lista = foldr (\x y -> y ++ [x]) [] lista

countIn :: [[Int]] -> Int -> [Int]
countIn lista numero = map (func numero) lista
  where
    func num list = length (filter (== num) list)

firstWord :: String -> String
firstWord palabra = takeWhile (/= ' ') (dropWhile (==' ') palabra) 
