#lang racket
(require math/number-theory)

(define (presentsForHouseA n)
  (* 10 (foldl + 0 (divisors n))))


(define (solutionA goal)
  (let loop ([n 1])
    (if (<= goal (presentsForHouseA n)) n
      (loop (add1 n)))))
(solutionA 36000000)

(define (presentsForHouseB n)
  (* 11 (foldl + 0 (filter (lambda (a) (<= (/ n a) 50))
                           (divisors n)))))
(define (solutionB goal)
  (let loop ([n 1])
    (if (<= goal (presentsForHouseB n)) n
      (loop (add1 n)))))
(solutionB 36000000)
