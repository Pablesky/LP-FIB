data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)

t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2

size :: Tree a -> Int
size Empty = 0
size (Node _ fe fd) = 1 + size fe + size fd

height :: Tree a -> Int
height Empty = 0
height (Node _ fe fd) = 1 + max (height fe) (height fd)

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty (Node _ _ _) = False
equal (Node _ _ _) Empty = False
equal Empty Empty = True
equal (Node x fex fdx) (Node y fey fdy)
  |x == y = (equal fex fey) && (equal fdx fdy)
  |otherwise = False

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty (Node _ _ _) = False
isomorphic (Node _ _ _) Empty = False
isomorphic Empty Empty = True
isomorphic (Node x fex fdx) (Node y fey fdy)
  |x == y = ((isomorphic fex fey) && (isomorphic fdx fdy)) || ((isomorphic fex fdy) && (isomorphic fdx fey))
  |otherwise = False

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node x fe fd) = x : (preOrder(fe)) ++ (preOrder$(fd))

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node x fe fd) = postOrder(fe) ++ postOrder(fd) ++ [x]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node x fe fd) = inOrder(fe) ++ [x] ++ inOrder(fd)

breadthFirst :: Tree a -> [a]
breadthFirst tree = breadthFirst' [tree]
  where
    breadthFirst' [] = []
    breadthFirst' (Empty:xs) = breadthFirst' xs
    breadthFirst' ((Node x fe fd):xs) = (x : breadthFirst' (xs ++ [fe] ++ [fd]))

build :: Eq a => [a] -> [a] -> Tree a
build _ [] = Empty
build [] _ = Empty
build (nodo:preordre) inordre = Node nodo (build preordreEsquerra inordreEsquerra) (build preordreDret inordreDret)
  where
    inordreEsquerra = takeWhile (/=nodo) inordre
    inordreDret = tail$dropWhile (/=nodo) inordre
    preordreEsquerra = take (length inordreEsquerra) preordre
    preordreDret = drop (length inordreEsquerra) preordre

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ t1 Empty = t1
overlap _ Empty t2 = t2
overlap operacio (Node x fex fdx) (Node y fey fdy) = Node (x `operacio` y) (overlap operacio fex fey) (overlap operacio fdx fdy
