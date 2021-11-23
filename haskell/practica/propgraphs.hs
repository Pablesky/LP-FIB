main :: IO()
main = do
  putStrLn $ "Benvinguts a la base de dades basades en grafs propis"

  --Input de la primera part del problema, l'usuari introdueix els fitxers.
  putStrLn $ "Introdueix el fitxer on es contenen les arestes"
  --fitxerArestes <- getLine
  let fitxerArestes = "rhoFile.pg"
  putStrLn $ "Introdueix el fitxer on es contenen els Labels dels nodes-arestes"
  --fitxerLabels <- getLine
  let fitxerLabels = "lambdaFile.pg"
  putStrLn $ "Introdueix el fitxer on es troben els valors de cada nodes-arestes X propietat"
  --fitxerSigma <- getLine
  let fitxerSigma = "sigmaFile.pg"
  putStrLn $ "Introdueix el fitxer on es troben el tipus dels valors de les propietats"
  --fitxerTvalors <- getLine
  let fitxerTvalors = "propFile.pg"

  graf <- populate fitxerArestes fitxerLabels fitxerSigma fitxerTvalors
  showGraph graf

  bucle graf

  return()

bucle :: Graf -> IO()
bucle graf = do
  putStrLn $ "Escull entre les seguents opcions:"
  putStrLn $ "0. Sortir"
  putStrLn $ "1. Afegir una aresta"
  putStrLn $ "2. Afegir una propietat a un vertex o aresta"
  putStrLn $ "3. Afegir un label a un vertex o aresta"

  linia <- getLine
  if linia == "0" then do
    return ()

  else if linia == "1" then do
    putStrLn $ "Introdueix el nom de la aresta i els dels vertexs (un per linia)"
    aresta <- getLine
    v1 <- getLine
    v2 <- getLine

    let temp = graf
    graf <- afegirAresta temp aresta v1 v2
    showGraph graf

    bucle graf
    return()

  else if linia == "2" then do
    putStrLn $ "Introdueix el nom del vertex/aresta, propietat i valor (un per linia)"
    vertex <- getLine
    propietat <- getLine
    valor <- getLine

    let temp = graf
    graf <- afegirPropietatVertexAresta temp vertex propietat valor
    showGraph graf

    bucle graf
    return()

  else if linia == "3" then do
    putStrLn $ "Introdueix el nom del vertex/aresta i label (un per linia)"
    vertex <- getLine
    label <- getLine

    let temp = graf
    graf <- afegirLabels temp vertex label
    showGraph graf

    bucle graf
    return()
  else
    bucle graf


--Creem un ABC
exact :: Aresta -> Aresta -> Bool
exact (Aresta aresta1 v11 v12) (Aresta aresta2 v21 v22) =
  aresta1 == aresta2 && v11 == v21 && v12 == v22

data Abc a = Buit | Node a (Abc a) (Abc a)

buit :: Abc a
buit = Buit

cerca :: Ord a => a -> Abc a -> Maybe a
cerca x Buit = Nothing
cerca x (Node k fe fd)
    | x <  k        = cerca x fe
    | x >  k        = cerca x fd
    | x == k        = Just k

existeix :: Aresta -> Abc Aresta -> Bool
existeix _ Buit = False
existeix x (Node k fe fd)
    | x <  k        = existeix x fe
    | x >  k        = existeix x fd
    | exact x k     = True

insereix :: Ord a => a -> Abc a -> Abc a
insereix x Buit = Node x Buit Buit
insereix x (Node k fe fd)
    | x <  k        = Node k (insereix x fe) fd
    | x >  k        = Node k fe (insereix x fd)
    | x == k        = Node k fe fd

--Llegeix un fitxer
llegirFitxerALlista :: String -> IO [String]
llegirFitxerALlista ubicacioFitxer = do
    arestaVertexs <- readFile(ubicacioFitxer)
    let llistaArestaVertexs = words arestaVertexs
    return llistaArestaVertexs

--Uneixes dos llistes dins de tuples
concatenaLlistesTuples :: ([String], [String]) -> ([String], [String]) -> ([String], [String])
concatenaLlistesTuples (llista11, llista12) (llista21, llista22) = (llista11 ++ llista21, llista12 ++ llista22)

--Separació de vertexs i arestes
separacioVertexsIArestes :: [String] -> ([String], [String])
separacioVertexsIArestes [] = ([], [])
separacioVertexsIArestes (aresta:vertex1:vertex2:llista) =
  concatenaLlistesTuples ([aresta], [vertex1, vertex2]) (separacioVertexsIArestes llista)

--Tipus de dada que representa una aresta i dos vertexs
data Aresta = Aresta String String String

instance Eq Aresta where
  (Aresta aresta1 _ _) == (Aresta aresta2 _ _) = aresta1 == aresta2

instance Ord Aresta where
  compare (Aresta aresta1 _ _) (Aresta aresta2 _ _ )
    |aresta1 == aresta2 = EQ
    |aresta1 < aresta2 = LT
    |aresta1 > aresta2 = GT

