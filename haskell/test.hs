type Dict = (String -> Int)
create = const
search = ($)
insert dict key value x
    | key == x      = value
    | otherwise     = dict x

--Funcio que utilitzarem per tal de facilitar la unio de tuples de llistes de Strings
concatTuples :: ([String], [String]) -> ([String], [String]) -> ([String], [String])
concatTuples (listaA1, listaA2) (listaB1, listaB2) = (listaA1 ++ listaB1, listaA2 ++ listaB2)

--Donada una llista on trobem Arestes i els dos Vertexs de l'aresta
inicilitzarUnIDos :: [String] -> ([String], [String])
inicilitzarUnIDos (unitari:double1:double2:[]) = ([unitari], [double1, double2])
inicilitzarUnIDos (unitari:double1:double2:lista) = concatTuples ([unitari], [double1, double2]) (inicilitzarUnIDos lista)

inicilitzarDosIUn :: [String] -> ([String], [String])
inicilitzarDosIUn (double1:double2:unitari:[]) = ([double1, double2], [unitari])
inicilitzarDosIUn (double1:double2:unitari:lista) = concatTuples ([double1, double2], [unitari]) (inicilitzarDosIUn lista)

inicilitzarUnIUn :: [String] -> ([String], [String])
inicilitzarUnIUn (unitari1:unitari2:[]) = ([unitari1], [unitari2])
inicilitzarUnIUn (unitari1:unitari2:lista) = concatTuples ([unitari1], [unitari2]) (inicilitzarUnIUn lista)


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

--Un vertex es el nom d'un node del graf
data Vertex = Vertex String
  deriving (Show, Eq, Ord)

--Una aresta es el nom d'una aresta del graf
data Aresta = Aresta String
  deriving (Show, Eq, Ord)

--Conjunt Aresta Lab

data ConjuntAresta = ConjuntAresta Aresta Vertex Vertex

instance Eq ConjuntAresta where
  (ConjuntAresta aresta1 vertex11 vertex12) == (ConjuntAresta aresta2 vertex21 vertex22) =
    aresta1 == aresta2

instance Ord ConjuntAresta where
  compare (ConjuntAresta aresta1 vertex11 vertex12) (ConjuntAresta aresta2 vertex21 vertex22)
    |aresta1 == aresta2 = EQ
    |aresta1 < aresta2 = LT
    |aresta1 > aresta2 = GT

--Creem el graf


--Inicialitzem l'arbre
inicilitzarArbreBinariCercaArestaVertexs :: [String] -> [String] -> Abc ConjuntAresta -> Abc ConjuntAresta
inicilitzarArbreBinariCercaArestaVertexs [] [] _ = Buit
inicilitzarArbreBinariCercaArestaVertexs (aresta:llistaArestes) (vertex1:vertex2:llistaVertexs) arbre =
  insereix (ConjuntAresta (Aresta aresta) (Vertex vertex1) (Vertex vertex2)) (inicilitzarArbreBinariCercaArestaVertexs llistaArestes llistaVertexs buit)

--Inicialitzem aresta i vertexs a Labels
inicilitzarArbreBinariCercaArestesVertexsLabels :: [String] -> [String] -> Abc
