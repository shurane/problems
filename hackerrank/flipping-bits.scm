#lang racket

(define (readlines n [lines (list)])
  (if (eq? n 0)
    lines
    (cons (string->number (read-line))
          (readlines (- n 1) lines))))

(define (number->binary-string number)
  (~r number #:min-width 32 #:pad-string "0" #:base 2))

(define (flip-bits bits)
  (list->string 
    (for/list ([bit bits])
      (cond
        [(eq? bit #\1) #\0]
        [(eq? bit #\0) #\1]
        [else (error "shouldn't get here")]))))

(define (inefficient-flip number)
  (string->number (flip-bits (number->binary-string number)) 2))

(define N (string->number (read-line)))
(define args (readlines N))
(for ([arg args])
  (printf "~a~n" (inefficient-flip arg)))

