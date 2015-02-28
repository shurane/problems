#lang racket

(define L (string->number (read-line)))
(define R (string->number (read-line)))

(apply max (map ((curry apply) bitwise-xor)
  (for*/list ([l (in-range L (+ R 1))]
              [r (in-range l (+ R 1))])
    (list l r))))