instance Show Aresta where
  show (Aresta aresta v1 v2) = "(" ++ show aresta ++ "," ++ show v1 ++ "," ++ show v2 ++ ")"

--Inicialitzem l'arbre binari de cerca amb Arestes per tal de donada una aresta -> v1 v2
inicialitzaArbreArestaAVertexs :: [String] -> [String] -> Abc Aresta -> Abc Aresta
inicialitzaArbreArestaAVertexs [] [] _ = buit
inicialitzaArbreArestaAVertexs (aresta:restaArestes) (vertex1:vertex2:restaVertexs) arbre =
  insereix (Aresta aresta vertex1 vertex2) (inicialitzaArbreArestaAVertexs restaArestes restaVertexs arbre)

--Tipus de dada que representa una Aresta/Vertex i un label
data Etiqueta = Etiqueta String String

instance Eq Etiqueta where
  (Etiqueta punt1 _) == (Etiqueta punt2 _) = punt1 == punt2

instance Ord Etiqueta where
  compare (Etiqueta punt1 _) (Etiqueta punt2 _)
    |punt1 == punt2 = EQ
    |punt1 < punt2 = LT
    |punt1 > punt2 = GT

instance Show Etiqueta where
  show (Etiqueta punt label) = show label

--Inicialitzem l'arbre binari de cerca amb punts i la seva etiqueta
inicialitzaArbreArestesVertexsALabels :: [String] -> Abc Etiqueta -> Abc Etiqueta
inicialitzaArbreArestesVertexsALabels [] _ = buit
inicialitzaArbreArestesVertexsALabels (punts:label:llista) arbre =
  insereix (Etiqueta punts label) (inicialitzaArbreArestesVertexsALabels llista arbre)

--Tipus de dades que relaciona un punt i una propietat amb un valor
data SigmaValue = SigmaValue String String String

instance Eq SigmaValue where
  (SigmaValue punt1 propietat1 _) == (SigmaValue punt2 propietat2 _) =
    punt1 == punt2 && propietat1 == propietat2

instance Ord SigmaValue where
  compare (SigmaValue punt1 propietat1 valor1) (SigmaValue punt2 propietat2 valor2)
    |punt1 < punt2 = LT
    |punt1 > punt2 = GT
    |punt1 == punt2 && propietat1 < propietat2 = LT
    |punt1 == punt2 && propietat1 > propietat2 = GT
    |punt1 == punt2 && propietat1 == propietat2 = EQ

instance Show SigmaValue where
  show (SigmaValue punt propietat valor) = "(" ++ show propietat ++ "," ++ show valor ++ ")"

--Inicialitzem l'abre binari de cerca per tal de relacionar un vertex/node amb una propietat i un valor
inicialitzaArbrePuntPropietatAValor :: [String] -> Abc SigmaValue -> Abc SigmaValue
inicialitzaArbrePuntPropietatAValor [] _ = buit
inicialitzaArbrePuntPropietatAValor (punt:propietat:valor:resta) arbre =
  insereix (SigmaValue punt propietat valor) (inicialitzaArbrePuntPropietatAValor resta arbre)

--Tipus de dada que relaciona la propietat amb el seu tipus
data TipusPropietat =  TipusPropietat String String

instance Eq TipusPropietat where
  (TipusPropietat propietat1 _) == (TipusPropietat propietat2 _) =
    propietat1 == propietat2

instance Ord TipusPropietat where
  compare (TipusPropietat propietat1 _) (TipusPropietat propietat2 _)
    |propietat1 < propietat2 = LT
    |propietat1 > propietat2 = GT
    |propietat1 == propietat2 = EQ

instance Show TipusPropietat where
  show (TipusPropietat propietat tipus) = "(" ++ show propietat ++ "," ++ show tipus ++ ")"

--Inicialitzem l'arbre binari de cerca per tal de relacionar propietat amb el seu tipus
inicialitzaArbrePropietatATipus :: [String] -> Abc TipusPropietat -> Abc TipusPropietat
inicialitzaArbrePropietatATipus [] _ = buit
inicialitzaArbrePropietatATipus (propietat:tipus:resta) arbre =
  insereix (TipusPropietat propietat tipus) (inicialitzaArbrePropietatATipus resta arbre)

--Funcio auxiliar per tal de conseguir Props
obtenirPropietats :: [String] -> [String]
obtenirPropietats [] = []
obtenirPropietats (propietat:_:resta) = [propietat] ++ resta

obtenirEtiquetes :: [String] -> [String]
obtenirEtiquetes [] = []
obtenirEtiquetes (_:etiqueta:resta) = [etiqueta] ++ resta

deleteDuplicate :: (Eq a) => [a] -> [a]
deleteDuplicate [] = []
deleteDuplicate (x:xs) = x : deleteDuplicate (filter (/= x) xs)

