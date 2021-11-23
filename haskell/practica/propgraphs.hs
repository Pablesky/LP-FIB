main = do
  putStrLn $ "Benvinguts a la base de dades basades en grafs propis"

  --Input de la primera part del problema, l'usuari introdueix els fitxers.
  putStrLn $ "Introdueix el fitxer on es contenen les arestes"
  fitxerArestes <- getLine
  putStrLn $ "Introdueix el fitxer on es contenen els Labels dels nodes-arestes"
  fitxerLabels <- getLine
  putStrLn $ "Introdueix el fitxer on es troben els valors de cada nodes-arestes X propietat"
  fitxerSigma <- getLine
  putStrLn $ "Introdueix el fitxer on es troben el tipus dels valors de les propietats"
  fitxerTvalors <- getLine

  graf <- populate fitxerArestes fitxerLabels fitxerSigma fitxerTvalors

  return()

--Creem un ABC
data Abc a = Buit | Node a (Abc a) (Abc a)

buit :: Abc a
buit = Buit

cerca :: Ord a => a -> Abc a -> Maybe a
cerca x Buit = Nothing
cerca x (Node k fe fd)
    | x <  k        = cerca x fe
    | x >  k        = cerca x fd
    | x == k        = Just k

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
  show (Etiqueta punt label) = "(" ++ show punt ++ "," ++ show label ++ ")"

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
  show (SigmaValue punt propietat valor) = "(" ++ show punt ++ "," ++ show propietat ++ "," ++ show valor ++ ")"

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
data Graf = Graf [String] [String] [String] [String] (Abc Aresta) (Abc Etiqueta) (Abc SigmaValue)

--Creem la funcio populate
populate :: String -> String -> String -> String -> IO Graf
populate fitxerArestes fitxerLabels fitxerSigma fitxerTvalors = do
  llista <- llegirFitxerALlista fitxerArestes
  let (arestes, vertexs) = separacioVertexsIArestes llista
  let arbreRho = inicialitzaArbreArestaAVertexs arestes vertexs buit

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
