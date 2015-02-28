#lang racket

(define (utopian-tree n)
  (if (eq? n 0)
    1
    (cond
      [(odd? n) (* 2 (utopian-tree (- n 1)))]
      [(even? n) (+ 1 (utopian-tree (- n 1)))]
      [ else (error "shouldn't get here")])))

(define (readlines n [lines (list)])
  (if (eq? n 0)
    lines
    (cons (string->number (read-line))
          (readlines (- n 1) lines))))

(define T (string->number (read-line)))
(define args (readlines T))

(for ([arg args])
  (displayln (utopian-tree arg)))