--Creem la estructura de dades graf
---               Vertexs  Arestes  Labels   Props  Aresta->(v1,v2) lambda(va)->l sigma
data Graf = Graf [String] [String] [String] [String] (Abc Aresta) (Abc Etiqueta) (Abc SigmaValue)

--Creem la funcio populate
populate :: String -> String -> String -> String -> IO Graf
populate fitxerArestes fitxerLabels fitxerSigma fitxerTvalors = do
  llista <- llegirFitxerALlista fitxerArestes
  let (arestesIntermig, vertexsIntermig) = separacioVertexsIArestes llista
  let arestes = deleteDuplicate arestesIntermig
  let vertexs = deleteDuplicate vertexsIntermig
  let arbreRho = inicialitzaArbreArestaAVertexs arestesIntermig vertexsIntermig buit

  llista <- llegirFitxerALlista fitxerLabels
  let labelsIntermig = obtenirEtiquetes llista
  let labels = deleteDuplicate labelsIntermig
  let arbreLambda = inicialitzaArbreArestesVertexsALabels llista buit

  llista <- llegirFitxerALlista fitxerSigma
  let arbreSigma = inicialitzaArbrePuntPropietatAValor llista buit

  llista <- llegirFitxerALlista fitxerTvalors
  let propietats = obtenirPropietats llista
  let arbreTipus = inicialitzaArbrePropietatATipus llista buit

  return (Graf vertexs arestes labels propietats arbreRho arbreLambda arbreSigma)

--Primera part imprimir
imprimirPropsPunto :: String -> [String] -> Abc SigmaValue -> IO()
imprimirPropsPunto punto [] _ = do return ()
imprimirPropsPunto punto (propiedadActual:props) sigmaTree = do
  case (cerca (SigmaValue punto propiedadActual " ") sigmaTree) of
    Just value -> putStr $ show value
    Nothing -> putStr $ ""

  imprimirPropsPunto punto props sigmaTree

  putStr $ ""

  return ()

imprimir1 :: Graf -> IO()
imprimir1 (Graf [] _ _ _ _ _ _) = do return ()
imprimir1 (Graf (vertexActual:vertexs) arestes labels props rho lambda sigma) = do
  putStr $ vertexActual ++ "["
  case ((cerca (Etiqueta vertexActual " ") lambda)) of
    Just value -> putStr $ show $ value
    Nothing -> putStr $ ""
  putStr $ "]{"

  imprimirPropsPunto vertexActual props sigma

  putStrLn $ "}"

  imprimir1 (Graf vertexs arestes labels props rho lambda sigma)

  return ()

--Segona part imprimir
imprimir2 :: Graf -> IO()
imprimir2 (Graf _ [] _ _ _ _ _) = do return ()
imprimir2 (Graf vertexs (arestaActual1:arestes) labels props rho lambda sigma) = do
  case ((cerca (Aresta arestaActual1 " " " ") rho)) of
    Just (Aresta a v1 v2) -> do
      putStr $ "(" ++ v1 ++ ")" ++ "-"
      putStr $ arestaActual1 ++ "["

      case ((cerca (Etiqueta arestaActual1 " ") lambda)) of
        Just value -> putStr $ show $ value
        Nothing -> putStr $ ""

      putStr $ "]->(" ++ v2 ++ "){"

      imprimirPropsPunto arestaActual1 props sigma

      putStrLn $ "}"

      imprimir2 (Graf vertexs arestes labels props rho lambda sigma)

    Nothing -> putStr $ ""

  return ()

--Funcio Total
showGraph :: Graf -> IO()
showGraph graf = do
  imprimir1 graf
  putStrLn $ ""
  imprimir2 graf
  return ()

--Afegim una Aresta
afegirAresta :: Graf -> String -> String -> String -> IO Graf
afegirAresta (Graf vertexs arestes labels props rho lambda sigma) aresta v1 v2 = do

  let tempVert = vertexs ++ [v1, v2]
  let tempArest = arestes ++ [aresta]

  let newVertexs = deleteDuplicate tempVert
  let newArestes = deleteDuplicate tempArest

  let temp = rho
  let rho = insereix (Aresta aresta v1 v2) temp

  return (Graf newVertexs newArestes labels props rho lambda sigma)

--Afegim una propietat al vertex
afegirPropietatVertexAresta :: Graf -> String -> String -> String -> IO Graf
afegirPropietatVertexAresta (Graf vertexs arestes labels props rho lambda sigma) vertex propietat valor = do

  let tempPropietats = props ++ [propietat]
  let propietats = deleteDuplicate tempPropietats

  let temp = sigma
  let sigma = insereix (SigmaValue vertex propietat valor) temp

  return (Graf vertexs arestes labels propietats rho lambda sigma)

--Afegim label a aresta i vertex
afegirLabels :: Graf -> String -> String -> IO Graf
afegirLabels (Graf vertexs arestes labels props rho lambda sigma) punto label = do
  let temp = lambda
  let lambda = insereix (Etiqueta punto label) temp

  return (Graf vertexs arestes labels props rho lambda sigma)
