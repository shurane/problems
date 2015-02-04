#lang racket

(define (digitsum n)
  (if (< n 10)
      n
      (+ (modulo n 10) (digitsum (floor (/ n 10))))))
  
(digitsum (expt 2 15))
(digitsum (expt 2 1000))
