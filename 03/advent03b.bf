99*:00"tupni"i$$>v  (stack has number of lines left on top)
<v  < v k!`0:    <  +-30             ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
 > & & & 73p53p33p & & & 75p55p35p v ; run like so:                                        ;
   A B C                             ; $ cfunge advent03b.bf < input                       ;
    ^ <  v p73 p75 p77 & & &       < ; it requires that the input file be named "input"    ;
   D E F > 33g35g+37gv               ; as well as that the input be redirected in on stdin ;
           A + D > G `               ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
   G H I             !
         v           _ 35g37g+33gv
        0              D + G > A `
        9                        !
         v                       _ 33g37g+35gv
        9                          A + G > D `
        *                                    ! triangle checks out
         v                                   _ 099*g1+099*p
         > 53g55g+57gv
        g  B + E > H `
                     !
         v           _ 55g57g+53gv
        1              E + H > B `
        3                        !
         v                       _ 53g57g+55gv
        +                          B + H > E `
        8                                    ! triangle checks out
         v                                   _ 099*g1+099*p
         > 73g75g+77gv
        *  C + F > I `
        -            !
         v           _ 75g77g+73gv
        .              F + I > C `
        a                        !
         v                       _ 73g77g+75gv
        ,                          C + I > F `
        @                                    ! triangle checks out
^        <                                   _ 099*g1+099*p
