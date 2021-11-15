data Tree a = Empty | Node a (Tree a) (Tree a)

instance Show a => Show (Tree a) where
  show Empty = "()"
  show (Node x fe fd) = "(" ++ show fe ++ "," ++ show x ++ "," ++ show fd ++ ")"

instance Functor Tree where
  fmap f Empty = Empty
  fmap f (Node x fe fd) = Node (f x) (fmap f fe) (fmap f fd)

doubleT :: Num a => Tree a -> Tree a
doubleT t = fmap (*2) t

data Forest a = Forest [Tree a] deriving (Show)

instance Functor Forest where
  fmap = fmap

doubleF :: Num a => Forest a -> Forest a
doubleF (Forest list) = Forest $ map (fmap (*2)) list

{--
instance Functor Forest where
  fmap f (Forest lista) = Forest $ map (fmap f) lista

doubleF :: Num a => Forest a -> Forest a
doubleF a = fmap (*2) a
--}
