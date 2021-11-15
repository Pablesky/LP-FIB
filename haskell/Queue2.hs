data Queue a = Queue [a] [a]
     deriving (Show)

create:: Queue a
create = Queue [] []

push:: a -> Queue a -> Queue a
push n (Queue xs ys) = Queue xs (n:ys)

top :: Queue a -> a
-- top (Queue [] []) =
top (Queue [] ys) = head (reverse ys)
top (Queue (x:_) _) = x

pop:: Queue a -> Queue a
pop (Queue [] ys) = Queue (tail (reverse ys)) []
pop (Queue (x:xs) ys) = Queue xs ys

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty (Queue _ _) = False

aux :: Queue a -> [a]
aux (Queue [] []) = []
aux (Queue xs ys) = xs ++ reverse ys

instance Eq a => Eq (Queue a) where
    --(Queue xs1 ys1) == (Queue xs2 ys2) = aux (Queue xs1 ys1) == aux (Queue xs2 ys2)
    (Queue xs1 ys1) == (Queue xs2 ys2) = xs1 ++ reverse ys1 == xs2 ++ reverse ys2

instance Functor Queue where
  fmap f (Queue lista1 lista2) = Queue (fmap f lista1) (fmap f lista2)

translation :: Num b => b -> Queue b -> Queue b
translation x q = fmap (+x) q

cuaLlista :: Queue a -> [a]
cuaLlista (Queue lista1 lista2) = lista1 ++ reverse lista2

instance Applicative Queue where
  pure x = Queue [] [x]
  f <*> q = Queue(cuaLlista f <*> cuaLlista q) []

instance Monad Queue where
  return x = Queue [] [x]
  cua >>= f = Queue (concatMap (cuaLlista . f) (cuaLlista cua)) []

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter func cua = do
  x <- cua
  if func x then
    return x
  else
    create
