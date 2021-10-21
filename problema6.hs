myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl _ a [] = a
myFoldl func n (x:xs) = myFoldl func (func n x) xs

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr _ a [] = a
myFoldr func n (x:xs) = func x (myFoldr func n xs)

myIterate :: (a -> a) -> a -> [a]
myIterate func num = [num] ++ myIterate func (func num)

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil funcbool func n
  |funcbool n = n
  |otherwise = myUntil funcbool func (func n)

myMap :: (a -> b) -> [a] -> [b]
myMap _ [] = []
myMap func (x:xs) = (func x) : (myMap func xs)

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = []
myFilter func (x:xs)
  |func x = x : myFilter func xs
  |otherwise = myFilter func xs

myAll :: (a -> Bool) -> [a] -> Bool
myAll _ [] = True
myAll func (x:xs) = func x && myAll func xs

myAny :: (a -> Bool) -> [a] -> Bool
myAny _ [] = False
myAny func (x:xs) = func x || myAny func xs

myZip :: [a] -> [b] -> [(a, b)]
myZip [] _ = []
myZip _ [] = []
myZip (a:as) (b:bs) = (a, b) : myZip as bs

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith _ [] _ = []
myZipWith _ _ [] = []
myZipWith func (a:as) (b:bs) = func a b : myZipWith func as bs
