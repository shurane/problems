#lang racket

(define N (string->number (read-line)))
(define matrix
  (for/list ([i (in-range N)])
    (map string->number (string-split (read-line)))))
(define diag-primary 
  (for/list ([i (in-range N)])
    (list-ref (list-ref matrix i) i)))
(define diag-secondary
  (for/list ([i (in-range N)])
    (list-ref (list-ref matrix i) (- N i 1))))

(displayln (abs (- (foldl + 0 diag-primary) (foldl + 0 diag-secondary))))
