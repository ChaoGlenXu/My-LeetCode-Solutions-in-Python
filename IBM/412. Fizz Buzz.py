{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue255;\red255\green255\blue255;\red0\green0\blue0;
\red32\green108\blue135;\red101\green76\blue29;\red0\green0\blue109;\red157\green0\blue210;\red19\green118\blue70;
\red15\green112\blue1;\red144\green1\blue18;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c100000;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;
\cssrgb\c14902\c49804\c60000;\cssrgb\c47451\c36863\c14902;\cssrgb\c0\c6275\c50196;\cssrgb\c68627\c0\c85882;\cssrgb\c3529\c52549\c34510;
\cssrgb\c0\c50196\c0;\cssrgb\c63922\c8235\c8235;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 class\cf0 \strokec4  \cf5 \strokec5 Solution\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf2 \strokec2 def\cf0 \strokec4  \cf6 \strokec6 fizzBuzz\cf0 \strokec4 (\cf7 \strokec7 self\cf0 \strokec4 , \cf7 \strokec7 n\cf0 \strokec4 : \cf5 \strokec5 int\cf0 \strokec4 ) -> List[\cf5 \strokec5 str\cf0 \strokec4 ]:\cb1 \
\cb3         result = []\cb1 \
\cb3         \cf8 \strokec8 for\cf0 \strokec4  i \cf2 \strokec2 in\cf0 \strokec4  \cf6 \strokec6 range\cf0 \strokec4 (\cf9 \strokec9 1\cf0 \strokec4 , n+\cf9 \strokec9 1\cf0 \strokec4 ):\cb1 \
\cb3             \cf10 \strokec10 #print(i)\cf0 \cb1 \strokec4 \
\cb3             \cf10 \strokec10 #print(i%3)\cf0 \cb1 \strokec4 \
\cb3             \cf8 \strokec8 if\cf0 \strokec4  i%\cf9 \strokec9 3\cf0 \strokec4  == \cf9 \strokec9 0\cf0 \strokec4  \cf2 \strokec2 and\cf0 \strokec4  i%\cf9 \strokec9 15\cf0 \strokec4  ==\cf9 \strokec9 0\cf0 \strokec4 :\cb1 \
\cb3                 result.append(\cf11 \strokec11 "FizzBuzz"\cf0 \strokec4 )\cb1 \
\cb3             \cf8 \strokec8 elif\cf0 \strokec4  i%\cf9 \strokec9 3\cf0 \strokec4  == \cf9 \strokec9 0\cf0 \strokec4 :\cb1 \
\cb3                 result.append(\cf11 \strokec11 "Fizz"\cf0 \strokec4 )\cb1 \
\cb3             \cf8 \strokec8 elif\cf0 \strokec4  i%\cf9 \strokec9 5\cf0 \strokec4  == \cf9 \strokec9 0\cf0 \strokec4 : \cb1 \
\cb3                 result.append(\cf11 \strokec11 "Buzz"\cf0 \strokec4 )\cb1 \
\cb3             \cf8 \strokec8 else\cf0 \strokec4 :\cb1 \
\cb3                 \cf10 \strokec10 #print("a")\cf0 \cb1 \strokec4 \
\cb3                 result.append(\cf5 \strokec5 str\cf0 \strokec4 (i))\cb1 \
\cb3         \cf8 \strokec8 return\cf0 \strokec4  result\cb1 \
}