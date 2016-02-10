#lang racket

(define (class-decision)
  (let* ([nk 
           (map string->number (string-split (read-line)))]
         [n (first nk)]
         [k (second nk)]
         [students 
           (map string->number (string-split (read-line)))]
         [students-on-time 
           (length (filter (compose1 not positive?) students))])
    (if (< students-on-time k)
      (displayln "YES")
      (displayln "NO"))))

(define (read-cases t)
  (for ([i (in-range t)])
    (class-decision)))

(define T (string->number (read-line)))
(read-cases T)
