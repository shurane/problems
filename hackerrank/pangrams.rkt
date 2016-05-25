#lang racket

(define S (read-line))

; this really isn't readable...
(define converted 
  ((compose 
     remove-duplicates
    (curryr sort <)
    (curry filter (lambda (x) (> x 0)))
    (curry map (lambda (x) (- x 97)))
    (curry map char->integer) 
     string->list
     string-downcase) S))

(if (equal? converted (range 1 26))
  (displayln "pangram")
  (displayln "not pangram"))

