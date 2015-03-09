#lang racket

(define (make-alternating s)
  (regexp-replaces s
    '(
      [#rx"A+" "A"]
      [#rx"B+" "B"])))

(define (make-alternating-diff s)
  (let ([alternated (make-alternating s)])
    (list alternated (- (string-length s)
                        (string-length alternated)))))

(define (readlines n)
  (if (eq? n 0)
    (list)
    (cons (read-line)
          (readlines (- n 1)))))

(define T (string->number (read-line)))
(define args (readlines T))

(for ([arg args])
  (printf "~a~n" (cadr (make-alternating-diff arg))))
