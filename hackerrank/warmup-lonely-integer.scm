#lang racket

;(define data (file->lines "warmup-lonely-integer.txt"))
;(define N (string->number (car data)))
;(define A (map string->number (regexp-split #px" " (cadr data))))
(define N (string->number (read-line)))
(define A (map string->number (regexp-split #px" " (read-line))))

; haskell naming
(define (init lst)
  (match lst
    ['()  (error "empty list")]
    [_    (take lst (- (length lst) 1))]))

; this is confusing, based off of lexi-lambda's code snippet
(define (group-up lst)
  (let ([sorted-lst (sort lst <)])
    (let loop ([sl sorted-lst])
      (define-values (head tail)
        (splitf-at sl ((curry eq?) (car sl))))
      ;(printf "sl:~a head:~a tail:~a~n" sl head tail)
      (cons head 
        (if (empty? tail)
          (list)
          (loop tail))))))

(printf "~a~n"
  (caar (filter
    (lambda (l) (eq? (length l) 1)) (group-up A))))
