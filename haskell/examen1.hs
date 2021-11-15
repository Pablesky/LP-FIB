--Ejercicio 1
eval1 :: String -> Int
eval1 lista = eval1' pila []
  where
    pila = words lista
    eval1' :: [String] -> [String] -> Int
    eval1' [] [x] = read x :: Int
    eval1' (x:xs) pila
      |x == "+" = eval1' xs (suma:resta)
      |x == "-" = eval1' xs (subi:resta)
      |x == "*" = eval1' xs (multi:resta)
      |x == "/" = eval1' xs (divi:resta)
      |otherwise = eval1' xs (x:pila)
        where
          segundo = read (head $ pila) :: Int
          primero = read (head $ tail $ pila) :: Int
          resta = drop 2 pila
          suma = show (primero + segundo)
          subi = show (primero - segundo)
          multi = show (primero * segundo)
          divi = show (div primero segundo)

eval2 :: String -> Int
eval2 s = head $ foldl (eval2') [] (words s)
  where
    eval2' :: [Int] -> String -> [Int]
    eval2' s l
      |l == "+" = ((head $ tail s) + head s):(tail $ tail s)
      |l == "-" = ((head $ tail s) - head s):(tail $ tail s)
      |l == "*" = ((head $ tail s) * head s):(tail $ tail s)
      |l == "/" = (div (head $ tail s) (head s)):(tail $ tail s)
      |otherwise = (read(l):s)

--mirar foto
--Ejercicio 2
fsmap :: a -> [a -> a] -> a
fsmap x f = foldl (flip ($)) x f

--Ejercicio 4
data Racional = Racional Integer Integer

racional :: Integer -> Integer -> Racional
racional a b = Racional (div a divisor) (div b divisor)
  where
    divisor = gcd a b

numerador :: Racional -> Integer
numerador (Racional a b) = a

denominador :: Racional -> Integer
denominador (Racional a b) = b

instance Eq Racional where
  (Racional a b) == (Racional x y) = (a * y) == (b * x)

instance Show Racional where
  show (Racional a b) = show (a) ++ "/" ++ show (b)

--Ejercicio 5
data Tree a = Node a (Tree a) (Tree a)

recXnivells :: Tree a -> [a]
recXnivells t = recXnivells' [t]
    where recXnivells' ((Node x fe fd):ts) = x:recXnivells' (ts ++ [fe, fd])

racionals :: [Racional]
racionals = recXnivells $ createTree $ racional 1 1

createTree :: Racional -> Tree Racional
createTree (Racional a b) = Node (Racional a b) fe fd
  where
    fe = createTree $ racional a (a + b)
    fd = createTree $ racional (a + b) b
