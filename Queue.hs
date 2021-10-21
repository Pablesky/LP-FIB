data Queue a = Queue [a] [a]
    deriving (Show)

create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push val (Queue primero final) = Queue primero (val:final)

top :: Queue a -> a
top (Queue (x:primero) []) = x
top (Queue [] final) = last final

pop :: Queue a -> Queue a
pop (Queue [] []) = (Queue [] [])
pop (Queue (x:xs) _) = (Queue xs [])
pop (Queue primero segundo) = (Queue (primero ++ reverse((init segundo))) [])

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty _ = False

instance Eq a => Eq (Queue a)
     where
       (Queue [] []) == (Queue [] []) = True
       (Queue primerox segundox) == (Queue primeroy segundoy)
        |(primerox ++ reverse(segundox)) == (primeroy ++ reverse(segundoy)) = True
        |otherwise = False
