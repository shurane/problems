#lang racket

(define (factorial n)
  (if (eq? n 0)
    1
    (* n (factorial (- n 1)))))

(define (binomial n k)
  (/ (factorial n) 
     (* (factorial k) 
        (factorial (- n k)))))

(binomial 40 20)
