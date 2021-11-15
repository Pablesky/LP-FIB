fizzBuzz :: [Either Int String]
fizzBuzz = map (func) [0..]
  where
    func :: Int -> Either Int String
    func x
      |mod x 5 == 0 && mod x 3 == 0 = Right "FizzBuzz"
      |mod x 3 == 0 = Right "Fizz"
      |mod x 5 == 0 = Right "Buzz"
      |otherwise = Left x
