main = do
  nom <- getLine
  let ultimo = last nom
  if ('a' == ultimo) || ('A' == ultimo) then
    putStrLn $ "Hola maca!"
  else
    putStrLn $ "Hola maco!"
