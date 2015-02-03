#lang racket

(define data (file->lines "13.txt"))

(define result (foldl + 0
  (for/list ([line data])
      (string->number (substring line 0 11)))))

(substring (number->string result) 0 10)
