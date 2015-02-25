#lang racket

; http://stackoverflow.com/a/20783438/198348
; `eval` needs a namespace
(define-namespace-anchor anc)
(define ns (namespace-anchor->namespace anc))

(define (readlines n [lines (list)])
  (if (eq? n 0)
    lines
    (cons (map string->number (regexp-split #px" " (read-line)))
          (readlines (- n 1) lines))))

(define N (string->number (read-line)))
(define args (readlines N))

(for ([arg args])
  (printf "~a~n" (eval (cons '+ arg) ns)))
