#lang racket

(require racket/generator)

;(define (factors number)
  ;(for/list ([divisor (range 1 (+ 1 (inexact->exact (floor (sqrt number)))))]
             ;#:when (eq? 0 (modulo number divisor)))
            ;divisor))
(define (simplefactors number)
  (cons number 
    (for/list ([num (range 1 (+ 1 (/ number 2)))]
                #:when (eq? 0 (modulo number num)))
      num)))

(define (triangle increment number)
  (let ([numfactors (length (simplefactors number))])
    (if (eq? 0 (modulo number 100))
      (printf "currently... increment: ~a, number: ~a, factors: ~a ~n" increment number numfactors)
    ;(sleep 0.01)
      (list))
    (if (>= numfactors 500)
      (printf "found it: ~a ~n" number)
      (triangle (+ increment 1) (+ number increment)))))
     
(triangle 1 0)
