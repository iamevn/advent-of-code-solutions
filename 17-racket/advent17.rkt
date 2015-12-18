#lang racket
#| ;test input (should result in 4 and 3):
  (define amount 25)
  (define containers '(20 15 10 5 5))
|#
;actual data
(define amount 150)
(define containers '(43 3 4 10 21 44 4 6 47 41 34 17 17 44 36 31 46 9 27 38));so maybe I'm a little lazy



(define ways-to-fill
  (λ (amt cnt)
    (cond [(or (null? cnt)
               (< amt 0))
           0]
          [(zero? amt)
           1]
          [(null? (cdr cnt))
           (if [equal? amt (car cnt)]
               1
               0)]
          ;can split into two groups:
          ;  those that don't involve the first container
          ;  those that do
          [else (+ (ways-to-fill amt (cdr cnt))
                   (ways-to-fill (- amt (car cnt)) (cdr cnt)))])))

;;part a
(ways-to-fill amount containers)

(define part-b
  (λ (amt cnt)
    (let ([ps (powerset cnt)])
      (let loop ([n 0])
        (let ([s (foldl + 0
                        (map (λ (c) (ways-to-fill amt c))
                             (filter (λ (l) (equal? n (length l)))
                                     ps))
                        )])
          (if (> s 0) s
              (loop (add1 n))))))))

(define (powerset lst)
  (if (null? lst) '(()) ;powerset of empty set is a set containing the empty set
      (let ([tail (powerset (cdr lst))])
        (append (map (lambda (e)
                       (cons (car lst) e))
                     tail)
                tail))))

;;part b
(part-b amount containers)