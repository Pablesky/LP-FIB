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

--eval2 :: String -> Int
--mirar foto

fsmap :: a -> [a -> a] -> a
fsmap x f = foldl (flip ($)) x f
