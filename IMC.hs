main = do
  linia <- getLine
  if linia == ['*'] then
    return ()
  else do
    let palabras = words linia
    let nombre = (palabras !! 0)
    let masa = read (palabras !! 1) :: Float
    let altura = read (palabras !! 2) :: Float
    let imc = masa / (altura * altura)
    if imc < 18 then
      putStrLn $ nombre ++ ": magror"
    else if imc < 25 then
      putStrLn $ nombre ++ ": corpulencia normal"
    else if imc < 30 then
      putStrLn $ nombre ++ ": sobrepes"
    else if imc < 40 then
      putStrLn $ nombre ++ ": obesitat"
    else
      putStrLn $ nombre ++ ": obesitat morbida"
    main
