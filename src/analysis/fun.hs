import qualified Danl as Dnl
import qualified Data.Map as Map
import qualified Json as Jsn
import qualified System.Environment as Env

fromLiteralInt (Jsn.LiteralInt x) = x
fromRecordValue (Jsn.RecordValue x) = x

main = do
  (print . Dnl.fromRight) ((Left 4) :: Either Int String)
  home <- Env.getEnv "HOME"
  c <- readFile (home ++ "/.dtt")
  let ls = lines c
      lists = filter f ls where
        f x =
          x /= "start session" && x /= "end session" &&
          not (x `Dnl.startsWith` "UTC " || x `Dnl.startsWith` "{\"wpm\": ")
      [bad, all] = (Dnl.stripe 2 . map (
        Map.map fromLiteralInt . fromRecordValue . Dnl.fromRight . Jsn.parseVal
        )) lists
      combine = foldl (Map.unionWith (+)) Map.empty
      badComb = combine bad
      allComb = combine all
  print badComb
  --(print . take 1) all
