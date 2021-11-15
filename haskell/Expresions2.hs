opera2 :: (Int -> Int -> Int) -> Either String Int -> Either String Int -> Either String Int
opera2 op (Right x) (Right y) = Right (op x y)
opera2 _ _ _ = Left "div0"

opera :: (Int -> Int -> Int) -> Maybe Int -> Maybe Int -> Maybe Int
opera op (Just x) (Just y) = Just (op x y)
opera _ _ _ = Nothing
