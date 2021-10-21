data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

eval1 :: Expr -> Int
eval1 (Val x) = x
eval1 (Add x y) = eval1(x) + eval1(y)
eval1 (Sub x y) = eval1(x) - eval1(y)
eval1 (Mul x y) = eval1(x) * eval1(y)
eval1 (Div x y) = eval1(x) `div` eval1(y)

eval2 :: Expr -> Maybe Int
eval2 (Val x) = Just x
eval2 (Add x y) = opera (+) (eval2 x) (eval2 y)
eval2 (Sub x y) = opera (-) (eval2 x) (eval2 y)
eval2 (Mul x y) = opera (*) (eval2 x) (eval2 y)
eval2 (Div x y)
  |eval2 y == Just 0 = Nothing
  |otherwise = opera (div) (eval2 x) (eval2 y)

eval3 :: Expr -> Either String Int
eval3 (Val x) = Right x
eval3 (Add x y) = opera2 (+) (eval3 x) (eval3 y)
eval3 (Sub x y) = opera2 (-) (eval3 x) (eval3 y)
eval3 (Mul x y) = opera2 (*) (eval3 x) (eval3 y)
eval3 (Div x y)
  |eval3 y == Right 0 = Left "div0"
  |otherwise = opera2 (div) (eval3 x) (eval3 y)

opera2 :: (Int -> Int -> Int) -> Either String Int -> Either String Int -> Either String Int
opera2 op (Right x) (Right y) = Right (op x y)
opera2 _ _ _ = Left "div0"

opera :: (Int -> Int -> Int) -> Maybe Int -> Maybe Int -> Maybe Int
opera op (Just x) (Just y) = Just (op x y)
opera _ _ _ = Nothing
