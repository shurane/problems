#lang racket

(define N (string->number (read-line)))

(define (reverse-staircase n)
  (if (= n 1)
    (list "#")
    (cons (make-string n #\#) (reverse-staircase (- n 1)))))

(define (staircase n)
  (reverse (reverse-staircase n)))

(for ([elem (staircase N)])
  (displayln (~a elem #:min-width N #:align 'right)))
