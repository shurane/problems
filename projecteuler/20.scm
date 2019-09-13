#lang racket

(require math/number-theory)

(define (digitize-b n)
  (if (< n 10)
      (list n)
      (cons (modulo n 10) (digitize (floor (/ n 10))))))

(define (digitize n)
  (reverse (digitize-b n)))

(foldl + 0 (digitize (factorial 100)))
