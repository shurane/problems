#lang racket

(define end (inexact->exact 1e6))

; TODO memoize
; TODO construct a lazy list
; this is fast enough though
(define (collatz n)
  (cond
    [(eq? n 1)  (list 1)]
    [(odd? n)   (cons n (collatz (+ (* 3 n) 1)))]
    [(even? n)  (cons n (collatz (/ n 2)))]
    [else (error "shouldn't get here")]))

(define (collatz-up-to start end)
  (let* ([collatz-length (length (collatz start))]
         [collatz-pair (list start collatz-length)])
    ;(printf "(collatz-up-to ~a ~a): ~a ~n" start end collatz-length)
    (if (eq? start end) (list collatz-pair)
                        (cons collatz-pair (collatz-up-to (+ start 1) end)))))

(foldl (lambda (xlist ylist)
        (if (> (second xlist) (second ylist))
          xlist
          ylist))
       '(0 0)
       (collatz-up-to 1 1000000))
