#lang racket

(define N (string->number (read-line)))
(define nums (map string->number (string-split (read-line))))
(displayln (foldl + 0 nums))
