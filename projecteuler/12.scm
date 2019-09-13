#lang racket

(require racket/generator)
(require profile)

; thanks agf for the algorithm: http://stackoverflow.com/a/6800214/198348
(define (factors number)
  (remove-duplicates
    (flatten
    (for/list ([divisor (range 1 (+ 1 (sqrt number)))]
                #:when (eq? 0 (modulo number divisor)))
      (list divisor (/ number divisor))))))

(define (triangle increment number)
  (let ([numfactors (length (factors number))])
    ;(if (eq? 0 (modulo number 1000))
      ;(printf "currently... increment: ~a, number: ~a, factors: ~a ~n" increment number numfactors)
      ;(list))
    (if (>= numfactors 500)
      (printf "found it: ~a ~n" number)
      (triangle (+ increment 1) (+ number increment)))))

(triangle 1 0)
;(profile (triangle 1 0))
;(length (factors 76576500))
