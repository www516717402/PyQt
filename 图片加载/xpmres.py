#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2017年12月23日
@author: Irony."[讽刺]
@site: http://alyl.vip, http://orzorz.vip, https://coding.net/u/892768447, https://github.com/892768447
@email: 892768447@qq.com
@file: xpmres
@description: 
'''

__Author__ = "By: Irony.\"[讽刺]\nQQ: 892768447\nEmail: 892768447@qq.com"
__Copyright__ = "Copyright (c) 2017 Irony.\"[讽刺]"
__Version__ = "Version 1.0"

# 这里把转换的xpm数组直接放到py文件中当做一个变量

# 这里需要把xpm文件里的内容做下修改成python的list
image_head = [
    "120 120 256 2",
    "8  c Black",
    "u. c #CACACA",
    " . c #0F0F0F",
    "I  c #D9D9D9",
    "x. c #1E1E1E",
    "@X c #E8E8E8",
    "%. c #2D2D2D",
    "l  c #F7F7F7",
    "S  c #3C3C3C",
    "1. c #4B4B4B",
    "XX c #5A5A5A",
    "{  c #696969",
    "U. c #787878",
    "7  c #878787",
    "wX c #969696",
    "JX c #A5A5A5",
    "SX c #B4B4B4",
    "p. c #C3C3C3",
    "|  c #080808",
    "9  c #D2D2D2",
    "r. c #171717",
    "2  c #E1E1E1",
    "<. c #262626",
    "0  c #F0F0F0",
    "3. c #353535",
    "   c #FFFFFF",
    "0X c #444444",
    "OX c #535353",
    "PX c #626262",
    "/  c #717171",
    "$X c #808080",
    "7X c #8F8F8F",
    "]  c #9E9E9E",
    "-X c #ADADAD",
    "c  c #BCBCBC",
    "O. c #010101",
    "B  c #CBCBCB",
    "b  c #101010",
    "@  c #DADADA",
    ";. c #1F1F1F",
    "dX c #E9E9E9",
    "F  c #2E2E2E",
    "j  c #F8F8F8",
    "C. c #3D3D3D",
    "N. c #4C4C4C",
    "J  c #5B5B5B",
    "G. c #6A6A6A",
    "HX c #797979",
    "FX c #888888",
    "/. c #979797",
    "m. c #A6A6A6",
    "uX c #B5B5B5",
    "$. c #C4C4C4",
    "t. c #090909",
    ":. c #D3D3D3",
    "a. c #181818",
    "$  c #E2E2E2",
    "#X c #272727",
    "F. c #F1F1F1",
    "VX c #363636",
    "Q  c #454545",
    "K. c #545454",
    "gX c #636363",
    "C  c #727272",
    " X c #818181",
    "KX c #909090",
    "P  c #9F9F9F",
    "e  c #AEAEAE",
    "yX c #BDBDBD",
    "5. c #020202",
    "p  c #CCCCCC",
    "i  c #111111",
    "+X c #DBDBDB",
    "J. c #202020",
    "T  c #EAEAEA",
    "b. c #2F2F2F",
    "r  c #F9F9F9",
    "6. c #3E3E3E",
    "g. c #4D4D4D",
    "v. c #5C5C5C",
    ",. c #6B6B6B",
    ";  c #7A7A7A",
    "&X c #898989",
    "D. c #989898",
    "t  c #A7A7A7",
    "k. c #B6B6B6",
    "w. c #C5C5C5",
    ".. c #0A0A0A",
    "c. c #D4D4D4",
    ";X c #191919",
    "6  c #E3E3E3",
    "sX c #282828",
    "{. c #F2F2F2",
    "iX c #373737",
    "-. c #464646",
    "l. c #555555",
    "~  c #646464",
    "P. c #737373",
    "a  c #828282",
    "*X c #919191",
    "CX c #A0A0A0",
    "BX c #AFAFAF",
    "6X c #BEBEBE",
    "w  c #030303",
    "s  c #CDCDCD",
    "R. c #121212",
    "]. c #DCDCDC",
    "q. c #212121",
    "x  c #EBEBEB",
    "D  c #303030",
    "o  c #FAFAFA",
    "f. c #3F3F3F",
    ".X c #4E4E4E",
    "4  c #5D5D5D",
    "K  c #6C6C6C",
    "GX c #7B7B7B",
    "jX c #8A8A8A",
    "rX c #999999",
    "8. c #A8A8A8",
    "mX c #B7B7B7",
    "4X c #C6C6C6",
    "y. c #0B0B0B",
    "|. c #D5D5D5",
    "4. c #1A1A1A",
    "B. c #E4E4E4",
    "ZX c #292929",
    ",  c #F3F3F3",
    "1X c #383838",
    "A  c #474747",
    "^  c #565656",
    ":  c #656565",
    "[  c #747474",
    "W. c #838383",
    "n. c #929292",
    "V. c #A1A1A1",
    "[. c #B0B0B0",
    "tX c #BFBFBF",
    "X. c #040404",
    "IX c #CECECE",
    "H. c #131313",
    "U  c #DDDDDD",
    "`. c #222222",
    ">X c #ECECEC",
    "G  c #313131",
    "+  c #FBFBFB",
    "xX c #404040",
    "T. c #4F4F4F",
    "lX c #5E5E5E",
    "E. c #6D6D6D",
    "z  c #7C7C7C",
    "!. c #8B8B8B",
    "i. c #9A9A9A",
    "oX c #A9A9A9",
    "zX c #B8B8B8",
    "%X c #C7C7C7",
    "v  c #0C0C0C",
    "*. c #D6D6D6",
    "z. c #1B1B1B",
    "=  c #E5E5E5",
    "R  c #2A2A2A",
    "k  c #F4F4F4",
    "H  c #393939",
    "_. c #484848",
    "L. c #575757",
    "d. c #666666",
    "MX c #757575",
    "Z. c #848484",
    "LX c #939393",
    "y  c #A2A2A2",
    "NX c #B1B1B1",
    "UX c #C0C0C0",
    "o. c #050505",
    "'. c #CFCFCF",
    "5X c #141414",
    "h. c #DEDEDE",
    ",X c #232323",
    ")  c #EDEDED",
    "I. c #323232",
    "O  c #FCFCFC",
    "3X c #414141",
    "Q. c #505050",
    "2. c #5F5F5F",
    "bX c #6E6E6E",
    "qX c #7D7D7D",
    "#  c #8C8C8C",
    "V  c #9B9B9B",
    "9X c #AAAAAA",
    "fX c #B9B9B9",
    "(. c #C8C8C8",
    "3  c #0D0D0D",
    "h  c #D7D7D7",
    "@. c #1C1C1C",
    "_  c #E6E6E6",
    "M. c #2B2B2B",
    "j. c #F5F5F5",
    "A. c #3A3A3A",
    ":X c #494949",
    "Z  c #585858",
    "8X c #676767",
    "d  c #767676",
    "hX c #858585",
    "AX c #949494",
    "=. c #A3A3A3",
    "0. c #B2B2B2",
    "#. c #C1C1C1",
    "+. c #060606",
    "N  c #D0D0D0",
    "u  c #151515",
    "cX c #DFDFDF",
    "Y. c #242424",
    "s. c #EEEEEE",
    "q  c #333333",
    ".  c #FDFDFD",
    ">  c #424242",
    "<X c #515151",
    "DX c #606060",
    "S. c #6F6F6F",
    "Y  c #7E7E7E",
    "e. c #8D8D8D",
    "^. c #9C9C9C",
    "1  c #ABABAB",
    "pX c #BABABA",
    ">. c #C9C9C9",
    "}  c #0E0E0E",
    "aX c #D8D8D8",
    "E  c #1D1D1D",
    "(  c #E7E7E7",
    "}. c #2C2C2C",
    "!  c #F6F6F6",
    "n  c #3B3B3B",
    "&. c #4A4A4A",
    "~. c #595959",
    "=X c #686868",
    "&  c #777777",
    "L  c #868686",
    "<  c #959595",
    "7. c #A4A4A4",
    "). c #B3B3B3",
    "`  c #C2C2C2",
    "W  c #070707",
    "-  c #D1D1D1",
    "eX c #161616",
    "g  c #E0E0E0",
    "f  c #252525",
    "5  c #EFEFEF",
    "m  c #343434",
    "X  c #FEFEFE",
    "2X c #434343",
    "nX c #525252",
    "*  c #616161",
    "kX c #707070",
    "%  c #7F7F7F",
    "M  c #8E8E8E",
    "vX c #9D9D9D",
    "9. c #ACACAC",
    "'  c #BBBBBB",

    "                                                                                                                                                  . .     X .   X   X X X   o                                                                   ",
    "                                                                                                                                                .     X   O   +         O .   +                                                                 ",
    "                                                                                                                                                .     X         @ # $     X                                                                     ",
    "                                                                                                                                                    X       o O % & * =                                                                         ",
    "                                                                                                                                                  . X   .   X - ; . : > ,   O X                                                                 ",
    "                                                                                                                                                  .     .     < 1   2 3 4                                                                       ",
    "                                                                                                                                                X           5 ; 6     7 8 % +                                                                   ",
    "                                                                                                                                                X   . X     9 % X   O 0 q w e O                                                                 ",
    "    r       X     o X   .   X     X     . .                       .       X     O               X X X           .       X           X X X     X O   O     . t y X X X   9 u i p X     .   O                                                     ",
    "+ X   X   +   .       . X     X X X .       X                     X     + .   O   . X   . O X .       . .     X     X X           X       X .     r   . .   a s       . + d 8 f g   O         X                                                 ",
    "    X         h r   o X   +   .       X X   X .                   . X X         X     X         . X       . o j 0 5 0 k j + .       X O     X X     . X   l z x   X   .   c v b n x   .     X                                                   ",
    "  X .   X   y 8 m M N . .         . .                                 .   + O X   . X     O . X   5 B V C Z A S m D F G H A J K L P c I k   X   X       X U Y .   X   X X T R E W Q !     X O                                                   ",
    "    O O   r Q ~ Y m F ^ / 1 ( X   . X   X O .                   X +     .     = )   _ ` ' ] [ { C S } |  .v W ..X.w X.o.O.8 8 X.O.+.3 @.m ^ # #.r O .   . $.V .     .       J O.%...J + .     +                                                 ",
    ". .     + . &.% X . *.=.-.;.Q a :.+   O     o                       O o X >.,.<.1.2.3.v E 4.8 o.+.| | X.8 8 8 O.8 8 8 5.w O.8 8 5.8 O...i 3 ..i 6.] o   X 1 7.      O   X X 8.w b ;.8 9.    .                                                   ",
    "    . O   . 0.q.w.      j e.D u f K B O o X   o                     X ` 2.r.W O.5.8 8 | 3 t.w 8 O.O.8 8 8 5.O.8 X.O.8 8 8 8 8 8 8 8 8 8 8 X.y.b o.8 &.u.  i.p.      X X     6 a.5.5.O.<.s.  +                                                   ",
    "X   X   O     d.-.l   .     f.5.8 5.b g.P p h.j.                  k.l.} 8 O.w 8 8 w 8 8 5.5.8 5.O.8 8 O.O.8 8 8 8 8 O.O.8 8 8 8 w 8 8 O.O.8 O.8 O.z.4.x.d a c.X X X     .   X ^ 8 5.8 5.v..   X                                                 ",
    "X X     O   O c.x.B     .   8.+.O.8 w 8 5.b.[ n.m.:.    X     ' l. .8 +.O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 | @.M.H N.B.X X .     .     < 8 8 O.8 O.V.      +       X .                                   ",
    "    X   .     k C.# .     O   Z.w 8 O.8 5.5...A.: S.D.F.o - G.;.H.8 X.X.8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 o.8 5.W J.K.j.        O     O c.b 8 5.8 8 ;.s.  +     +   O                                     ",
    "    X     .     L.S.X         j P.o.O.8 8 O.8 8 +.@.u l.z H R 3.W O.5.8 8 X.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.O.8 8 { o . X O         + j.I.8 O.8 8 w z .   + X   X     X                                 ",
    ".           .   U.&.    +   r   + d 5.O.5.O.O.5.O.8 8 5.Y.T.l.R.5.8 O.8 5.O.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 X.8 8 8 5.E.O           X     . v.O.w O.8 8 H.I .     X   O                                     ",
    "  X X X       X 7 6.O +     X X     W.+.8 8 +.8 O.8 O.X.z.f 8 5.8 8 w O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 Q.O   O     +   X     !.8 8 8 5.8 5.~.. o   +   .                                     ",
    "  + X   .       ^.I.,   O         +   /.J.5.8 5.8 w 8 O.5.8 8 8 o.8 8 8 8 O.5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 X.8 5.8 3.( X   o       X . X 8.o.O.o.8 w O.o.(.          +                                   ",
    "  O     X   O   c ;.U O       X   X   X ).m 5.w 8 8 8 w 8 5.w 8 8 8 8 5.O.8 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 5.t.V   O X     X       B z.8 5.X.8 8 O._.X     X X .                                   ",
    "      O X   X   - `.(.X   +   X X O   .   I b.8 O.8 w 8 O.8 8 O.8 X.O.8 5.8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 w 8 O.8 O.A.h '.  O .   . . X ].F +.8 8 O.w 8 5.[.    X   .                                   ",
    "                {.}.i.. .     X   .     X |.<.W 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 5.5.8 8 .. X.XN   ].+   X   k ,...O.o.8 w 8 8 R T   O X                                     ",
    "                  XXZ       o   .   O   0 *  .8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.8 8 8 O.> d.G.oXOX+X  . O . @X#X5.5.W 8 w O.8 V .     . .                                 ",
    "                  7.E 2   .   .   X   X 7 b w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 w 8 O.8 8 8 y.}...I.Q.+X8.$X%X&X].!.8 ..8 8 5.8 w *X  .                                       ",
    "                X ) <.L         X     c ;.8 5.O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 O.5.8 w 8 O.8 w ..Y.=XF : -Xd./.I.;XX.8 w O.z.:Xt O X   .                                 ",
    "                  . *XJ.2 X   O   r >X1.8 O.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 8 O.8 O.O.8 5.O.5.5.@.A ~.Z 1 { XX,X .8 8 5.8 3.<X` X                                     ",
    "                O   0 1X=Xo   X   X n.o.8 w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.5.8 8 O.8 O.5.8 8 8 5.5.b }.3 ~.; 2X3X@.3  .8 8 } > .Xs.. .                                 ",
    "                  X . 4Xz.[..   r h.Y.8 X.8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.8 8 w 8 8 8 X.X.w 8 O.8 O.8  .8 ;X3Xi y.1XJ.3 i ;Xx.S.                                    ",
    "                . X     i.}.h     C X.O.8 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 O.8 8 5.8 8 8 5.8 O.O.8 8 8 5.O.8 w 8 u H x...5X5X6X                                  ",
    "                O   +     W.N.s.9 z.5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 w 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.W r. .| w > j . .     X   X                   ",
    "                X X   .     7X& 8X5.8 O.8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 +.8 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 w 5.X.W +.9X      O   .   X                 ",
    "                  X   O   O   oXi 8 8 w 8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.8 5.8 8 | 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 8 8 W X.8 0Xk X   O   .   .                 ",
    "                    +   .   . qX8 w 8 O.O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 8 w 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.w 8 o.8 3 +.' .     O                       ",
    "                +     .   . I ,XO.5.8 8 5.O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 8 5.5.5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.5.O.: X     O   X                   ",
    "                  + .   X X % 5.8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.8 8 8 w 8 +.E $   X     X X                 ",
    "                      .   x m 8 O.8 O.O.8 8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 8 8 X.5.O.w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 o.8 5.wXX .       X                 ",
    "                .   X     oX+.8 O.8 8 w 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 w 8 8 5.w K b 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 5.8 X.o.&..     X                     ",
    "                    X     * 8 O.8 8 8 8 8 8 8 8 8 5.8 8 8 O.8 O.r.5X8 8 5.8 w 8 8 8 8 8 8 8 8 8 w 8 8 8 O. .(.G.8 O.8 8 5.5.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.5...eXc.      X                   ",
    "                .     . 0 n 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 5.f a z.5.8 8 8 8 w 8 8 8 8 8 8 8 8 8 O.w 8 8 ..B c.;.8 O.8 8 8 X.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.5.t.W rXX O   X                   ",
    "                        4XY.8 5.8 8 8 8 8 8 8 8 8 5.o.8 w 8 a.tXM o.8 O.8 X.8 8 8 8 8 8 8 8 8 8 8 O.8 O.5.i yX  W.W 8 w o.8 O.O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.t.o.^ X       X                 ",
    "                  .     L ;X8 O.8 8 8 8 8 8 8 8 8 O.8 w 8 b uX  ~.8 O.8 8 8 O.8 8 8 8 8 8 8 8 8 5.O.8 8 8 R.c   ) 0XO.8 8 +.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.W b <.T       X                 ",
    "                  +   k _.X.8 8 8 8 8 8 8 8 8 8 w 8 w 8 v wX  F.iXo.8 8 5.8 O.O.8 8 8 8 8 8 8 8 8 8 O.8 8 a.:.  r 4XE 8 W 8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.w u W pX  O                     ",
    "                X     aX;.8 O.8 8 8 8 8 8 8 8 8 O.8 8 W ~ . O 6 ;.8 8 O.5.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 +.`.6 X     M b 8 8 8 w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.u 5. X    .                   ",
    "                    o P y.5.O.O.8 8 8 8 8 8 8 8 8 X.8 G ].O   w.b 8 w 8 8 8 5.8 8 8 8 8 8 8 8 8 O.w 8 8 8 b.s.  X _ uXsX8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.5.R.3 1.+   X                   ",
    "                  .   d.X.8 8 8 8 8 8 8 8 8 8 8 5.8 3 rX  X O 9XX.8 5.8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.w .XX . U qX,.XX;X8 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.} H.J.dXX                     ",
    "                    @XA.X.8 O.8 w 8 8 O.O.8 8 8 O.w A dXk.L ( D.8 O.8 8 O.O.8 8 8 8 8 8 8 8 8 8 8 5.O.8 X.d.    5 k X   pXz.8 8 8 O.8 8 O.O.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 v 4.3 ` .                     ",
    "                X + ' #XO.8 O.8 8 8 5.8 8 O.8 X.8 u fX6XgXhX5 W.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 8 O.y.jX  O   + o   O D.3 8 8 8 8 5.8 O.w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 t.4.o.D.X                     ",
    "                  . jX;XO.8 O.8 8 8 8 8 8 5.8 8 o.T.k j + +   hXO.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 w b k.              O kX| 8 O.O.5.X.8 5.5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.@.t.K                       ",
    "                  k lXi O.8 O.8 O.8 8 O.8 8 O.8 5XzX  .       P.w 8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 O.w w J.h.X   X X   O .   l XXt.8 O.8 8 5.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 ;Xi T.X .                   ",
    "                O s %.o.8 8 8 O.8 8 8 O.8 8 +.w A r     X   O C +.8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 O.O.5.-.o   X     X     X X F.> 8 O.5.w 8 X.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 i  .iXF.X                   ",
    "                  i.y.8 w 8 8 8 8 O.8 8 5.8 8 v 8.O     .     kX..O.8 O.8 8 O.8 8 8 8 8 8 8 8 8 8 O.8 w & X     .   . , c.).m.B.$ 6.8 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.3 3 sX$                     ",
    "                l { 5.8 w O.8 8 8 O.8 8 w 8 8 xXF.X       +   7 } O.8 O.8 8 O.8 8 8 8 8 8 8 8 8 8 8 O.i uX+   +   cXV.a L V L 4Xo aXA.+.8 8 O.w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.3 i J.*.  .                 ",
    "                h.Q w 5.8 8 5.8 8 O.8 8 8 O.t.!.  j j.s.  X X 1 b 5.8 O.8 8 5.8 8 8 8 8 8 8 8 8 O.8 w Y.x     ) P Z.[.pXvXbXlX&.> nXA.v o.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 3 u 4.p                     ",
    ".   X   X   X   mX1X5.8 8 O.8 8 8 8 5.8 8 X.q.9.oXjXMX{ y .   tXz.8 8 w 8 8 8 5.8 8 8 8 8 8 8 8 8 8 O.: O   6 ^.e 7.* %.y.z.u w O.8 x.sXw 8 5.8 8 8 8 5.8 5.8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 y.x. .>.  X                 ",
    "    .   X     X rXm 8 O.O.8 8 O.5.O.8 5.o.5.Q.- cXcXN NXmX= l s J.X.8 8 8 O.8 O.8 8 8 8 8 8 8 8 8 w o.).. . B.BX^ D L.b.R ;Xw 8 8 w w sX}.v 8 O.O.8 8 8 o.8 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 X.`.3 w.                    ",
    "    .   X X   0 L VX8 5.5.8 O.8 8 8 5.5.8 i CXc.% <Xb.,XE J.A._.5XO.8 O.8 5.8 8 8 8 8 8 8 8 8 8 5.O.R ,     vXF S.:.* ;Xi 8 8 X.8 8 +.8 3 @.o.5.8 w 8 5.8 5.5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 8 %.i tX                    ",
    "  X     X X   |.L 3.8 O.8 8 5.8 O.8 O.8 w q.T.F ZX| 8 8 w 5.8 w w 8 O.w 8 8 8 8 8 8 8 8 8 8 8 8 8 w Z.  + AXI.SXX D.i i O.w 8 8 O.O.8 O.8 8 } X.v 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 H @.0.  X                 ",
    "X       X   X zXL ZX8 8 8 O.5.8 8 8 w 8 +.u L.~.5X8 8 8 5.8 8 | w 8 5.O.8 8 O.5.8 8 8 8 8 8 8 8 O.5XB.  ` lX+X  _ b.+.| 5.8 8 8 8 8 X.8 8 X.O.8 W b 8 5.O.o.w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 1XY.rX  X                 ",
    "      X       CXY z.5.w 8 8 O.8 5.O.8 X.8 2.~ t.5.5.O.8 5.8 O.8 o.O.8 8 8 O.O.8 8 8 8 8 8 8 8 8 O./ X + zXh.+   8.w o.o.8 8 8 O.O.8 8 8 5.8 8 5.O.-.sX8 X.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 8 }.`.;                     ",
    "  X   X     O e.P.H.5.5.8 8 O.8 8 8 8 O.x.0Xo.8 8 8 8 8 8 8 5.w O.8 8 O.O.O.8 8 8 8 8 8 8 8 8 8 R.cX.   X O   O d.8 O.8 5.w 8 8 8 8 O.5.5.8 X.8 8 2.*.Q.X.5.8 w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 ,X;.DX.                   ",
    "  O X     . j  XK  .8 8 O.8 w 8 8 8 O.W J.i 8 w 5.8 o.8 8 w 8 8 8 O.8 8 8 8 O.O.8 8 8 8 8 8 8 8 U..     O     j q w 8 8 8 8 5.O.8 8 5.8 O.8 8 8 O.#   j.e.f 3 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.O.J.J.K.+                   ",
    "    X       = L kXW 5.O.8 8 5.8 8 O.8 H.4.t.5.8 8 8 O.O.8 5.O.8 X.8 8 8 5.8 w 8 8 w 8 8 8 O.8 ,Xs.X .   X     $ eX8 8 8 8 O.8 % B 1X8 8 5.8 8 X.X.{   +   /.v eXH.W 8 8 O.8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 w 8 f Y.:XX                   ",
    "  X X   X   +XFXC o.8 O.8 O.8 8 8 5.8 r.J.t.8 O.8 8 8 8 X.8 8 5.8 w 8 w 8 8 8 O.8 8 8 5.8 8 X.vX+       X X   s 8 8 o.8 8 O.H.x . e w 8 5.8 O.8 8 T.X   O vX8 O.H.y.X.w 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.iXY._.X                   ",
    "X X X   . X u.7Xd 5.8 8 O.8 8 8 8 O.O.J.%.| 8 5.w R.lXeX8 O.8 8 8 +.w 8 5.w 8 8 5.O.O.5.| 8 1.    X   X   X   ' 5.w 8 8 8 8 4.{.  zX8 O.8 5.O.8 8 xXo     zXX.w 5.8 8 8 8 8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.8 ..Z M.&.                    ",
    "        . X pXrXGXO.8 8 8 8 8 O.8 8 o.VXxXt.8 8 8 e.  [.X.8 O.8 5.v ;X8 R.a.8 8 8 5.8 5.5Xz.+X.   O X X       tX8 8 8 5.5.8 w -XX ; 8 O.O.8 8 O.8 S O .   I a.O.8 8 O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O. .MXH g.                    ",
    "        .   [.8.W.O.5.8 8 O.8 O.O.8 | DXZ i 5.8 8 1   $ W 8 8 5.8 5XH w }.VX8 O.5.8 +.J.t.m.  . X   .     X   *.w 5.X.X.8 5.8 H.D | 8 8 O.5.O.8 O.&.    . @Xm 8 8 5.5.O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.3 L _._.+                   ",
    "  X     X   1 uXn.O.w 8 8 O.8 8 O.8 3 < z E 8 8 8 J r 9XO.w 8 w 8 eXK.8 _..X8 O.8 5.E t.;     X .   X   .     , D O.+.8 w O.8 O.O.8 5.X.O.O.8 o.8 d .   O s.A O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.3 wXv.xXr                   ",
    "  X   X     t ' 9.+.w O.8 8 8 8 8 8 4.4X0.<.8 8 8 o.}.} o.8 5.8 8 x. XO.C OX8 8 O.5X..=X+ .     X       .       kX8 O.8 8 8 +.8 O.8 8 8 8 X.8 8 w mX+     ! nX8 w 5.O.O.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.u [.HXS o                   ",
    "  X   X   X JXyXw.} o.X.8 8 5.8 8 8 R B.cX}.5.8 8 8 5.5.8 5.8 O.O.F mXu i.g.O.O.3 r.v.k   .       X     X   O   e 8 O.8 5.5.8 8 8 8 O.5.8 8 5.8 Y.F.    O X ~ 8 8 8 8 8 8 8 8 5.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 ;.(.KXn O .                 ",
    "    X   X . [.k.B.z.3 O.w 8 8 8 8 8 :Xr X 4 8 O.O.O.8 w 8 w 8 5.8 2X2 :XpX=Xy.o.%.Z.r O     X                   s.J.8 8 O.8 8 8 8 8 O.8 5.5.8 O.LX  X   X X kX8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 O.;.@ SXC.,                   ",
    "      O     0.SXO }.} W 8 w 8 8 8 +.PX.   B 3 8 8 8 O.8 O.O.5.O.8 : + NXaX&.q.$X(.  +     +   O                   P 8 X.8 8 X.8 O.O.8 X.8 8 8 A.j     X   O [ W 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 w 8 b.x :.<Xj.X                 ",
    "X     o     ` m.  L.+...8 8 8 O.8 8 ,.O   X P.8 5.8 8 8 8 8 8 8 o.e   . l p.h O     o X O                         o [ 8 8 O.8 X.8 5.8 8 8 8 A.cX  .   X     $X| 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 _.j _ GX. .                 ",
    ".     .   X 2 CXX jX+.R.w 8 8 O.5...M._   O j.PX8 8 O.o.8 W 5.8 sX!     . O       +         X                   X     JX%.8 8 8 O.8 8 b D KX{.O X   .       hXt.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 +.* X T 0.                    ",
    "          X r tX  zXH.q.t.O.O.O.8  .R.zX      0 S.J.O.8 8 8 5.} c   . .     .   O   O O     .                   X       l NXHXv.lX% p.2 j..     . .   O   O jX..8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.| qX  5 g O                   ",
    "      .     X ) r B.#X,X,X8 O.8 o.3 o.M   X     . dXwXDX* V =.p   O                   X     . X                 X     + O   o       r   X O s..       . X   7X..8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 } t X {.j . X                 ",
    "X   X .   X X   j.  gX;X.Xo.8 8 w q.8 v.+   o     r   X   .   X .   X   + .   X X +     X O   O                 X o X     X O           +Xl.[ T @X'.cX      !.| 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 4.R :.. ! X                     ",
    "X   O   X .   o     NXeX,.;X8 8 +.x.8 3X  o   .     O   . .   O   .       .   X           O .                         . . X   X   O   {.1.K.h ,.~ f.zXX .   jXO.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 <XN.T                           ",
    "                X   j PXDX2.X.8 O.i O.%.O   O                     .       X       g _               @X  .     X   O O   +       +   . F.7.j.s.1 9.yXX     O FXO.8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 O.8 O.8 O.y.xX8X      X X                   ",
    "                X   r *.1.JXx.5.8 b 8 M.F.O                     o     o   +   X X  XN.  U   .   9 CX_.:.+   X   O             .   . X +     X     O         % 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.5.8 8 8 O.;X3.D.      X                     ",
    "                      X ; oX{ w 5.y.8 sX!                           O           +X@.+.^ 4.E.mXY x.+.8 N.    O       r   . O X     X         .   O   O . .   S.w 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 5.8 8 O.8 8 4.G c.    X     X                 ",
    "                  +     ].9X0.E O.8 8 q l   .                   O .         O c ,Xt.S.C MXb.r.sX$Xw.=Xi <Xw.  O .       .   +   +     . O       X           J 8 O.O.8 8 8 8 8 8 8 8 8 8 8 O.O.8 O.8 8 O.5.8 5.5X&.l                             ",
    "                .         @X_ DXVX5X8 %.k                         .     + X wXv n *.X   . x aXF..     >.g.eX*X+   . + .   X   .     X O   O O     O   X .   A 8 O.O.8 8 8 8 8 8 8 8 8 8 8 O.O.8 8 8 O.w 8 8 ..i 7     X                         ",
    "                    O X     ! p 1X| 8 ;X0 X O                   X   . O O C w ~ T   O O     O     X .   O IXA ~.B..     . X .   X X +   +       X O     . r F O.O.O.O.8 8 8 8 8 8 8 8 8 8 5.5.8 8 8 O.8 8 8 o.5XB .   X   X X                   ",
    "                +   X X O   X   & O.8 8 BX  .                     X O 0 L.+.L     +   X   X .   +     .   X T ^ }.p X O     .       .     O O .   X +   X dXr.8 O.O.O.8 8 8 8 8 8 O.8 8 8 5.5.8 8 8 8 8 5.O.8 2Xj.O       X X                   ",
    "                  +       .   . $.8 X.8 -.+                     .   _ xXy.e   X X X   X   .   X   O X   +     {.~ r.NX  O     X     .   X .           .   :.| O.O.O.O.8 8 8 8 8 8 O.8 8 8 w 5.8 8 O.8 8 8 8 5.&X  .     X     X                 ",
    "                                B.eX8 8 8 oX  O   . O   X .   X   cXVX4.yX  .                                   + ,.} e . X   .       .   +   X .     X   zX8 O.w +.8 8 5.8 w 8 8 w 8 O.8 w 8 5.8 O.O.8 8 5. .@                                 ",
    "                                ) #XO.X.w 8XO         X         = q Y.@ .     +                                   + { +.).  .   o     O     O     O .   X < X.8 5.X.X.O.8 8 5.8 5.8 8 8 w 5.o.8 5.8 8 w O.8 2XO                                 ",
    "                                X 1XO.o.5...[.X O     + . X + x f.#X2   O     X                                 X   + J y.pX                X   .     o   [ 8 o.| o.o.5.8 O.8 8 8 +.8 5.8 8 8 O.8 W w 8 8 O.e.                                  ",
    "                                X hX8  .H.8 y.BX    o       j Q.J.].+ O     l                                   .   . ! _.E @ O     X     +         X     :X8 W v t.5.O.8 8 8 O.8 8 5.8 8 X.X.8 5.} w 8 5.X.w.+                                 ",
    "                                X pX| o.b 5.o.X.*X.     O + GX} zX        O                                           O ( ZX3.r +     X   .   X   .   X j D 8 b +.y.w 8 O.8 8 8 5.8 8 O.8 X.8 8 W @.X.5.8 5X>X                                  ",
    "                                  _ f 8 ,X+.5.5.8 &.pXo   5 ,X=.  X X   . .                                       O .   + >.o./     .   X     X   X     I i 8 y.| | W 8 8 8 5.8 O.O.w 8 8 Y.a.| }.C.O.O.8 S X X                                 ",
    "                                  X L.8 Y.q.8 3 X.8 8 > 9X/.C O       +                                           .   O O   L w p.X .   O       X X X {.9.8 W 4.#X5.+.8 8 8 O.8 8 o.8 8 b M.Q.v < $X| o.X.=X.                                   ",
    "                                . X t w W 3Xt.8 +.w 5.8 8 b pX  . X     X   X                                       O       0 sX_..   .     X   X   g L.m 8 5.U.N.8 w 8 8 8 8 O.| 8 w 8 4.r.R.b.l '.,X+.8 jX  X                                 ",
    "                                O   >Xb.5.T.=XO.W 5.X.O. .c     X             .                                   X   X       AX+.>.X     O     ) -Xm G @.O.VXh.m 5.w 8 8 O.8 5X .8 w H.t.W 8 JX    8X8 O.Z..     O   X   X   O     X .         ",
    "                                  X   ^.o.sX8.b.8 y.W 8 b.( X   X     X X                                       O . X     O   U v E.      = -X8XH ,XGX7 X.u pXT r.8 8 w 8 w o.kX@.5.#Xu %.3 D l . . u.4.5.-.          . X         .       O     ",
    "                                + X O + / eXd D.O.R.v 8 f.x   .           X                                               X   X }.r.L [ l.I.q T.XXI , I.8 z X 9X+.8 O.8 eX5.lX; 8 ..q C.k.5.d.      O vX3XFX  + X . X     O O         O         ",
    "                                  .     X W.A.zXS 5.+.,X|..       X       X X                                     . X   X     + jX8 VXC i W.5   6XL qX+.^ r   ~ w 5.5.@.r.I.# W 8 * '.dX5 _.yX. . O   O   .           +       . . O   O       O ",
    "                                O   X . X k 7.@X[.O.8 -X+ X X . X . X                                             O .     X     5 H.Z   }.$XX     ,.b -.j.  +XZXeX8 ;XG 1.U.} z.,.+X  .     X         X . O X   O .   .   + X     +       O     ",
    "                                    O   .     o r A 8 N.(     X         X                                                 r X   . ~.q.>X`.P.  {.) i.X.xX! X &XH. .m 9.7 ; y.a.|.+   .   +   O     . o             . X .         O   . o         ",
    "                                X X       X .     :.sX8 q.rXl   +       X                                       +     +         X LXH.V.%.UX. o O >Xb.8 4 +X}.O.2X$ $.1X5.E c.    . X   O       X     r X     X   X     +   l _ {.      X   o   ",
    "                                    X . X     . X   I V.A 8 }.AX5 j   X .     X                                   .     .   X     - a.i l.  X       A.8 v N.#XQ.) X < 8 I.+X      .         +     .     X     X   X   X oXXXY.z.q.1.9X  X X     ",
    "                                                X     X ! wX#X5.4     X X   +                                   X X         X s.AXI.8 3 c.  r     B +.v ..o.{ X   6 g.nXT   X                     .   O X   O     . F.XX8 8 w 8 5.8 8 d.X X     ",
    "                                                  . O     O 9 eXSX+ X X       O                                     X x aX0.G.}.t.W X.P X X   .   DX8 5.8  .x.4X  KX% ! O     X                             X X X r T.o.X.X.W O.8 5.8 5.a   . . ",
    "                                                  .   X O   jXq.s.    X   O                                       +   Z.M..X,Xu 0XH.jXo   . X O /.8 8 8 5.x.0X#XB.{.O O     .                                 X X bX8 8 8 8 8 w w 8 O.8 ;X,     ",
    "                                                X   X     r iX<XX     X                                               vXiX( GX=Xu ,..   .   ].2.8 8 X.O.8 ; U x.l.X       .   O                 X   X X   X     k.o.8 X.8 8 O.8 O.O.8 w W aX  X ",
    "                                                X X   X   ].b &X  + X       o                                   .   X N #XE.6.b C.    X h HXu O.O.5.8 A.fXX   -X5.vXX   .   X                     X   .       j.6.8 O.8 O.8 5.8 8 o.8 8 W '.  X ",
    "                                                    .     mXX.c O   X         .                                   .   g u b 3 ZXSXt qXQ v 8 8 8  .L.mXo   . . O 2.b ].  X   .                     X   .       #.w 8 O.5.8 8 8 w O.8 X.w eX(     ",
    "                                                O .   O   0.X.-   +   + X +   .                                   .   aX .w 8 b v O.8 O.8 R.0Xn.U   .   . X     g r.^ X       o                   X X   .   . [ O.5.8 8 O.8 O.8 5.8 8 8 HXX   . ",
    "                                                      X   ) C ; a / _       .                                       + @ H u O.O.O.5XA.kX1 B.  O   X   O     +     KXO.k.O X                         X   X   . H 8 8 O.w 8 8 5.8 8 8 8 f F.      ",
    "                                                  O   .   U / lX< C.:Xj.    .                   X X X   X   .   l V.6.;.`.a.O.O.~.>X+ X   O                 X     k A.D 0                       .   + X   X _ r.O.O.8 8 O.8 8 8 w 8 w (.  r     ",
    "                                                . O     '.XX8.o . h R.-X      X                       X   X   + [ 8 i ~ vXM.8 { r     o .   . .   + O             X P.8 wX  +                     .     X   s | 8 8 8 8 8 8 8 w 8 8 8XO .   + X ",
    "                                                      B.OX0.  X   ` ;.c +   O                   X     X X X + >X4.d.cX  . p.sXrX  j   T B   X       X     +       9 z.5.q.>X  .                   +     +   k.8 8 O.8 8 8 8 5.W o.5.IX  X X     ",
    "                                                .   . HX<Xo O     a ^ X O   X                     X     X   X mX8 yXr   X X G.5XT   F.Y >.    O +   O o       X 0 ZX8 w 8 FX.                     X .   X   9XO.8 O.O.8 8 8 5.| O.J.j.X   X   X ",
    "                                                    . -.Z.. +   + B d.+ X   O                     O       X   bX3.aX  O     - E wX  !.Y   X O     +     O   + p C.8 +.y.q.;._                       O X   X CXw 8 O.8 8 8 8 O.o.8 K..   X   .   ",
    "                                                  O   S DX    .   >X_.LXX X                       .     .   @ > - X       . . J ;.Q.3 / mX5 U g !     ! @ m.Z t.O.8 8 `.=.8 AX                    X   .   X ^.8 8 8 8 8 8 8 8 O.8 a   .   O     ",
    "                                                X     =X,Xj.    j   K.n       .                 .       O   c F {.O     .   . DX8 8 C.y.O.q.4.eXF f.f.#Xv 8 8 8 8 5.8 qXj.ZXG l                   .   X   X e 8 8 8 8 O.5.8 8 8 O.NXO   X   X O ",
    "                                                  .   ' 3 PX^.kXU.JXv d.O   O                   .   . .     *.z.7X+   .   .   W.8 A.l 0.x.8 O.8 8 O.8 8 O.5.8 O.w 8 Q.+ O M 8 '                     X       %Xw 8 O.5.w X.O.8 O...@     X   X   "
]
